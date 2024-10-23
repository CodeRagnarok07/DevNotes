---
sticker: ""
---



### Navigation

Position anterior `('' or ``)` 
next line out of text `[`  and last `]`


### Copy and paste

cut with 'd'
copy with 'y'
paste with 'p'

decrease number `C-x`
increase number C-a


### search and replace

> method 1
	command: %s/old/new/gc
	'g' = global in every line
	'c' = ask for confirmation in any case

> Method 2
> 	command:  'on-word * `cgn` "new change" `n.` '
> 	Select all concurrent `*` on a word
> 	'cgn' = replace
> 	'n' = next concurrent
> 	'.' = apply last change



## LazzyVim

### Tree files

#### open tree files

from terminal 'vim .'
from vim  ':Ex'

#### open tab
'enter' on same tab

#### new tab 

'alt v' vertical
'alt h' horizontal


#### navigation from tabs (nerdTree)

Next tab 'C- w w'
or control 'C- w <hjkl>
close tab 'C- w T' (abre otro tab)


