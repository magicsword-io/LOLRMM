'use strict';

// global variables;
const doc = document.documentElement;
const toggle_id = 'toggle';
const show_id = 'show';
const menu = 'menu';
const active = 'active';
// root_url must end with '/' for relative URLs to work properly
let root_url = '{{ strings.TrimSuffix "/" .Site.BaseURL }}/';
root_url = root_url.startsWith('http') ? root_url : window.location.origin;

const search_field_class = '.search_field';
const search_class = '.search';
const go_back_class = 'button_back';
const line_class = '.line';

// config defined values
const code_block_config = JSON.parse('{{ partial "functions/getCodeConfig" . }}');
const iconsPath = `{{ partialCached "functions/getIconPath" . }}`;

// values defined under config/_default/params.toml
let other_searchable_fields = '{{ delimit (default slice site.Params.otherSearchableFields) ", " }}'

if(other_searchable_fields.length > 2) {
  other_searchable_fields = other_searchable_fields
    .split(",")
    .map(search_value => search_value.toLowerCase().trim());
} else {
  other_searchable_fields = [];
}

// defined in i18n / translation files
const quick_links = '{{ T "quick_links" }}';
const search_results_label = '{{ T "search_results_label" }}';
const short_search_query = '{{ T "short_search_query" }}'
const type_to_search = '{{ T "type_to_search" }}';
const no_matches_found = '{{ T "no_matches" }}';
const copy_text = '{{ T "copy" }}';
const copied_text = '{{ T "copied" }}';
const toggle_line_numbers_text = '{{ T "toggle_line_numbers" }}';
const toggle_line_wrap_text = '{{ T "toggle_line_wrap" }}';
const resize_snippet = '{{ T "resize_snippet" }}';
const not_set = '{{ T "not_set" }}';

const shell_based = ['sh', 'shell', 'zsh', 'bash'];

const body = elem('body');
const max_lines = code_block_config.maximum;
const show_lines = code_block_config.show;
const copy_id = 'panel_copy';
const wrap_id = 'panel_wrap';
const lines_id = 'panel_lines';
const panel_expand = 'panel_expand';
const panel_expanded = 'panel_expanded';
const panel_box = 'panel_box';
const panel_hide = 'panel_hide';
const panel_from = 'panel_from';
const full_height = 'initial';
const highlight = 'highlight';
const highlight_wrap = 'highlight_wrap'

const light = 'light';
const dark = 'dark';
const storageKey = 'colorMode';
const key = '--color-mode';
const mode_data = 'data-mode';
const bank = window.localStorage;
