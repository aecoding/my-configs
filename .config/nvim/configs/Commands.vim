" This is a shortcut to use FZF
map <C-P> :FZF<CR>

" This will make 'jj' act like Esc 
imap jk <Esc>

" This will auto complete the signs
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O

" This has to do with nerdtree
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

command! -nargs=0 Prettier :CocCommand prettier.formatFile

let g:user_emmet_leader_key=','

" This will let me go back/foward or delete a buffer
map gn :bn<cr>
map gp :bp<cr>
map gd :bd<cr>

vnoremap <C-C> :w !xclip -i -sel c<CR><CR>
" This let me save root files without sudo
command! -nargs=0 Sw w !sudo tee % > /dev/null
