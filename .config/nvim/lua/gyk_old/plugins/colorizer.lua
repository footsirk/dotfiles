return {
  "NvChad/nvim-colorizer.lua",
  config = function()
    require("colorizer").setup {
      filetypes={
        "*",
      },
      mode="background"
    }
  end
}
