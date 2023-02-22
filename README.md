# CSSMediaQuery
Sublime Text 3 plugin for css files with media queries

## Hotkeys
*Ctrl+Alt+,* - Toggle to next media query
*Ctrl+Alt+M* - Show panel with all media queries
*Ctrl+Alt+N* - Fold Toggle all media queries

Using Command Palette *Ctrl+Shift+P* find "Media Query: Next"

## Default.sublime-keymap
```
[{
	"keys": ["ctrl+alt+."],
	"command": "select",
	"args": {"eval_type": "eval"}
},{
	"keys": ["ctrl+alt+,"],
	"command": "next",
},{
	"keys": ["ctrl+alt+m"],
	"command": "panel",
},{
	"keys": ["ctrl+alt+n"],
	"command": "fold_toggle",
}]
```

, you can add a setting like this to your .sublime-keymap file (eg: Packages/User/Default (Linux).sublime-keymap):
