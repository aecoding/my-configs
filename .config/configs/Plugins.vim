call plug#begin('~/.config/nvim/plugged')
  Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
  Plug 'neoclide/coc.nvim', {'branch': 'release'}
  Plug 'preservim/nerdcommenter'
  Plug 'morhetz/gruvbox'
  Plug 'vimwiki/vimwiki'
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
  Plug 'mattn/emmet-vim'
  Plug 'lifepillar/vim-solarized8'
  Plug 'editorconfig/editorconfig-vim'
  Plug 'christoomey/vim-system-copy'
  Plug 'vimwiki/vimwiki'
  Plug 'preservim/nerdtree'
  Plug 'junegunn/limelight.vim'
  Plug 'junegunn/goyo.vim'
  Plug 'pangloss/vim-javascript'
call plug#end()


