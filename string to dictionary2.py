<!DOCTYPE html>
<!-- saved from url=(0030)https://www.online-python.com/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style>#ace_settingsmenu, #kbshortcutmenu {background-color: #F7F7F7;color: black;box-shadow: -5px 4px 5px rgba(126, 126, 126, 0.55);padding: 1em 0.5em 2em 1em;overflow: auto;position: absolute;margin: 0;bottom: 0;right: 0;top: 0;z-index: 9991;cursor: default;}.ace_dark #ace_settingsmenu, .ace_dark #kbshortcutmenu {box-shadow: -20px 10px 25px rgba(126, 126, 126, 0.25);background-color: rgba(255, 255, 255, 0.6);color: black;}.ace_optionsMenuEntry:hover {background-color: rgba(100, 100, 100, 0.1);transition: all 0.3s}.ace_closeButton {background: rgba(245, 146, 146, 0.5);border: 1px solid #F48A8A;border-radius: 50%;padding: 7px;position: absolute;right: -8px;top: -8px;z-index: 100000;}.ace_closeButton{background: rgba(245, 146, 146, 0.9);}.ace_optionsMenuKey {color: darkslateblue;font-weight: bold;}.ace_optionsMenuCommand {color: darkcyan;font-weight: normal;}.ace_optionsMenuEntry input, .ace_optionsMenuEntry button {vertical-align: middle;}.ace_optionsMenuEntry button[ace_selected_button=true] {background: #e7e7e7;box-shadow: 1px 0px 2px 0px #adadad inset;border-color: #adadad;}.ace_optionsMenuEntry button {background: white;border: 1px solid lightgray;margin: 0px;}.ace_optionsMenuEntry button:hover{background: #f0f0f0;}</style><style id="autocompletion.css">.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {    background-color: #CAD6FA;    z-index: 1;}.ace_dark.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {    background-color: #3a674e;}.ace_editor.ace_autocomplete .ace_line-hover {    border: 1px solid #abbffe;    margin-top: -1px;    background: rgba(233,233,253,0.4);    position: absolute;    z-index: 2;}.ace_dark.ace_editor.ace_autocomplete .ace_line-hover {    border: 1px solid rgba(109, 150, 13, 0.8);    background: rgba(58, 103, 78, 0.62);}.ace_completion-meta {    opacity: 0.5;    margin: 0.9em;}.ace_completion-message {    color: blue;}.ace_editor.ace_autocomplete .ace_completion-highlight{    color: #2d69c7;}.ace_dark.ace_editor.ace_autocomplete .ace_completion-highlight{    color: #93ca12;}.ace_editor.ace_autocomplete {    width: 300px;    z-index: 200000;    border: 1px lightgray solid;    position: fixed;    box-shadow: 2px 3px 5px rgba(0,0,0,.2);    line-height: 1.4;    background: #fefefe;    color: #111;}.ace_dark.ace_editor.ace_autocomplete {    border: 1px #484747 solid;    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.51);    line-height: 1.4;    background: #25282c;    color: #c1c1c1;}
/*# sourceURL=ace/css/autocompletion.css */</style><style>.ace_snippet-marker {    -moz-box-sizing: border-box;    box-sizing: border-box;    background: rgba(194, 193, 208, 0.09);    border: 1px dotted rgba(211, 208, 235, 0.62);    position: absolute;}</style><style>    .error_widget_wrapper {        background: inherit;        color: inherit;        border:none    }    .error_widget {        border-top: solid 2px;        border-bottom: solid 2px;        margin: 5px 0;        padding: 10px 40px;        white-space: pre-wrap;    }    .error_widget.ace_error, .error_widget_arrow.ace_error{        border-color: #ff5a5a    }    .error_widget.ace_warning, .error_widget_arrow.ace_warning{        border-color: #F1D817    }    .error_widget.ace_info, .error_widget_arrow.ace_info{        border-color: #5a5a5a    }    .error_widget.ace_ok, .error_widget_arrow.ace_ok{        border-color: #5aaa5a    }    .error_widget_arrow {        position: absolute;        border: solid 5px;        border-top-color: transparent!important;        border-right-color: transparent!important;        border-left-color: transparent!important;        top: -5px;    }</style><style id="ace-tm">.ace-tm .ace_gutter {background: #f0f0f0;color: #333;}.ace-tm .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-tm .ace_fold {background-color: #6B72E6;}.ace-tm {background-color: #FFFFFF;color: black;}.ace-tm .ace_cursor {color: black;}.ace-tm .ace_invisible {color: rgb(191, 191, 191);}.ace-tm .ace_storage,.ace-tm .ace_keyword {color: blue;}.ace-tm .ace_constant {color: rgb(197, 6, 11);}.ace-tm .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-tm .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-tm .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-tm .ace_invalid {background-color: rgba(255, 0, 0, 0.1);color: red;}.ace-tm .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-tm .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-tm .ace_support.ace_type,.ace-tm .ace_support.ace_class {color: rgb(109, 121, 222);}.ace-tm .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-tm .ace_string {color: rgb(3, 106, 7);}.ace-tm .ace_comment {color: rgb(76, 136, 107);}.ace-tm .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-tm .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-tm .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-tm .ace_variable {color: rgb(49, 132, 149);}.ace-tm .ace_xml-pe {color: rgb(104, 104, 91);}.ace-tm .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-tm .ace_heading {color: rgb(12, 7, 255);}.ace-tm .ace_list {color:rgb(185, 6, 144);}.ace-tm .ace_meta.ace_tag {color:rgb(0, 22, 142);}.ace-tm .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-tm .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-tm.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-tm .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-tm .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-tm .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-tm .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-tm .ace_gutter-active-line {background-color : #dcdcdc;}.ace-tm .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-tm .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-tm */</style><style id="ace_editor.css">.ace_br1 {border-top-left-radius    : 3px;}.ace_br2 {border-top-right-radius   : 3px;}.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}.ace_br4 {border-bottom-right-radius: 3px;}.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}.ace_br8 {border-bottom-left-radius : 3px;}.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}.ace_editor {position: relative;overflow: hidden;font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;direction: ltr;text-align: left;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);}.ace_scroller {position: absolute;overflow: hidden;top: 0;bottom: 0;background-color: inherit;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;cursor: text;}.ace_content {position: absolute;box-sizing: border-box;min-width: 100%;contain: style size layout;font-variant-ligatures: no-common-ligatures;}.ace_dragging .ace_scroller:before{position: absolute;top: 0;left: 0;right: 0;bottom: 0;content: '';background: rgba(250, 250, 250, 0.01);z-index: 1000;}.ace_dragging.ace_dark .ace_scroller:before{background: rgba(0, 0, 0, 0.01);}.ace_selecting, .ace_selecting * {cursor: text !important;}.ace_gutter {position: absolute;overflow : hidden;width: auto;top: 0;bottom: 0;left: 0;cursor: default;z-index: 4;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;contain: style size layout;}.ace_gutter-active-line {position: absolute;left: 0;right: 0;}.ace_scroller.ace_scroll-left {box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;}.ace_gutter-cell {position: absolute;top: 0;left: 0;right: 0;padding-left: 19px;padding-right: 6px;background-repeat: no-repeat;}.ace_gutter-cell.ace_error {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: 2px center;}.ace_gutter-cell.ace_warning {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");background-position: 2px center;}.ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");background-position: 2px center;}.ace_dark .ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");}.ace_scrollbar {contain: strict;position: absolute;right: 0;bottom: 0;z-index: 6;}.ace_scrollbar-inner {position: absolute;cursor: text;left: 0;top: 0;}.ace_scrollbar-v{overflow-x: hidden;overflow-y: scroll;top: 0;}.ace_scrollbar-h {overflow-x: scroll;overflow-y: hidden;left: 0;}.ace_print-margin {position: absolute;height: 100%;}.ace_text-input {position: absolute;z-index: 0;width: 0.5em;height: 1em;opacity: 0;background: transparent;-moz-appearance: none;appearance: none;border: none;resize: none;outline: none;overflow: hidden;font: inherit;padding: 0 1px;margin: 0 -1px;contain: strict;-ms-user-select: text;-moz-user-select: text;-webkit-user-select: text;user-select: text;white-space: pre!important;}.ace_text-input.ace_composition {background: transparent;color: inherit;z-index: 1000;opacity: 1;}.ace_composition_placeholder { color: transparent }.ace_composition_marker { border-bottom: 1px solid;position: absolute;border-radius: 0;margin-top: 1px;}[ace_nocontext=true] {transform: none!important;filter: none!important;clip-path: none!important;mask : none!important;contain: none!important;perspective: none!important;mix-blend-mode: initial!important;z-index: auto;}.ace_layer {z-index: 1;position: absolute;overflow: hidden;word-wrap: normal;white-space: pre;height: 100%;width: 100%;box-sizing: border-box;pointer-events: none;}.ace_gutter-layer {position: relative;width: auto;text-align: right;pointer-events: auto;height: 1000000px;contain: style size layout;}.ace_text-layer {font: inherit !important;position: absolute;height: 1000000px;width: 1000000px;contain: style size layout;}.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {contain: style size layout;position: absolute;top: 0;left: 0;right: 0;}.ace_hidpi .ace_text-layer,.ace_hidpi .ace_gutter-layer,.ace_hidpi .ace_content,.ace_hidpi .ace_gutter {contain: strict;will-change: transform;}.ace_hidpi .ace_text-layer > .ace_line, .ace_hidpi .ace_text-layer > .ace_line_group {contain: strict;}.ace_cjk {display: inline-block;text-align: center;}.ace_cursor-layer {z-index: 4;}.ace_cursor {z-index: 4;position: absolute;box-sizing: border-box;border-left: 2px solid;transform: translatez(0);}.ace_multiselect .ace_cursor {border-left-width: 1px;}.ace_slim-cursors .ace_cursor {border-left-width: 1px;}.ace_overwrite-cursors .ace_cursor {border-left-width: 0;border-bottom: 1px solid;}.ace_hidden-cursors .ace_cursor {opacity: 0.2;}.ace_hasPlaceholder .ace_hidden-cursors .ace_cursor {opacity: 0;}.ace_smooth-blinking .ace_cursor {transition: opacity 0.18s;}.ace_animate-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: step-end;animation-name: blink-ace-animate;animation-iteration-count: infinite;}.ace_animate-blinking.ace_smooth-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: ease-in-out;animation-name: blink-ace-animate-smooth;}@keyframes blink-ace-animate {from, to { opacity: 1; }60% { opacity: 0; }}@keyframes blink-ace-animate-smooth {from, to { opacity: 1; }45% { opacity: 1; }60% { opacity: 0; }85% { opacity: 0; }}.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {position: absolute;z-index: 3;}.ace_marker-layer .ace_selection {position: absolute;z-index: 5;}.ace_marker-layer .ace_bracket {position: absolute;z-index: 6;}.ace_marker-layer .ace_error_bracket {position: absolute;border-bottom: 1px solid #DE5555;border-radius: 0;}.ace_marker-layer .ace_active-line {position: absolute;z-index: 2;}.ace_marker-layer .ace_selected-word {position: absolute;z-index: 4;box-sizing: border-box;}.ace_line .ace_fold {box-sizing: border-box;display: inline-block;height: 11px;margin-top: -2px;vertical-align: middle;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");background-repeat: no-repeat, repeat-x;background-position: center center, top left;color: transparent;border: 1px solid black;border-radius: 2px;cursor: pointer;pointer-events: auto;}.ace_dark .ace_fold {}.ace_fold:hover{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");}.ace_tooltip {background-color: #FFF;background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));border: 1px solid gray;border-radius: 1px;box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);color: black;max-width: 100%;padding: 3px 4px;position: fixed;z-index: 999999;box-sizing: border-box;cursor: default;white-space: pre;word-wrap: break-word;line-height: normal;font-style: normal;font-weight: normal;letter-spacing: normal;pointer-events: none;}.ace_folding-enabled > .ace_gutter-cell {padding-right: 13px;}.ace_fold-widget {box-sizing: border-box;margin: 0 -12px 0 1px;display: none;width: 11px;vertical-align: top;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: center;border-radius: 3px;border: 1px solid transparent;cursor: pointer;}.ace_folding-enabled .ace_fold-widget {display: inline-block;   }.ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");}.ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");}.ace_fold-widget:hover {border: 1px solid rgba(0, 0, 0, 0.3);background-color: rgba(255, 255, 255, 0.2);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);}.ace_fold-widget:active {border: 1px solid rgba(0, 0, 0, 0.4);background-color: rgba(0, 0, 0, 0.05);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);}.ace_dark .ace_fold-widget {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");}.ace_dark .ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget:hover {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);background-color: rgba(255, 255, 255, 0.1);}.ace_dark .ace_fold-widget:active {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);}.ace_inline_button {border: 1px solid lightgray;display: inline-block;margin: -1px 8px;padding: 0 5px;pointer-events: auto;cursor: pointer;}.ace_inline_button:hover {border-color: gray;background: rgba(200,200,200,0.2);display: inline-block;pointer-events: auto;}.ace_fold-widget.ace_invalid {background-color: #FFB4B4;border-color: #DE5555;}.ace_fade-fold-widgets .ace_fold-widget {transition: opacity 0.4s ease 0.05s;opacity: 0;}.ace_fade-fold-widgets:hover .ace_fold-widget {transition: opacity 0.05s ease 0.05s;opacity:1;}.ace_underline {text-decoration: underline;}.ace_bold {font-weight: bold;}.ace_nobold .ace_bold {font-weight: normal;}.ace_italic {font-style: italic;}.ace_error-marker {background-color: rgba(255, 0, 0,0.2);position: absolute;z-index: 9;}.ace_highlight-marker {background-color: rgba(255, 255, 0,0.2);position: absolute;z-index: 8;}.ace_mobile-menu {position: absolute;line-height: 1.5;border-radius: 4px;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;background: white;box-shadow: 1px 3px 2px grey;border: 1px solid #dcdcdc;color: black;}.ace_dark > .ace_mobile-menu {background: #333;color: #ccc;box-shadow: 1px 3px 2px grey;border: 1px solid #444;}.ace_mobile-button {padding: 2px;cursor: pointer;overflow: hidden;}.ace_mobile-button:hover {background-color: #eee;opacity:1;}.ace_mobile-button:active {background-color: #ddd;}.ace_placeholder {font-family: arial;transform: scale(0.9);transform-origin: left;white-space: pre;opacity: 0.7;margin: 0 10px;}
/*# sourceURL=ace/css/ace_editor.css */</style><script src="./string to dictionary2_files/973535300821278" async=""></script><script async="" src="./string to dictionary2_files/fbevents.js.download"></script><script async="" src="./string to dictionary2_files/coreid.min.js.download"></script><script async="" src="./string to dictionary2_files/launcher.min.js.download"></script><script src="./string to dictionary2_files/rules-p-31iz6hfFutd16.js.download" async=""></script><script src="./string to dictionary2_files/quant.js.download" async="true"></script><script async="" defer="" src="./string to dictionary2_files/launchpad.bundle.js.download"></script><script src="./string to dictionary2_files/hadron.js.download"></script><script src="./string to dictionary2_files/apstag.js.download" async="true"></script><script type="text/javascript" async="" src="./string to dictionary2_files/analytics.js.download"></script><script type="text/javascript" async="" src="./string to dictionary2_files/js"></script><script src="./string to dictionary2_files/f.txt"></script><script>var __ezHttpConsent={setByCat:function(src,tagType,attributes,category,force){var setScript=function(){if(force||window.ezTcfConsent[category]){var scriptElement=document.createElement(tagType);scriptElement.src=src;attributes.forEach(function(attr){for(var key in attr){if(attr.hasOwnProperty(key)){scriptElement.setAttribute(key,attr[key]);}}});var firstScript=document.getElementsByTagName(tagType)[0];firstScript.parentNode.insertBefore(scriptElement,firstScript);}};if(force||(window.ezTcfConsent&&window.ezTcfConsent.loaded)){setScript();}else if(typeof getEzConsentData==="function"){getEzConsentData().then(function(ezTcfConsent){if(ezTcfConsent&&ezTcfConsent.loaded){setScript();}else{console.error("cannot get ez consent data");force=true;setScript();}});}else{force=true;setScript();console.error("getEzConsentData is not a function");}},};</script>
<script>var ezTcfConsent=window.ezTcfConsent?window.ezTcfConsent:{loaded:false,store_info:false,develop_and_improve_services:false,measure_ad_performance:false,measure_content_performance:false,select_basic_ads:false,create_ad_profile:false,select_personalized_ads:false,create_content_profile:false,select_personalized_content:false,understand_audiences:false,use_limited_data_to_select_content:false,};function getEzConsentData(){return new Promise(function(resolve){document.addEventListener("ezConsentEvent",function(event){var ezTcfConsent=event.detail.ezTcfConsent;resolve(ezTcfConsent);});});}</script>
<script>function _setEzCookies(ezConsentData){var cookies=[{name:"ezosuibasgeneris-1",value:"64db2719-960b-47bd-76e1-1b6e57de3e4a; Path=/; Domain=online-python.com; Expires=Fri, 07 Nov 2025 08:06:09 UTC; Secure; SameSite=None",tcfCategory:"understand_audiences",isEzoic:"true",},{name:"ezopvc_214055",value:"1; Path=/; Domain=online-python.com; Expires=Thu, 07 Nov 2024 08:36:09 UTC",tcfCategory:"understand_audiences",isEzoic:"true",},{name:"ezoab_214055",value:"mod1-c; Path=/; Domain=online-python.com; Max-Age=7200",tcfCategory:"store_info",isEzoic:"true",},{name:"active_template::214055",value:"pub_site.1730966872; Path=/; Domain=online-python.com; Expires=Sat, 09 Nov 2024 08:07:52 UTC",tcfCategory:"store_info",isEzoic:"true",},{name:"ezoadgid_214055",value:"-1; Path=/; Domain=online-python.com; Max-Age=1800",tcfCategory:"understand_audiences",isEzoic:"true",}];for(var i=0;i<cookies.length;i++){var cookie=cookies[i];if(ezConsentData&&ezConsentData.loaded&&ezConsentData[cookie.tcfCategory]){document.cookie=cookie.name+"="+cookie.value;}}}
if(window.ezTcfConsent&&window.ezTcfConsent.loaded){_setEzCookies(window.ezTcfConsent);}else if(typeof getEzConsentData==="function"){getEzConsentData().then(function(ezTcfConsent){if(ezTcfConsent&&ezTcfConsent.loaded){_setEzCookies(window.ezTcfConsent);}else{console.error("cannot get ez consent data");_setEzCookies(window.ezTcfConsent);}});}else{console.error("getEzConsentData is not a function");_setEzCookies(window.ezTcfConsent);}</script><script type="text/javascript" data-ezscrex="false" data-cfasync="false">window._ezaq = Object.assign({"edge_cache_status":34,"edge_response_time":4,"url":"https://www.online-python.com/"}, typeof window._ezaq !== "undefined" ? window._ezaq : {});</script><script type="text/javascript" data-ezscrex="false" data-cfasync="false">window._ezaq = Object.assign({"ezcache_level":2}, typeof window._ezaq !== "undefined" ? window._ezaq : {});</script><script type="text/javascript" data-ezscrex="false" data-cfasync="false">window._ezaq = Object.assign({"ab_test_id":"mod1-c"}, typeof window._ezaq !== "undefined" ? window._ezaq : {});window.__ez=window.__ez||{};window.__ez.tf={};</script><script data-ezscrex="false" data-cfasync="false" data-pagespeed-no-defer="">var __ez=__ez||{};__ez.stms=Date.now();__ez.evt={};__ez.script={};__ez.ck=__ez.ck||{};__ez.template={};__ez.template.isOrig=false;__ez.queue=function(){var e=0,i=0,t=[],n=!1,o=[],r=[],s=!0,a=function(e,i,n,o,r,s,a){var l=arguments.length>7&&void 0!==arguments[7]?arguments[7]:window,d=this;this.name=e,this.funcName=i,this.parameters=null===n?null:w(n)?n:[n],this.isBlock=o,this.blockedBy=r,this.deleteWhenComplete=s,this.isError=!1,this.isComplete=!1,this.isInitialized=!1,this.proceedIfError=a,this.fWindow=l,this.isTimeDelay=!1,this.process=function(){u("... func = "+e),d.isInitialized=!0,d.isComplete=!0,u("... func.apply: "+e);var i=d.funcName.split("."),n=null,o=this.fWindow||window;i.length>3||(n=3===i.length?o[i[0]][i[1]][i[2]]:2===i.length?o[i[0]][i[1]]:o[d.funcName]),null!=n&&n.apply(null,this.parameters),!0===d.deleteWhenComplete&&delete t[e],!0===d.isBlock&&(u("----- F'D: "+d.name),m())}},l=function(e,i,t,n,o,r,s){var a=arguments.length>7&&void 0!==arguments[7]?arguments[7]:window,l=this;this.name=e,this.path=i,this.async=o,this.defer=r,this.isBlock=t,this.blockedBy=n,this.isInitialized=!1,this.isError=!1,this.isComplete=!1,this.proceedIfError=s,this.fWindow=a,this.isTimeDelay=!1,this.isPath=function(e){return"/"===e[0]&&"/"!==e[1]},this.getSrc=function(e){return void 0!==window.__ezScriptHost&&this.isPath(e)&&"banger.js"!==this.name?window.__ezScriptHost+e:e},this.process=function(){l.isInitialized=!0,u("... file = "+e);var i=this.fWindow?this.fWindow.document:document,t=i.createElement("script");t.src=this.getSrc(this.path),!0===o?t.async=!0:!0===r&&(t.defer=!0),t.onerror=function(){var e={url:window.location.href,name:l.name,path:l.path,user_agent:window.navigator.userAgent};"undefined"!=typeof _ezaq&&(e.pageview_id=_ezaq.page_view_id);var i=encodeURIComponent(JSON.stringify(e)),t=new XMLHttpRequest;t.open("GET","//g.ezoic.net/ezqlog?d="+i,!0),t.send(),u("----- ERR'D: "+l.name),l.isError=!0,!0===l.isBlock&&m()},t.onreadystatechange=t.onload=function(){var e=t.readyState;u("----- F'D: "+l.name),e&&!/loaded|complete/.test(e)||(l.isComplete=!0,!0===l.isBlock&&m())},i.getElementsByTagName("head")[0].appendChild(t)}},d=function(e,i){this.name=e,this.path="",this.async=!1,this.defer=!1,this.isBlock=!1,this.blockedBy=[],this.isInitialized=!0,this.isError=!1,this.isComplete=i,this.proceedIfError=!1,this.isTimeDelay=!1,this.process=function(){}};function c(e,i,n,s,a,d,c,f,u){var m=new l(e,i,n,s,a,d,c,u);!0===f?o[e]=m:r[e]=m,t[e]=m,h(m)}function h(e){!0!==f(e)&&0!=s&&e.process()}function f(e){if(!0===e.isTimeDelay&&!1===n)return u(e.name+" blocked = TIME DELAY!"),!0;if(w(e.blockedBy))for(var i=0;i<e.blockedBy.length;i++){var o=e.blockedBy[i];if(!1===t.hasOwnProperty(o))return u(e.name+" blocked = "+o),!0;if(!0===e.proceedIfError&&!0===t[o].isError)return!1;if(!1===t[o].isComplete)return u(e.name+" blocked = "+o),!0}return!1}function u(e){var i=window.location.href,t=new RegExp("[?&]ezq=([^&#]*)","i").exec(i);"1"===(t?t[1]:null)&&console.debug(e)}function m(){++e>200||(u("let's go"),p(o),p(r))}function p(e){for(var i in e)if(!1!==e.hasOwnProperty(i)){var t=e[i];!0===t.isComplete||f(t)||!0===t.isInitialized||!0===t.isError?!0===t.isError?u(t.name+": error"):!0===t.isComplete?u(t.name+": complete already"):!0===t.isInitialized&&u(t.name+": initialized already"):t.process()}}function w(e){return"[object Array]"==Object.prototype.toString.call(e)}return window.addEventListener("load",(function(){setTimeout((function(){n=!0,u("TDELAY -----"),m()}),5e3)}),!1),{addFile:c,addFileOnce:function(e,i,n,o,r,s,a,l,d){t[e]||c(e,i,n,o,r,s,a,l,d)},addDelayFile:function(e,i){var n=new l(e,i,!1,[],!1,!1,!0);n.isTimeDelay=!0,u(e+" ...  FILE! TDELAY"),r[e]=n,t[e]=n,h(n)},addFunc:function(e,n,s,l,d,c,f,u,m,p){!0===c&&(e=e+"_"+i++);var w=new a(e,n,s,l,d,f,u,p);!0===m?o[e]=w:r[e]=w,t[e]=w,h(w)},addDelayFunc:function(e,i,n){var o=new a(e,i,n,!1,[],!0,!0);o.isTimeDelay=!0,u(e+" ...  FUNCTION! TDELAY"),r[e]=o,t[e]=o,h(o)},items:t,processAll:m,setallowLoad:function(e){s=e},markLoaded:function(e){if(e&&0!==e.length){if(e in t){var i=t[e];!0===i.isComplete?u(i.name+" "+e+": error loaded duplicate"):(i.isComplete=!0,i.isInitialized=!0)}else t[e]=new d(e,!0);u("markLoaded dummyfile: "+t[e].name)}},logWhatsBlocked:function(){for(var e in t)!1!==t.hasOwnProperty(e)&&f(t[e])}}}();__ez.evt.add=function(e,t,n){e.addEventListener?e.addEventListener(t,n,!1):e.attachEvent?e.attachEvent("on"+t,n):e["on"+t]=n()},__ez.evt.remove=function(e,t,n){e.removeEventListener?e.removeEventListener(t,n,!1):e.detachEvent?e.detachEvent("on"+t,n):delete e["on"+t]};__ez.script.add=function(e){var t=document.createElement("script");t.src=e,t.async=!0,t.type="text/javascript",document.getElementsByTagName("head")[0].appendChild(t)};__ez.dot={};__ez.queue.addFile('/detroitchicago/boise.js', '/detroitchicago/boise.js?gcb=195-1&cb=5', true, [], true, false, true, false);__ez.queue.addFile('/parsonsmaize/abilene.js', '/parsonsmaize/abilene.js?gcb=195-1&cb=41', true, [], true, false, true, false);</script><script src="./string to dictionary2_files/boise.js.download" async=""></script><script src="./string to dictionary2_files/abilene.js.download" async=""></script>
<script data-ezscrex="false" data-cfasync="false">__ez.ssaf=[];__ez.sswp=4;__ez.ssv=686310;__ez.sshsdef=false;</script>
<script data-ezscrex="false" data-cfasync="false">(function(){if("function"===typeof window.CustomEvent)return!1;window.CustomEvent=function(c,a){a=a||{bubbles:!1,cancelable:!1,detail:null};var b=document.createEvent("CustomEvent");b.initCustomEvent(c,a.bubbles,a.cancelable,a.detail);return b}})();</script><script data-ezscrex="false" data-cfasync="false">__ez.queue.addFile('/detroitchicago/tulsa.js', '/detroitchicago/tulsa.js?gcb=195-1&cb=9', false, [], true, false, true, false);</script><script src="./string to dictionary2_files/tulsa.js.download" async=""></script>
<script data-ezscrex="false" type="text/javascript" data-cfasync="false">window._ezaq = Object.assign({"ad_cache_level":1,"adpicker_placement_cnt":0,"ai_placeholder_cache_level":1,"ai_placeholder_placement_cnt":-1,"author":"online-python","domain_id":214055,"ezcache_level":2,"ezcache_skip_code":0,"has_bad_image":0,"has_bad_words":0,"is_sitespeed":1,"lt_cache_level":0,"response_size":44280,"response_size_orig":36154,"response_time_orig":2,"template_id":134,"url":"https://www.online-python.com/","word_count":870,"worst_bad_word_level":0}, typeof window._ezaq !== "undefined" ? window._ezaq : {});__ez.queue.markLoaded('ezaqBaseReady');</script>
<link rel="preconnect" href="https://cdnjs.cloudflare.com/" crossorigin="">
<link rel="preconnect" href="https://fonts.googleapis.com/" crossorigin="">
<link rel="preconnect" href="https://www.googletagmanager.com/" crossorigin="">
<link rel="preconnect" href="https://pagead2.googlesyndication.com/" crossorigin="">
<link rel="preconnect" href="https://s7.addthis.com/" crossorigin="">
<link rel="preconnect" href="https://go.ezoic.net/" crossorigin="">
<link rel="preload" as="script" href="./string to dictionary2_files/f(2).txt">
<link rel="preload" as="script" href="./string to dictionary2_files/dall.js.download">
<script type="text/javascript">(function(){function storageAvailable(type){var storage;try{storage=window[type];var x='__storage_test__';storage.setItem(x,x);storage.removeItem(x);return true;}
catch(e){return e instanceof DOMException&&(e.code===22||e.code===1014||e.name==='QuotaExceededError'||e.name==='NS_ERROR_DOM_QUOTA_REACHED')&&(storage&&storage.length!==0);}}
function remove_ama_config(){if(storageAvailable('localStorage')){localStorage.removeItem("google_ama_config");}}
remove_ama_config()})()</script>
<script type="text/javascript">var ezoicTestActive = true</script>
<script type="text/javascript" data-ezscrex="false" data-cfasync="false">
window.ezAnalyticsStatic = true;

function analyticsAddScript(script) {
	var ezDynamic = document.createElement('script');
	ezDynamic.type = 'text/javascript';
	ezDynamic.innerHTML = script;
	document.head.appendChild(ezDynamic);
}
function getCookiesWithPrefix() {
    var allCookies = document.cookie.split(';');
    var cookiesWithPrefix = {};

    for (var i = 0; i < allCookies.length; i++) {
        var cookie = allCookies[i].trim();

        for (var j = 0; j < arguments.length; j++) {
            var prefix = arguments[j];
            if (cookie.indexOf(prefix) === 0) {
                var cookieParts = cookie.split('=');
                var cookieName = cookieParts[0];
                var cookieValue = cookieParts.slice(1).join('=');
                cookiesWithPrefix[cookieName] = decodeURIComponent(cookieValue);
                break; // Once matched, no need to check other prefixes
            }
        }
    }

    return cookiesWithPrefix;
}
function productAnalytics() {
	var d = {"pr":[6,3,2,1],"aop":{"12":0,"14":0,"2":0,"21":0,"26":0,"4":134,"7":0,"8":0},"omd5":"1416d76a920395e52c8f1cd047529e93"};
	d.u = _ezaq.url;
	d.p = _ezaq.page_view_id;
	d.v = _ezaq.visit_uuid;
	d.ab = _ezaq.ab_test_id;
	d.e = JSON.stringify(_ezaq);
	d.ref = document.referrer;
	d.c = getCookiesWithPrefix('active_template', 'ez', 'lp_');
	if(typeof ez_utmParams !== 'undefined') {
		d.utm = ez_utmParams;
	}

	var dataText = JSON.stringify(d);
	var xhr = new XMLHttpRequest();
	xhr.open('POST','/ezais/analytics?cb=1', true);
	xhr.onload = function () {
		if (xhr.status!=200) {
            return;
		}

        if(document.readyState !== 'loading') {
            analyticsAddScript(xhr.response);
            return;
        }

        var eventFunc = function() {
            if(document.readyState === 'loading') {
                return;
            }
            document.removeEventListener('readystatechange', eventFunc, false);
            analyticsAddScript(xhr.response);
        };

        document.addEventListener('readystatechange', eventFunc, false);
	};
	xhr.setRequestHeader('Content-Type','text/plain');
	xhr.send(dataText);
}
__ez.queue.addFunc("productAnalytics", "productAnalytics", null, true, ['ezaqBaseReady'], false, false, false, true);
</script><script type="text/javascript" data-ezscrex="false" data-cfasync="false" async="">
function productEzoicAds() {
if(window.ezDisableAds === true) {
	return;
}
window.google_reactive_ads_global_state = {
                adCount: {},
                floatingAdsStacking: { maxZIndexListeners: [], maxZIndexRestrictions: {}, nextRestrictionId: 0 },
                messageValidationEnabled: false,
                reactiveTypeDisabledByPublisher: {},
                reactiveTypeEnabledInAsfe: {},
                sideRailAvailableSpace: [],
                sideRailOverlappableElements: [],
                stateForType: {},
                tagSpecificState: {},
                wasPlaTagProcessed: true,
                wasReactiveAdConfigReceived: { 1: true, 2: true, 8: true },
                wasReactiveAdVisible: {},
                wasReactiveTagRequestSent: true,
                description: "Can't disable auto ads programmatically on the page, so here we are!"
            };
var d = {"ab":"","km":{},"pv":"","vu":"34855c16-bdfa-4898-4f78-89a202417840","r":{"r":[{"p":" ezoic_pub_ad_placeholder-119-top_of_page-160x600-119-nonexxxnonexxxxxxezmaxscaleval100 ","s":119,"h":600,"w":250,"r":true},{"p":" ezoic_pub_ad_placeholder-114-under_page_title-250x250-114-nonexxxnonexxxxxxezmaxscaleval100 ","s":114},{"p":" ezoic_pub_ad_placeholder-114-under_page_title-300x250-114-nonexxxnonexxxxxxezmaxscaleval100 ","s":114},{"p":" ezoic_pub_ad_placeholder-114-under_page_title-336x280-114-nonexxxnonexxxxxxezmaxscaleval100 ","s":114},{"p":" ezoic_pub_ad_placeholder-114-under_page_title-320x100v2-114-nonexxxnonexxxxxxezmaxscaleval100 ","s":114},{"p":" ezoic_pub_ad_placeholder-117-under_second_paragraph-970x90-117-nonexxxnonexxxxxxezmaxscaleval100 ","s":117,"h":280,"w":970,"r":true},{"p":" ezoic_pub_ad_placeholder-122-bottom_of_page-250x250-122-nonexxxnonexxxxxxezmaxscaleval100 ","s":122},{"p":" ezoic_pub_ad_placeholder-122-bottom_of_page-300x250-122-nonexxxnonexxxxxxezmaxscaleval100 ","s":122},{"p":" ezoic_pub_ad_placeholder-122-bottom_of_page-336x280-122-nonexxxnonexxxxxxezmaxscaleval100 ","s":122},{"p":" ezoic_pub_ad_placeholder-122-bottom_of_page-320x100v2-122-nonexxxnonexxxxxxezmaxscaleval100 ","s":122},{"p":" ezoic_pub_ad_placeholder-122-bottom_of_page-728x90-122-nonexxxnonexxxxxxezmaxscaleval100 ","s":122},{"p":" ezoic_pub_ad_placeholder-122-bottom_of_page-970x250-122-nonexxxnonexxxxxxezmaxscaleval100 ","s":122,"h":280,"w":970},{"p":" ezoic_pub_ad_placeholder-122-bottom_of_page-300x250x3-122-nonexxxnonexxxxxxezmaxscaleval100 ","s":122},{"p":" ezoic_pub_ad_placeholder-122-bottom_of_page-970x90-122-nonexxxnonexxxxxxezmaxscaleval100 ","s":122},{"p":" ezoic_pub_ad_placeholder-136-under_first_paragraph-160x600-136-nonexxxnonexxxxxxezmaxscaleval100 ","s":136,"h":600,"w":250,"r":true},{"p":" ezoic_pub_ad_placeholder-100-bottom_floating-728x90-100-nonexxxnonexxxxxxezmaxscaleval100 ","s":100},{"p":" ezoic_pub_ad_placeholder-100-bottom_floating-970x90-100-nonexxxnonexxxxxxezmaxscaleval100 ","s":100,"h":90,"w":970}],"a":{"100":true,"114":true,"117":true,"119":true,"122":true,"136":true,"6":true},"g":-1,"l":{"0":7,"1":3,"2":2,"3":1,"4":-1,"5":-1},"m":{"0":7,"1":3,"2":2,"3":1,"4":-1,"5":-1},"v":0,"ve":false,"hr":false},"cr":"","tid":134,"tn":"pub_site","url":"","wc":870,"ff":1,"dhh":""};
d.ab = _ezaq.ab_test_id;
d.pv = _ezaq.page_view_id;
d.vu = _ezaq.visit_uuid;
d.url = window.location.href;
var dynamicAddScript = function(script) {
	if(window.ezFinishedStatic === true) {
		console.error("attempted to load dynamic script again");
		return;
	}
	var errorMessages = [];
	function errorHandler(event) {
	  var errorObj = event.error;
	  if (errorObj && errorObj.stack && errorObj.stack.indexOf('dynamicAddScript') !== -1) {
		var errorMessage = {
		  Message: event.message,
		  LineNo: event.lineno,
		  ColumnNo: event.colno,
		  Stack: errorObj.stack
		};
		errorMessages.push(errorMessage);
	  }

	  if (typeof window.onerror === 'function') {
		window.onerror.apply(this, arguments);
	  }
	}
 	window.addEventListener('error', errorHandler);

	var ezDynamic = document.createElement('script');
	ezDynamic.type = 'text/javascript';
	ezDynamic.innerHTML = script;
	document.head.appendChild(ezDynamic);

	window.removeEventListener('error', errorHandler);
	if (window.ezFinishedStatic !== true || typeof window.ezstaticerrors !== 'undefined') {
		d.Script = script;
		d.ErrorMessages = JSON.stringify(errorMessages);
		d.ErrorStaticMessages = window.ezstaticerrors || '';
		var dataTxt = JSON.stringify(d);
		if (dataTxt.length > 0) {
			var logXHR = new XMLHttpRequest()
			logXHR.open('POST','/ezais/log?cb=1', true);
			logXHR.setRequestHeader('Content-Type','application/json');
			logXHR.send(dataTxt);
		}
	}
};
var dataText = JSON.stringify(d);
if (dataText.length > 0) {
	var startTime = Date.now() - __ez.stms;

	var xhr = new XMLHttpRequest();
	xhr.open('POST','/ezais/dynamic?cb=1', true);
	xhr.onload = function () {
		if (xhr.status!=200) {
            return;
		}

        if(document.readyState !== 'loading') {
            dynamicAddScript(xhr.response);
            return;
        }

        var eventFunc = function() {
            if(document.readyState === 'loading') {
                return;
            }
            document.removeEventListener('readystatechange', eventFunc, false);
            dynamicAddScript(xhr.response);
        };

        document.addEventListener('readystatechange', eventFunc, false);
	};
	xhr.setRequestHeader('Content-Type','text/plain');
	xhr.send(dataText);
}
}
__ez.queue.addFunc("productEzoicAds", "productEzoicAds", null, true, ['ezaqReady'], false, false, false, true);
</script><!--<base href="https://www.online-python.com/">--><base href=".">
    <title>Online Python - IDE, Editor, Compiler, Interpreter</title>

    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- Tell the browser to be responsive to screen width -->
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">

    <meta name="description" content="Build and Run your Python code instantly. Online-Python is a quick and easy tool that helps you to build, compile, test your python programs.">
    <meta name="keywords" content="online python compiler, online python ide, online python interpreter, python online interpreter, online python editor, online python 3, online python code runner, run python script online, online python code editor, online python syntax checker, online python with numpy, online python text editor, python online ide free, online python editor free">
    <meta name="author" content="online-python">
    <meta name="copyright" content="ShareAlike">

    <meta name="robots" content="index, follow">
    <meta name="googlebot" content="index, follow">

    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-touch-fullscreen" content="yes">

    <link rel="icon" type="image/png" href="https://www.online-python.com/logo.png">

    <!-- Bootstrap 3.3.7 -->
    <link rel="stylesheet" href="./string to dictionary2_files/bootstrap.min.css">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="./string to dictionary2_files/all.min.css">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="./string to dictionary2_files/ide.css">

    <!-- Google Font -->
    <link rel="stylesheet" href="./string to dictionary2_files/css" ezfontsrc="https://fonts.googleapis.com/css?display=swap&amp;family=Source+Sans+Pro%3A300%2C400%2C600%2C700%2C300italic%2C400italic%2C600italic" as="style">

    <!-- jQuery 3 -->
    <script src="./string to dictionary2_files/jquery.min.js.download"></script>
    <!-- Bootstrap 3.3.7 -->
    <script src="./string to dictionary2_files/bootstrap.min.js.download"></script>

    <script src="./string to dictionary2_files/ide.js.download"></script>

    <!-- Ace Editor -->
    <script src="./string to dictionary2_files/ace.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./string to dictionary2_files/ext-language_tools.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./string to dictionary2_files/ext-settings_menu.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script async="" src="./string to dictionary2_files/ext-keybinding_menu.min.js.download" type="text/javascript" charset="utf-8"></script>

    <!-- Split JS -->
    <script type="text/javascript" src="./string to dictionary2_files/split.min.js.download"></script>

    <link rel="stylesheet" href="./string to dictionary2_files/toastr.min.css">

    <script src="./string to dictionary2_files/toastr.min.js.download"></script>

    <script async="" src="./string to dictionary2_files/socket.io.js.download"></script>

<!-- Hotjar Tracking Code for https://online-python.com/ -->
<!-- <script>
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:1755613,hjsv:6};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
</script> -->


<!-- Global site tag (gtag.js) - Google Analytics -->
<script async="" src="./string to dictionary2_files/js(1)"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-161735093-1');
</script>

<script data-ad-client="ca-pub-8595466052839863" async="" src="./string to dictionary2_files/f(1).txt" data-checked-head="true"></script>

<script type="text/javascript">
var ezoTemplate = 'pub_site';
var ezouid = '1';
var ezoFormfactor = '1';
</script><script data-ezscrex="false" type="text/javascript">
var soc_app_id = '0';
var did = 214055;
var ezdomain = 'online-python.com';
var ezoicSearchable = 1;
</script>
<script data-cfasync="false">__ez.queue.addFile('/tardisrocinante/lazy_load.js', '/tardisrocinante/lazy_load.js?gcb=1&cb=6', false, [], true, false, true, false);</script><script src="./string to dictionary2_files/lazy_load.js.download" async=""></script>
<link rel="canonical" href="https://www.online-python.com/"><meta http-equiv="origin-trial" content="AlK2UR5SkAlj8jjdEc9p3F3xuFYlF6LYjAML3EOqw1g26eCwWPjdmecULvBH5MVPoqKYrOfPhYVL71xAXI1IBQoAAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="Amm8/NmvvQfhwCib6I7ZsmUxiSCfOxWxHayJwyU1r3gRIItzr7bNQid6O8ZYaE1GSQTa69WwhPC9flq/oYkRBwsAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="A9wSqI5i0iwGdf6L1CERNdmsTPgVu44ewj8QxTBYgsv1LCPUVF7YmWOvTappqB1139jAymxUW/RO8zmMqo4zlAAAAACNeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A+d7vJfYtay4OUbdtRPZA3y7bKQLsxaMEPmxgfhBGqKXNrdkCQeJlUwqa6EBbSfjwFtJWTrWIioXeMW+y8bWAgQAAACTeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script src="./string to dictionary2_files/text.js.download"></script><script src="./string to dictionary2_files/mode-python.js.download"></script><script type="text/javascript">function _setEzCookies(ezConsentData){var cookies=[{name:"ezosuibasgeneris-1",value:"701a7281-e01d-4ae3-535b-f7c889f61bdf; Path=/; Domain=online-python.com; Expires=Fri, 07 Nov 2025 08:07:54 UTC; Secure; SameSite=None",tcfCategory:"understand_audiences",isEzoic:"true",},{name:"lp_214055",value:"https://www.online-python.com/; Path=/; Domain=online-python.com; Expires=Thu, 07 Nov 2024 08:37:54 UTC",tcfCategory:"store_info",isEzoic:"true",},{name:"ezovuuidtime_214055",value:"1730966874; Path=/; Domain=online-python.com; Expires=Sat, 09 Nov 2024 08:07:54 UTC",tcfCategory:"understand_audiences",isEzoic:"true",},{name:"ezovuuid_214055",value:"ad7ea96e-7e44-4023-4375-6f941a045025; Path=/; Domain=online-python.com; Expires=Thu, 07 Nov 2024 08:37:54 UTC",tcfCategory:"understand_audiences",isEzoic:"true",},{name:"ezoref_214055",value:"bing.com; Path=/; Domain=online-python.com; Expires=Thu, 07 Nov 2024 08:37:54 UTC",tcfCategory:"understand_audiences",isEzoic:"true",}];for(var i=0;i<cookies.length;i++){var cookie=cookies[i];if(ezConsentData&&ezConsentData.loaded&&ezConsentData[cookie.tcfCategory]){document.cookie=cookie.name+"="+cookie.value;}}}
if(window.ezTcfConsent&&window.ezTcfConsent.loaded){_setEzCookies(window.ezTcfConsent);}else if(typeof getEzConsentData==="function"){getEzConsentData().then(function(ezTcfConsent){if(ezTcfConsent&&ezTcfConsent.loaded){_setEzCookies(window.ezTcfConsent);}else{console.error("cannot get ez consent data");_setEzCookies(window.ezTcfConsent);}});}else{console.error("getEzConsentData is not a function");_setEzCookies(window.ezTcfConsent);}window._ezaq = Object.assign({"ab_test_id":"mod1-c","ad_cache_level":1,"ad_count_adjustment":0,"ad_lazyload_version":0,"ad_load_version":1,"ad_location_ids":"","adpicker_placement_cnt":0,"adx_ad_count":0,"ai_placeholder_cache_level":1,"ai_placeholder_placement_cnt":-1,"author":"online-python","bidder_method":0,"bidder_version":3,"city":"Rubavu","country":"RW","days_since_last_visit":-1,"display_ad_count":0,"domain_id":214055,"domain_test_group":20230807,"ds_adsize_opt_id":-1,"edge_cache_status":34,"edge_response_time":4,"engaged_time_visit":134,"ezcache_level":2,"ezcache_skip_code":0,"form_factor_id":1,"framework_id":1,"has_bad_image":0,"has_bad_words":0,"iab_category":"","is_embed":false,"is_from_recommended_pages":false,"is_return_visitor":false,"is_sitespeed":1,"last_page_load":"1730965814126","last_pageview_id":"2aa4f5ca-9f32-47bf-55a7-99f9dde04d05","lt_cache_level":0,"max_ads":0,"metro_code":0,"optimization_version":0,"page_ad_positions":"","page_iab_categories":[631],"page_view_count":0,"page_view_id":"d5c7bc38-0e7d-465c-4bfb-019ebab32d3c","position_selection_id":0,"postal_code":"","product_1":true,"product_2":true,"product_3":true,"product_5":true,"product_6":true,"pv_event_count":0,"referring_domain":"bing.com","response_size":44280,"response_size_orig":36154,"response_time_orig":2,"serverid":"i-058b6d7c79c5ae4fe","state":"04","sub_page_ad_positions":"","t_epoch":1730966874,"template_id":134,"time_on_site_visit":793,"url":"https://www.online-python.com/","visit_uuid":"ad7ea96e-7e44-4023-4375-6f941a045025","weather_precipitation":0,"weather_summary":"","weather_temperature":0,"word_count":870,"worst_bad_word_level":0}, typeof window._ezaq !== "undefined" ? window._ezaq : {});__ez.queue.markLoaded('ezaqReady');
__ez.queue.addFile('/parsonsmaize/mulvane.js', '/parsonsmaize/mulvane.js?gcb=195-1&cb=11', true, ['/parsonsmaize/abilene.js'], true, false, true, false);__ez.queue.addFile('/parsonsmaize/olathe.js', '/parsonsmaize/olathe.js?gcb=195-1&cb=26', false, ['/parsonsmaize/abilene.js','/parsonsmaize/mulvane.js'], true, false, true, false);__ez.queue.addFile('/porpoiseant/et.js', '/porpoiseant/et.js?gcb=195-1&cb=3', false, [], true, false, true, false);__ez.queue.addFile('/detroitchicago/reno.js', '/detroitchicago/reno.js?gcb=195-1&cb=3', false, ['/parsonsmaize/abilene.js'], true, false, true, false);!function(){var e=function(e,i,t){var o=[],n=null;return{Add:function(t,d){var a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:null;if(__ez.dot.isDefined(t)&&__ez.dot.isValid(d))if(n==t&&o.length>0&&o[o.length-1].data.length+d.length<=5)o[o.length-1].data=o[o.length-1].data.concat(__ez.dot.dataToStr(d));else{var _={type:e,domain_id:__ez.dot.getDID(),t_epoch:__ez.dot.getEpoch(0),data:__ez.dot.dataToStr(d)};_[i]=t,a&&a.hasOwnProperty("impression_id")&&a.hasOwnProperty("ad_unit")&&(_.impression_id=a.impression_id.toString(),_.unit=a.ad_unit),o.push(_),n=t}},Fire:function(){if(void 0===document.visibilityState||"prerender"!==document.visibilityState){if(__ez.dot.isDefined(o)&&o.length>0)for(;o.length>0;){var e=5;e>o.length&&(e=o.length);var i=o.splice(0,e),n=__ez.dot.getURL(t)+"?orig="+(!0===__ez.template.isOrig?1:0)+"&v="+btoa(JSON.stringify(i));__ez.dot.Fire(n)}o=[]}}}};__ez.vep=e("video","video_impression_id","/detroitchicago/grapefruit.gif"),__ez.vaep=e("video-ad","video_ad_impression_id","/porpoiseant/lemon.gif"),__ez.osvaep=e("outstream-video-ad","video_ad_impression_id","/porpoiseant/tangerine.gif")}();
__ez.queue.addFile('/detroitchicago/wichita.js', '/detroitchicago/wichita.js?gcb=195-1&cb=16', false, ['/parsonsmaize/abilene.js'], true, false, true, false);__ez.queue.addFile('/detroitchicago/raleigh.js', '/detroitchicago/raleigh.js?gcb=195-1&cb=8', false, ['/parsonsmaize/abilene.js'], true, false, true, false);__ez.queue.addFile('/detroitchicago/vista.js', '/detroitchicago/vista.js?gcb=195-1&cb=7', false, ['/parsonsmaize/abilene.js'], true, false, true, false);
function create_ezolpl() {
	var d = new Date();
	d.setTime(d.getTime() + 365 * 24 * 60 * 60 * 1000);
	var expires = "expires=" + d.toUTCString();
	__ez.ck.setByCat(
	  "ezux_lpl_214055",
	  new Date().getTime() +
		"|" +
		_ezaq.page_view_id +
		"|" +
		_ezaq.is_return_visitor +
		"; " +
		expires,
	  "understand_audiences",
	  false
	);
  }
  function attach_ezolpl() {
	if (document.readyState === "complete") {
	  create_ezolpl();
	  return;
	}
	window.addEventListener("load", create_ezolpl);
  }  

__ez.queue.addFunc("attach_ezolpl", "attach_ezolpl", null, false, ['/detroitchicago/boise.js'], true, false, false, false);

__ez.queue.addFile('/tardisrocinante/vitals.js', '/tardisrocinante/vitals.js?gcb=1&cb=5', false, ['/parsonsmaize/mulvane.js'], true, false, true, false);
var _audins_dom="online_python_com",_audins_did=214055;__ez.queue.addDelayFunc("audins.js","__ez.script.add", "//go.ezodn.com/detroitchicago/audins.js?cb=3");
__ez.queue.addFile('/beardeddragon/drake.js', '/beardeddragon/drake.js?gcb=1&cb=8', false, [], true, false, true, false);
var __ez_dims = (function() {
		var setCookie = function( name, content, expiry ) {
			return document.cookie = name+'='+content+((expiry)?';expires='+(new Date(Math.floor(new Date().getTime()+expiry*1000)).toUTCString()):'')+';path=/';
		};
		var ffid = 1;
		var oh = window.screen.height;
		var ow = window.screen.width;
		var h = ffid === 1 ? oh : (oh > ow) ? oh : ow;
		var w = ffid === 1 ? ow : (oh > ow) ? ow : oh;
		var uh = window.innerHeight || document.documentElement.clientHeight || document.getElementsByTagName('body')[0].clientHeight;
		var uw = window.innerWidth || document.documentElement.clientWidth || document.getElementsByTagName('body')[0].clientWidth;
	
		var setAllCookies = function() {
			setCookie('ezds', encodeURIComponent('ffid='+ffid+',w='+w+',h='+h), (31536e3*7));
			setCookie('ezohw', encodeURIComponent('w='+uw+',h='+uh), (31536e3*7));    
		};
	
		if (window.ezTcfConsent && window.ezTcfConsent.loaded) {
			if (window.ezTcfConsent.understand_audiences) { 
				setAllCookies();
			}
		} else if (typeof getEzConsentData === "function") {
			getEzConsentData().then(function (ezTcfConsent) {
				if (ezTcfConsent && ezTcfConsent.loaded) {
					if (ezTcfConsent.understand_audiences) { 
						setAllCookies();
					}
				} else {
					console.error("cannot get ez consent data");
					setAllCookies();
				}
			});
		} else {
			console.error("getEzConsentData is not a function");
			setAllCookies();
		}
	
	})();
__ez.queue.addFile('/parsonsmaize/chanute.js', '/parsonsmaize/chanute.js?a=a&cb=15&dcb=195-1&shcb=34', true, ['/parsonsmaize/mulvane.js'], true, false, false, false);
__ez.queue.addFile('/porpoiseant/jellyfish.js', '/porpoiseant/jellyfish.js?a=a&cb=17&dcb=195-1&shcb=34', false, [], true, false, false, false);
if(typeof _ezaq!=="undefined"&&typeof __ez=="object"&&typeof __ez.bit=="object"&&typeof __ezDotData=="function"){if("cookieDeprecationLabel"in navigator){navigator.cookieDeprecationLabel.getValue().then((label)=>{__ez.bit.Add(_ezaq["page_view_id"],[new __ezDotData("chrome_cookie_deprecation_label",label),]);});}}
</script><script src="./string to dictionary2_files/mulvane.js.download" async=""></script><script src="./string to dictionary2_files/et.js.download" async=""></script><script src="./string to dictionary2_files/reno.js.download" async=""></script><script src="./string to dictionary2_files/wichita.js.download" async=""></script><script src="./string to dictionary2_files/raleigh.js.download" async=""></script><script src="./string to dictionary2_files/vista.js.download" async=""></script><script src="./string to dictionary2_files/drake.js.download" async=""></script><script src="./string to dictionary2_files/jellyfish.js.download" async=""></script><script src="./string to dictionary2_files/python.js.download"></script><script src="./string to dictionary2_files/olathe.js.download" async=""></script><script src="./string to dictionary2_files/vitals.js.download" async=""></script><script src="./string to dictionary2_files/chanute.js.download" async=""></script><script type="text/javascript">var ezStaticAnchor = function(anchorXPath, htmlStr, isRequired) {
	var ezRange = document.createRange();
	var ezAnchor = document.evaluate(anchorXPath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
	if (typeof ezAnchor !== 'undefined' && ezAnchor !== null) {
		ezRange.selectNode(ezAnchor);
		var fragment = ezRange.createContextualFragment(htmlStr);
		if(isRequired===true) {
			ezAnchor.appendChild(fragment);
		} else {
			ezAnchor.parentNode.insertBefore(fragment, ezAnchor.nextSibling);
		}
	} else {
		var errMsg = 'cannot find anchor for ad position' + anchorXPath + ';';
		console.error(errMsg);
		window.ezstaticerrors = (window.ezstaticerrors || '') + errMsg;
	}
};
try {window.ezslots_raw=[];window.ezslotdivs={};var __sellerid='587c830043a3da4558d8d4559387900e';var __ez_nid ='1254144';
__ez.jitver=1;
!function(){function e(e,t){for(var i=0;i<t.length;i++){var o=t[i];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}function t(e,t,i){return t in e?Object.defineProperty(e,t,{value:i,enumerable:!0,configurable:!0,writable:!0}):e[t]=i,e}window.ezasLoaded=!1;var i=!1;window.ezasBuild=function(e){window.ezasLoaded||(void 0===window.ezasAutoAds&&(window.google_reactive_ads_global_state={adCount:{},floatingAdsStacking:{maxZIndexListeners:[],maxZIndexRestrictions:{},nextRestrictionId:0},messageValidationEnabled:!1,reactiveTypeDisabledByPublisher:{},reactiveTypeEnabledInAsfe:{},sideRailAvailableSpace:[],sideRailOverlappableElements:[],stateForType:{},tagSpecificState:{},wasPlaTagProcessed:!0,wasReactiveAdConfigReceived:{1:!0,2:!0,8:!0},wasReactiveAdVisible:{},wasReactiveTagRequestSent:!0,description:"Can't disable auto ads programmatically on the page, so here we are!"}),window.ezasLoaded=!0);var t=new o(e);if(1!=t.getValue("compid"))return!1;if("function"!=typeof MutationObserver||"function"!=typeof IntersectionObserver)return t.setValue("compid","0"),!1;if(void 0===e||void 0===window.ezasVars)return t.setValue("compid","0"),!1;if(void 0!==window.ezgconsent&&0==window.ezgconsent)return t.setValue("compid","0"),!1;if(!i&&void 0===window.ezasAutoAds){var a=document.createElement("script");a.src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js",a.crossOrigin="anonymous",a.async=!0,document.getElementsByTagName("head")[0].appendChild(a),i=!0}if(5==t.getValue("al")%1e3)return t.setValue("compid","0"),t.setValue("nocompoverride","1"),!1;var n=window.ezasVars.cid,d="ca-"+window.ezasVars.pid;if(void 0===n||""===n)return t.setValue("compid","0"),!1;t.setValue("reft","n");var s=document.getElementById(e);if(!s)return t.setValue("compid","0"),!1;var l=e+"-asloaded";if(null!==document.getElementById(l))return!0;var r=document.createElement("ins");r.id=l,r.className="adsbygoogle ezasloaded",r.dataset.adClient=d,r.dataset.adChannel=n;var w=t.getValue("asau");return"mod105"==t.getValue("bra")&&""!=w?(r.dataset.adSlot=w,r.dataset.matchedContentUiType="text",r.dataset.matchedContentRowsNum="4",r.dataset.matchedContentColumnsNum="1"):void 0!==window.__ezasAggressive&&!0===window.__ezasAggressive&&(r.dataset.fullWidthResponsive="true"),r.style.display="block",r.style.margin="0px auto","undefined"!=typeof handleResponsiveAdsense?window.handleResponsiveAdsense(r,s):(r.style.width=s.attributes.ezaw.value+"px",r.style.height=s.attributes.ezah.value+"px"),s.appendChild(r),window.ezaslWatch=window.ezaslWatch||[],window.ezaslWatch.push(e),window.__ez&&__ez.fads&&__ez.fads.log("ezasbuild firing adsense for slot",e),(window.adsbygoogle=window.adsbygoogle||[]).push({}),ezoSTPixelAdd(e,"stat_source_id",44),ezoSTPixelAdd(e,"adsensetype",1),!0};var o=function(){function i(e){!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,i),t(this,"slot",null),t(this,"allValues",null),t(this,"isEzSlot",!1),t(this,"divID",""),this.divID=e;var o=window.ezslotdivs&&window.ezslotdivs[e]&&window.ezslotdivs[e].slot;if(void 0===window[o+"_raw"]){if(!ezslots||0==ezslots.length)return null;var a=ezslots.filter((function(t){return window[t].getSlotElementId()===e}));if(0==a.length)return null;console.debug("as2"),this.slot=window[a[0]],this.allValues=window[a[0]].getTargetingMap(),this.isEzSlot=!0}else this.allValues=window[o+"_raw"]}var o,a;return o=i,(a=[{key:"getValue",value:function(e){return this.isEzSlot&&this.slot?this.slot.getTargeting(e)[0]:this.allValues[e]}},{key:"setValue",value:function(e,t){this.isEzSlot&&this.slot?this.slot.setTargeting(e,t):this.allValues[e]=t}},{key:"getSlot",value:function(){if(this.slot)return this.slot;var e=window.ezslotdivs&&window.ezslotdivs[this.divID]&&window.ezslotdivs[this.divID].adunit;if(!e){e="";var t=this.divID.match(/div-gpt-ad-([a-z0-9_-]+)-0(_[0-9])?/);t&&t.length>1&&(e=t[1])}return{ElementId:this.divID,Targeting:this.allValues,AdUnitPath:e}}}])&&e(o.prototype,a),Object.defineProperty(o,"prototype",{writable:!1}),i}();window.ezasvEvent=function(e,t){if(!0===e[0].isIntersecting){var i=e[0].target.attributes[0].value.substr(0,e[0].target.attributes[0].value.length-9);window.ezoSTPixelAdd(i,"viewed",1),t.disconnect()}},window.ezaslEvent=function(e,t){if(window.__ez&&__ez.fads&&__ez.fads.log("ezaslEvent slot event triggered"),void 0!==e[0].target.attributes["data-ad-status"]){var i=e[0].target.attributes["data-ad-status"].value,o=e[0].target.attributes[0].value.substr(0,e[0].target.attributes[0].value.length-9);if(window.__ez&&__ez.fads&&__ez.fads.log("ezaslEvent slot event found ad",o,i),"filled"==i)return window.ezoSTPixelAdd(o,"loaded",1),window.ezoSTPixelAdd(o,"ad_load_time",Date.now()-__ez.stms),new IntersectionObserver(window.ezasvEvent,{threshold:[1]}).observe(document.getElementById(o+"-asloaded")),void t.disconnect();if("unfilled"==i){var a=ezslots_raw.filter((function(t){return t.tap&&t.tap.startsWith(e[0].target.parentElement.id.slice(11,-2))}));if(a.length>0&&"1"==a[0].nocompoverride)return;return setTimeout((function(){window.ezoAdBackFill(e)}),2e3),void t.disconnect()}}},window.ezoAdBackFill=function(e){var t=e[0].target,i=t.parentElement;t.style.display="none !important",window.__ez&&__ez.fads&&__ez.fads.log("ezoAdBackFill attempting to backfill adsense with GAM",t,t.id);var o,a=ezoGetSlotNum(i.id);if(o=void 0!==__ez.fads?__ez.fads.initslots[i.id]:__ez_fad_initslot[i.id],void 0===a&&"function"==typeof o&&(a=o(6)),void 0!==a)var n=window[a];if(void 0!==n){n.setTargeting("compid","0"),n.setTargeting("nocompoverride","1"),n.setTargeting("bkfl","1"),n.setTargeting("reft","t");var d=n.getTargeting("br2")[0];if(void 0!==window.ezoibfh&&void 0!==window.ezoibfh[d]&&(n.setTargeting("br1",d),n.setTargeting("eb_br",window.ezoibfh[d])),googletag.display(n),void 0!==window.ezoResponsiveSizes&&void 0!==n&&null!=n&&"1005"!=n.getTargeting("al")[0]&&"3005"!=n.getTargeting("al")[0]){var s=__ez.fads.adLoadGAM.buildSlotResponsiveSizes(n.getSlotElementId());""!==s&&(__ez.fads.adLoadGAM.adjustResponsiveDiv(n.getSlotElementId()),n.defineSizeMapping(s))}setTimeout((function(){googletag.pubads().refresh([n])}),500)}},window.ezaslWatch=window.ezaslWatch||[],window.ezaslWatch.push=function(e){var t=e+"-asloaded";window.__ez&&__ez.fads&&__ez.fads.log("attached observer to slot",t),new MutationObserver(window.ezaslEvent).observe(document.getElementById(t),{attributes:!0});var i=document.getElementById(t);i.hasAttribute("data-ad-status")&&(i.setAttribute("data-ezasl","1"),i.removeAttribute("data-ezasl"))};for(var a=0;a<ezaslWatch.length;a++){var n=new MutationObserver(window.ezaslEvent);n.observe(document.getElementById(ezaslWatch[a]+"-asloaded"),{attributes:!0}),window.ezaslEvent([{target:document.getElementById(ezaslWatch[a]+"-asloaded")}],n)}window.ezoSTPixels=window.ezoSTPixels||[];var d=setInterval((function(){"undefined"!=typeof __ez&&"undefined"!=typeof __ezDotData&&"undefined"!=typeof ezslots&&"undefined"!=typeof ezslots_raw&&window.ezslots_raw.length>0&&(window.ezoSTPixelFire(),clearInterval(d))}),250);window.ezoSTPixelAdd=function(e,t,i){window.ezoSTPixels.push({id:e,name:t,value:i}),window.ezoSTPixelFire()},window.ezoGetSlotById=function(e){var t;for(var i in t=e.includes("/")?e.split("div-gpt-ad-")[1].split("-")[0]:e.split("div-gpt-ad-")[1].split("-",3).join("-"),window.ezslots_raw)if(window.ezslots_raw[i].tap.includes(t))return window.ezslots_raw[i]},window.ezoGetSlotNum=function(e){if(void 0!==window.ezslots&&0!=window.ezslots)for(var t=0;t<window.ezslots.length;t++){var i=window[ezslots[t]];if(void 0!==i){var o=i.getSlotElementId();if(void 0!==o&&o==e)return ezslots[t]}}},window.ezoSTPixelFire=function(){if("undefined"!=typeof __ez&&"undefined"!=typeof __ezDotData&&"undefined"!=typeof ezslots)for(;window.ezoSTPixels.length>0;){var e=window.ezoSTPixels.shift(),t=window.ezoGetSlotById(e.id);if(void 0===t){var i;if(i=void 0!==__ez.fads?__ez.fads.initslots[e.id]:__ez_fad_initslot[e.id],void 0===googletag.defineSlot)return void window.ezoSTPixels.push(e);if(i(1),void 0===(t=window.ezoGetSlotById(e.id)))return void window.ezoSTPixels.push(e)}var o=[{type:"impression",impression_id:t.eid,domain_id:window.did.toString(),unit:e.id,t_epoch:__ez.dot.getEpoch(0),ad_position:parseInt(t.ap),country_code:__ez.dot.getCC(),pageview_id:__ez.dot.getPageviewId(),comp_id:1,data:__ez.dot.dataToStr([new __ezDotData(e.name,e.value.toString())]),is_orig:0}],a=__ez.dot.getURL("/porpoiseant/army.gif")+"?orig=0&sts="+btoa(JSON.stringify(o));__ez.dot.Fire(a)}}}();
window.__ezaps=[{"slotID":"div-gpt-ad-online_python_com-box-2-0","divID":"","slotName":"/1254144,22108676293/online_python_com-box-2","sizes":[[160,600]]},{"slotID":"div-gpt-ad-online_python_com-medrectangle-2-0","divID":"","slotName":"/1254144,22108676293/online_python_com-medrectangle-2","sizes":[[970,90],[728,90]]},{"slotID":"div-gpt-ad-online_python_com-medrectangle-3-0","divID":"","slotName":"/1254144,22108676293/online_python_com-medrectangle-3","sizes":[[160,600]]}];window.__ezapsVideo=[];window.__ezapid='aa05931b-5308-4ea3-95a2-adf84f4ffde4';
var ezS = document.createElement("script");ezS.src="/edmontonalberta/calgary.js?cb=37";document.head.appendChild(ezS);
!function(){var e=setInterval((function(){var t=document.querySelectorAll('[id^="outbrain_widget_"]');0!==t.length&&(function(e){e.forEach((function(e){if(e.parentElement.hasAttribute("data-ez-name")){var t=e.parentElement.attributes["data-ez-name"].value;new IntersectionObserver((function(e,i){e[0].isIntersecting&&(n({unit:t,name:"viewed"}),i.disconnect())}),{threshold:[1]}).observe(e);var i=e.attributes["data-widget-id"].value;window.OBREvents=window.OBREvents||[],OBREvents.push({event:"widgetDataReturned",widgetId:i,func:function(){n({unit:t,name:"loaded"})}})}}))}(t),clearInterval(e))}),250),t=[],i=setInterval((function(){"undefined"!=typeof __ez&&"undefined"!=typeof _ezim_d&&"undefined"!=typeof __ezDotData&&(d(),clearInterval(i))}),2500);function n(e){t.push(e),d()}function d(){var e,i;if(0!==t.length&&"undefined"!=typeof __ez&&"undefined"!=typeof _ezim_d&&"undefined"!=typeof __ezDotData)for(;t.length>0;){var n=t.shift(),d=(e=n.unit,i=n.name,[{type:"impression",impression_id:_ezim_d[e].full_id.split("/")[2],domain_id:window.did.toString(),unit:e,t_epoch:__ez.dot.getEpoch(0),ad_position:_ezim_d[e].position_id,country_code:__ez.dot.getCC(),pageview_id:__ez.dot.getPageviewId(),comp_id:2,data:__ez.dot.dataToStr([new __ezDotData(i,"1")]),is_orig:0}]),o=__ez.dot.getURL("/porpoiseant/army.gif")+"?orig="+(!0===__ez.template.isOrig?1:0)+"&sts="+btoa(JSON.stringify(d));void 0!==window.ezWp&&ezWp&&void 0!==window._ezaq&&_ezaq.hasOwnProperty("visit_uuid")&&(o+="&visit_uuid="+window.visit_uuid),__ez.dot.Fire(o)}}}();
window.ezhbopt=true;
window.ezpbCache=true;

	var __banger_pmp_deals=function(){var d={1428:{"DealId":1428,"Floor":25},17:{"DealId":17,"Floor":160},18:{"DealId":18,"Floor":25},19:{"DealId":19,"Floor":100},2351:{"DealId":2351,"Floor":155},2610:{"DealId":2610,"Floor":125},2688:{"DealId":2688,"Floor":100},2693:{"DealId":2693,"Floor":50},2761:{"DealId":2761,"Floor":200},3044:{"DealId":3044,"Floor":175},3045:{"DealId":3045,"Floor":75},3052:{"DealId":3052,"Floor":20},3053:{"DealId":3053,"Floor":37},3856:{"DealId":3856,"Floor":15},4276:{"DealId":4276,"Floor":65},7035:{"DealId":7035,"Floor":150},7327:{"DealId":7327,"Floor":150},7330:{"DealId":7330,"Floor":80},7331:{"DealId":7331,"Floor":40}};return[{"SlotName":"/1254144,22108676293/online_python_com-box-2","Deals":[d[18],d[1428],d[3052],d[3856]]},{"SlotName":"/1254144,22108676293/online_python_com-medrectangle-2","Deals":[d[17],d[18],d[19],d[1428],d[2351],d[2610],d[2688],d[2693],d[2761],d[3044],d[3045],d[3052],d[3053],d[3856],d[4276],d[7035],d[7327],d[7330],d[7331]]},{"SlotName":"/1254144,22108676293/online_python_com-medrectangle-3","Deals":[d[18],d[1428],d[3052],d[3053],d[3856],d[7331]]}]}();

_ebcids=[138231308856,138231308940,138231308949,138231387842,138231421744,138231421759,138231421774,138231421783,138231421789,138231421792,138242067587,138242067590,138242067602,138242067605,138242067608,138242067614,138242229406,138242229415,138242229421,138242229430];
var __ez_gcb="gcb=195-1&cb=240";"use strict";window.googletag=window.googletag||{};googletag.cmd=googletag.cmd||[];__ez.fads=window.__ez.fads||{cmd:[],initslots:{},kvStore:{},divs:[[],[],[],[],[],[],[]],divsd:[],fadcount:0,isJIT:true,};var ez_ad_units=ez_ad_units||[];var ezslots=[];var ezrpos=[];var ezsrqt={};var __ez_fad_haspo=false;var __ez_fad_hascp=false;if(typeof PerformanceObserver!=='undefined'&&typeof PerformanceObserver.supportedEntryTypes!=='undefined'){if(PerformanceObserver.supportedEntryTypes.indexOf('largest-contentful-paint')>-1){__ez_fad_haspo=true;}}
try{var __ez_fad_po=new PerformanceObserver(function(){window.__ez_fad_hascp=true;__ez.fads.cmd.push(function(){__ez.fads.__ez_fad_hascp=true;});});__ez_fad_po.observe({type:'largest-contentful-paint',buffered:true});}catch(e){console.log(e);}
function __ez_fad_position(id){__ez.fads.cmd.push(function(){__ez.fads.__ez_fad_position(id);});}
function ezSetTargetingFromMap(slot,obj){if(typeof slot==='undefined'){return;}
for(var key in obj){if(!obj.hasOwnProperty(key)){continue;}
slot.setTargeting(key,obj[key]);}}
function ezSetSlotTargeting(divid,key,value){var slot=ezGetSlotById(divid);if(slot){slot.setTargeting(key,value);}else{if(typeof __ez.fads.kvStore[divid]==='undefined'){__ez.fads.kvStore[divid]={};}
__ez.fads.kvStore[divid][key]=value;}}
function ezGetSlotById(id){if(typeof window.ezslots==='undefined'||window.ezslots==0){return;}
for(var i=0;i<window.ezslots.length;i++){var slot=window[ezslots[i]];if(typeof slot==='undefined'){continue;}
var slotId=slot.getSlotElementId();if(typeof slotId!=='undefined'&&slotId==id){return slot;}}}
function __ez_close_anchor(){googletag.cmd.push(function(slot){for(var i=0;i<window.ezslots.length;i++){var slot=window[ezslots[i]];if(typeof slot==='undefined'){continue;}
var alS=slot.getTargeting('al')[0]%1000;if(alS==5){googletag.destroySlots([slot]);}}
if(typeof window.ezdomain!=='undefined'){var d=new Date();d.setTime(d.getTime()+(2*60*60*1000));var expires="expires="+d.toGMTString();var cookie="ez_anchor_closed=true;domain=."+ezdomain+';'+expires+"; path=/";document.cookie=cookie;}
if(typeof(__ez_set_outstream_floor)!=='undefined'){__ez_set_outstream_floor(0);}
var anchor=document.getElementById('ezmobfooter');if(!anchor){return;}
anchor.innerHTML='';anchor.style.paddingTop=0;var styleElement=document.getElementById('ezoicCSS');if(!styleElement){return;}
var cert=document.getElementById('ezoic-certification-fixed');if(cert){cert.style.bottom='15px';}
var styles=styleElement.sheet?styleElement.sheet:styleElement.styleSheet;for(var i=0;i<styles.cssRules.length;i++){var rules=styles.cssRules[i];if(rules.selectorText==='body'&&rules.style.height==='auto'&&(rules.style.paddingTop!==''||rules.style.paddingBottom!=='')){styles.deleteRule(i);}}});}__ez.fads=(__ez.fads&&__ez.fads.loaded===true)?__ez.fads:{cmd:typeof window.__ez.fads!="undefined"?window.__ez.fads.cmd||[]:[],logEnabled:typeof URLSearchParams==='function'&&new URLSearchParams(window.location.search).get('ez_debug')==='jit',doc_ht:0,vp_ht:0,loaded:true,isJIT:true,libraryRoot:'https://go.ezodn.com/porpoiseant/',scrollMonitor:{loaded:false,url:'ezjitscroll.js'},positionMonitor:{loaded:false,url:'ezjitpos.js'},adLoadGAM:{loaded:false,url:'ezadloadgam.js'},adLoadAMZN:{loaded:false,url:'ezadloadamzn.js'},adLoadAS:{loaded:false,url:'ezadloadas.js'},adLoadHB:{loaded:false,url:'ezadloadhb.js'},adFilled:{loaded:false,url:'ezadfilled.js'},incontentSticky:{loaded:false,url:'ezicsticky.js'},identity:{loaded:false,url:'ezidentity.js'},amznH2Bid:{loaded:false,url:'ezamznh2bid.js'},libraries:['positionMonitor','scrollMonitor','adLoadGAM','adLoadAMZN','adLoadAS','adLoadHB','incontentSticky','adFilled','identity','amznH2Bid'],librariesLoading:[],libraryCmds:{},kvStore:typeof window.__ez.fads!="undefined"?window.__ez.fads.kvStore||{}:{},addedDivs:[],floatingAdsShown:false,loadTime:new Date().getTime(),onScreenDelay:0,isInit:false,triggerFloatingOnAdd:false,eligibleRefreshAds:[],onScreenObserver:undefined,observedElements:[],onScreenDivs:[],onScreenLoadStatus:0,callGAMOnAuctionComplete:[],runOnScreenFallback:true,headerBiddingTimeout:3000,pageDataQueued:false,pageDataCallCount:0,skipBangCheck:[],initslots:typeof window.__ez.fads!="undefined"?window.__ez.fads.initslots||{}:{},divsd:typeof window.__ez.fads!="undefined"?window.__ez.fads.divsd||[]:[],divsdExt:[],version:1,__ez_fad_haspo:window.__ez_fad_haspo||false,__ez_fad_hascp:window.__ez_fad_hascp||false,init:function(){if(this.isInit){return;}
this.isInit=true;if(typeof window.__ez.jitver!='undefined'){this.version=window.__ez.jitver;}
this.initCommon();this.cmd=(function(commandsToRun){var newCmd={push:function(f){f();}};for(var i=0;i<commandsToRun.length;i++){if(typeof commandsToRun[i]==='function'){commandsToRun[i]();}}
return newCmd;})(this.cmd);if(this.version==6){this.onScreenDelay=2500;}
this.initOnScreenFallbacks();},reset:function(){this.loadTime=new Date().getTime();this.divsd=[];this.addedDivs=[];this.onScreenDivs=[];this.teardownOnScreenObserver();this.onScreenLoadStatus=0;this.eligibleRefreshAds=[];this.callGAMOnAuctionComplete=[];this.divsdExt=[];this.runOnScreenFallback=true;this.callLibrary('positionMonitor','reset');this.callLibrary('scrollMonitor','reset');this.callLibrary('adLoadGAM','reset');this.callLibrary('adLoadAMZN','reset');this.callLibrary('adLoadAS','reset');this.callLibrary('adLoadHB','reset');this.callLibrary('incontentSticky','reset');this.initCommon();},cleanupAdData:function(divId){this.addedDivs=this.addedDivs.filter(function(id){return id!==divId;});this.divsd=this.divsd.filter(function(id){return id!==divId;});this.divsdExt=this.divsdExt.filter(function(id){return id!==divId;});this.onScreenDivs=this.onScreenDivs.filter(function(id){return id!==divId;});this.callGAMOnAuctionComplete=this.callGAMOnAuctionComplete.filter(function(id){return id!==divId;});this.eligibleRefreshAds=this.eligibleRefreshAds.filter(function(id){return id!==divId;});this.onScreenLoadStatus=0;this.runOnScreenFallback=true;delete this.initslots[divId];delete this.kvStore[divId];this.callLibrary('positionMonitor','cleanupAdData',[divId]);this.callLibrary('adLoadGAM','cleanupAdData',[divId]);this.callLibrary('adLoadHB','cleanupAdData',[divId]);},initCommon:function(){this.doc_ht=this.__ez_fad_docht();this.vp_ht=this.__ez_fad_vpht();if(this.__ez_fad_scroll()>0){this.handleScroll();}
this.initOnScreenObserver();this.initializePositions();this.handleEventListeners();},loadLibrary:function(url,name){if(this.librariesLoading.indexOf(name)==-1&&typeof this[name]!="undefined"&&this[name].loaded!==true){if(document==null||typeof document.body=='undefined'||document.body==null){setTimeout(function(){__ez.fads.loadLibrary(url,name);},100);return;}
this.librariesLoading.push(name);var script=document.createElement('script');script.src=this.libraryRoot+url+"?"+this.getCacheBustParams();script.async=true;script.onload=function(){__ez.fads.LibraryLoaded(name);};document.body.appendChild(script);}},LibraryLoaded:function(name){if(this.libraries.indexOf(name)==-1){return;}
this[name].loaded=true;if(typeof this[name].init==='function'){this[name].init(this.vp_ht,this.doc_ht,this.version);}
this.runLibraryCmds(name);},runLibraryCmds:function(name){if(typeof this.libraryCmds[name]!=='undefined'){for(var i=0;i<this.libraryCmds[name].length;i++){this.libraryCmds[name][i]();}
this.libraryCmds[name]=[];}},callLibrary:function(name,func,args,skipLibraryLoad){this.log("calling library",name,func,args);if(typeof args!='undefined'&&typeof args.length=='undefined'){args=[args];}
if(this.libraries.indexOf(name)==-1){this.log("invalid library",name);return;}
if(typeof this[name]!='undefined'&&this[name].loaded==true&&typeof this[name][func]=='function'){return this[name][func].apply(this[name],args);}else{this.libraryCmds[name]=this.libraryCmds[name]||[];this.libraryCmds[name].push(function(){__ez.fads[name][func].apply(__ez.fads[name],args);});if(skipLibraryLoad!==true){this.loadLibrary(this[name].url,name);}}},__ez_fad_docht:function(){return document.documentElement.scrollHeight},__ez_fad_vpht:function(){if(typeof window.innerHeight!='undefined'){return window.innerHeight;}
if(typeof document.documentElement!='undefined'){return document.documentElement.clientHeight;}
var body=typeof document.body!='undefined'&&document.body!=null?document.body:document.getElementsByTagName('body')[0];var screenHeight=typeof window.screen!='undefined'?window.screen.height:0;return Math.min(body.clientHeight,screenHeight)||0;},__ez_fad_scroll:function(){return window.pageYOffset||(document.documentElement||document.body.parentNode||document.body).scrollTop},getCacheBustParams:function(){if(typeof window.__ez_gcb=='undefined'){var d=new Date();gcb='gcb='+d.getFullYear()+d.getMonth()+d.getDate()+d.getHours();cb='0';return gcb+"&"+cb;}else{return window.__ez_gcb}},initializePositions:function(){if(typeof window.ez_ad_units=='undefined'){setTimeout(function(){__ez.fads.initializePositions();},100);return;}
for(var i=0;i<window.ez_ad_units.length;i++){var unit=window.ez_ad_units[i];this.__ez_fad_position('div-gpt-ad-'+unit[6]);}},SetViewportHeight:function(viewportHeight){this.vp_ht=viewportHeight;this.callLibrary('positionMonitor','setViewportHeight',[viewportHeight]);},SetDocumentHeight:function(documentHeight){this.doc_ht=documentHeight;this.callLibrary('positionMonitor','setDocumentHeight',[documentHeight]);},handleScroll:function(){this.callLibrary('scrollMonitor','SetAdLoadFunctions',[this.__ez_fad_load.bind(this)]);this.loadFloatingAds(this.headerBiddingTimeout+500);if(this.onScreenLoadStatus==0){this.loadOnScreenAds();this.onScreenLoadStatus=1;}
this.callLibrary('incontentSticky','CheckIncontentSticky',[]);},__ez_fad_position:function(id){if(this.runOnScreenFallback){this.runOnScreenFallback=false;this.initOnScreenFallbacks();}
if(document.getElementById(id)==null){return;}
if(this.addedDivs.indexOf(id)!=-1){return;}
this.callLibrary('positionMonitor','AddDiv',[id,4],true);this.__ez_fad_add(id);if(!this.isFloating(id)&&!this.isPixel(id)&&this.isOnScreen(id)){this.log("intial div on screen",id);}else if(this.onScreenLoadStatus==0&&this.version!=6){setTimeout(function(){this.loadOnScreenAds();}.bind(this),200);this.onScreenLoadStatus=1;}},initOnScreenFallbacks:function(){setTimeout(function(){if(__ez.fads.onScreenLoadStatus==false){__ez.fads.loadOnScreenAds(true);}},1000+this.onScreenDelay);if(this.__ez_fad_rdy()==false){document.addEventListener('DOMContentLoaded',function(){setTimeout(function(){if(__ez.fads.onScreenLoadStatus==false){__ez.fads.loadOnScreenAds(true);}},1000+__ez.fads.onScreenDelay);}.bind(this));}},handleEventListeners:function(){__ez.fads.interactionEvents=__ez.fads.GetInteractionEvents();function __ez_handle_init_scroll(e){__ez.fads.handleScroll();for(var i=0;i<__ez.fads.interactionEvents.length;i++){window.removeEventListener(__ez.fads.interactionEvents[i],__ez_handle_init_scroll);}}
for(var ieIdx=0;ieIdx<__ez.fads.interactionEvents.length;ieIdx++){window.addEventListener(__ez.fads.interactionEvents[ieIdx],__ez_handle_init_scroll);}},loadOnScreenAds:function(force){if(this.onScreenLoadStatus==2){return;}
this.log("start on screen load");var floatAds=window.__ez_fad_floating||[];var divs=this.onScreenDivs.concat(floatAds);divs=divs.filter(function(value,index,self){return self.indexOf(value)===index;});this.log("on screen divs",divs);if(divs.length>0){this.markIdsAsRunGAMOnAuctionComplete(divs);this.onScreenLoadStatus=2;setTimeout(function(){this.loadAdsWaitForExternal(divs);}.bind(this),this.onScreenDelay);}},loadAdsWaitForExternal:function(ids,isInitailLoad){if(this.adLoadHB.loaded==true){var auctionIds=this.adLoadHB.FilterByAuctionEligible(ids);}else{var auctionIds={eligible:ids,notEligible:[],running:[]};}
if(auctionIds.eligible.length>0){this.markIdsAsRunGAMOnAuctionComplete(auctionIds.eligible);this.callExternalBidders(auctionIds.eligible,true);}
if(auctionIds.notEligible.length>0){if(isInitailLoad){this.callLibrary('adLoadGAM','LoadAd',[auctionIds.notEligible]);}else{this.refreshAds(auctionIds.notEligible);}}
if(auctionIds.running.length>0){var loadIds=[];for(var i=0;i<auctionIds.running.length;i++){if(this.isGAMOnAuctionComplete(auctionIds.running[i])==false){loadIds.push(auctionIds.running[i]);}}
if(loadIds.length>0){setTimeout(function(){if(isInitailLoad){this.callLibrary('adLoadGAM','LoadAd',[loadIds]);}else{this.refreshAds(loadIds);}}.bind(this),1000);}}},initOnScreenObserver:function(){if(this.onScreenObserver)return;this.onScreenObserver=new IntersectionObserver(entries=>{entries.forEach(entry=>this.handleIntersection(entry));},{root:null,threshold:0});},handleIntersection:function(entry){const id=entry.target.id;const index=this.onScreenDivs.indexOf(id);if(entry.isIntersecting){this.log("Ad container detected as on-screen:",id);if(index===-1){this.onScreenDivs.push(id);}}else{this.log("Ad container detected as off-screen:",id);if(index!==-1){this.onScreenDivs.splice(index,1);}}},observeElement:function(id){this.log("Observing element for on-screen detection:",id);const elem=document.getElementById(id);if(!elem)return;if(!this.observedElements.includes(id)){this.onScreenObserver.observe(elem);this.observedElements.push(id);if(this.isElementInViewport(elem)){this.log("Initial observe of ad element is on screen:",id);this.onScreenDivs.push(id);}}},isOnScreen:function(id){if(!this.observedElements.includes(id)){this.observeElement(id);}
const isOnScreen=this.onScreenDivs.includes(id);this.log("isOnScreen check for element "+id+": "+isOnScreen);return isOnScreen;},isBangSkip:function(id){return this.skipBangCheck.indexOf(id)!==-1;},isElementInViewport:function(element){const rect=element.getBoundingClientRect();return(rect.top>=0&&rect.left>=0&&rect.bottom<=(window.innerHeight||document.documentElement.clientHeight)&&rect.right<=(window.innerWidth||document.documentElement.clientWidth));},teardownOnScreenObserver:function(){if(this.onScreenObserver){this.onScreenObserver.disconnect();this.onScreenObserver=undefined;this.observedElements=[];}},LoadAds:function(ids,force,waitForExternal){for(var i=0;i<ids.length;i++){this.LoadAd(ids[i],force,waitForExternal);}},EnsureSlotInitialized:function(id){if(typeof window.ezslots=='undefined'){return false;}
var slotElementIds=[];ezslots.forEach(function(slotName){let slot=window[slotName];if(slot&&typeof slot.getSlotElementId==='function'){let slotElementId=slot.getSlotElementId();slotElementIds.push(slotElementId);}});if(typeof slotElementIds=='undefined'||slotElementIds.includes(id)==false){this.log("slot not initialized.",id);let initslotFunction=__ez.fads.initslots[id];if(typeof initslotFunction==='function'){this.log("slot not initialized. doing that now",id);initslotFunction();}}
return true;},LoadAd:function(id,force,waitForExternal){this.logAdStats(id,'load');if(!force&&!this.__ez_fad_rdy()){setTimeout(function(){__ez.fads.LoadAd(id,force,waitForExternal);},50);return;}
if(__ez.fads.divsd.indexOf(id)==-1){this.log("loading ad",id,force,waitForExternal);this.EnsureSlotInitialized(id);__ez.fads.divsd.push(id);if(this.handleAdsense(id)){this.removeLoadingIcon(id);return;}
this.loadLibrary(this.adLoadGAM.url,'adLoadGAM');if(waitForExternal==true){this.loadAdsWaitForExternal([id],true);}else{this.callExternalBidders(id);this.callLibrary('adLoadGAM','LoadAd',[id]);}}else if(this.isEligibleAdRefresh(id)){this.refreshAds([id]);}else{}},refreshAds:function(ids){this.log("Calling adLoadGAM RefreshAds",ids);this.callLibrary('adLoadGAM','RefreshAds',[ids]);for(var i=0;i<ids.length;i++){this.removeEligibleAdRefresh(ids[i]);}},removeLoadingIcon:function(id){var adDiv=document.getElementById(id);if(adDiv){adDiv.classList.remove("ezoic-adl");}},isFloating:function(id){if(typeof __ez_fad_floating!='undefined'&&__ez_fad_floating.indexOf(id)!=-1){return true;}
return false;},isPixel:function(id){return id.indexOf('-pixel')!==-1;},callExternalBidders:function(ids,force){if(!Array.isArray(ids)){ids=[ids];}
if(force!==true){var ids=ids.filter(function(id){return __ez.fads.divsdExt.indexOf(id)==-1||__ez.fads.isEligibleAdRefresh(id)==true;});}
if(ids.length==0){this.log("no ids left to call external bidders",ids);return;}
this.divsdExt=this.divsdExt.concat(ids);var br1s=this.getRawSlotsById(ids,'br1');this.log("call external bidders",ids);this.callLibrary('adLoadHB','LoadAd',[ids,0,br1s,this.headerBiddingTimeout]);if(typeof window.__ezaps!='undefined'&&window.__ezaps.length>0||typeof __ez_hasamzn!='undefined'&&__ez_hasamzn==true){this.callLibrary('adLoadAMZN','LoadAd',[ids,0,br1s]);}
if(typeof openwrapRequestAdUnits==='function'){if(typeof window.__ezPWTAdUnits!='undefined'){var slotsToRequest=ids.map(id=>window.__ezPWTAdUnits[id]);slotsToRequest=slotsToRequest.filter(slot=>slot!=="");this.log("Requesting openwrap bids:",slotsToRequest);openwrapRequestAdUnits(slotsToRequest);}}},SetGAMTargeting:function(id,key,value){this.callLibrary('adLoadGAM','SetTargeting',[id,key,value]);},getRawSlotsById:function(ids,key){var rawSlots={};if(typeof window.ezslots_raw!='undefined'){for(var i=0;i<ids.length;i++){var id=ids[i];this.log("get raw slots by id",id,i);var slotId=id.split('div-gpt-ad-')[1].split('-',3).join('-');if(id.includes("/")){slotId=id.split('div-gpt-ad-')[1];slotId=slotId.slice(0,slotId.lastIndexOf('-'));}
for(var s in window.ezslots_raw){if(typeof window.ezslots_raw[s].tap!="undefined"&&window.ezslots_raw[s].tap.includes(slotId)){rawSlots[id]=window.ezslots_raw[s];}}}
if(key!=null){for(var k in rawSlots){rawSlots[k]=rawSlots[k][key];}}}
return rawSlots;},AdLoadComplete:function(library,ids){this.log("ad load complete",library,ids);if(library=='adLoadHB'){var loadIds=[];var refreshIds=[];for(var i=0;i<ids.length;i++){if(this.isGAMOnAuctionComplete(ids[i])){if(this.eligibleRefreshAds.indexOf(ids[i])!=-1){refreshIds.push(ids[i]);}else{loadIds.push(ids[i]);}
this.removeGAMOnAuctionComplete(ids[i]);}else{this.log("not calling GAM on auction complete for",ids[i]);}}
this.log("load ids",loadIds,"refresh ids",refreshIds);if(loadIds.length>0){this.callLibrary('adLoadGAM','LoadAd',[loadIds]);}
if(refreshIds.length>0){this.refreshAds(refreshIds);}}},AdFilled:function(id){__ez.fads.logAdStats(id,'filled');this.callLibrary('adFilled','AdFilled',[id]);this.QueuePageData();},QueuePageData:function(){if(this.pageDataQueued==false){this.pageDataQueued=true;var time=10000;if(this.pageDataCallCount>0){time=10000;}
setTimeout(function(){__ez.fads.RecordPageData();},time);}},RecordPageData:function(){if(this.adFilled.loaded==false){setTimeout(function(){__ez.fads.callLibrary('identity','RecordPageData');return;});}else{this.pageDataQueued=false;this.callLibrary('identity','RecordPageData');}},GetPageTotals:function(){return this.adFilled.GetPageTotals();},__ez_fad_load:function(adLoadBounds,force){if(!force&&!this.__ez_fad_rdy()){return;}
if(this.positionMonitor.loaded==false){this.loadLibrary(this.positionMonitor.url,'positionMonitor');setTimeout(function(){__ez.fads.__ez_fad_load(adLoadBounds,force);},50);return;}
var divs=this.positionMonitor.getPositionsSorted();var s=[];var loadIds=[];var externalIds=[];for(var i=0;i<divs.length;i++){if(this.divsd.indexOf(divs[i])!=-1&&this.isEligibleAdRefresh(divs[i])==false){continue;}
if(this.positionMonitor.isInBounds(divs[i][0],adLoadBounds)){loadIds.push(divs[i][0]);}else if(this.positionMonitor.isInBounds(divs[i][0],adLoadBounds,true)){externalIds.push(divs[i][0]);}}
if(this.positionMonitor.isUniversalVideoPlayerInBounds(adLoadBounds)){this.log('video player in bounds');}
if(loadIds.length>0){for(var i=0;i<loadIds.length;i++){this.LoadAd(loadIds[i],force,true);}}
if(externalIds.length>0){this.callExternalBidders(externalIds);}},handleAdsense:function(id){var ezslotName=window.ezslotdivs&&ezslotdivs[id]&&ezslotdivs[id].slot;if(typeof ezslotName!='undefined'){var rawTargeting=window[ezslotName+'_raw'];if(rawTargeting&&rawTargeting['compid']=='1'){if(typeof window.ezasBuild==='function'&&window.ezasBuild(id)){this.log("built adsense on ",id);__ez.fads.divsd.push(id);return true;}
rawTargeting['compid']='0';}}
return false},addEligibleAdRefresh:function(id){if(this.eligibleRefreshAds.indexOf(id)==-1){this.eligibleRefreshAds.push(id);}},removeEligibleAdRefresh:function(id){if(this.eligibleRefreshAds.indexOf(id)!=-1){this.eligibleRefreshAds.splice(this.eligibleRefreshAds.indexOf(id),1);}},isEligibleAdRefresh:function(id){return this.eligibleRefreshAds.indexOf(id)!=-1;},addGAMOnAuctionComplete:function(id){if(this.callGAMOnAuctionComplete.indexOf(id)===-1){this.callGAMOnAuctionComplete.push(id);}},removeGAMOnAuctionComplete:function(id){var index=this.callGAMOnAuctionComplete.indexOf(id);if(index!==-1){this.callGAMOnAuctionComplete.splice(index,1);}},isGAMOnAuctionComplete:function(id){return this.callGAMOnAuctionComplete.indexOf(id)!==-1;},markIdsAsRunGAMOnAuctionComplete:function(ids){for(var i=0;i<ids.length;i++){if(!this.isGAMOnAuctionComplete(ids[i])){this.addGAMOnAuctionComplete(ids[i]);}
if(this.divsd.indexOf(ids[i])==-1){this.divsd.push(ids[i]);}}},RefreshAdFromPlaceholderId:function(placeholderId,skipExternal,force){},RefreshAd:function(id,skipExternal,force){this.log("refresh ad",id);if(!isNaN(id)){var ids=this.getIdsFromPlaceholderId(id);this.log("refresh ad after placeholder translation",id);for(var i=0;i<ids.length;i++){this.RefreshAd(ids[i],skipExternal,force);}
return;}
this.callLibrary('adLoadGAM','resetTargeting',[id]);this.addEligibleAdRefresh(id);if(force===true){this.skipBangCheck.push(id);}
if(skipExternal!==true&&force!==true){this.callExternalBidders(id);this.addGAMOnAuctionComplete(id);}else{this.LoadAd(id,true,false);}},getIdsFromPlaceholderId:function(placeholderId){if(typeof ez_ad_units==='undefined'){return;}
var slotArray=[];var pcAdUnits=ez_ad_units.filter((adUnit)=>{return adUnit.length>=4?placeholderId===adUnit[3]:false;});for(var i=0;i<pcAdUnits.length;i++){slotArray.push('div-gpt-ad-'+pcAdUnits[i][6]);}
return slotArray;},ShouldResize:function(id){if(this.isOnScreen(id)){return false;}
return true;},ShouldRefresh:function(id){if(!this.isFloating(id)&&!this.isPixel(id)&&!this.isOnScreen(id)){return false;}
return true;},ShouldBang:function(id){if(!this.isFloating(id)&&!this.isPixel(id)&&!this.isBangSkip(id)&&this.version!=97){if(!this.isOnScreen(id)&&this.positionMonitor.loaded&&this.scrollMonitor.loaded&&this.positionMonitor.isInBounds(id,this.scrollMonitor.GetAdLoadBounds(),true)==false){this.addEligibleAdRefresh(id);return false;}else{}}
return true;},loadFloatingAds:function(timeout,force){this.log("load floating ads",timeout,force);if(this.__ez_fad_rdy()||force){if(!this.floatingAdsShown&&typeof window.__ez_fad_floating!=='undefined'&&window.__ez_fad_floating.length>0){this.floatingAdsShown=true;setTimeout(function(){window.__ez.fads.callLibrary('adLoadGAM','ShowFloatingAds');},timeout);}else if(!this.floatingAdsShown){this.triggerFloatingOnAdd=true;}}},FloatingAdded:function(){if(this.onScreenLoadStatus==2){this.loadFloatingAds(0,true);}},__ez_fad_add:function(id){if(this.addedDivs.indexOf(id)==-1){this.addedDivs.push(id);}},GetInteractionEvents:function(){return["scroll","mousedown","keydown","touchstart","pointerdown","wheel"];},__ez_fad_rdy:function(){if(document.body!==null&&(this.__ez_fad_haspo==false&&this.doc_ht>this.vp_ht||this.__ez_fad_hascp)||document.readyState!="loading"){return true;}else{this.doc_ht=this.__ez_fad_docht();this.vp_ht=this.__ez_fad_vpht();}
return false;},log:function(){if(__ez.fads.logEnabled){let args=Array.from(arguments);var a=new Date();args.unshift(`${a.getHours()}:${a.getMinutes()}:${a.getSeconds()}.${a.getMilliseconds()}`);args.unshift('%c🧠 ezjit::');args.splice(1,0,'color: #5FA624;');console.log.apply(console,args);}},logAdStats:function(id,stage){if(!__ez.fads.logEnabled){return;}
if(Array.isArray(id)){for(var idx=0;idx<id.length;idx++){this.logAdStats(id[idx],stage);}
return;}
try{var slotID=id.replace('div-gpt-ad-','');slotID=slotID.substr(0,slotID.lastIndexOf('-'));var refreshCnt=1;if(window.googletag&&window.googletag.pubads){var matchingSlots=window.googletag.pubads().getSlots().filter(s=>s.getSlotElementId()===id);if(matchingSlots.length>0){refreshCnt=matchingSlots[0].getTargeting('alc')[0]||0;}}
__ez.fads.adStats=__ez.fads.adStats||{};__ez.fads.adStats[id]=__ez.fads.adStats[id]||[];while(__ez.fads.adStats[id].length<=refreshCnt-1){__ez.fads.adStats[id].push({});}
__ez.fads.adStats[id][refreshCnt-1]=__ez.fads.adStats[id][refreshCnt-1]||{};switch(stage){case 'load':__ez.fads.adStats[id][refreshCnt-1].loadStatsTime=performance.now()/1000;__ez.fads.adStats[id][refreshCnt-1].initialFloor=ezslots_raw.filter(s=>s.tap.includes(slotID))[0].br1/100;break;case 'adloadhb':__ez.fads.adStats[id][refreshCnt-1].hbStatsTime=performance.now()/1000;__ez.fads.adStats[id][refreshCnt-1].bestHBBid=null;if(epbjs.adUnits.filter(a=>a.code==id).length<=0){this.log("logAdStats :: ad unit not contained in epbjs.adUnits finished adloadhb",id);break;}
var bids=__ez.fads.adLoadHB.bidCache.getBidsForAdUnit(epbjs.adUnits.filter(a=>a.code==id)[0]);if(bids!==null||bids.length>0){__ez.fads.adStats[id][refreshCnt-1].bestHBBid=bids.sort((i,j)=>{return j.cpm-i.cpm})[0].cpm;}
break;case 'bang':var bang={};bang.bangTime=performance.now()/1000;bang.bangStartingFloor=ezslots_raw.filter(s=>s.tap.includes(slotID))[0].br1/100;__ez.fads.adStats[id][refreshCnt-1].bangs=__ez.fads.adStats[id][refreshCnt-1].bangs||[];__ez.fads.adStats[id][refreshCnt-1].bangs.push(bang);break;case 'filled':__ez.fads.adStats[id][refreshCnt-1].fillTime=performance.now()/1000;__ez.fads.adStats[id][refreshCnt-1].filledFloor=ezslots_raw.filter(s=>s.tap.includes(slotID))[0].br1/100;__ez.fads.adStats[id][refreshCnt-1].filledSSID=_ezim_d[slotID].ssid;break;}}catch(e){this.log("Error logging ad stats",e);}},showScrollAnchor:function(){const anchor=document.getElementById('ezmobfooter');if(anchor==null){return;}
Array.from(document.getElementsByClassName('ezmob-footer')).forEach(s=>{s.style.top='0px';});document.body.style.transition='padding-top 0.5s ease-in-out';document.body.style.paddingTop='100px';setTimeout(function(){try{let ids=ezslots_raw.filter(s=>s.tap.includes('medrectangle-2')).map(s=>'div-gpt-ad-'+s.tap.split('-').slice(0,3).join('-')+'-0');window.__ez_fad_floating=window.__ez_fad_floating.concat(ids);this.onScreenDivs=this.onScreenDivs.concat(ids);this.markIdsAsRunGAMOnAuctionComplete(ids);this.loadAdsWaitForExternal(ids);}catch(e){this.log("Error showing scroll anchor",e);}}.bind(this),750);},getAmazonBidFromHash:function(hash){var self=this;function resolveBid(){return self.callLibrary('amznH2Bid','GetBidForHash',[hash]);}
if(this.amznH2Bid.loaded===true){return{then:function(callback){return callback(resolveBid());}};}
return{then:function(callback){self.loadLibrary(self.amznH2Bid.url,'amznH2Bid');setTimeout(function(){return callback(resolveBid());},750);}};},};__ez.fads.init();function __ez_hb_render(id){setTimeout(function(){window.top.epbjs.renderAd(document,id);},10);}__ez.fads.adLoadGAM=(__ez.fads.adLoadGAM&&__ez.fads.adLoadGAM.loaded===true)?__ez.fads.adLoadGAM:{loaded:true,floatingAdsShown:false,slotsDone:[],slotKV:{},isInit:false,floatingStyleLoaded:false,bangerName:'IL11ILILIIlLLLILILLLLIILLLIIL11111LLILiiLIliLlILlLiiLLIiILL',version:1,refreshTargetingResetParams:{'hb_bidder':'','hb_adid':'','hb_pb':'','hb_opt':'','nam':'','pwtsid':'','pwtbst':'','hb_ssid':'','hb_format':'','hb_rt':'','epb':'','epa':'','epp':'','eps':'','epf':'','amznbid':'','amzniid':'','amznp':'','amznsz':'','r_amznbid':'','r_amzniid':'','r_amznp':'','rbs':''},log:__ez.fads.log,hbAsFloorThreshold:0.75,hbAsFloorCap:10.0,init:function(viewportHeight,documentHeight,version){if(this.isInit){return;}
if(version){this.version=version;}else{this.version=__ez.fads.version;}
this.isInit=true;if(this.version!=4){this.LoadGPT();}
if(this.version==15){this.hbAsFloorThreshold=0.5;}
__ez.fads.LibraryLoaded("adLoadGAM");},reset:function(){this.floatingAdsShown=false;this.slotsDone=[];this.slotKV={}},cleanupAdData:function(divId){this.slotsDone=this.slotsDone.filter(function(id){return id!==divId;});},RefreshAds:function(ids){if(!Array.isArray(ids)){ids=[ids];}
if(typeof window[this.bangerName]!='undefined'){for(var i=0;i<ids.length;i++){var id=ids[i];if(__ez.fads.adLoadHB.loaded===true){__ez.fads.adLoadHB.SetAdBid(id);}
this.adjustFloor(id);this.adjustFloorToExtBid(id);window[this.bangerName].RefreshById(id);}}else{setTimeout(function(){__ez.fads.adLoadGAM.RefreshAds(ids)},100);}},replaceOpenwrapBid:function(slot,hb_bid){var ow_bid=slot.getTargeting('ow_hb_opt')[0];if(typeof ow_bid==='undefined'||ow_bid===''||isNaN(ow_bid)){return false;}
ow_bid=parseFloat(ow_bid);if(ow_bid>hb_bid){this.log("adjustFloorToHBBid: openwrap bid is higher",slot.getSlotElementId(),ow_bid,hb_bid);var targetingParams=slot.getTargetingMap();for(var key in targetingParams){if(key.startsWith('ow_hb_')){var newKey='hb_'+key.slice(6);slot.setTargeting(newKey,targetingParams[key][0]);this.log("adjustFloorToHBBid: setting targeting",slot.getSlotElementId(),newKey,targetingParams[key][0]);}}
return ow_bid;}
return false;},adjustFloor:function(id){if(__ez.fads.adFilled.loaded!==true){this.log("adjustFloor: adFilled not loaded",id);return;}
var percentOfMax=1.0;if(this.version==16){percentOfMax=1.0;}else{return;}
var maxFloor=__ez.fads.adFilled.GetMaxFloor(id,percentOfMax,2);this.log("adjustFloor: max floor",id,maxFloor,percentOfMax);if(maxFloor!==false){var slot=this.GetSlotById(id);var floor=this.getFloor(slot);this.log("adjustFloor: max floor",id,maxFloor,floor);if(floor>maxFloor){this.setFloor(slot,maxFloor);}}},adjustFloorToExtBid:function(id){var slot=this.GetSlotById(id);if(slot==null){return;}
var hb_bid=slot.getTargeting('hb_opt')[0];if(typeof hb_bid==='undefined'||hb_bid===''||isNaN(hb_bid)){return;}
var bidType=slot.getTargeting('hb_bidtype')[0];hb_bid=parseFloat(hb_bid);var floor=this.getFloor(slot);this.log("adjustFloorToHBBid: header bid vs floor!",id,"hb_bid:",hb_bid,"floor:",floor,"cap:",this.hbAsFloorCap,"hb must be more than:",(floor*this.hbAsFloorThreshold));let isForcedBid=false;let hbBidder=slot.getTargeting('hb_bidder')[0];if(hbBidder===new URLSearchParams(window.location.search).get('ez_force_hb_solo')){isForcedBid=true;}
if(hb_bid>(floor*this.hbAsFloorThreshold)||hb_bid>this.hbAsFloorCap||isForcedBid){this.setFloor(slot,hb_bid,bidType);}
if(window.ezhbonly){this.activateHbTargeting(slot,bidType);}},getFloor(slot){if(!slot){return 0;}
var floor=parseInt(slot.getTargeting('br1')[0]);if(typeof floor==='undefined'||floor===''||isNaN(floor)){return 0;}
return floor/100;},setFloor(slot,floor,bidType){if(!slot){return;}
var GAMAccount=slot.getTargeting('ga')[0];var formattedFloor=this.formatBid(floor,GAMAccount);if(window.ezoibfh.hasOwnProperty(formattedFloor)){var bidFloorHash=window.ezoibfh[formattedFloor];}
this.log("adjustFloorToHBBid: setting floor for ",slot.getSlotElementId(),floor,formattedFloor,bidFloorHash,slot.getTargeting('hb_rt')[0]);if(typeof bidFloorHash!=='undefined'){slot.setTargeting('br1',formattedFloor);slot.setTargeting('eb_br',bidFloorHash);this.activateHbTargeting(slot,bidType);}},activateHbTargeting:function(slot,bidType){if(bidType=='ow'){this.log("adjustFloorToHBBid: activating openwrap line item",slot.getSlotElementId());slot.setTargeting('pwtbst','1');slot.setTargeting('nam','');}else if(bidType=='hb'){this.log("adjustFloorToHBBid: activating prebid line item",slot.getSlotElementId());slot.setTargeting('nam','1');slot.setTargeting('pwtbst','');}else{slot.setTargeting('pwtbst','');slot.setTargeting('nam','');}},LoadAd:function(ids,attempt){if(!Array.isArray(ids)){ids=[ids];}
var idsToDo=[];for(var i=0;i<ids.length;i++){if(this.slotsDone.indexOf(ids[i])==-1){idsToDo.push(ids[i]);}}
ids=idsToDo;if(ids.length<1){return;}
if(attempt<1){attempt=1;}else if(attempt>100){return;}
this.slotsDone=this.slotsDone.concat(ids);googletag.cmd.push(function(){if(googletag.pubadsReady!==true){setTimeout(function(){__ez.fads.adLoadGAM.SlotsNotDone(ids);__ez.fads.adLoadGAM.LoadAd(ids,attempt+1)},100);return;}
var gamSlots=[];for(var i=0;i<ids.length;i++){var id=ids[i];var slot=__ez.fads.adLoadGAM.GetSlotById(id);if(slot==null){if(!__ez.fads.initslots.hasOwnProperty(id)){__ez.fads.log("id does not exist in initslots",id);continue;}
var slot_id=__ez.fads.initslots[id](5);var slot=window[slot_id];}
if(parseInt(slot.getTargeting('al')[0])%1000==5){__ez.fads.adLoadGAM.showFloatingStyle();}
if(!slot.getOutOfPage()&&document.getElementById(slot.getSlotElementId())===null){__ez.fads.log("gam slot element isn't on the page",id,slot.getSlotElementId());setTimeout(function(){__ez.fads.adLoadGAM.SlotsNotDone(id);__ez.fads.adLoadGAM.LoadAd(id,attempt+1)},100);continue;}else{googletag.display(slot.getSlotElementId());if(typeof window.ezoResponsiveSizes!='undefined'&&typeof slot!='undefined'&&slot!=null&&slot.getTargeting('al')[0]!='1005'&&slot.getTargeting('al')[0]!='3005'){var sizeString=__ez.fads.adLoadGAM.buildSlotResponsiveSizes(slot.getSlotElementId());if(sizeString!==''){__ez.fads.adLoadGAM.adjustResponsiveDiv(slot.getSlotElementId());slot.defineSizeMapping(sizeString);}}
if(typeof window.__ezWillLoadCnx!=='undefined'&&typeof slot!='undefined'&&slot!=null&&slot.getTargeting('al')[0]=='1039'){__ez.fads.adLoadGAM.loadConnatix(slot);continue;}
if(__ez.fads.adLoadHB.loaded===true){__ez.fads.adLoadHB.SetAdBid(id);}
__ez.fads.adLoadGAM.setQueuedTargeting(id);__ez.fads.adLoadGAM.adjustFloor(id);__ez.fads.adLoadGAM.adjustFloorToExtBid(id);gamSlots.push(slot);}}
__ez.fads.log("initial loading gam slots",ids,gamSlots);if(gamSlots.length>0){googletag.pubads().refresh(gamSlots);for(var i=0;i<gamSlots.length;i++){if(typeof __ez!=='undefined'&&typeof __ez.pel!=='undefined'){__ez.pel.Add(gamSlots[i],[(new __ezDotData('fetched',1))]);}}
if(typeof __ez!=='undefined'&&typeof __ez.pel!=='undefined'){__ez.pel.Fire();}}});if(this.floatingAdsShown!==true){setTimeout(window.__ez.fads.loadFloatingAds(0,true),0);}},GetTargeting:function(id,key){var slot=this.GetSlotById(id);if(slot){return slot.getTargeting(key);}
return[];},GetStatSourceId:function(id){var slot=this.GetSlotById(id);if(slot){if(slot.getTargeting('nam')[0]=='1'){return parseInt(slot.getTargeting('hb_ssid')[0]);}else{return 35;}}
return 0;},SlotsNotDone:function(ids){for(var i=0;i<ids.length;i++){var index=this.slotsDone.indexOf(ids[i]);if(index>-1){this.slotsDone.splice(index,1);}}},ShowFloatingAds:function(){if(this.floatingAdsShown===true||typeof __ez_fad_floating==='undefined'||__ez_fad_floating.length<1){return;}
this.floatingAdsShown=true;this.showFloatingStyle();this.LoadAd(__ez_fad_floating);},showFloatingStyle:function(){if(this.floatingStyleLoaded){return;}
this.floatingStyleLoaded=true;var e=document.getElementById('ezmobfooter');if(e!=null){e.classList.add('ezmobtrans');}else{var head=document.head||document.getElementsByTagName('head')[0];var style=document.createElement('style');head.appendChild(style);var css="body > #ezmobfooter{bottom:0px;visibility:visible;}";style.type='text/css';if(style.styleSheet){style.styleSheet.cssText=css;}else{style.appendChild(document.createTextNode(css));}}},loadConnatix:function(slot){window.__ezsbwcmd=window.__ezsbwcmd||[];var sr=[slot];window.__ezsbwcmd.push(function(){if(typeof __ezcnxPlayer==='undefined'||!__ezcnxPlayer.getSize()){googletag.pubads().refresh(sr);}else{__ezcnxPlayer.once('removed',function(){googletag.pubads().refresh(sr);});}});},SetTargeting:function(id,key,value){var slot=this.GetSlotById(id);if(slot){slot.setTargeting(key,value);if(this.slotKV[id]&&this.slotKV[id][key]){delete this.slotKV[id][key];}}else{this.slotKV[id]=this.slotKV[id]||{};this.slotKV[id][key]=value;}},resetTargeting:function(id){var slot=this.GetSlotById(id);if(slot){slot.updateTargetingFromMap(this.refreshTargetingResetParams);}},setQueuedTargeting:function(id){if(this.slotKV[id]){var slot=this.GetSlotById(id);if(slot){for(var key in this.slotKV[id]){slot.setTargeting(key,this.slotKV[id][key]);}}}},GetSlotById:function(n){if(typeof googletag=='undefined'||typeof googletag.pubads!='function'||typeof googletag.pubads().getSlots!='function'){return;}
var slots=googletag.pubads().getSlots();for(var i=0;i<slots.length;i++){if(slots[i].getSlotElementId()==n){return slots[i];}}},LoadGPT:function(){var attempts=0;var loadGpt=function(){var scriptTag="script";var src="//securepubads.g.doubleclick.net/tag/js/gpt.js";var script=document.createElement(scriptTag);script.async=true;script.type="text/javascript";script.src=src;script.onerror=function(event){if(attempts>1){return;}
setTimeout(loadGpt,500);};script.onload=function(){if(attempts<=1){return;}
if(typeof reportEzReqError==='function'){reportEzReqError(src,"gpt.js");}};var head=document.head||document.getElementsByTagName('head')[0];head.appendChild(script);attempts++;};loadGpt();},buildSlotResponsiveSizes:function(domID){var gptSizeMapping=googletag.sizeMapping();if(typeof window.ezoResponsiveSizes==='undefined'||typeof window.ezoResponsiveSizes[domID]==='undefined'){return false}
window.ezoResponsiveSizes[domID].responsiveSizes.sort(function(a,b){var largerWidth=a.minWidth>b.minWidth;var equalWidth=a.minWidth===b.minWidth;var largerHeight=a.minHeight>b.minHeight;if(largerWidth)return-1;if(equalWidth&&largerHeight)return-1;return 0;});if(window.ezoResponsiveSizes[domID].responsiveSizes){var hasSizesAtZero=false;for(var sizeIdx=0;sizeIdx<window.ezoResponsiveSizes[domID].responsiveSizes.length;sizeIdx++){var sizeDirective=window.ezoResponsiveSizes[domID].responsiveSizes[sizeIdx];if(sizeDirective.minWidth===0&&sizeDirective.minHeight===0){hasSizesAtZero=true;}
gptSizeMapping.addSize([sizeDirective.minWidth,sizeDirective.minHeight],sizeDirective.sizes);}
if(!hasSizesAtZero){gptSizeMapping.addSize([0,0],[]);}}else{return false;}
var mapping=gptSizeMapping.build();if(mapping.length<1){return false;}else{return mapping;}},adjustResponsiveDiv:function(divID){if(!window.ezoResponsiveSizes||!window.ezoResponsiveSizes[divID]){return;}
var adDiv=document.getElementById(divID);if(!adDiv){return;}
var fillSize=__ez_get_largest_ad_size(divID);if(fillSize.length===0||fillSize[0]===0||fillSize[1]===0){return;}
var orivDivSize=[adDiv.getAttribute('ezaw'),adDiv.getAttribute('ezah')];if(orivDivSize[0]===null||orivDivSize[1]===null){return;}
if(fillSize[0]>=orivDivSize[0]){return;}
this.gamResponsiveResizeDiv(adDiv,fillSize,false);this.gamResponsiveResizeDiv(adDiv.parentElement,fillSize,true);this.gamResponsiveResizeDiv(adDiv.parentElement.parentElement,fillSize,false);},gamResponsiveResizeDiv:function(adDiv,fillSize,isParent){if(!adDiv){return;}
adDiv.style.minWidth=fillSize[0]+'px';adDiv.style.maxWidth="100%";if(isParent){adDiv.style.width=fillSize[0]+'px';}else{adDiv.style.width='';}},getLargestAdSize:function(slotID){var applicableSizes=[];if(ezoResponsiveSizes[slotID]){var clientWidth=document.documentElement.clientWidth;var clientHeight=document.documentElement.clientHeight;var bestResponsiveFit=null;window.ezoResponsiveSizes[slotID].responsiveSizes.forEach(responsiveSize=>{var appliesToViewport=responsiveSize.minWidth<=clientWidth&&responsiveSize.minHeight<=clientHeight;var betterResponsiveFit=bestResponsiveFit===null||responsiveSize.minWidth>bestResponsiveFit.minWidth||(bestResponsiveFit.minWidth==responsiveSize.minWidth&&responsiveSize.minHeight>bestResponsiveFit.minHeight);if(appliesToViewport&&betterResponsiveFit){bestResponsiveFit=responsiveSize;}});if(bestResponsiveFit!==null){applicableSizes=bestResponsiveFit.sizes;}}
var largestDims=[0,0];applicableSizes.forEach(size=>{if(size[0]>largestDims[0]){largestDims[0]=size[0];}
if(size[1]>largestDims[1]){largestDims[1]=size[1];}});return largestDims;},formatBid:function(e,t){var o=e;var gaTargets=this.getGaTargets();if(o>300){o=300;}
if(this.isEzoicGamAccount(t,gaTargets)){o=o<=0?0:o<=0.5?2*Math.floor(100*o/2+0.5):o<=1?10*Math.floor(10*o+0.5):o<=3?20*Math.floor(100*o/20+0.5):o<=10?50*Math.floor(100*o/50+0.5):o<=30?100*Math.floor(100*o/100+0.5):o<=50?200*Math.floor(100*o/200+0.5):o<=120?500*Math.floor(100*o/500+0.5):1000*Math.floor(100*o/1000+0.5);if((o/100>e)&&(o>2)){o-=o<=50?2:o<=100?10:o<=300?20:o<=1000?50:o<=3000?100:o<=5000?500:1000;}}else{o=o<=0?0:o<=1?10*Math.floor(10*o+0.5):o<=3?20*Math.floor(100*o/20+0.5):o<=10?50*Math.floor(100*o/50+0.5):o<=30?100*Math.floor(100*o/100+0.5):o<=50?200*Math.floor(100*o/200+0.5):o<=120?500*Math.floor(100*o/500+0.5):1000*Math.floor(100*o/1000+0.5);if((o/100>e)&&(o>2)){o-=o<=100?10:o<=300?20:o<=1000?50:o<=3000?100:o<=5000?200:o<=12000?500:1000;}}
return o;},isEzoicGamAccount:function(accountId,gaTargets){if(accountId==""){return true;}
return gaTargets.includes(accountId);},getGaTargets:function(){var DfpToADXMap={"1254144":"ca-pub-6396844742497208","104418548":"ca-pub-7958959566206860","21732118914":"ca-pub-5902083285302779","23019951954":"ca-pub-4940289314435286","23057718401":"ca-pub-4419175981112334","23057360293":"ca-pub-1175987143200523","23058280356":"ca-pub-1164220389861002","23058284193":"ca-pub-2105917194427515","23058297354":"ca-pub-9462567873887378","23057404840":"ca-pub-1106480674481786",};let results=[];for(let value of Object.values(DfpToADXMap)){let lastSeven=value.substring(value.length-7);results.push(lastSeven);}
return results;}};__ez.fads.adLoadGAM.init();
window.isEZABL=false;window.ezmadspc=300;window.ezoViewCheck=false;
window.ezDisableInitialLoad=false;
window.googletag=window.googletag||{};googletag.cmd=googletag.cmd||[];
window.ezogetbrkey = function(s){ var k = 'br1';var k2 = 'eb_br';if(window.ezogtk == ""){k='br1u';k2='eb_bru';}else if(window.ezogtk != "NT"){k='br1t';k2='eb_brt';} s.setTargeting('br1', s.getTargeting(k));s.setTargeting('eb_br', s.getTargeting(k2));};googletag.cmd.push(function() {googletag.pubads().enableSingleRequest();googletag.pubads().addEventListener('slotRenderEnded', function(event) { __ez.queue.addFunc("ezbanger", "ezbanger", event, false, ['banger.js'], true, true, false, true); });googletag.pubads().addEventListener('impressionViewable', function(event) { __ez.queue.addFunc("ezvb", "ezvb", event, false, ['banger.js'], true, true, false, true); });googletag.pubads().addEventListener('slotVisibilityChanged', function(event) { __ez.queue.addFunc("ezvt", "ezvt", event, false, ['banger.js'], true, true, false, true); });googletag.pubads().addEventListener('slotResponseReceived', function(event) { __ez.queue.addFunc("ezsr", "ezsr", event, false, ['banger.js'], true, true, false, true); });googletag.pubads().addEventListener('slotRequested', function(e) { window.ezsrqt[e.slot.getSlotElementId()] = Date.now();});googletag.setConfig({adExpansion: {enabled: true}});googletag.pubads().disableInitialLoad();googletag.pubads().enableLazyLoad({fetchMarginPercent: 700, renderMarginPercent: 10, mobileScaling: 1.0});var ezppid = document.cookie.split('; ').reduce((val, cookie) => val || (cookie.startsWith('ezppid_ck=') ? cookie.split('=')[1] : null), null); if (ezppid) googletag.pubads().setPublisherProvidedId(ezppid);googletag.enableServices();googletag.pubads().setTargeting('iab_ct', ['631']);});window.ezoll = false;window.ezoadxnc = '1254144';window.ezoadhb = '220';var ezoibfh = {0:'zero',1000000:'off',10000:'f1e225445ec024e41bfd8ce2ba4aa91b',1000:'c5429b6ddd929d0bc40a832a87789a7c',100:'a495ce7dbb4cefcd3e0a722048894f41',10500:'42a903505d4ae4416a53434b5cb0a4d9',10:'291d27313eb66c50243129b23df8a579',11000:'b6b0d056da189d64dad3536d1704244e',1100:'39abb99448d54704c4afa42efe76e15d',11500:'8eb8a64575469eb8117112aafe0739a6',12000:'e66f3eb6142bbf8f4ebbbd31c5540a1a',1200:'736e09a0771285737509ab8954c475a7',120:'58ef7bddb438af5e257c4377f32c243a',12:'14e8a85d4c42ff1db8790cbef9e33493',13000:'ca9543a8ad10743f5aa794997ac1abc5',1300:'bfa042bdb1583c959161b7823290dc1f',14000:'bbd63bbbf7aa5d55b64d29b4f3919d02',1400:'04b5efc3207e2390972f099a6a3c4757',140:'af063c244089b52ec5a0423a258f1f8e',14:'ad0061a38dd7c6f7bcb692aee88dfda4',15000:'12f5d1db0577f9224a03666dcf42dc53',1500:'d81e229576f8cb8a43ff5c6a8e596727',16000:'0be7d3ca3d2b552da080ad176e959a53',1600:'6dbaa2f5e27e83e2fcd15988d9095988',160:'3530fcb6bcc13dc3c1712eaef7d92700',16:'e29f69dd468d31a5514dc9b5587ce757',17000:'3da233249b44074269c3efb64036ffd5',1700:'ff69c327c284033fca821ae81630bfa9',18000:'f889e5f2be62dc0efa8535a9ac72a5ae',1800:'72c13a89ac876aaffdde39253459460b',180:'9ae587f95e95c876b7b76fd4c72a3838',18:'8de355ef1cf56b7da61277050d9957b1',19000:'9df342ed088a8ed25a61eedd7f755215',1900:'65b2c11be72ed8610e2ac0304f3023a9',20000:'1c275170760cdb315e09a0caab859d82',2000:'12a3b3570adcf20fd41a00445219acaa',200:'86802a923a1f32517e4c5d3b6d550271',20:'7432360301409ae695ba255f16fbcf06',21000:'e2cb818af42582fdeb5b2404292a4fdc',2100:'b2ac58e6c0c84fc65f344f47dd85768b',22000:'186f90c3cb2b602e78597d6478cc05e6',2200:'2620dac3b050a8e36c132f49cccab5a1',220:'43aa1607a0c08c74b14a9039e7b909b4',22:'1e913e99b80640fd5b86a539e5b97c94',23000:'552e8e97b01f90c98fb547b2a5981bd0',2300:'a835e008e248a793da87524a4919f755',24000:'848e945a6d42b7cae5b508d9d9c916fd',2400:'6240c545bce1855c4e5a6ca430f526b1',240:'8de2c8ca79e8623e3cb37120a35ebaa2',24:'e66c30deca31b19eda212eeca1258584',25000:'ede18341593c9244092e13352cd25399',2500:'78e9436ba8e29037bc31f94589331e0b',26000:'3353de688cbba074dc3d34ad3502a0ff',2600:'cc65d2d1fcda72df55233f97cf215dad',260:'57914c3716312cb7e954090f0717ea25',26:'bf9a045b836005b6c23b7b0749249612',27000:'8462e0f3d6ab7810a949e580cef2530d',2700:'401612ca672af30f67eaf5e0989ce385',28000:'6e7360126718801a2c512a507353f6ba',2800:'a9ec56005762ef40746ec1b6d554f472',280:'c16fac08e79a971524b1c6834f5caad3',28:'674294a1b21a1e89fc99c14c9b17be44',29000:'c50a963ecc62061b386b119512894997',2900:'ef3231a19d034bff92faf99318a47a5f',2:'b6c98a8bb15764f1c4ee331dcb724178',30000:'bdc0577cc25fcd86ffc2dedc35a93ae4',3000:'92831edb305b955e915a7cc2288d5df6',300:'90c3c48d0172916d27c102ea4aa9d49c',30:'54d0fa6d5f6aabe7623cb24faa42a441',3200:'41ad5c6ea7dab736638507e437e60604',32:'d31e71883d00099e275b6c5878eed023',3400:'2c0082dd1efc5e4dfdd4f50677fea822',34:'a7a863b24978e69c4cdbb5a49be70d5e',350:'9e0a1ce5b2455cb9b48d5df4c6bf4053',3600:'81f896ad12450b2f0257b1df6d3f1edc',36:'8c5ffefb122f59a66a8b7672d4452af2',3800:'58e03b675175bbbec8566d319041c5ee',38:'23b5ca1d9de2587e6a4ecfd33d61b709',4000:'e95a0029a1c0d52e1f82ee010826e7d9',400:'76163170a8636ae5b88417f095893e08',40:'ee685f77592ce296910ee91457d66ba3',4200:'e9b52ed700c176b9b3f036aa176f3f3e',42:'947f1d5169cc7d0f997560e34838fb04',4400:'a2de9c8773c426848d7815dff1d2d44f',44:'a928cf2c3ad36f5e9ed2d90f655c1dc9',450:'6e85b37de1b1ffc2593baa5d6e4b02fc',4600:'d297138284357206d38c781a2291b99a',46:'fe5b0c99ab7ba15f050582be1301303f',4800:'f0459c7057d45e6fbbed62c0762b551e',48:'8fc09e60bfd78aa82afac0405213359a',4:'9c3e4ee8eae7f1433cb2fe69b1326605',5000:'116f73d8738ced0c5546d5313109581e',500:'5f2b94bb26a5aa9b1a00e66d30cfd5ec',50:'3ba982fc4238dd4197b1d51b345478dc',5500:'b069a06daabd6e3043166f0e7a2edef4',550:'26dfa00588543c52511429ade391f561',6000:'49d60519eec4f00cfb2d91dec1e48d41',600:'45a351e981f435b4c20fafca8a5d741c',60:'c352ba581bd3ffd8cea608cf2d55f519',6500:'b6ac10cddc8471927cec0144110502e9',650:'5bac35e1a3b6adc56da706000a645484',6:'33dd523f8e4dda158f0aa99686dda7f2',7000:'4552fb4beab2a055aec0d6113a8d9e42',700:'8b07bae800b215e481d05a271b3e723b',70:'527e52c10635ac8136a4c84094ee49a8',7500:'0de5c793b95df3adacbee8e14c308afc',750:'6ac330e431a70c7d8ce9fb95aee95c72',8000:'e41b3739f340bda9dcfb30f79c9db1c9',800:'dc3573d5dc41abdf97751be02f53537f',80:'dfa60cee6e1053fc0c9e607c8047bd28',8500:'d5abc50791c030d76efa2ded02dcc115',850:'5297de5240aa45da173a0792747e0d26',8:'2e8b8c60843e52e5aaa1e3a52287a2bb',9000:'e4c87a0c427c95c548a2ad50bc2fc99d',900:'eeb0e32289ff31f9ddef18331038e5e9',90:'b355e9227b551c119a30a68852723b62',9500:'6fd3046d2172040882079eb07d0038c9',950:'c410f2a2b0c2123f4b6651cda6c5cf53'};var ezaxmns={};var ezaucmns={};ezaxmns["div-gpt-ad-online_python_com-medrectangle-3-0"]=24;
var __ez_fad_floating = ['div-gpt-ad-online_python_com-medrectangle-2-0'];if(typeof __ez.fads != 'undefined' && typeof __ez.fads.FloatingAdded == "function"){__ez.fads.FloatingAdded();}
	function __ez_init_slot(bvr, did, slotNum, defineFunc) {
		googletag.cmd.push(function() {
			defineFunc();
			ezrpos[slotNum]=slotNum;
			ezslots.push("ezslot_" + slotNum);
			if(__ez.fads.kvStore[did] !== 'undefined') {
				for (var name in __ez.fads.kvStore[did]) {
					if (!__ez.fads.kvStore.hasOwnProperty(name)) {
						ezSetSlotTargeting(did, name, __ez.fads.kvStore[did][name]);
					}
				}
				__ez.fads.kvStore[did] = {};
			}
		});return "ezslot_" + slotNum;
	}
var ezslot_1_raw = {'a':'1','iid1':'1293263702248002','eid':'1293263702248002','t':'134','d':'214055','t1':'134','pvc':'0','ap':'1119','sap':'1119','a':'|0|','as':'revenue','plat':'1','bra':'mod1-c','ic':'1','at':'mbf','adr':'399','ezosn':'1','reft':'tf','refs':'30','refa':'0','ga':'2497208','gala':'','rid':'99998','pt':'1','al':'1001','compid':'0','tap':'online_python_com-box-2-1293263702248002','eb_br':'674294a1b21a1e89fc99c14c9b17be44','eba':'1','ebss':[10017,10082,10061,10015,10063,11307,11291,11315,11296],'asau':'4952030191','bv':'12','bvm':'0','bvr':'2','avc':'69','shp':'1','ftsn':'12','ftsng':'12','acptad':'1','br1':'28','br2':'14','ezoic':'1','nmau':'0','mau':'0','stl':[157,168,0,67,0,193,142,20,0,0,192,31,902,903,901,902,903],'deal1':[17,19,20,21,22,23,24,25,26,27,28,29,30,760,761,813,815,816,817,818,819,893,899,903,917,918,919,1794,2310,2339,2351,2526,2527,2610,2688,2693,2761,2763,2764,2765,3044,3045,3053,3054,3154,3430,3455,3456,3457,3458,3460,3682,3683,3684,3915,3919,3933,4184,4185,4186,4276,4604,4605,5747,6044,6045,6293,6294,6295,6983,7035,7036,7046,7060,7144,7327,7330,7331,2030,4312,4312,2030,6772,5534,7175,7053,774],'ax_ssid':'10082'}; window.ezslots_raw.push(ezslot_1_raw); window.ezslotdivs['div-gpt-ad-online_python_com-box-2-0'] = {slot:'ezslot_1',adunit:'/1254144,22108676293/online_python_com-box-2'};__ez.fads.initslots['div-gpt-ad-online_python_com-box-2-0'] = function(bvr){var defScript = function() {ezslot_1 = googletag.defineSlot('/1254144,22108676293/online_python_com-box-2',[160,600],'div-gpt-ad-online_python_com-box-2-0').addService(googletag.pubads()).setCollapseEmptyDiv(false);ezSetTargetingFromMap(ezslot_1,ezslot_1_raw);};return __ez_init_slot(bvr,'div-gpt-ad-online_python_com-box-2-0',1, defScript);};
var ezslot_0_raw = {'a':'1','iid1':'1427516974217456','eid':'1427516974217456','t':'134','d':'214055','t1':'134','pvc':'0','ap':'1100','sap':'1100','a':'|0|','as':'revenue','plat':'1','bra':'mod1-c','ic':'1','at':'mbf','adr':'399','ezosn':'0','reft':'tf','refs':'30','refa':'0','ga':'2497208','gala':'','rid':'99998','pt':'5','al':'1005','compid':'0','tap':'online_python_com-medrectangle-2-1427516974217456','eb_br':'43aa1607a0c08c74b14a9039e7b909b4','eba':'1','ebss':[10017,10082,10061,10015,10063,11307,11291,11315,11296],'asau':'4952030191','bv':'23','bvm':'0','bvr':'3','avc':'115','shp':'1','ftsn':'12','ftsng':'12','br1':'220','br2':'120','ezoic':'1','nmau':'0','mau':'0','stl':[157,193,0,67,0,193,142,20,0,0,192,31,902,903,901,902,903],'deal1':[20,21,22,23,24,25,26,27,28,29,30,760,761,813,814,815,816,817,818,819,893,899,903,917,918,919,1794,2310,2339,2526,2527,2763,2764,2765,3054,3154,3430,3455,3456,3457,3458,3460,3682,3683,3684,3915,3919,3933,4184,4185,4186,4604,4605,5747,6044,6045,6293,6294,6295,6983,7036,7046,7060,7144,2030,4312,4312,2030,6772,5534,7175,7053,774],'ax_ssid':'10082'}; window.ezslots_raw.push(ezslot_0_raw); window.ezslotdivs['div-gpt-ad-online_python_com-medrectangle-2-0'] = {slot:'ezslot_0',adunit:'/1254144,22108676293/online_python_com-medrectangle-2'};__ez.fads.initslots['div-gpt-ad-online_python_com-medrectangle-2-0'] = function(bvr){var defScript = function() {ezslot_0 = googletag.defineSlot('/1254144,22108676293/online_python_com-medrectangle-2',[970,90],'div-gpt-ad-online_python_com-medrectangle-2-0').addService(googletag.pubads()).setCollapseEmptyDiv(false);ezSetTargetingFromMap(ezslot_0,ezslot_0_raw);};return __ez_init_slot(bvr,'div-gpt-ad-online_python_com-medrectangle-2-0',0, defScript);};
var ezslot_2_raw = {'a':'1','iid1':'8632721256216256','eid':'8632721256216256','t':'134','d':'214055','t1':'134','pvc':'0','ap':'1136','sap':'1136','a':'|0|','as':'revenue','plat':'1','bra':'mod1-c','ic':'1','at':'mbf','adr':'399','ezosn':'2','reft':'tf','refs':'30','refa':'0','ga':'2497208','gala':'','rid':'99998','pt':'21','al':'1021','compid':'0','tap':'online_python_com-medrectangle-3-8632721256216256','eb_br':'8fc09e60bfd78aa82afac0405213359a','eba':'1','ebss':[10017,10082,10061,10015,10063,11307,11291,11315,11296],'asau':'4952030191','bv':'24','bvm':'0','bvr':'2','avc':'79','shp':'2','ftsn':'12','ftsng':'12','br1':'48','br2':'24','ezoic':'1','nmau':'0','mau':'0','stl':[77,193,0,0,0,168,196,0,0,0,187,0,901,182,901,902,903],'deal1':[17,19,20,21,22,23,24,25,26,27,28,29,30,760,761,813,815,816,817,818,819,893,899,903,917,918,919,1794,2310,2339,2351,2526,2527,2610,2688,2693,2761,2763,2764,2765,3044,3045,3054,3154,3430,3455,3456,3457,3458,3460,3682,3683,3684,3915,3919,3933,4184,4185,4186,4276,4604,4605,5747,6044,6045,6293,6294,6295,6983,7035,7036,7046,7060,7144,7327,7330,2030,4312,4312,2030,6772,5534,7175,7053,774],'ax_ssid':'10082'}; window.ezslots_raw.push(ezslot_2_raw); window.ezslotdivs['div-gpt-ad-online_python_com-medrectangle-3-0'] = {slot:'ezslot_2',adunit:'/1254144,22108676293/online_python_com-medrectangle-3'};__ez.fads.initslots['div-gpt-ad-online_python_com-medrectangle-3-0'] = function(bvr){var defScript = function() {ezslot_2 = googletag.defineSlot('/1254144,22108676293/online_python_com-medrectangle-3',[[160,600],[180,150]],'div-gpt-ad-online_python_com-medrectangle-3-0').addService(googletag.pubads()).setCollapseEmptyDiv(false);ezSetTargetingFromMap(ezslot_2,ezslot_2_raw);};return __ez_init_slot(bvr,'div-gpt-ad-online_python_com-medrectangle-3-0',2, defScript);};

__ez.queue.addFile('banger.js', '/porpoiseant/banger.js?cb=195-1&bv=391&PageSpeed=off', true, ['ezaqReady'], true, false, false, true);
var _ezim_d = {"online_python_com-box-2":{"adsense_stat_source_id":5,"adx_ad_count":3,"adx_stat_source_id":35,"div_id":"div-gpt-ad-online_python_com-box-2-0","full_id":"online_python_com-box-2/2024-11-07/1293263702248002","height":"600","position_id":1119,"sub_position_id":1119,"width":"160"},"online_python_com-medrectangle-2":{"adsense_stat_source_id":5,"adx_ad_count":3,"adx_stat_source_id":35,"div_id":"div-gpt-ad-online_python_com-medrectangle-2-0","full_id":"online_python_com-medrectangle-2/2024-11-07/1427516974217456","height":"90","position_id":1100,"sub_position_id":1100,"width":"970"},"online_python_com-medrectangle-3":{"adsense_stat_source_id":5,"adx_ad_count":3,"adx_stat_source_id":35,"div_id":"div-gpt-ad-online_python_com-medrectangle-3-0","full_id":"online_python_com-medrectangle-3/2024-11-07/8632721256216256","height":"600","position_id":1136,"sub_position_id":1136,"width":"160"}};
var ezS = document.createElement("script");ezS.src="/detroitchicago/reportads.js?gcb=195-1&cb=5";document.head.appendChild(ezS);
window.__ez_get_largest_ad_size=function(i){var e=[];if(ezoResponsiveSizes[i]){var n=document.documentElement.clientWidth,t=document.documentElement.clientHeight,o=null;window.ezoResponsiveSizes[i].responsiveSizes.forEach((function(i){var e=i.minWidth<=n&&i.minHeight<=t,m=null===o||i.minWidth>o.minWidth||o.minWidth==i.minWidth&&i.minHeight>o.minHeight;e&&m&&(o=i)})),null!==o&&(e=o.sizes)}var m=[0,0];return e.forEach((function(i){i[0]>m[0]&&(m[0]=i[0]),i[1]>m[1]&&(m[1]=i[1])})),m};
var ezasVars = {'cid':'5263855531','pid':'pub-8595466052839863','ssid':44};window.handleResponsiveAdsense=function(t,e){var s=[];(e=e||t.parentNode)&&e.attributes&&e.attributes.ezaw&&e.attributes.ezah&&(s=[e.attributes.ezaw.value,e.attributes.ezah.value]);var i=t.id.replace("-asloaded","");if(window.ezoResponsiveSizes&&window.ezoResponsiveSizes[i]&&window.__ez_get_largest_ad_size&&e){s=window.__ez_get_largest_ad_size(i),e.style.cssText+="width: "+s[0]+"px !important",e.style.cssText+="max-width: "+s[0]+"px !important",e.style.cssText+="min-width: 0px !important";var a=e.parentNode;a&&a.classList.contains("ezoic-ad")&&(a.style.cssText+="width: "+s[0]+"px !important",a.style.cssText+="max-width: "+s[0]+"px !important",a.style.cssText+="min-width: 0px !important")}t.style.cssText+="width: "+s[0]+"px",t.style.cssText+="height: "+s[1]+"px"};if(typeof window.ezAutoAdsSetup == 'undefined'){window.google_reactive_ads_global_state = {
                adCount: {},
                floatingAdsStacking: { maxZIndexListeners: [], maxZIndexRestrictions: {}, nextRestrictionId: 0 },
                messageValidationEnabled: false,
                reactiveTypeDisabledByPublisher: {},
                reactiveTypeEnabledInAsfe: {},
                sideRailAvailableSpace: [],
                sideRailOverlappableElements: [],
                stateForType: {},
                tagSpecificState: {},
                wasPlaTagProcessed: true,
                wasReactiveAdConfigReceived: { 1: true, 2: true, 8: true },
                wasReactiveAdVisible: {},
                wasReactiveTagRequestSent: true,
                description: "Can't disable auto ads programmatically on the page, so here we are!"
            };};var __ezasAggressive=true;
window.ezAnchorDisableBodyPadding=false;
window.ezAnchorPosition='bottom';
var ezAardvarkDetected;function ezDetectAardvark(){var bait=document.createElement("div");bait.className="textads banner-ads banner_ads ad-unit ad-zone ad-space adsbox";bait.style.height="1px";document.body.appendChild(bait);var baitOffsetHeight=bait.offsetHeight;if(typeof window["_ezaq"]!=="undefined"){if(baitOffsetHeight){ezAardvarkDetected=false;__ez&&__ez.bit&&__ez.bit.Add(window["_ezaq"]["page_view_id"],[(new __ezDotData('is_ad_blocked',false))]);}
else{ezAardvarkDetected=true;__ez&&__ez.bit&&__ez.bit.Add(window["_ezaq"]["page_view_id"],[(new __ezDotData('is_ad_blocked',true))]);}
var observer=new MutationObserver(function(e){if(e[0].removedNodes){ezAardvarkDetected=true;__ez&&__ez.bit&&__ez.bit.Add(window["_ezaq"]["page_view_id"],[(new __ezDotData('is_ad_blocked',true))]);}});}
if(typeof observer!=='undefined'){observer.observe(bait,{childList:true,attributes:true});}}
window.addEventListener('load',ezDetectAardvark);
var ezS = document.createElement("style");ezS.innerHTML=".ezoic-ad.medrectangle-2100{display:inline-block;float:none !important;line-height:0px;max-width:100% !important;min-height:90px;min-width:0px;padding:0;}";document.head.appendChild(ezS);
var ezS = document.createElement("style");ezS.innerHTML=".ezoic-ad.box-2119{align-items:center;display:flex !important;flex-direction:column !important;float:none !important;justify-content:center;line-height:0px;margin-bottom:0px !important;margin-left:auto !important;margin-right:auto !important;margin-top:0px !important;max-width:100% !important;min-height:600px;min-width:250px;padding:0;text-align:center !important;}";document.head.appendChild(ezS);
var ezS = document.createElement("style");ezS.innerHTML=".ezoic-ad.medrectangle-3136{align-items:center;display:flex !important;flex-direction:column !important;float:none !important;justify-content:center;line-height:0px;margin-bottom:0px !important;margin-left:auto !important;margin-right:auto !important;margin-top:0px !important;max-width:100% !important;min-height:600px;min-width:250px;padding:0;text-align:center !important;}";document.head.appendChild(ezS);
var ezS = document.createElement("style");ezS.innerHTML=".ezoic-ad{display:inline-block;border:0px;}.ezoic-ad>div>iframe{margin:0px!important;padding:0px!important;width:revert-layer;}.ezoic-ad .ezoic-ad>div{text-align:center}";document.head.appendChild(ezS);
var ezS = document.createElement("style");ezS.innerHTML=".ad-reporter-menu-backdrop{display:none;position:absolute;bottom:20px;right:15px;width:120px;height:100px;flex-direction:row;justify-content:center;align-items:center;background:transparent;box-shadow:#000 0 2px 10px;border-radius:10px;z-index:1002}.ad-reporter-menu{position:absolute;z-index:1003;display:flex;flex-direction:column;width:100%;height:100%;background:#fff;border-radius:5px;align-items:center;justify-content:space-around;font-weight:200;font-size:14px;font-family:sans-serif}.ad-reporter-menu .ad-reporter-menu-item{width:100%;height:100%;cursor:pointer;display:flex;justify-content:center;align-items:center}.ad-reporter-menu .ad-reporter-menu-item:not(:last-child){border-bottom:solid #d3d3d3 1px}";document.head.appendChild(ezS);
var ezS = document.createElement("style");ezS.innerHTML="@keyframes ezIn { 			from { opacity: 0; } 		  }		  .ezoic-ad .ezoic-adl:before {content: '\\00B7\\00B7\\00B7';position: absolute;display: flex!important;align-items: center;justify-content: center;text-align: center;color: #C4C4C4;font-size: 62px;letter-spacing: 2px;z-index: 0;animation: ezIn 1s infinite alternate;left: 50%;top: 50%;transform: translate(-50%, -50%);} .ezoic-ad .ezfound,.ezmob-footer .ezoic-ad .ezoic-ad,.ezoic-ad-adaptive > .ezoic-ad, .ezoic-ad-rl {background:0 0;border-radius:0;border:none}";document.head.appendChild(ezS);
var ezS = document.createElement("style");ezS.innerHTML=".ezmob-footer{position:fixed;left:0;bottom:0;width:100%;background:#fff;z-index:100000;line-height:0}.ezmob-footer-desktop{background-color:#f6f6f6cc;white-space:nowrap}.ezmob-footer-close-wrap{height:90px;padding:3px 0 0 16px;display:inline-block;width:35px;vertical-align:top}span.ezmob-footer-close{cursor:pointer;display:inline-block;width:18px;height:18px;border-radius:50%;border:1px solid #696969;position:relative;background:#fff;opacity:1}span.ezmob-footer-close:hover{border:1px solid #5fa624}span.ezmob-footer-close::before,span.ezmob-footer-close::after{content:'';position:absolute;top:50%;left:50%;width:60%;height:1px;background:#696969}span.ezmob-footer-close::before{transform:translate(-50%,-50%) rotate(45deg)}span.ezmob-footer-close::after{transform:translate(-50%,-50%) rotate(-45deg)}img.ezmob-anchor-img{height:18px!important;padding:0!important;border:0!important;cursor:pointer!important;width:18px!important;margin:45px 0 3px 1px!important;box-sizing:content-box!important}@media(min-width:450px) and (max-width:780px){.ezmob-footer-close-wrap,.ezoicwhat{display:none!important}}.ezoicwhat{display:block}body {					padding-bottom: 100px !important;					height: auto;				}				";document.head.appendChild(ezS);
ezStaticAnchor('//*/span[@data-ez-ph-id="119"]', '<span class="ezoic-ad ezoic-at-0 box-2 box-2119 adtester-container adtester-container-119" data-ez-name="online_python_com-box-2"><span id="div-gpt-ad-online_python_com-box-2-0" ezaw="160" ezah="600" style="position:relative;z-index:0;display:inline-block;padding:0;min-height:600px;min-width:160px;" class="ezoic-ad"><script data-ezscrex="false" data-cfasync="false" type="text/javascript" style="display:none;">if(typeof ez_ad_units == "undefined"){ez_ad_units=[];}ez_ad_units.push([[160,600],"online_python_com-box-2","ezslot_1",119,"0","0", "online_python_com-box-2-0"]);if(typeof __ez_fad_position == "function"){__ez_fad_position("div-gpt-ad-online_python_com-box-2-0");}</sc' + 'ript></span></span>',true);
ezStaticAnchor('//*/span[@data-ez-ph-id="136"]', '<span class="ezoic-ad ezoic-at-0 medrectangle-3 medrectangle-3136 adtester-container adtester-container-136" data-ez-name="online_python_com-medrectangle-3"><span id="div-gpt-ad-online_python_com-medrectangle-3-0" ezaw="160" ezah="600" style="position:relative;z-index:0;display:inline-block;padding:0;min-height:600px;min-width:160px;" class="ezoic-ad"><script data-ezscrex="false" data-cfasync="false" type="text/javascript" style="display:none;">if(typeof ez_ad_units == "undefined"){ez_ad_units=[];}ez_ad_units.push([[160,600],"online_python_com-medrectangle-3","ezslot_2",136,"0","0", "online_python_com-medrectangle-3-0"]);if(typeof __ez_fad_position == "function"){__ez_fad_position("div-gpt-ad-online_python_com-medrectangle-3-0");}</sc' + 'ript></span><span data-nosnippet="" style="display:block;height:14px;margin:2px auto;position:relative; width:100%" class="reportline" data-ez-ph-owner-id="136"><span style="text-align:center;font-size:12px !important;font-family: arial!important;float:right;line-height:normal;" class="ezoicwhat"><img src="https://go.ezodn.com/utilcave_com/ezoicbwa.png" alt="Ezoic" loading="lazy" style="height:14px !important; padding:2px !important; border:0px !important; cursor:pointer !important; width: 14px !important; margin:0 !important; box-sizing: content-box !important;" title="ezoic" name="?pageview_id=d5c7bc38-0e7d-465c-4bfb-019ebab32d3c&amp;ad_position_id=136&amp;impression_group_id=online_python_com-medrectangle-3/2024-11-07/8632721256216256&amp;ad_size=160x600&amp;domain_id=214055&amp;url=https://www.online-python.com/"/></span></span></span>',true);
ezStaticAnchor('//*/span[@data-ez-ph-id="100"]', '<div class="ezmob-footer ezoic-floating-bottom ezo_ad ezmob-footer-desktop" id="ezmobfooter"><center><span class="ezoic-ad ezoic-at-4 medrectangle-2 medrectangle-2100 adtester-container adtester-container-100" data-ez-name="online_python_com-medrectangle-2"><span id="div-gpt-ad-online_python_com-medrectangle-2-0" ezaw="970" ezah="90" style="position:relative;z-index:0;display:inline-block;padding:0;min-height:90px;min-width:970px;" class="ezoic-ad"><script data-ezscrex="false" data-cfasync="false" type="text/javascript" style="display:none;">if(typeof ez_ad_units == "undefined"){ez_ad_units=[];}ez_ad_units.push([[970,90],"online_python_com-medrectangle-2","ezslot_0",100,"0","0", "online_python_com-medrectangle-2-0"]);if(typeof __ez_fad_position == "function"){__ez_fad_position("div-gpt-ad-online_python_com-medrectangle-2-0");}</sc' + 'ript></span></span><span class="ezmob-footer-close-wrap" id="ezmob-footer-close" style="display: none;"><span class="ezmob-footer-close" onclick="__ez_close_anchor()" title="close"></span><span class="ezoicwhat"><img src="https://go.ezodn.com/utilcave_com/ezoic.png" title="ezoic" class="ezmob-anchor-img"/></span></span></center></div>',false);
var ezS = document.createElement("script");ezS.src="https://g.ezodn.com/cmp/v2/v.js?v=4";document.head.appendChild(ezS);
(function(){if(typeof document.body==='undefined'||document.body===null){return;}
var attachEvent=function(element,evt,func){if(element.addEventListener){element.addEventListener(evt,func,false);}else{element.attachEvent("on"+evt,func);}};attachEvent(document.body,"ezVigImpression",function(e){if(typeof(_ezaq)!=="undefined"&&typeof e==="object"){__ez.pel.AddAndFire(e.slot,[(new __ezDotData(e.key,e.value))]);}});})();
window.__ez_vig_close_wrapper=function(closeFunc,urlAddition){closeFunc();var vc={"enabled":false,"useVignetteLoader":true,"fireEventName":"ezVigImpression","impressionSource":"anchor","urlAddition":"utm_content=anc-true","disableFloor":true,"eventHandlerTest":false};if(typeof urlAddition=='string'){vc.urlAddition=urlAddition;}
var v=newEzVignette(vc);v.handleClick();};
__ez.queue.addFile('/detroitchicago/stickyfix.js', '/detroitchicago/stickyfix.js?gcb=1&cb=37', false, [], true, true, true, false);
__ez.queue.addFile('anchorfix.js', '/ezoic/anchorfix.js?cb=27', false, [], true, true, true, false);
var didTimeoutVign=false;setTimeout(function(){function getCookie(cname){var name=cname+"=";var ca=document.cookie.split(';');for(var i=0;i<ca.length;i++){var c=ca[i];while(c.charAt(0)==' '){c=c.substring(1);}
if(c.indexOf(name)==0){return c.substring(name.length,c.length);}}
return "";}
var cookieTest=getCookie("ezvignetteviewed");if(cookieTest==""){window.googletag=window.googletag||{};googletag.cmd=googletag.cmd||[];googletag.cmd.push(function(){if(typeof window.ezslot_interstitial!='undefined'&&window.ezslot_interstitial!=null){googletag.display(window.ezslot_interstitial);googletag.pubads().refresh([window.ezslot_interstitial]);if(typeof __ez!=='undefined'&&typeof __ez.pel!=='undefined'){__ez.pel.Add(window.ezslot_interstitial,[(new __ezDotData('fetched',1))]);__ez.pel.Fire();}
didTimeoutVign=true;}});}},1000);if(typeof _ezaq!='undefined'&&typeof _ezaq.ab_test_id!='undefined'&&_ezaq.ab_test_id=='mod34'){document.addEventListener("click",expzscr);}
function expzscr(){if(!didTimeoutVign){return;}
var x=window.open();if(x){x.close();document.removeEventListener("click",expzscr);}}
__ez.queue.addFile('/detroitchicago/kenai.js', '/detroitchicago/kenai.js?gcb=1&cb=17', false, [], true, false, true, false);
function __ez_fad_ezpbinit(){
		var srcs = ['//go.ezodn.com/hb/dall.js?cb=195-1-107'];
		var srcLoads = [null];
		var scriptTag = "script";
		for (var i = 0; i < srcs.length; i++) {
			var hbScript = document.createElement(scriptTag);
			var scriptURL = srcs[i];
			hbScript.setAttribute('src', scriptURL);
			hbScript.onerror = function () {window.ezDallErr = true};
			hbScript.onload = srcLoads[i];
			document.body.appendChild(hbScript);
		}
	}__ez.queue.addFile('/detroitchicago/tuscon.js', '/detroitchicago/tuscon.js?gcb=1&cb=14', false, [], true, false, true, false);__ez.queue.addFile('/detroitchicago/kenai.js', '/detroitchicago/kenai.js?gcb=1&cb=17', false, [], true, false, true, false);var ezMedianet={bidder:'medianet',params:{"cid":"8CUBCB617","crid":"188911743"}};var ezOneTag={bidder:'onetag',params:{pubId:'62499636face9dc'}};var ezCriteo={bidder:'criteo',params:{networkId:'7987'}};var ezjsps=function(obj){return JSON.parse(JSON.stringify(obj));};var epbjs=epbjs||{};epbjs.que=epbjs.que||[];epbjs.bidderTimeout=1000;epbjs.useAdj=true;epbjs.SS={"appnexus":10087,"conversant":10033,"criteo":10050,"ix":10082,"medianet":11307,"onetag":11291,"openx":10015,"pubmatic":10061,"pulsepoint":11301,"rubicon":10063,"sharethrough":11309,"triplelift":11296};epbjs.bidders=['appnexus','conversant','criteo','ix','medianet','onetag','openx','pubmatic','pulsepoint','rubicon','sharethrough','triplelift'];epbjs.que.push(function(){});epbjs.bidderSettings={'rubicon': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'medianet': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'onetag': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'criteo': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'triplelift': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'pubmatic': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'openx': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'conversant': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'appnexus': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'ix': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'pulsepoint': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},'sharethrough': { bidCpmAdjustment: function(bidCpm, bid) { var adjBid = 0; if(typeof bid === 'undefined'){return bidCpm;} if(bid.mediaType === 'video'){adjBid = bidCpm - 0.18;}else{adjBid = bidCpm - 0.015;} if(adjBid < 0){adjBid=0;} return adjBid;}},};epbjs.gadj=1.000000;var __enableAnalytics=false;epbjs.testFeatures=[''];
var __s2sbidders=[];
var __s2sinstreambidders=[];
var __allBidders=['appnexus','conversant','criteo','ix','medianet','onetag','openx','pubmatic','pulsepoint','rubicon','sharethrough','triplelift'];
var __allSiteApprovedBidders=['33across','adyoulike','amx','appnexus','conversant','criteo','ix','medianet','minutemedia','onetag','openx','pubmatic','pulsepoint','rubicon','sharethrough','smartadserver','sovrn','triplelift','vidazoo','yieldmo'];
__ez.queue.addFile('/detroitchicago/portland.js', '/detroitchicago/portland.js?gcb=1&cb=260', true, [], true, false, true, false);var epbjs=epbjs||{};epbjs.ezAdUnits=[{bidPoolId: 'Header_BPID',code: 'div-gpt-ad-online_python_com-box-2-0', ortb2Imp: {ext: {gpid: 'div-gpt-ad-online_python_com-box-2-0', data: {pbadslot: 'div-gpt-ad-online_python_com-box-2-0', adserver: {name: 'gam', adslot: 'div-gpt-ad-online_python_com-box-2-0'}}}}, mediaTypes: {banner: { sizes:[[160,600]] }}, bids: [{bidder: 'rubicon', params:{ accountId: 21150, siteId: 269072, zoneId: 3326304, bidonmultiformat: true  }},ezjsps(ezMedianet),ezjsps(ezOneTag),ezjsps(ezCriteo),{bidder: 'triplelift', params: { inventoryCode: 'Ezoic_RON_Top_of_Page_DT_728x90'}},{bidder: 'pubmatic', params:{ publisherId: '156983', adSlot: 'e_top_of_page_160x600' }},{bidder: 'openx',params: { delDomain: 'ezoic-d.openx.net', unit: '538151780' }},{bidder: 'conversant', params: { site_id: '211803' }}], tfl: [] },{bidPoolId: 'Content_BPID_Lazy',code: 'div-gpt-ad-online_python_com-medrectangle-2-0', ortb2Imp: {ext: {gpid: 'div-gpt-ad-online_python_com-medrectangle-2-0', data: {pbadslot: 'div-gpt-ad-online_python_com-medrectangle-2-0', adserver: {name: 'gam', adslot: 'div-gpt-ad-online_python_com-medrectangle-2-0'}}}}, mediaTypes: {banner: { sizes:[[728,90],[970,90]] }}, bids: [{bidder: 'rubicon', params:{ accountId: 21150, siteId: 269072, zoneId: 3326304, bidonmultiformat: true  }},ezjsps(ezMedianet),ezjsps(ezOneTag),ezjsps(ezCriteo),{bidder: 'pubmatic', params:{ publisherId: '156983', adSlot: 'e_bottom_floating_970x90' }},{bidder: 'openx',params: { delDomain: 'ezoic-d.openx.net', unit: '560605964' }},{bidder: 'conversant', params: { site_id: '211803' }}], tfl: [] },{bidPoolId: 'Content_BPID_Lazy',code: 'div-gpt-ad-online_python_com-medrectangle-3-0', ortb2Imp: {ext: {gpid: 'div-gpt-ad-online_python_com-medrectangle-3-0', data: {pbadslot: 'div-gpt-ad-online_python_com-medrectangle-3-0', adserver: {name: 'gam', adslot: 'div-gpt-ad-online_python_com-medrectangle-3-0'}}}}, mediaTypes: {banner: { sizes:[[160,600],[180,150]] }}, bids: [{bidder: 'rubicon', params:{ accountId: 21150, siteId: 269072, zoneId: 3326304, bidonmultiformat: true  }},ezjsps(ezMedianet),ezjsps(ezOneTag),ezjsps(ezCriteo),{bidder: 'triplelift', params: { inventoryCode: 'Ezoic_RON_UnderFirstParagraph'}},{bidder: 'pubmatic', params:{ publisherId: '156983', adSlot: 'e_under_first_paragraph_160x600' }},{bidder: 'openx',params: { delDomain: 'ezoic-d.openx.net', unit: '538151780' }},{bidder: 'conversant', params: { site_id: '211803' }}], tfl: [] }];var ez__id5pd = 'MTA9MTk3LjI0My42OC4yMDImMTI9TW96aWxsYSUyRjUuMCslMjhXaW5kb3dzK05UKzEwLjAlM0IrV2luNjQlM0IreDY0JTI5K0FwcGxlV2ViS2l0JTJGNTM3LjM2KyUyOEtIVE1MJTJDK2xpa2UrR2Vja28lMjkrQ2hyb21lJTJGMTI5LjAuMC4wK1NhZmFyaSUyRjUzNy4zNitFZGclMkYxMjkuMC4wLjA=';var ez__uIdHash = 'eb057bfd2791a4a3acfa2cc8286f4ec6d90e89e7e0db68600e04b9c6e20d9e8b';var ez__sspDomain = 'www.online-python.com';var epbjs=epbjs||{};epbjs.que=epbjs.que||[];epbjs.que.push(function(){epbjs.setConfig({})});
var __advertiserRule=['ixl.com'];
} catch(e) {window.ezstaticerrors = (window.ezstaticerrors || '') + e.toString();}window.ezFinishedStatic=true;</script><script src="./string to dictionary2_files/calgary.js.download"></script><script async="" type="text/javascript" src="./string to dictionary2_files/f(2).txt"></script><script src="./string to dictionary2_files/banger.js.download" async=""></script><script src="./string to dictionary2_files/reportads.js.download"></script><style>.ezoic-ad.medrectangle-2100{display:inline-block;float:none !important;line-height:0px;max-width:100% !important;min-height:90px;min-width:0px;padding:0;}</style><style>.ezoic-ad.box-2119{align-items:center;display:flex !important;flex-direction:column !important;float:none !important;justify-content:center;line-height:0px;margin-bottom:0px !important;margin-left:auto !important;margin-right:auto !important;margin-top:0px !important;max-width:100% !important;min-height:600px;min-width:250px;padding:0;text-align:center !important;}</style><style>.ezoic-ad.medrectangle-3136{align-items:center;display:flex !important;flex-direction:column !important;float:none !important;justify-content:center;line-height:0px;margin-bottom:0px !important;margin-left:auto !important;margin-right:auto !important;margin-top:0px !important;max-width:100% !important;min-height:600px;min-width:250px;padding:0;text-align:center !important;}</style><style>.ezoic-ad{display:inline-block;border:0px;}.ezoic-ad>div>iframe{margin:0px!important;padding:0px!important;width:revert-layer;}.ezoic-ad .ezoic-ad>div{text-align:center}</style><style>.ad-reporter-menu-backdrop{display:none;position:absolute;bottom:20px;right:15px;width:120px;height:100px;flex-direction:row;justify-content:center;align-items:center;background:transparent;box-shadow:#000 0 2px 10px;border-radius:10px;z-index:1002}.ad-reporter-menu{position:absolute;z-index:1003;display:flex;flex-direction:column;width:100%;height:100%;background:#fff;border-radius:5px;align-items:center;justify-content:space-around;font-weight:200;font-size:14px;font-family:sans-serif}.ad-reporter-menu .ad-reporter-menu-item{width:100%;height:100%;cursor:pointer;display:flex;justify-content:center;align-items:center}.ad-reporter-menu .ad-reporter-menu-item:not(:last-child){border-bottom:solid #d3d3d3 1px}</style><style>@keyframes ezIn { 			from { opacity: 0; } 		  }		  .ezoic-ad .ezoic-adl:before {content: '\00B7\00B7\00B7';position: absolute;display: flex!important;align-items: center;justify-content: center;text-align: center;color: #C4C4C4;font-size: 62px;letter-spacing: 2px;z-index: 0;animation: ezIn 1s infinite alternate;left: 50%;top: 50%;transform: translate(-50%, -50%);} .ezoic-ad .ezfound,.ezmob-footer .ezoic-ad .ezoic-ad,.ezoic-ad-adaptive > .ezoic-ad, .ezoic-ad-rl {background:0 0;border-radius:0;border:none}</style><style>.ezmob-footer{position:fixed;left:0;bottom:0;width:100%;background:#fff;z-index:100000;line-height:0}.ezmob-footer-desktop{background-color:#f6f6f6cc;white-space:nowrap}.ezmob-footer-close-wrap{height:90px;padding:3px 0 0 16px;display:inline-block;width:35px;vertical-align:top}span.ezmob-footer-close{cursor:pointer;display:inline-block;width:18px;height:18px;border-radius:50%;border:1px solid #696969;position:relative;background:#fff;opacity:1}span.ezmob-footer-close:hover{border:1px solid #5fa624}span.ezmob-footer-close::before,span.ezmob-footer-close::after{content:'';position:absolute;top:50%;left:50%;width:60%;height:1px;background:#696969}span.ezmob-footer-close::before{transform:translate(-50%,-50%) rotate(45deg)}span.ezmob-footer-close::after{transform:translate(-50%,-50%) rotate(-45deg)}img.ezmob-anchor-img{height:18px!important;padding:0!important;border:0!important;cursor:pointer!important;width:18px!important;margin:45px 0 3px 1px!important;box-sizing:content-box!important}@media(min-width:450px) and (max-width:780px){.ezmob-footer-close-wrap,.ezoicwhat{display:none!important}}.ezoicwhat{display:block}body {					padding-bottom: 100px !important;					height: auto;				}				</style><script src="./string to dictionary2_files/v.js.download"></script><script src="./string to dictionary2_files/stickyfix.js.download" async=""></script><script src="./string to dictionary2_files/anchorfix.js.download" async=""></script><script src="./string to dictionary2_files/kenai.js.download" async=""></script><script src="./string to dictionary2_files/tuscon.js.download" async=""></script><script src="./string to dictionary2_files/kenai.js.download" async=""></script><script src="./string to dictionary2_files/portland.js.download" async=""></script><meta http-equiv="origin-trial" content="AlK2UR5SkAlj8jjdEc9p3F3xuFYlF6LYjAML3EOqw1g26eCwWPjdmecULvBH5MVPoqKYrOfPhYVL71xAXI1IBQoAAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="Amm8/NmvvQfhwCib6I7ZsmUxiSCfOxWxHayJwyU1r3gRIItzr7bNQid6O8ZYaE1GSQTa69WwhPC9flq/oYkRBwsAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="A9wSqI5i0iwGdf6L1CERNdmsTPgVu44ewj8QxTBYgsv1LCPUVF7YmWOvTappqB1139jAymxUW/RO8zmMqo4zlAAAAACNeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A+d7vJfYtay4OUbdtRPZA3y7bKQLsxaMEPmxgfhBGqKXNrdkCQeJlUwqa6EBbSfjwFtJWTrWIioXeMW+y8bWAgQAAACTeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script src="./string to dictionary2_files/f(3).txt" async=""></script><script src="./string to dictionary2_files/aa05931b-5308-4ea3-95a2-adf84f4ffde4" type="text/javascript" async="async"></script><script async="async" defer="defer" src="./string to dictionary2_files/launchpad-liveramp.js.download"></script><script src="./string to dictionary2_files/pubcid.min.js.download"></script><script src="./string to dictionary2_files/sync.min.js.download"></script><script src="./string to dictionary2_files/id5-api.js.download"></script><script type="text/javascript" async="" src="./string to dictionary2_files/launcher-stub.min.js.download"></script><script src="./string to dictionary2_files/audins.js.download" async="" type="text/javascript"></script><script src="./string to dictionary2_files/524" async=""></script><script src="./string to dictionary2_files/js(2)" async=""></script></head>
<body style="padding-bottom: 100px !important;">
<ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;" data-ad-status="unfilled"><div id="aswift_0_host" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_0" name="aswift_0" browsingtopics="true" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="./string to dictionary2_files/ads.html" data-google-container-id="a!1" tabindex="0" title="Advertisement" aria-label="Advertisement" data-load-complete="true"></iframe></div></ins><div>
<nav class="nav navbar-top primary">
    <h2 class="nav_logo">
        <!-- <i class="fab fa-product-hunt"></i> -->
        <a href="https://www.online-python.com/"><img src="./string to dictionary2_files/logo.png" alt="IDE" width="40" height="34" style="margin-top: -7px" ezimgfmt="rs rscb4 src ng ngcb4" class=" ezlazyloaded" data-ezsrc="logo.png?ezimgfmt=rs:40x34/rscb4/ngcb4/notWebP" ezoid="0.12436056359264902"></a>

        <span>Online Python <sup>beta</sup> </span>
    </h2>
    <div class="addthis_inline_share_toolbox_28pb"></div> 
</nav>
<div class="main-content d-flex">
<div id="sidebar-left-ad">
    <!-- Ezoic - sidebar_left - sidebar -->
    <span id="ezoic-pub-ad-placeholder-119"></span><span data-ez-ph-id="119" style="margin-right:auto !important;align-items:center;min-height:600px;max-width:100% !important;margin-top:15px !important;margin-bottom:15px !important;margin-left:auto !important;float:none !important;line-height:0px;padding:0;display:flex !important;text-align:center !important;flex-direction:column !important;min-width:250px;"><span class="ezoic-ad ezoic-at-0 box-2 box-2119 adtester-container adtester-container-119" data-ez-name="online_python_com-box-2"><span id="div-gpt-ad-online_python_com-box-2-0" ezaw="160" ezah="600" style="position: relative; z-index: 0; padding: 0px; min-height: 600px; min-width: 160px;" class="ezoic-ad ezfound" data-google-query-id="CMjzl8PlyYkDFWBKFQgd4UorZg"><div id="google_ads_iframe_/1254144,22108676293/online_python_com-box-2_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1254144,22108676293/online_python_com-box-2_0" name="google_ads_iframe_/1254144,22108676293/online_python_com-box-2_0" title="3rd party ad content" width="160" height="600" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Advertisement" tabindex="0" allow="private-state-token-redemption;attribution-reporting" data-load-complete="true" style="border: 0px; vertical-align: bottom;" data-google-container-id="3" src="./string to dictionary2_files/saved_resource.html"></iframe></div></span></span></span>
    <!-- End Ezoic - sidebar_left - sidebar -->
</div>
<div class="container" id="container">
    <!-- Ezoic - top_of_page - top_of_page -->
    
    <!-- End Ezoic - top_of_page - top_of_page -->
    <div id="header-control">
        <div class="btn-group">
            <button type="button" class="btn btn-default btn-custom" id="open_file" onclick="openFile(dispFile)" data-toggle="tooltip" data-container="body" data-placement="right" title="" data-original-title="Open File from Disk"><i class="fas fa-folder-open"></i></button>
            <button type="button" class="btn btn-default btn-custom" onclick="save_code_modal()" id="save_file" data-toggle="tooltip" data-container="body" data-placement="right" title="" data-original-title="Save File to Disk - F9"><i class="fas fa-save"></i></button>
            <!-- <button type="button" class="btn btn-default btn-custom" onclick="share_code_modal()" data-toggle="tooltip" data-container="body" data-placement="right" title="Share Code - F10"><i class="fas fa-share-alt"></i></button> -->
            <button type="button" class="btn btn-default btn-custom" id="undo-editor" data-toggle="tooltip" data-container="body" data-placement="right" title="" data-original-title="Undo / Crtl+z"><i class="fas fa-undo-alt"></i></button>
            <button type="button" class="btn btn-default btn-custom" id="redo-editor" data-toggle="tooltip" data-container="body" data-placement="right" title="" disabled="disabled" data-original-title="Redo / Crtl+y"><i class="fas fa-redo-alt"></i></button>
        </div>

        <div class="btn-group setting-btn" role="group">
            <button type="button" class="btn btn-default" id="toggle-theme" data-toggle="tooltip" data-container="body" data-placement="left" title="" data-original-title="Change Theme"><i class="fas fa-moon fa-lg"></i></button>
            <button type="button" class="btn btn-default" onclick="about_modal()" id="info" data-toggle="tooltip" data-container="body" data-placement="left" title="" data-original-title="About Site"><i class="fas fa-info-circle"></i></button>
            <button type="button" class="btn btn-default" onclick="ace_setting()" id="setting" data-toggle="tooltip" data-container="body" data-placement="left" title="" data-original-title="Settings"><i class="fas fa-cogs"></i></button>
        </div>
    </div>
    <div id="mi" class="split" style="height: calc(66% - 2.5px);">
        <div id="editor-main">
        <ul class="nav nav-tabs" role="tablist">
            <li class="active" id="editor-1"><a data-toggle="tab">main.py</a></li>
            <li id="new_file_btn"><button type="button" class="btn btn-default btn-sm add-editor" id="create_tab" data-title="New File"><i class="fas fa-plus"></i></button></li>
        </ul>

        <div id="editor" class=" ace_editor ace-tm" style="line-height: 1.5;" draggable="false"><div style="position: absolute;"></div><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px; height: 1px; width: 1px; top: 231px; left: 314px;"></textarea><div class="ace_gutter" aria-hidden="true" style="left: 0px; width: 49px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 0px; left: 0px; width: 49px;"><div class="ace_gutter-cell " style="height: 21px; top: 0px;">1<span class="ace_fold-widget ace_start ace_open" style="display: inline-block; height: 21px;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 21px;">2<span class="ace_fold-widget ace_start ace_open" style="display: none; height: 21px;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 42px;">3<span style="display: none; height: 21px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 63px;">4<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 84px;">5<span style="display: none; height: 21px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 105px;">6<span class="ace_fold-widget ace_start ace_open" style="display: none; height: 21px;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 126px;">7<span class="ace_fold-widget ace_start ace_open" style="display: none; height: 21px;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 147px;">8<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 168px;">9<span class="ace_fold-widget ace_start ace_open" style="display: inline-block; height: 21px;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 189px;">10<span class="ace_fold-widget ace_start ace_open" style="display: none; height: 21px;"></span></div><div class="ace_gutter-active-line ace_gutter-cell " style="height: 21px; top: 210px;">11<span style="display: inline-block; height: 21px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 231px;">12<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 252px;">13<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 273px;">14<span class="ace_fold-widget ace_start ace_open" style="height: 21px; display: inline-block;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 294px;">15<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 315px;">16<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 336px;">17<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 357px;">18<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21px; top: 378px;">19<span class="ace_fold-widget ace_start ace_open" style="height: 21px; display: none;"></span></div></div></div><div class="ace_scroller" style="line-height: 21px; left: 48.3945px; right: 15px; bottom: 0px;"><div class="ace_content" style="top: 0px; left: 0px; width: 948.605px; height: 406px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 620px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;"><div class="ace_line" style="height: 21px; top: 0px;"><span class="ace_keyword">def</span> <span class="ace_identifier">word_frequencies</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">input_string</span><span class="ace_paren ace_rparen">)</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 21px; top: 21px;"> </div><div class="ace_line" style="height: 21px; top: 42px;">    <span class="ace_identifier">words</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">input_string</span><span class="ace_punctuation">.</span><span class="ace_function ace_support">split</span><span class="ace_paren ace_lparen">(</span><span class="ace_paren ace_rparen">)</span></div><div class="ace_line" style="height: 21px; top: 63px;">    </div><div class="ace_line" style="height: 21px; top: 84px;">   </div><div class="ace_line" style="height: 21px; top: 105px;">    <span class="ace_identifier">frequency_dict</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_paren ace_lparen">{</span><span class="ace_paren ace_rparen">}</span></div><div class="ace_line" style="height: 21px; top: 126px;">    </div><div class="ace_line" style="height: 21px; top: 147px;">   </div><div class="ace_line" style="height: 21px; top: 168px;">    <span class="ace_keyword">for</span> <span class="ace_identifier">word</span> <span class="ace_keyword">in</span> <span class="ace_identifier">words</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 21px; top: 189px;"><span class="ace_indent-guide">    </span>   </div><div class="ace_line" style="height: 21px; top: 210px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">if</span> <span class="ace_identifier">word</span> <span class="ace_keyword">in</span> <span class="ace_identifier">frequency_dict</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 21px; top: 231px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">frequency_dict</span><span class="ace_paren ace_lparen">[</span><span class="ace_identifier">word</span><span class="ace_paren ace_rparen">]</span> <span class="ace_keyword ace_operator">+=</span> <span class="ace_constant ace_numeric">1</span></div><div class="ace_line" style="height: 21px; top: 252px;"><span class="ace_indent-guide">    </span>   </div><div class="ace_line" style="height: 21px; top: 273px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">else</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 21px; top: 294px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">frequency_dict</span><span class="ace_paren ace_lparen">[</span><span class="ace_identifier">word</span><span class="ace_paren ace_rparen">]</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_constant ace_numeric">1</span></div><div class="ace_line" style="height: 21px; top: 315px;">    </div><div class="ace_line" style="height: 21px; top: 336px;">    <span class="ace_keyword">return</span> <span class="ace_identifier">frequency_dict</span></div><div class="ace_line" style="height: 21px; top: 357px;"></div><div class="ace_line" style="height: 21px; top: 378px;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_overwrite-cursors ace_hidden-cursors"><div class="ace_cursor" style="animation-duration: 1000ms; display: block; top: 210px; left: 266px; width: 8px; height: 21px;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="width: 20px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 20px; height: 420px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 20px; left: 48.3945px; right: 15px;"><div class="ace_scrollbar-inner" style="height: 20px; width: 948px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; font-optical-sizing: inherit; font-size-adjust: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>
        <div class="boxed" id="editor_footer"> Ln: 11, Col: 35</div>
        </div>

        <div class="control-bar">
            <div id="control-btn"><button type="button" class="btn btn-success btn-sm" id="run-btn" onclick="run_python()"><i class="fa fa-play"></i> <strong>Run</strong></button></div>
            <a tabindex="0" type="button" class="btn btn-default btn-sm" id="share-btn" onclick="share_code_modal()" data-toggle="popover" data-placement="right" data-trigger="hover" data-content="Share the code to your friends and colleagues" data-original-title="" title=""><i class="fa fa-share"></i> <strong>Share</strong></a>
            <!-- <a tabindex="0" type="button" class="btn btn-default btn-sm" id="support-btn" target="_blank" href="https://www.buymeacoffee.com/onlinepython" data-toggle="popover" data-placement="right" data-trigger="hover" data-content="Please Support us by buying a coffee!!"><i class="fa fa-dollar-sign"></i></a> -->
            <input class="textbox" type="text" id="input_arguments" placeholder=" Command Line Arguments">
        </div>

    </div>

    <div class="gutter gutter-vertical" style="height: 5px;"></div><div id="d" class="split" style="height: calc(28% - 2.5px);">
        <div class="boxed1" id="output_header">
            <div id="hint-section"></div>
            <div class="btn-group status" id="tool-btn">
                <button type="button" data-toggle="tooltip" data-container="body" data-placement="right" title="" class="btn btn-default btn-sm status" onclick="copy_output()" data-original-title="Copy to Clipboard"><i class="fas fa-copy"></i></button>
                <button type="button" data-toggle="tooltip" data-container="body" data-placement="right" title="" class="btn btn-default btn-sm status" onclick="download_modal()" data-original-title="Download"><i class="fas fa-download"></i></button>
                <button type="button" data-toggle="tooltip" data-container="body" data-placement="right" title="" class="btn btn-default btn-sm status" onclick="clear_output()" data-original-title="Clear"><i class="fas fa-eraser"></i></button>
            </div>
            <button type="button" data-toggle="tooltip" data-container="body" data-placement="right" title="" class="btn btn-default btn-sm status" id="start-term" onclick="start_terminal()" data-original-title="Start Terminal"><i class="fas fa-terminal"></i></button>
            <button type="button" data-toggle="tooltip" data-container="body" data-placement="right" title="" class="btn btn-default btn-sm status" id="term-expand" onclick="term_expand()" data-original-title="Expand/Collapse"><i class="fas fa-expand-alt fa-lg"></i></button>
             
            <div id="output-status"><span class="label label-primary"><i class="fas fa-sync-alt fa-spin"></i> Connecting to Server</span></div>
        </div>

        <div id="terminal">
            <div id="progress-status"><div class="progress" id="progress-bar"><div class="progress-bar progress-bar-warning active" role="progressbar"></div></div></div>
            <div class="boxed2" id="output" style="display: block;"><div class="wrapper" id="wrap"><p id="term-output">Enter a string: </p><p id="term-output">

Session Killed due to Timeout.</p><p id="term-output">
Press Enter to exit terminal</p></div><form id="term-form"><input id="term-input" autocomplete="off"></form></div>
            <div id="terminal-ad" style="display: none;">
                <!-- Ezoic - terminal_ad - under_page_title -->
                
                <!-- End Ezoic - terminal_ad - under_page_title -->
            </div>
        </div>
    </div>

    <!-- Ezoic - below_terminal - under_page_title -->
    <span id="ezoic-pub-ad-placeholder-114"></span><span data-ez-ph-id="114"></span>
    <!-- End Ezoic - below_terminal - under_page_title -->

    <div id="info">
    <h1 class="header1">Online Python IDE</h1>
    <p class="para">Build, run, and share Python code online for free with the help of online-integrated python's development environment (IDE). It is one of the most efficient, dependable, and potent online compilers for the Python programming language. It is not necessary for you to bother about establishing a Python environment in your local. Now You can immediately execute the Python code in the web browser of your choice. Using this Python editor is simple and quick to get up and running with. Simply type in the programme, and then press the <b>RUN</b> button! The code can be saved online by choosing the <b>SHARE</b> option, which also gives you the ability to access your code from any location providing you have internet access.</p>
    <!-- Ezoic - content_1 - mid_content -->
    
    <!-- End Ezoic - content_1 - mid_content -->
    <h2 class="header1">About Python</h2>
    <p class="para">Python, which was initially developed by Guido van Rossum and made available to the public in 1991, is currently one of the most widely used general-purpose programming languages. Python's source code is freely available to the public, and its usage and distribution are unrestricted, including for commercial purposes. It is widely used for web development, and using it, practically anything can be created, including mobile apps, online apps, tools, data analytics, machine learning, and so on. It is intended to be straightforward and uncomplicated, much like the English language. When compared to other programming languages such as C++, Java, and C#, it is a lot simpler to read and write Python programs. Because of its excellent productivity and efficiency, it has become a very popular choice for use as a programming language.</p>
<p class="para">To learn more about Python check out some of the following links.</p>

<ul>
<li><a target="_blank" title="Visit python.org" href="https://www.python.org/">python.org <i class="fas fa-external-link-alt"></i></a></li>
<li><a target="_blank" title="Visit Wikipedia&#39;s Python Entry" href="https://en.wikipedia.org/wiki/Python_(programming_language)">Wikipedia - Python <i class="fas fa-external-link-alt"></i></a></li>
<li><a target="_blank" title="Visit w3schools.com&#39;s Python Tutorial" href="https://www.w3schools.com/python/default.asp" rel="nofollow">w3schools.com - Python Tutorial <i class="fas fa-external-link-alt"></i></a></li>
<li><a target="_blank" title="Visit Programiz&#39;s Python Tutorial" href="https://www.programiz.com/python-programming" rel="nofollow">programiz.com - Python Tutorial <i class="fas fa-external-link-alt"></i></a></li>
</ul>
<!-- Ezoic - content_2 - long_content -->
<span id="ezoic-pub-ad-placeholder-117"></span><span data-ez-ph-id="117" style="line-height:0px;float:none !important;display:flex !important;margin-left:auto !important;text-align:center !important;min-width:970px;margin-right:auto !important;margin-bottom:15px !important;margin-top:15px !important;align-items:center;min-height:90px;max-width:100% !important;padding:0;flex-direction:column !important;"></span>
<!-- End Ezoic - content_2 - long_content -->
<ul>
</ul>
<h2 class="header1">Why Learn Python?</h2>
<ul>
<li>Python is a simple language to pick up. It has a simple syntax, and the code is quite easy to read.</li>
<li>Python is useful in a wide variety of contexts. It is put to use in the creation of quick application development, data science, Internet of Things, and web applications, among other things.</li>
<li>When compared to most other programming languages, it enables you to develop applications using a smaller number of lines of code.</li>
<li>It has a very huge community behind it, and there are active forums for users to participate in.</li>
<li>The presence of Third Party Modules contributes to the increased power of the Python programming language.</li>
<li>The user is able to easily solve difficult problems with the help of extensive support libraries (for example, NumPy, which is used for numerical computations and Pandas, which is used for data analytics).</li>
<li>It includes extremely user-friendly data structures, which simplify both the design of the code and the reasoning behind it.</li>
<li>The number of people using Python is constantly on the rise. It has quickly become one of the most widely used programming languages.</li>
</ul>
<!-- Ezoic - content_3 - longer_content -->

<!-- End Ezoic - content_3 - longer_content -->
<h2 class="header1">Features of <a target="_blank" title="Python Compiler" href="https://www.online-python.com/online_python_compiler" rel="nofollow">Online Python Compiler </a> <a target="_blank" title="Python Compiler" href="https://www.online-python.com/online_python_interpreter" rel="nofollow">(Interpreter)</a></h2>
<ul>
    <li>Design that is Uncomplicated and Sparse, along with Being Lightweight, Easy, and Quick to Use</li>
    <li><b>Version 3.8</b> of Python is supported for interactive program execution, which requires the user to provide inputs to the program in real time.</li>
    <li>Options for a dark and light theme, as well as a customised code editor with additional themes, are helpful for novices learning and practising Python.</li>
    <li>Options to Undo or Redo Changes Made in the Code Editor Options to Copy or Download the Results of the Program Expandable Output Terminal Options to Undo or Redo Changes</li>
    <li>A hint for the frequently occurring problems in Python</li>
    <li>Interactive Python Shell Advanced Python module support relevant to Data Science, including Pandas and NumPy Coding sharing functionality allows you to save your code in the cloud, where it can be retrieved whenever and wherever there is internet connectivity.</li>
</ul>
<!-- Ezoic - content_4 - longest_content -->

<!-- End Ezoic - content_4 - longest_content -->
<h2 class="header1">Learn Other Programming Language?</h2>
<p class="para">Visit <a href="https://online-ide.com/?utm_medium=referral&amp;utm_source=online-python.com" target="_blank">online-ide.com</a> to learn and practice top programming languages - C, C++, Java, Ruby, PHP, R, GoLang</p>
<!-- Ezoic - content_5 - incontent_5 -->
<span id="ezoic-pub-ad-placeholder-122"></span><span data-ez-ph-id="122"></span>
<!-- End Ezoic - content_5 - incontent_5 -->
    </div>
    <br><br>
<p id="footer">© 2024 online-python.com | <a href="https://www.online-python.com/about" target="_blank">About</a> | <a href="https://www.online-python.com/terms_and_conditions" target="_blank">Terms &amp; Conditions</a> | <a href="https://www.online-python.com/privacy_policy" target="_blank">Privacy Policy</a></p>
</div>
<div id="sidebar-right-ad">
    <!-- Ezoic - sidebar_right - sidebar -->
    <span id="ezoic-pub-ad-placeholder-136"></span><span data-ez-ph-id="136" style="margin-top:15px !important;text-align:center !important;min-width:250px;margin-bottom:15px !important;padding:0;margin-right:auto !important;display:flex !important;flex-direction:column !important;line-height:0px;float:none !important;margin-left:auto !important;align-items:center;min-height:600px;max-width:100% !important;"><span class="ezoic-ad ezoic-at-0 medrectangle-3 medrectangle-3136 adtester-container adtester-container-136" data-ez-name="online_python_com-medrectangle-3"><span id="div-gpt-ad-online_python_com-medrectangle-3-0" ezaw="160" ezah="600" style="position: relative; z-index: 0; padding: 0px; min-height: 600px; min-width: 160px;" class="ezoic-ad ezfound" data-google-query-id="CP2dh6rjyYkDFdmfUAYdb10ZtQ"><div id="google_ads_iframe_/1254144,22108676293/online_python_com-medrectangle-3_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1254144,22108676293/online_python_com-medrectangle-3_0" name="google_ads_iframe_/1254144,22108676293/online_python_com-medrectangle-3_0" title="3rd party ad content" width="160" height="600" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Advertisement" tabindex="0" allow="private-state-token-redemption;attribution-reporting" data-load-complete="true" style="border: 0px; vertical-align: bottom;" data-google-container-id="1" src="./string to dictionary2_files/saved_resource(1).html"></iframe></div></span><span data-nosnippet="" style="display:block;height:14px;margin:2px auto;position:relative; width:100%" class="reportline" data-ez-ph-owner-id="136"><span style="text-align:center;font-size:12px !important;font-family: arial!important;float:right;line-height:normal;" class="ezoicwhat"><img src="./string to dictionary2_files/ezoicbwa.png" alt="Ezoic" loading="lazy" style="height:14px !important; padding:2px !important; border:0px !important; cursor:pointer !important; width: 14px !important; margin:0 !important; box-sizing: content-box !important;" title="ezoic" name="?pageview_id=d5c7bc38-0e7d-465c-4bfb-019ebab32d3c&amp;ad_position_id=136&amp;impression_group_id=online_python_com-medrectangle-3/2024-11-07/8632721256216256&amp;ad_size=160x600&amp;domain_id=214055&amp;url=https://www.online-python.com/"></span></span></span></span>
    <!-- End Ezoic - sidebar_right - sidebar -->
    <!-- Ezoic - sidebar_right_bottom - sidebar_bottom -->
    
    <!-- End Ezoic - sidebar_right_bottom - sidebar_bottom -->
</div>
</div>




<!-- Save Result modal -->
<div class="modal fade" tabindex="-1" role="dialog" id="downloadResult">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
              <h3 class="modal-title">Download Result</h3>
            </div>

            <div class="modal-body">
              <form>
              <div class="form-group">
                  <label for="name">File Name:</label>
                  <input type="text" class="form-control" id="download_file_name" value="main_output.txt">
              </div>
              </form>
            </div>
            
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary" onclick="download_output()" data-dismiss="modal">Download</button>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<!-- Delete Editor Tab modal -->
<div class="modal fade" tabindex="-1" role="dialog" id="closeEditorTab">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
        <h3 class="modal-title" id="close_file_title">Close File</h3>
      </div>

        <div class="modal-body">
        <p>Your changes will be lost. Are you sure you want to Close the file ?</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">No</button>
          <button type="submit" class="btn btn-primary" onclick="close_editor_tab()" data-dismiss="modal">Yes</button>
        </div>

    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<!-- Delete Editor Tab modal -->
<div class="modal fade" tabindex="-1" role="dialog" id="saveEditorTab">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
          <h3 class="modal-title" id="save_file_title">Save</h3>
        </div>

        <div class="modal-body">
            <p>Do you want to save the file ?</p>
            <form>
            <div class="form-group">
                <label for="name">File Name:</label>
                <input type="text" class="form-control" id="code_file_name" value="main.py">
            </div>
            </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">No</button>
          <button type="submit" class="btn btn-primary" onclick="download_code()" data-dismiss="modal">Yes</button>
        </div>

    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

<!-- Share modal -->
<div class="modal fade" tabindex="-1" role="dialog" id="shareModal">
  <div class="modal-dialog" role="document" id="share-dialog">
    <div class="modal-content" id="share-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
          <h3 class="modal-title" id="share_code">Share the Code</h3>
        </div>

        <div class="modal-body">
            <!-- <p>Do you want to save the file ?</p> -->
            <form>
            <div class="form-group">
                <label for="name">Expiry Period:</label>
                <select class="form-control" id="expiry_select">
                    <option value="1">24 hour</option>
                    <option value="30">1 month</option>
                    <option selected="" value="180">6 month</option>
                    <option value="-1">Never</option>
                </select>
            </div>
            </form>
        <br>
        <button type="submit" class="btn btn-primary" onclick="share_code()" data-dismiss="modal" id="share-btn-modal">Share</button>
        </div>
        
        <!-- <div class="modal-footer">
        </div> -->

    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<!-- Share modal After -->
<div class="modal fade" tabindex="-1" role="dialog" id="shareModalAfter">
  <div class="modal-dialog" role="document" id="share-dialog-after">
    <div class="modal-content" id="share-content-after">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
          <h3 class="modal-title" id="share_code">Share the Code</h3>
        </div>

        <div class="modal-body">
            <!-- <p>Do you want to save the file ?</p> -->
            <form>
            <div class="form-group">
                <label for="name">URL:</label><span id="share-copy" onclick="copy_share_url()"><i class="far fa-copy"></i></span>
                <input type="text" class="form-control" id="share_url_box" value="" readonly="">
            </div>
            </form>
            <div class="addthis_inline_share_toolbox_7qby" id="addthis_share_modal"></div> 
            <!-- <a tabindex="0" type="button" class="btn btn-primary" target="_blank" href="https://www.buymeacoffee.com/onlinepython"><i class="fa fa-coffee"></i> Buy us a Coffee!!</a> -->
        </div>
        <!-- <div class="modal-footer">
        </div> -->

    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<!-- About Site modal -->
<div class="modal" tabindex="-1" role="dialog" id="aboutSiteModal">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
          <h2 class="modal-title"><strong>About online-python.com</strong></h2>
        </div>

        <div class="modal-body abountModalBody">
          <p><a href="https://www.online-python.com/" target="_blank">Online Python IDE</a> is a web-based tool powered by <a href="https://ace.c9.io/" target="_blank">ACE</a> code editor. This tool can be used to learn, build, run, test your python script. You can open the script from your local and continue to build using this IDE. Code and output can be downloaded to local. Code can be saved online using the "share" option which enables to access the code anytime, anywhere using internet. Supported Python <b>Version - Python3.8</b></p>

          <h3><strong>Keyboard Shortcuts</strong></h3>
          <ul style="font-size: larger;">
          <li>Run Code - F8</li>
          <li>Share Code - F9</li>
          <li>Save Code - F10</li>
          <li>Open Editor Command Palette - F1</li>
          </ul>
          
          <h3><strong>Report a bug</strong></h3>
          <p>If you encounter a bug or have questions or suggestions for improvements, please report it via feedback.</p>
          
          <h3><strong>Data policy</strong></h3>
          <p>No data is saved in the server. The code is sent to the server for execution and will be cleared after completion. Shared Code will be saved in the server till the selected expiry period.</p>
        </div>
        
        <div class="modal-footer">
          <p> Copyright © 2022 online-python.com</p>
          <button type="submit" class="btn btn-default" data-dismiss="modal">Close</button>
        </div>

    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<script type="text/javascript">
    ace.require("ace/ext/language_tools");
    var editor = ace.edit("editor");
    ace.require('ace/ext/settings_menu').init(editor);
    var editor_cnt = 1, editor_index = 1, active_editor = 1, editor_session = [];
    var request, init_ts, open_file_name;
    var lang = 'python3';
    default_content = "\
\n\
# Online Python - IDE, Editor, Compiler, Interpreter\n\
\n\
def sum(a, b):\n\
    return (a + b)\n\
\n\
a = int(input('Enter 1st number: '))\n\
b = int(input('Enter 2nd number: '))\n\
\n\
print(f'Sum of {a} and {b} is {sum(a, b)}')\n\
";
    var prev_result = 'in'; 
    var site_url = "https://www.online-python.com/"
    var base_url = "https://www.online-python.com/"
    var share_url = base_url;
    var exe_cnt = 0;
    var addthis_share = {
        url: share_url,
        // title: "THE TITLE",
        // description: "THE DESCRIPTION",
        // media: "THE IMAGE"
    }
    var csrf_token_name = 'ci_csrf_token'
    var csrf_token = ''


    var isMobile = window.orientation > -1;
    
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": true,
        "positionClass": "toast-top-right",
        "preventDuplicates": true,
        "preventOpenDuplicates": true,
        "maxOpened": 1,
        "onclick": null,
        "showDuration": "100",
        "hideDuration": "1000",
        "timeOut": "3000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        // "showMethod": "show",
        // "hideMethod": "hide"
    };
    
    var instance = Split(['#mi', '#d'], {
        direction: 'vertical',
        sizes: [66, 28],
        gutterSize: 5,
        cursor: 'row-resize',
        minSize: [0, 180],
        onDrag: function() {
            editor.resize();
        },
    });

    function term_expand() {
        var element = document.getElementById('term-expand').innerHTML;
        if (element === '<i class="fas fa-expand-alt fa-lg"></i>' ) {
            instance.setSizes([0, 94]);
            editor.resize();
            document.getElementById('term-expand').innerHTML = '<i class="fas fa-compress-alt fa-lg"></i>'
        } else {
            instance.setSizes([66, 28]);
            editor.resize();
            document.getElementById('term-expand').innerHTML = '<i class="fas fa-expand-alt fa-lg"></i>'
        }
        $('#term-expand').blur();
        $('[data-toggle="tooltip"]').tooltip('hide');
    }

    editor.setOptions({
        enableBasicAutocompletion: true, // the editor completes the statement when you hit Ctrl + Space
        enableLiveAutocompletion: true, // the editor completes the statement while you are typing
        enableSnippets: true,
        showPrintMargin: false, // hides the vertical limiting strip
        fixedWidthGutter: true,
        autoScrollEditorIntoView: true,
        copyWithEmptySelection: true,
        highlightActiveLine: false,
    });

    editor.setTheme("ace/theme/textmate");
    // editor.setTheme("ace/theme/tomorrow_night_bright");
    editor.container.style.lineHeight = 1.5;

    editor_session[0] = ace.createEditSession(default_content, "ace/mode/python");
    editor.setSession(editor_session[0]);
    var active_editor_id = $('#editor-1').children('a');
    var active_file_name = 'main.py';
    var repl_host = get_host();
    var command_list = [];
    var command_index = 0;
    var cur_cmd;
    var hint_glow;

    var y = document.getElementById('editor_footer');
    var output = document.getElementById('output');
    var exec_detail = document.getElementById('output-status');
    var progress_status = document.getElementById('progress-status');
    var display_flag = true;

    $(function () {
        $('[data-toggle="tooltip"]').tooltip({
        delay: {show: 750, hide: 50}
    })
    });

    $(function () {
        $('[data-toggle="popover"]').popover({
            delay: { "show": 0, hide: 0 }
        })
    });

    $('.popover-dismiss').popover({
        trigger: 'hover'
    });


    $(".nav-tabs").on("click", "a", function(e) {
        // e.stopPropagation();
        e.preventDefault();
        detail_chk = (e.detail === undefined) ? 1 : e.detail;
        if (!$(this).hasClass('add-editor') && !$(this).children('input').hasClass('thVal') && detail_chk == 1) {
            active_editor = parseInt($(this).parent().attr('id').split('-')[1]);
            active_editor_id = $(this);

            editor.setSession(editor_session[active_editor - 1]);
            active_file_name = $(this).html();
            $(this).tab('show');
            editor.focus();
            update_editor_footer();
            undo_redo_update();
        }
    })
    .on("click", "span", function() {
        close_tab = $(this).parent();
        close_tab.children('a').click();
        $('#close_file_title').text('Close - ' + active_file_name);
        if (editor.getValue() === "") {
            close_editor_tab();
        }
        else {
            $("#closeEditorTab").modal('show');
        }
    });

    $('#redo-editor').attr('disabled', 'disabled');
    $('#undo-editor').attr('disabled', 'disabled');

    $('#rename_file').click(function(e) {
        e.stopPropagation();
        e.preventDefault();
        active_editor_id.dblclick();
    });

    $('#undo-editor').click(function(e) {
        editor.session.getUndoManager().undo();
        undo_redo_update();

    });

    $('#redo-editor').click(function(e) {
        editor.session.getUndoManager().redo();
        undo_redo_update();
    });

    editor.getSession().on('change', function() {
        undo_redo_update();
    });

    let theme = localStorage.getItem('theme') !== undefined && localStorage.getItem('theme') !== null ? localStorage.getItem('theme') : 'light'

    if ( theme === 'dark') {
        $('body').addClass('dark');
        document.getElementById('toggle-theme').innerHTML = '<i class="fas fa-sun fa-lg"></i>';
        editor.setTheme("ace/theme/tomorrow_night_bright");
    } else {
        $('body').removeClass('dark');
        document.getElementById('toggle-theme').innerHTML = '<i class="fas fa-moon fa-lg"></i>';
        editor.setTheme("ace/theme/textmate");
    }

    $('#toggle-theme').click(function(e) {
        document.body.classList.toggle('dark');
        if ($('body').hasClass("dark")) {
            editor.setTheme("ace/theme/tomorrow_night_bright");
            document.getElementById('toggle-theme').innerHTML = '<i class="fas fa-sun fa-lg"></i>';
            localStorage.setItem('theme', 'dark');
        } else {
            editor.setTheme("ace/theme/textmate");
            document.getElementById('toggle-theme').innerHTML = '<i class="fas fa-moon fa-lg"></i>';
            localStorage.setItem('theme', 'light');
        }
        $('#toggle-theme').blur();
        $('[data-toggle="tooltip"]').tooltip('hide');
    });

    $('.add-editor').click(function(e) {
        e.stopPropagation();
        e.preventDefault();
        editor_cnt += 1;
        editor_index += 1;
        var id = editor_cnt;
        
        active_editor = id;
        editor_session[active_editor - 1] = ace.createEditSession('', "ace/mode/python");
        editor.setSession(editor_session[active_editor - 1]);

        $(this).closest('li').before('<li id="editor-' + id + '"><a data-toggle="tab">Untitled' + id + '.py</a> <span> <i class="fa fa-times"></i></span></li>');
        // $('.nav-tabs li:nth-child(' + id + ') a').click();

        active_editor_id = $(".nav-tabs li").children('a').last();
        active_editor_id.tab('show');
        active_editor_id.dblclick();
        update_editor_footer();
        undo_redo_update();

        editor.selection.on('changeCursor', function(e) {
            update_editor_footer();
        });

        editor.selection.on('changeSelection', function(e) {
            update_editor_footer();
        });

        editor.getSession().on('change', function() {
            undo_redo_update();
        });

    });

    $(document).on('dblclick', '.nav-tabs > li > a', function (event) {
        if($(event.target).attr('class')!="thVal")
            {
                event.stopPropagation();
                event.preventDefault();
                var currentEle = $(this);
                var value = $(this).html();
                if (value.search('<input') === -1) updateVal(currentEle, value);
        }
    });

    editor.focus();
    editor.navigateFileEnd();

    update_editor_footer();

    editor.selection.on('changeCursor', function(e) {
        update_editor_footer();
    });

    editor.selection.on('changeSelection', function(e) {
        update_editor_footer();
    });

    $('.status button').attr('disabled','disabled');
    $('#stop-btn').attr('disabled', 'disabled');

    socket_options = { 
        transports: ["websocket"], 
        'timeout': 3000, 
        'connect timeout': 3000,
        'reconnection': true,
        'reconnectionDelay': 1000,
        'reconnectionDelayMax' : 5000,
        'reconnectionAttempts': 5
    };

    socket_options['query'] = { type : "shell"};

    // ace.config.loadModule("ace/ext/keybinding_menu", function(module) {
    //     module.init(editor);
    // });

    $(document).keyup(function (e) {
        IsCtrl = false;
        IsShift = false;
    }).keydown(function (e) {

        // first capture Ctrl 
        if (e.which == 17) { IsCtrl = true; }

        // now capture Shift 
        if (e.which == 16) { IsShift = true; }

        switch (e.which) {

            // now capture S and if Ctrl is pressed                                                                                                                                                                                          
            // case 75: 
            //     if (IsCtrl) { alert("Ctrl K pressed"); editor.showKeyboardShortcuts();} 
            //     if (IsShift) { alert("Shift R pressed");  } 
            //     e.preventDefault(); 
            //     break;

            // capture F8
            case 119: run_python(); e.preventDefault(); break;
            //F9
            case 120: share_code_modal(); e.preventDefault(); break;
            //F10
            case 121: save_code_modal(); e.preventDefault(); break;

            // capture ESC
            // case 27: stop_python(); e.preventDefault(); break;
        }
    });

    $('#output').on('click', function() {
        $('#term-input').focus();
    });

    window.onbeforeunload=goodbye;

</script>

<!-- Go to www.addthis.com/dashboard to customize your tools --> 
<script type="text/javascript" src="./string to dictionary2_files/addthis_widget.js.download"></script> 


</div><!--[selectrongo:done]--><span id="ezoic-pub-ad-placeholder-100"></span><span data-ez-ph-id="100"></span><div class="ezmob-footer ezoic-floating-bottom ezo_ad ezmob-footer-desktop ezmobtrans" id="ezmobfooter"><center><span class="ezoic-ad ezoic-at-4 medrectangle-2 medrectangle-2100 adtester-container adtester-container-100" data-ez-name="online_python_com-medrectangle-2"><span id="div-gpt-ad-online_python_com-medrectangle-2-0" ezaw="970" ezah="90" style="position: relative; z-index: 0; padding: 0px; min-height: 90px; min-width: 970px;" class="ezoic-ad ezfound" data-google-query-id="CP3LptfjyYkDFelJFQgd_4Qqdg"><div id="google_ads_iframe_/1254144,22108676293/online_python_com-medrectangle-2_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1254144,22108676293/online_python_com-medrectangle-2_0" name="google_ads_iframe_/1254144,22108676293/online_python_com-medrectangle-2_0" title="3rd party ad content" width="970" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Advertisement" tabindex="0" allow="private-state-token-redemption;attribution-reporting" data-load-complete="true" style="border: 0px; vertical-align: bottom;" data-google-container-id="2" src="./string to dictionary2_files/saved_resource(2).html"></iframe></div></span></span><span class="ezmob-footer-close-wrap" id="ezmob-footer-close" style=""><span class="ezmob-footer-close" onclick="__ez_close_anchor()" title="close"></span><span class="ezoicwhat"><img src="./string to dictionary2_files/ezoic.png" title="ezoic" class="ezmob-anchor-img"></span></span></center></div><script type="text/javascript" data-cfasync="false">!function(){var e=function(e,t){for(var r=0;r<t.length;r++){var n=t[r];if(0==n.complete||void 0!==n.readyState&&n.readyState<4){var o=n.getAttribute("src")||n.currentSrc;void 0!==n.readyState&&0==n.readyState?n.addEventListener("loadstart",(function(e){var t=e.currentTarget.getAttribute("src")||e.currentSrc;window.ezorqs(e,t)})):(o=n.getAttribute("src")||n.currentSrc,window.ezorqs(n,o)),n.addEventListener("load",(function(e){var t=e.currentTarget.getAttribute("src")||e.srcElement.currentSrc;window.ezorqe(e,t)})),n.addEventListener("loadeddata",(function(e){var t=e.currentTarget.getAttribute("src")||e.srcElement.currentSrc;window.ezorqe(e,t)})),n.addEventListener("error",(function(e){var t=e.currentTarget.getAttribute("src")||e.srcElement.currentSrc;window.ezorqe(e,t)}))}}};function t(e){for(var t=0;t<document.styleSheets.length;t++)if(document.styleSheets[t].href==e)return!0;return!1}__ez_addAllListeners=function(){e(0,document.querySelectorAll("img")),e(0,document.querySelectorAll("video")),e(0,document.querySelectorAll("audio")),function(e){for(var r=0;r<e.length;r++){var n=e[r];if(("preload"==n.getAttribute("rel")||"stylesheet"==n.getAttribute("rel"))&&null!=n.getAttribute("href")&&t(n.getAttribute("href"))){window.ezorqs(n,n.getAttribute("href"));var o=document.createElement("img");o.onerror=function(e){void 0!==e.path&&void 0!==e.path[0].currentSrc?window.ezorqe(n,e.path[0].currentSrc):void 0!==e.srcElement&&void 0!==e.srcElement.href&&window.ezorqe(n,e.srcElement.href)},o.src=n.getAttribute("href")}}}(document.querySelectorAll("link")),void 0!==window.__ez.ssaf&&window.__ez.ssaf.indexOf(16)>-1&&void 0!==window.__ez.sshsdef&&!1===window.__ez.sshsdef&&Element.prototype.addEventListener&&("function"==typeof window.onload&&(window.addEventListener("load",window.onload),window.onload=null),"function"==typeof document.onload&&(document.addEventListener.addEventListener("load",document.onload),document.onload=null))},__ez.queue.addFunc("__ez_addAllListeners","__ez_addAllListeners",null,!1,["/detroitchicago/tulsa.js"],!0,!0,!0,!0)}();</script>
<script type="text/javascript" data-ezscrex="false">var EmbedExclusionEvaluated = 'exempt'; var EzoicMagicPlayerExclusionSelectors = ["#ez-toc-container",".excerpt",".ez-video-wrap","nav","table","blockquote","#toc-container","#ez-cookie-dialog",".entry-summary",".entry-actions",".humix-off",".ace_scroller"];var EzoicMagicPlayerInclusionSelectors = [];var EzoicPreferredLocation = '2';</script><script data-cfasync="false">function _emitEzConsentEvent(){var customEvent=new CustomEvent("ezConsentEvent",{detail:{ezTcfConsent:window.ezTcfConsent},bubbles:true,cancelable:true,});document.dispatchEvent(customEvent);}
(function(window,document){function _setAllEzConsentTrue(){window.ezTcfConsent.loaded=true;window.ezTcfConsent.store_info=true;window.ezTcfConsent.develop_and_improve_services=true;window.ezTcfConsent.measure_ad_performance=true;window.ezTcfConsent.measure_content_performance=true;window.ezTcfConsent.select_basic_ads=true;window.ezTcfConsent.create_ad_profile=true;window.ezTcfConsent.select_personalized_ads=true;window.ezTcfConsent.create_content_profile=true;window.ezTcfConsent.select_personalized_content=true;window.ezTcfConsent.understand_audiences=true;window.ezTcfConsent.use_limited_data_to_select_content=true;window.ezTcfConsent.select_personalized_content=true;}
function _clearEzConsentCookie(){document.cookie="ezCMPCookieConsent=tcf2;Domain=.online-python.com;Path=/;expires=Thu, 01 Jan 1970 00:00:00 GMT";}
_clearEzConsentCookie();if(typeof window.__tcfapi!=="undefined"){window.ezgconsent=false;var amazonHasRun=false;function _ezAllowed(tcdata,purpose){return(tcdata.purpose.consents[purpose]||tcdata.purpose.legitimateInterests[purpose]);}
function _reloadAds(){if(typeof window.ezorefgsl==="function"&&typeof window.ezslots==="object"){if(typeof __ezapsFetchBids=="function"&&amazonHasRun===false){ezapsFetchBids(__ezaps);if(typeof __ezapsVideo!="undefined"){ezapsFetchBids(__ezapsVideo,"video");}
amazonHasRun=true;}
var slots=[];for(var i=0;i<window.ezslots.length;i++){if(window[window.ezslots[i]]&&typeof window[window.ezslots[i]]==="object"){slots.push(window[window.ezslots[i]]);}else{setTimeout(_reloadAds,100);return false;}}
for(var i=0;i<slots.length;i++){window.ezorefgsl(slots[i]);}}else if(!window.ezadtimeoutset){window.ezadtimeoutset=true;setTimeout(_reloadAds,100);}}
function _handleConsentDecision(tcdata){window.ezTcfConsent.loaded=true;if(!tcdata.vendor.consents["347"]&&!tcdata.vendor.legitimateInterests["347"]){window._emitEzConsentEvent();return;}
window.ezTcfConsent.store_info=_ezAllowed(tcdata,"1");window.ezTcfConsent.develop_and_improve_services=_ezAllowed(tcdata,"10");window.ezTcfConsent.measure_content_performance=_ezAllowed(tcdata,"8");window.ezTcfConsent.select_basic_ads=_ezAllowed(tcdata,"2");window.ezTcfConsent.create_ad_profile=_ezAllowed(tcdata,"3");window.ezTcfConsent.select_personalized_ads=_ezAllowed(tcdata,"4");window.ezTcfConsent.create_content_profile=_ezAllowed(tcdata,"5");window.ezTcfConsent.measure_ad_performance=_ezAllowed(tcdata,"7");window.ezTcfConsent.use_limited_data_to_select_content=_ezAllowed(tcdata,"11");window.ezTcfConsent.select_personalized_content=_ezAllowed(tcdata,"6");window.ezTcfConsent.understand_audiences=_ezAllowed(tcdata,"9");window._emitEzConsentEvent();}
function _handleGoogleConsentV2(tcdata){if(!tcdata||!tcdata.purpose||!tcdata.purpose.consents){return;}
var googConsentV2={};if(tcdata.purpose.consents[1]){googConsentV2.ad_storage='granted';googConsentV2.analytics_storage='granted';}
if(tcdata.purpose.consents[3]&&tcdata.purpose.consents[4]){googConsentV2.ad_personalization='granted';}
if(tcdata.purpose.consents[1]&&tcdata.purpose.consents[7]){googConsentV2.ad_user_data='granted';}
if(googConsentV2.analytics_storage=='denied'){gtag('set','url_passthrough',true);}
gtag('consent','update',googConsentV2);}
__tcfapi("addEventListener",2,function(tcdata,success){if(!success||!tcdata){window._emitEzConsentEvent();return;}
if(!tcdata.gdprApplies){_setAllEzConsentTrue();window._emitEzConsentEvent();return;}
if(tcdata.eventStatus==="useractioncomplete"||tcdata.eventStatus==="tcloaded"){if(typeof gtag!='undefined'){_handleGoogleConsentV2(tcdata);}
_handleConsentDecision(tcdata);if(tcdata.purpose.consents["1"]===true&&tcdata.vendor.consents["755"]!==false){window.ezgconsent=true;(adsbygoogle=window.adsbygoogle||[]).pauseAdRequests=0;_reloadAds();}else{_reloadAds();}
if(window.__ezconsent){__ezconsent.setEzoicConsentSettings(ezConsentCategories);}
__tcfapi("removeEventListener",2,function(success){return null;},tcdata.listenerId);if(!(tcdata.purpose.consents["1"]===true&&_ezAllowed(tcdata,"2")&&_ezAllowed(tcdata,"3")&&_ezAllowed(tcdata,"4"))){if(typeof __ez=="object"&&typeof __ez.bit=="object"&&typeof window["_ezaq"]=="object"&&typeof window["_ezaq"]["page_view_id"]=="string"){__ez.bit.Add(window["_ezaq"]["page_view_id"],[new __ezDotData("non_personalized_ads",true),]);}}}});}else{_setAllEzConsentTrue();window._emitEzConsentEvent();}})(window,document);</script><iframe src="./string to dictionary2_files/aframe.html" width="0" height="0" style="display: none;"></iframe><script src="./string to dictionary2_files/ezjitscroll.js.download" async=""></script><script src="./string to dictionary2_files/ezicsticky.js.download" async=""></script><script src="./string to dictionary2_files/ezjitpos.js.download" async=""></script><div id="uglipop_overlay_wrapper" style="position:absolute;top:0;bottom:0;left:0;right:0;display:none"><div id="uglipop_overlay" style="position: fixed; inset: 0px; opacity: 0.3; width: 100%; height: 100%; background-color: black; display: none;"></div></div><div id="uglipop_content_fixed" style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); opacity: 1; z-index: 10000000; display: none;"><div id="uglipop_popbox"></div></div><script src="./string to dictionary2_files/ezadloadhb.js.download" async=""></script><script src="./string to dictionary2_files/ezadloadamzn.js.download" async=""></script><script src="./string to dictionary2_files/dall.js.download"></script><iframe marginwidth="0" marginheight="0" scrolling="no" frameborder="0" id="1f326f0b55a164" width="0" height="0" src="./string to dictionary2_files/saved_resource(3).html" name="__pb_locator__" style="display: none; height: 0px; width: 0px; border: 0px;"></iframe><iframe name="__launchpadLocator" style="display: none;" src="./string to dictionary2_files/saved_resource(4).html"></iframe><iframe src="./string to dictionary2_files/iu3.html" style="display: none;"></iframe><script src="./string to dictionary2_files/ezadfilled.js.download" async=""></script><script src="./string to dictionary2_files/524(1)"></script><img height="1" width="1" src="./string to dictionary2_files/halo_match" alt="" style="display: none;"><img height="1" width="1" src="./string to dictionary2_files/ip_match" alt="" style="display: none;"><img height="1" width="1" src="./string to dictionary2_files/ux" alt="" style="display: none;"><img height="1" width="1" src="./string to dictionary2_files/getuid" alt="" style="display: none;"><img height="1" width="1" src="./string to dictionary2_files/rtset" alt="" style="display: none;"><img height="1" width="1" src="./string to dictionary2_files/0" alt="" style="display: none;"><img height="1" width="1" src="./string to dictionary2_files/cm" alt="" style="display: none;"><img height="1" width="1" src="./string to dictionary2_files/ebfa23da174faa55634171c5e49d0152.gif" alt="" style="display: none;"><img height="1" width="1" src="./string to dictionary2_files/ium" alt="" style="display: none;"><img height="1" width="1" src="./string to dictionary2_files/saved_resource" alt="" style="display: none;"><script type="text/javascript" src="./string to dictionary2_files/getpixels" async=""></script><iframe src="./string to dictionary2_files/join-ad-interest-groups.html" allow="join-ad-interest-group; attribution-reporting" sandbox="allow-scripts allow-same-origin" style="display: none;"></iframe><script src="./string to dictionary2_files/ezidentity.js.download" async=""></script><div class=" ace_editor ace_autocomplete ace-tm" style="top: 134.4px; left: 397.452px; height: 172.375px; display: none;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px; top: 0px; left: -100px;"></textarea><div class="ace_gutter" aria-hidden="true" style="display: none; left: 0px; width: 42px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 0px; left: 0px; width: 42px;"><div class="ace_gutter-cell " style="height: 21.5469px; top: 0px;">1<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21.5469px; top: 21.5469px;">2<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21.5469px; top: 43.0938px;">3<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 21.5469px; top: 64.6406px;">4<span style="display: none;"></span></div></div></div><div class="ace_scroller" style="line-height: 0px; left: 0px; right: 15px; bottom: 0px;"><div class="ace_content" style="cursor: default; top: 0px; left: 0px; width: 283px; height: 215.469px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 4px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height: 21.5469px; top: 0px; left: 0px; right: 0px;"></div></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;"><div class="ace_line ace_selected" style="height: 21.5469px; top: 0px;"><span class="ace_completion-highlight">al</span><span class="ace_">l</span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 21.5469px; top: 21.5469px;"><span class="ace_">Ex</span><span class="ace_completion-highlight">a</span><span class="ace_">mp</span><span class="ace_completion-highlight">l</span><span class="ace_">e</span><span class="ace_completion-meta">local</span></div><div class="ace_line" style="height: 21.5469px; top: 43.0938px;"><span class="ace_">c</span><span class="ace_completion-highlight">al</span><span class="ace_">lable</span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 21.5469px; top: 64.6406px;"><span class="ace_">F</span><span class="ace_completion-highlight">al</span><span class="ace_">se</span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 21.5469px; top: 86.1875px;"><span class="ace_completion-highlight">a</span><span class="ace_">pp</span><span class="ace_completion-highlight">l</span><span class="ace_">y</span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 21.5469px; top: 107.734px;"><span class="ace_">ev</span><span class="ace_completion-highlight">al</span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 21.5469px; top: 129.281px;"><span class="ace_">fin</span><span class="ace_completion-highlight">al</span><span class="ace_">ly</span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 21.5469px; top: 150.828px;"><span class="ace_">loc</span><span class="ace_completion-highlight">al</span><span class="ace_">s</span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 21.5469px; top: 172.375px;"><span class="ace_">glob</span><span class="ace_completion-highlight">al</span><span class="ace_completion-meta">keyword</span></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors" style="opacity: 0;"><div class="ace_cursor" style="display: block; top: 0px; left: 4px; width: 8px; height: 21.5469px;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="width: 20px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 20px; height: 280.109px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 20px; left: 0px; right: 15px;"><div class="ace_scrollbar-inner" style="height: 20px; width: 283px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; font-optical-sizing: inherit; font-size-adjust: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div></body><iframe id="google_esf" name="google_esf" src="./string to dictionary2_files/zrt_lookup_fy2021.html" style="display: none;"></iframe><iframe name="goog_topics_frame" src="./string to dictionary2_files/topics_frame.html" style="display: none;"></iframe><iframe sandbox="allow-scripts allow-same-origin" id="34c4f624c028f16" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./string to dictionary2_files/checksync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="35d862356ee5db9" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./string to dictionary2_files/syncframe.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="3646a838b4784ec" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./string to dictionary2_files/user_sync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="37d651e491374c7" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./string to dictionary2_files/pd.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="38c10a32a3e74d9" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./string to dictionary2_files/sync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="397d3b30d4c1daf" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./string to dictionary2_files/usync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="404bf7edef8d633" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./string to dictionary2_files/saved_resource(5).html">
    </iframe></html>