function initializeSearch(index) {
  let search_keys = ['title', 'id', 'link', 'body', 'section'];
  search_keys = search_keys.concat(other_searchable_fields);

  const search_page_element = elem('#searchpage');

  const search_options = {
    ignoreLocation: true,
    findAllMatches: true,
    includeScore: true,
    shouldSort: true,
    keys: search_keys,
    threshold: 0.5
  };

  index = new Fuse(index, search_options);

  function minQueryLen(query) {
    query = query.trim();
    const query_is_float = parseFloat(query);
    const min_query_length = query_is_float ? 1 : 2;
    return min_query_length;
  }

  function searchResults(results=[], query="", passive = false) {
    let results_fragment = new DocumentFragment();
    let show_results = elem('.search_results');
    if(passive) {
      show_results = search_page_element;
    }
    emptyEl(show_results);

    const query_len = query.length;
    const required_query_len = minQueryLen(query);

    if(results.length && query_len >= required_query_len) {
      let results_title = createEl('h3');
      results_title.className = 'search_title';
      results_title.innerText = quick_links;

      let go_back_button = createEl('button');
      go_back_button.textContent = 'Go Back';
      go_back_button.className = go_back_class;
      if(passive) {
        results_title.innerText = search_results_label;
      }
      if(!search_page_element) {
        results = results.slice(0,8);
      } else {
        results_fragment.appendChild(go_back_button);
        results = results.slice(0,12);
      }
      results_fragment.appendChild(results_title);

      results.forEach(function(result){
        let item = createEl('a');
        item.href = `${result.link}?query=${query}`;
        item.className = 'search_result';
        item.style.order = result.score;
        if(passive) {
          pushClass(item, 'passive');
          let item_title = createEl('h3');
          item_title.textContent = result.title;
          item.appendChild(item_title);

          let item_description = createEl('p');
          // position of first search term instance
          let query_instance = result.body.indexOf(query);
          item_description.textContent = `${result.body.substring(query_instance, query_instance + 200)}`;
          item.appendChild(item_description);
        } else {
          item.textContent = result.title;
        }
        results_fragment.appendChild(item);
      });
    }

    if(query_len >= required_query_len) {
      if (!results.length) {
        show_results.innerHTML = `<span class="search_result">${no_matches_found}</span>`;
      }
    } else {
      show_results.innerHTML = `<label for="find" class="search_result">${ query_len > 1 ? short_search_query : type_to_search }</label>`
    }

    show_results.appendChild(results_fragment);
  }

  function search(search_term, scope = null, passive = false) {
    if(search_term.length) {
      let raw_results = index.search(search_term);
      raw_results = raw_results.map(function(result){
        const score = result.score;
        const result_item = result.item;
        result_item.score = (parseFloat(score) * 50).toFixed(0);
        return result_item;
      })

      if(scope) {
        raw_results = raw_results.filter(result_item => {
          return result_item.section == scope;
        });
      }

      passive ? searchResults(raw_results, search_term, true) : searchResults(raw_results, search_term);

    } else {
      passive ? searchResults([], "", true) : searchResults();
    }
  }

  function liveSearch() {
    const search_field = elem(search_field_class);

    if (search_field) {
      const search_scope = search_field.dataset.scope;
      search_field.addEventListener('input', function() {
        const search_term = search_field.value.trim().toLowerCase();
        search(search_term, search_scope);
      });

      if(!search_page_element) {
        search_field.addEventListener('search', function(){
          const search_term = search_field.value.trim().toLowerCase();
          if(search_term.length)  {
            const scope_parameter = search_scope ? `&scope=${search_scope}` : '';
            window.location.href = new URL(`search/?query=${search_term}${ scope_parameter }`, root_url).href;
          }
        });
      }
    }
  }

  function findQuery(query = 'query') {
    const url_params = new URLSearchParams(window.location.search);
    return url_params.has(query) ? url_params.get(query) : "";
  }

  function passiveSearch() {
    if(search_page_element) {
      const search_term = findQuery();
      const search_scope = findQuery('scope');
      // search actively after search page has loaded
      const search_field = elem(search_field_class);

      search(search_term, search_scope, true);

      if(search_field) {
        search_field.addEventListener('input', function() {
          const search_term = search_field.value.trim().toLowerCase();
          search(search_term, true);
          wrapText(search_term, main);
        });
      }
    }
  }

  function hasSearchResults() {
    const search_results = elem('.results');
    if(search_results) {
        const body = search_results.innerHTML.length;
        return [search_results, body];
    }
    return false
  }

  function clearSearchResults() {
    let search_results = hasSearchResults();
    if(search_results) {
      search_results = search_results[0];
      search_results.innerHTML = "";
      // clear search field
      const search_field = elem(search_field_class);
      search_field.value = "";
    }
  }

  function onEscape(fn){
    window.addEventListener('keydown', event => event.code === "Escape" ? fn() : false);
  }

  let main = elem('main');
  main = main ? main : elem('.main');

  search_page_element ? false : liveSearch();
  passiveSearch();

  wrapText(findQuery(), main);

  onEscape(clearSearchResults);

  window.addEventListener('click', function(event){
    const target = event.target;
    const is_search = target.closest(search_class) || target.matches(search_class);
    !is_search && !search_page_element ? clearSearchResults() : false;
  });
}

window.addEventListener('load', function() {
  const page_language = document.documentElement.lang;
  const search_index = `${ page_language === 'en' ? '': page_language}/index.json`;
  fetch(new URL(search_index, root_url).href)
  .then(response => response.json())
  .then(function(search_data) {
    search_data = search_data.length ? search_data : [];
    initializeSearch(search_data);
  })
  .catch((error) => console.error(error));
});
