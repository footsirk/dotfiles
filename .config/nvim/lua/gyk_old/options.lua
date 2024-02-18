
vim.g.mapleader = " "

local options = {
  backup = false,
  clipboard = "unnamed",
  cmdheight = 2,
  fileencoding = "utf-8",
  hlsearch = false,
  ignorecase = true,
  mouse = "a",
  smartindent = true,
  splitbelow = true,
  splitright = true,
  swapfile = false,
  termguicolors = true,
  timeoutlen = 1000,
  undofile = true,
  updatetime = 300,
  expandtab = true,
  shiftwidth = 4,
  tabstop = 4,
  number = true,
  relativenumber = true,
  numberwidth = 4,
  signcolumn = yes,
  wrap = true,
  linebreak = true,
  scrolloff = 8,
  cursorline = true,
}

for k, v in pairs(options) do
  vim.opt[k] = v
end

