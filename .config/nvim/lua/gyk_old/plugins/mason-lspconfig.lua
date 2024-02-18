return {
  "williamboman/mason-lspconfig.nvim",
  lazy = false,
  config = function()
    require("mason-lspconfig").setup {
      ensure_installed = {
        "rust_analyzer",
        "pyright",
        -- "pylyzer"
      }
    }
  end
}

