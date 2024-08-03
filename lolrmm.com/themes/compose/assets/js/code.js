const snippet_actions = [
  {
    icon: 'copy',
    id: 'copy',
    title: copy_text,
    show: true
  },
  {
    icon: 'order',
    id: 'lines',
    title: toggle_line_numbers_text,
    show: true
  },
  {
    icon: 'carly',
    id: 'wrap',
    title: toggle_line_wrap_text,
    show: false
  },
  {
    icon: 'expand',
    id: 'expand',
    title: resize_snippet,
    show: false
  }
];

function addLines(block) {
  let text = block.textContent;
  const snippet_fragment = [];
  if (text.includes('\n') && block.closest('pre') && !block.children.length) {
    text = text.split('\n');
    text.forEach((text_node, index) => {
      if(text_node.trim().length) {
        const new_node = `
        <span class="line line-flex">
          <span class="ln">${index + 1}</span>
          <span class="cl">${text_node.trim()}</span>
        </span>`.trim();
        // snippet_fragment.push(':;:');
        snippet_fragment.push(new_node);
        block.closest('pre').className = 'chroma';
        pushClass(block, 'language-unknown');
        block.dataset.lang = not_set;
      }
    });

    block.innerHTML = snippet_fragment.join('').trim(' ');
  }
}

function wrapOrphanedPreElements() {
  const pres = elems('pre');
  Array.from(pres).forEach(function(pre){
    const parent = pre.parentNode;
    const is_orpaned = !containsClass(parent, highlight);
    if(is_orpaned) {
      const pre_wrapper = createEl();
      pre_wrapper.className = highlight;
      const outer_wrapper = createEl();
      outer_wrapper.className = highlight_wrap;
      wrapEl(pre, pre_wrapper);
      wrapEl(pre_wrapper, outer_wrapper);
    }
  })
  /*
  @Todo
  1. Add UI control to orphaned blocks
  */
}

wrapOrphanedPreElements();

function codeBlocks() {
  const marked_code_blocks = elems('code');
  const blocks = Array.from(marked_code_blocks).filter(function(block){
    addLines(block);
    return block.closest("pre") && !Array.from(block.classList).includes('noClass');
  }).map(function(block){
    return block
  });
  return blocks;
}

function codeBlockFits(block) {
  // return false if codeblock overflows
  const block_width = block.offsetWidth;
  const highlight_block_width = block.closest(`.${highlight}`).offsetWidth;
  return block_width <= highlight_block_width ? true : false;
}

function maxHeightIsSet(elem) {
  let max_height = elem.style.maxHeight;
  return max_height.includes('px')
}

function restrainCodeBlockHeight(lines) {
  const last_line = lines[max_lines-1];
  let max_code_block_height = full_height;
  if(last_line) {
    const last_line_pos = last_line.offsetTop;
    if(last_line_pos !== 0) {
      max_code_block_height = `${last_line_pos}px`;
      const codeBlock = lines[0].parentNode;
      const outer_block = codeBlock.closest(`.${highlight}`);
      const is_expanded = containsClass(outer_block, panel_expanded);
      if(!is_expanded) {
        codeBlock.dataset.height = max_code_block_height;
        codeBlock.style.maxHeight = max_code_block_height;
      }
    }
  }
}

const blocks = codeBlocks();

function collapseCodeBlock(block) {
  const lines = elems(line_class, block);
  const code_lines = lines.length;
  if (code_lines > max_lines) {
    const expand_dot = createEl()
    pushClass(expand_dot, panel_expand);
    pushClass(expand_dot, panel_from);
    expand_dot.title = "Toggle snippet";
    expand_dot.textContent = "...";
    const outer_block = block.closest('.highlight');
    window.setTimeout(function(){
      const expand_icon = outer_block.nextElementSibling.lastElementChild;
      deleteClass(expand_icon, panel_hide);
    }, 150)

    restrainCodeBlockHeight(lines);
    const highlight_element = block.parentNode.parentNode;
    highlight_element.appendChild(expand_dot);
  }
}

blocks.forEach(function(block){
  collapseCodeBlock(block);
})

function actionPanel() {
  const panel = createEl();
  panel.className = panel_box;

  snippet_actions.forEach(function(button) {
    // create button
    const btn = createEl('a');
    btn.href = '#';
    btn.title = button.title;
    btn.className = `icon panel_icon panel_${button.id}`;
    button.show ? false : pushClass(btn, panel_hide);
    // load icon inside button
    loadSvg(button.icon, btn);
    // append button on panel
    panel.appendChild(btn);
  });

  return panel;
}

function toggleLineNumbers(elems) {
  if(elems) {
    // mark the code element when there are no lines
    elems.forEach(elem => modifyClass(elem, 'pre_nolines'));
    restrainCodeBlockHeight(elems);
  }
}

function toggleLineWrap(elem) {
  modifyClass(elem, 'pre_wrap');
  // retain max number of code lines on line wrap
  const lines = elems('.ln', elem);
  restrainCodeBlockHeight(lines);
}

function copyCode(code_element) {

  const copy_btn = code_element.parentNode.parentNode.querySelector(`.${copy_id}`);
  const original_title = copy_btn.title;
  loadSvg('check', copy_btn);
  copy_btn.title = copied_text;

  // remove line numbers before copying
  code_element = code_element.cloneNode(true);
  const line_numbers = elems('.ln', code_element);
  line_numbers.length ? line_numbers.forEach(line => line.remove()) : false;

  // remove leading '$' from all shell snippets
  let lines = elems('span', code_element);
  lines.forEach(line => {
    const text = line.textContent.trim(' ');
    if(text.indexOf('$') === 0) {
      line.textContent = line.textContent.replace('$ ', '');
    }
  })
  const snippet = code_element.textContent.trim(' ');
  // copy code
  copyToClipboard(snippet);

  setTimeout(function() {
    copy_btn.title = original_title;
    loadSvg('copy', copy_btn);
  }, 2250);
}

(function codeActions(){
  const highlight_wrap_id = highlight_wrap;
  blocks.forEach(function(block){
    // disable line numbers if disabled globally
    show_lines === false ? toggleLineNumbers(elems('.ln', block)) : false;

    const highlight_element = block.parentNode.parentNode;
    // wrap code block in a div
    const highlight_wrapper = createEl();
    highlight_wrapper.className = highlight_wrap_id;

    wrapEl(highlight_element, highlight_wrapper);

    const panel = actionPanel();
    // show wrap icon only if the code block needs wrapping
    const wrap_icon = elem(`.${wrap_id}`, panel);
    codeBlockFits(block) ? false : deleteClass(wrap_icon, panel_hide);

    // append buttons
    highlight_wrapper.appendChild(panel);
  });

  function isItem(target, id) {
    // if is item or within item
    return target.matches(`.${id}`) || target.closest(`.${id}`);
  }

  function showActive(target, targetClass) {
    const target_element = target.matches(`.${targetClass}`) ? target : target.closest(`.${targetClass}`);

    deleteClass(target_element, active);
    setTimeout(function() {
      modifyClass(target_element, active)
    }, 50)
  }

  doc.addEventListener('click', function(event){
    // copy code block
    const target = event.target;
    const is_copy_icon = isItem(target, copy_id);
    const is_wrap_icon = isItem(target, wrap_id);
    const is_lines_icon = isItem(target, lines_id);
    const is_expand_icon = isItem(target, panel_expand);
    const is_actionable = is_copy_icon || is_wrap_icon || is_lines_icon || is_expand_icon;

    if(is_actionable) {
      event.preventDefault();
      showActive(target, 'icon');
      const code_element = target.closest(`.${highlight_wrap_id}`).firstElementChild.firstElementChild;
      let lineNumbers = elems('.ln', code_element);

      is_wrap_icon ? toggleLineWrap(code_element) : false;
      is_lines_icon ? toggleLineNumbers(lineNumbers) : false;

      if (is_expand_icon) {
        let this_code_block = code_element.firstElementChild;
        const outer_block = this_code_block.closest('.highlight');
        if(maxHeightIsSet(this_code_block)) {
          this_code_block.style.maxHeight = full_height;
          // mark code block as expanded
          pushClass(outer_block, panel_expanded)
        } else {
          this_code_block.style.maxHeight = this_code_block.dataset.height;
          // unmark code block as expanded
          deleteClass(outer_block, panel_expanded)
        }
      }

      is_copy_icon ? copyCode(code_element) : false;
    }
  });

  (function addLangLabel() {
    blocks.forEach(block => {
      let label = block.dataset.lang;
      const is_shell_based = shell_based.includes(label);
      if(is_shell_based) {
        const lines = elems(line_class, block);
        Array.from(lines).forEach(line => {
          line = line.lastElementChild;
          let line_contents = line.textContent.trim(' ');
          line_contents.indexOf('$') !== 0 ? pushClass(line, 'shell') : false;
        });
      }

      label = label === 'sh' ? 'shell' : label;
      if(label !== "fallback") {
        const label_el = createEl();
        label_el.textContent = label;
        pushClass(label_el, 'lang');
        block.closest(`.${highlight_wrap}`).appendChild(label_el);
      }
    });
  })();
})();
