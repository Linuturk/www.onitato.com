Title: PEP8 Checking in Vim
Tags: pep8, python, vim, flake8, vim-pathogen
Category: tutorial
Slug: pep8-checking-in-vim
Author: Justin Phelps
Summary: Following proper coding standards is important to ensure others can read and modify your code. I make use of the following tools when writing Python to ensure I am formatting my code properly.

Following proper coding standards is important to ensure others can read and modify your code. I make use of the following tools when writing Python to ensure I am formatting my code properly.

## Install Dependencies

Let's start by installing a dependency of the Vim plugin we are going to use. The [Flake8](https://pypi.python.org/pypi/flake8/) module will be needed for our vim-flake8 setup. As root (or using sudo), run the following commands:

```bash
easy_install pip
pip install flake8
```

The first command installs the latest version of [pip](https://pypi.python.org/pypi/pip), a tool for installing and managing Python packages. The second command uses pip to install the flake8 package. Now let's configure vim.

## vim-pathogen

The [github repository](https://github.com/tpope/vim-pathogen) for vim-pathogen has a great set of installation instructions for this tool. We will use this to load the vim-flake8 plugin that is used to check compliance. Follow their installation instructions, and then move on to the next step.

## vim-flake8

Here is the plugin that will work our magic. Go follow the [installation instructions](https://github.com/nvie/vim-flake8) for vim-flake8. Just clone this repository into the ~/.vim/bundle directory. If you've followed the instructions properly up to this point, everything should be working as expected. Here is my .vimrc file for comparison. Note that I've added a few additional options I find useful when coding in Python.

```
execute pathogen#infect()
syntax on
filetype plugin indent on
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
```

## Icing on the Cake

There's one more plugin I load into vim to make things easier. The [vim-sensible](https://github.com/tpope/vim-sensible) plugin sets some useful and sensible defaults that have made my vim experience easier. It installs just like vim-flake8, and is immediately available the next time you start vim.

Now go and write your Python code!
