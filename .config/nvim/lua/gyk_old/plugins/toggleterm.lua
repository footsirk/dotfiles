return {
  "akinsho/toggleterm.nvim",
  lazy = false,
  opts = {
    size = 40,
    open_mapping = [[<C-j>]],
    direction = "float",
    close_on_exit = true,
    shell = vim.o.shell,
  },
}
