# Sublime Text 3 plugin CSSMediaQuery
Sublime Text 3 plugin for css files with media queries, highlight, fold and select next media query

# Install in Package Control
Open `Package Control` (Ctrl+Shift+P find Package Control) -> Select `Package Control: Add Repository` paste in url https://github.com/biohazardhome/CSSMediaQuery/ Repo has been added to `Package Control`, it's not installed though
Open `Package Control` again -> `Select Package Control: Install Packages` -> search for, and install the package CSSMediaQuery

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

you can add a setting like this to your .sublime-keymap file (eg: Packages/User/Default (Linux).sublime-keymap):
