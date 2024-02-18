return {
  'nvim-telescope/telescope.nvim',
  tag = '0.1.3',
  lazy = false,
  dependencies = { 'nvim-lua/plenary.nvim' },
  keys = {
    {
      "<leader>f",
      function()
        require("telescope.builtin").find_files()
      end,
      desc = "Toggle Telescope find files"
    }
  }
}
