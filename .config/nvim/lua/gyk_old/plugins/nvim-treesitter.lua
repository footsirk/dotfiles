
return {
  "nvim-treesitter/nvim-treesitter",
  lazy = false,
  build = ":TSUpdate",
  config = function()
    local configs = require("nvim-treesitter.configs")
    configs.setup({
      ensure_installed = {"cpp", "lua", "python", "toml", "rust", "pascal"},
      sync_install = false,
      highlight = { enable = true },
      indent = { enable = true },
    })
  end
}

