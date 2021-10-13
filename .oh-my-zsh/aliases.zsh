# variables
browser=qutebrowser

# Global aliases
alias -g l="| less"

# arch
alias spi='sudo pacman -S'
alias spr='sudo pacman -R'
alias spra='sudo pacman -Rs'
alias spu='sudo pacman -Syu; gopreload-batch-refresh.sh'
alias carch='sudo pacman -Rs $(pacman -Qtdq)'
alias search='pacman -Ss'
alias orphans='pacman -Qtdq'
alias removeOrphans='sudo pacman -Rns $(pacman -Qtdq)'

# python
alias pyi='sudo pip install'
alias pyr='sudo pip uninstall'

# qtile
alias qtest='pytest ~/.config/qtile/config.py -s'
alias qc='$EDITOR ~/.config/qtile/config.py'
alias qs='$EDITOR ~/.config/qtile/autostart.sh'

# yarn
alias ya='yarn add'
alias yad='yarn add -D'

# simple commands
alias cl='clear'

# make
alias smci='sudo rm config.h; make; sudo make install'

# xclip
alias pbcopy='xclip -selection clipboard'

# firefox
alias fds='firefox-developer-edition --search '

# zsh
alias sc='$EDITOR ~/.zshrc'
alias sz='source ~/.zshrc'
alias sca='$EDITOR ~/.oh-my-zsh/aliases.zsh'

# cpupower
alias boost="sudo cpupower frequency-set -g performance"
alias powersave="sudo cpupower frequency-set -g powersave"

# terminal apps
alias n='nnn'
alias reddit='ttrv --enable-media'
alias sv='sudo -e'
alias go='googler'
alias v='nvim'
alias vimwiki='nvim ~/.vimwki/index.wiki'

# Anki
alias ave='anki-vim English'
alias avp='anki-vim Portuguese'
alias avm='anki-vim Math'

# task warrior
alias tn='task next'
alias tw='task waiting'

# translate shell
alias t="trans -brief en:pt-br"
alias tb="trans -brief pt-br:en"
alias ytvf="youtube-dl -F"

# youtube-dl
ytdw() {
  youtube-dl -f $@ 
}

# translate shell
translate() {
  trans -brief $1:$2 $3
}

# task warrior
ta() {
  task add '$@'; nh gitTask; 
}

td() {
  task done '$@'; nh gitTask;
}

tdel() {
  task delete '$@'; nh gitTask; 
}

nh() {
  nohup $1 >/dev/null 2>&1& 
}

# markmap
Markmap() {
  markmap ~/Documents/Mindmaps/$1/.sources/$2.md; mv ~/Documents/Mindmaps/$1/.sources/$2.html ~/Documents/Mindmaps/$1/$2.html 
}

openMap() {
  $browser ~/Docuents/Mindmaps/$1/$2.html 
}

Mindir() {
  mkdir -p ~/Documents/Mindmaps/$1/.sources 
}

# file
srm() {
  sudo rm -r $1
}

# st
std() {
  nh st;
}

RenameExt() {
  # rename ts mp4 *.ts
  rename $1 $2 *.$1
}

# copy file name
fName() {
  ls $1 | xclip -selection clipboard
}

bindkey '^ ' autosuggest-accept
