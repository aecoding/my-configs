set tabstop=2
set shiftwidth=2
set expandtab
set smartindent
set autoindent
set smartindent
set conceallevel=1
set termguicolors
set background=dark
set number relativenumber
set nonu nornu
set number relativenumber
set viewoptions=folds,cursor
set sessionoptions=folds

filetype indent on

let g:coc_global_extensions = ['coc-json', 'coc-git', 'coc-html', 'coc-css', 'coc-prettier']
let g:airline_theme = 'simple'
let g:user_emmet_leader_key='<C-E>'
" This is used to change vimwiki default folder location.
let g:vimwiki_list = [{'path': '~/.vimwki/'}]
let g:javascript_conceal_function             = "ƒ"
let g:javascript_conceal_null                 = "ø"
let g:javascript_conceal_this                 = "@"
let g:javascript_conceal_return               = "⇚"
let g:javascript_conceal_undefined            = "¿"
let g:javascript_conceal_NaN                  = "ℕ"
let g:javascript_conceal_prototype            = "¶"
let g:javascript_conceal_static               = "•"
let g:javascript_conceal_super                = "Ω"
let g:javascript_conceal_arrow_function       = "⇒"
let g:javascript_conceal_noarg_arrow_function = "🞅"
let g:javascript_conceal_underscore_arrow_function = "🞅"


autocmd! User GoyoEnter Limelight
autocmd! User GoyoLeave Limelight!
augroup AutoSaveFolds
  autocmd!
  " view files are about 500 bytes
  " bufleave but not bufwinleave captures closing 2nd tab
  " nested is needed by bufwrite* (if triggered via other autocmd)
  " BufHidden for for compatibility with `set hidden`
  autocmd BufWinLeave,BufLeave,BufWritePost,BufHidden,QuitPre ?* nested silent! mkview!
  autocmd BufWinEnter ?* silent! loadview
augroup end
"augroup remember_folds
  "autocmd!
  "autocmd BufWinLeave ?* mkview
  "autocmd BufWinEnter ?* silent! loadview
"augroup END


augroup vimrc
  au BufReadPre * setlocal foldmethod=indent
  au BufWinEnter * if &fdm == 'indent' | setlocal foldmethod=manual | endif
augroup END

augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END

