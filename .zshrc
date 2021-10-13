export ZSH="/home/aedigo/.oh-my-zsh"
export PATH=/home/aedigo/.local/bin:$PATH
export MOZ_X11_EGL=1
export VIMTO_COLOR_NORMAL_TEXT=#282828
export VIMTO_COLOR_NORMAL_BACKGROUND=#f1fbc7
export NNN_PLUG='f:finder;o:preview-tabbed;p:imgview;d:diffs;t:nmount;v:pdfview'
export NNN_FIFO=/tmp/nnn.fifo
export RANGER_LOAD_DEFAULT_RC=FALSE

alias vifmrun="~/.bin/vifmrun ."

# Editor
export EDITOR="/usr/bin/nvim"
export VISUAL="/usr/bin/nvim"

alias pth='patch -p1 <'

# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="theunraveler"

# Uncomment the following line to use case-sensitive completion.
CASE_SENSITIVE="false"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git pip command-not-found zsh-autosuggestions fast-syntax-highlighting zsh-vim-mode)

source $ZSH/aliases.zsh
source $ZSH/oh-my-zsh.sh

# Setting vim keybindgs on the terminal.
bindkey -M viins 'jk' vi-cmd-mode
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=980'

# Here Qtile is kept as default
session=${1:-'qtile start'}

case $session in
    dwl               ) exec dwl;;
    sway              ) exec sway;;
    steam             ) exec steam;;
    # No known session, try to run it as command
    *                 ) exec $1;;
esac

if [ -z "${DISPLAY}" ] && [ "$(tty)" = "/dev/tty1" ]; then
  exec xinit session
fi

#xinit /usr/bin/xonotic-glx -- :1 vt$XDG_VTNR
