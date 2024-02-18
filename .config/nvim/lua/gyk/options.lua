
vim.g.mapleader = " "

local options = {
    guicursor = "",

    number = true,
    relativenumber = true,
    numberwidth = 4,

    backup = false,
    clipboard = "unnamed",
    cmdheight = 2,
    fileencoding = "utf-8",
    hlsearch = false,
    incsearch = true,
    ignorecase = true,
    mouse = "a",

    expandtab = true,
    tabstop = 4,
    softtabstop = 4,
    shiftwidth = 4,
    smartindent = true,

    splitbelow = true,
    splitright = true,
    swapfile = false,
    termguicolors = true,
    timeoutlen = 1000,
    undofile = true,
    updatetime = 5000,

    signcolumn = yes,
    wrap = false,
    linebreak = true,
    scrolloff = 8,
    cursorline = true,
}

for k, v in pairs(options) do
  vim.opt[k] = v
end

