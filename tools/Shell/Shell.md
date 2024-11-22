




#### Install fish

To change your login shell to fish:
1. Add the shell to `/etc/shells` with:
```
echo /usr/local/bin/fish | sudo tee -a /etc/shells


```
2. Change your default shell with:
```
chsh -s /usr/local/bin/fish

chsh -s $(which fish)
```

customice fish
1. oh-my-fish
```
curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish
```
3. Fish Themes  https://github.com/oh-my-fish/oh-my-fish/blob/master/docs/Themes.md

```
omf install https://github.com/komarnitskyi/theme-zephyr
omf theme zephyr
```

pluggins for fish
curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher

fisher install jorgebucaran/nvm.fish => nvm



### 3.  Add Temux
1. Customize temux


### 4. Add Nvim y LazzyVim

[GitHub - Gentleman-Programming/Gentleman.Dots: My personal configuration for LazyVim !](https://github.com/Gentleman-Programming/Gentleman.Dots)



```
sudo add-apt-repository ppa:neovim-ppa/unstable -y
sudo apt update
sudo apt install neovim npm git gcc fzf fd-find ripgrep coreutils bat curl make  gcc ripgrep unzip git xclip neovim build-essential curl file git  fzf fd-find ripgrep bat exa git gcc curl lazygit jq bash -y

sudo apt-get install -y 
```

brew install jesseduffield/lazygit/lazygit


Rust install 
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
rustc --version
cargo --version
```



2.- install node  nvm
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
set -x NVM_DIR $HOME/.nvm # with fish

nvm install --lts
```



```

git clone https://github.com/LazyVim/starter ~/.config/nvim

rm -rf ~/.config/nvim/.git
```



- https://github.com/nvim-lua/kickstart.nvim


#### LazzyVim themes

- https://vimcolorschemes.com/i/trending
- https://dotfyle.com/neovim/colorscheme/trending


----



# shells 

## fish terminal
| "to set default in archlinux need logout"  ohMyFish


https://fishshell.com/
https://github.com/oh-my-fish/oh-my-fish/blob/master/docs/Themes.md