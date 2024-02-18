
local opts = { noremap = true, silent = true }
local keymap = vim.api.nvim_set_keymap

-- Normal --
-- Better window navigation
keymap("n", "<C-h>", "<C-w>h", opts)
keymap("n", "<C-j>", "<C-w>j", opts)
keymap("n", "<C-k>", "<C-w>k", opts)
keymap("n", "<C-l>", "<C-w>l", opts)

-- resize split with arrows
-- keymap("n", "<C-K>", ":resize +2<CR>", opts)
-- keymap("n", "<C-J>", ":resize -2<CR>", opts)
-- keymap("n", "<C-H>", ":vertical resize -2<CR>", opts)
-- keymap("n", "<C-L>", ":vertical resize +2<CR>", opts)

-- Visual --
-- Move text
keymap("v", "<A-h>", "<gv", opts)
keymap("v", "<A-l>", ">gv", opts)
keymap("v", "<A-j>", ":m .+1<CR>==", opts)
keymap("v", "<A-k>", ":m .-2<CR>==", opts)

keymap("v", "p", '"_dP', opts)

