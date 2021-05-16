set tabstop=2
set shiftwidth=2
set expandtab
set smartindent
set autoindent
set smartindent
filetype indent on
let g:coc_global_extensions = ['coc-json', 'coc-git', 'coc-html', 'coc-css', 'coc-prettier']
set number relativenumber
set nonu nornu
set number relativenumber
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END

