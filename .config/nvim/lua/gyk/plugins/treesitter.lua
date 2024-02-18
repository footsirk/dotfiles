
local ensure_installed = {
    "cpp", "lua", "python",
    "toml", "rust", "ron",
    "html", "css", "javascript"
}

-- Syntax highlighting
return {
    "nvim-treesitter/nvim-treesitter",
    -- lazy = false,
    build = ":TSUpdate",
    config = function()
        require("nvim-treesitter.configs").setup({
            ensure_installed = {
                "cpp", "lua", "python",
                "toml", "rust", "ron",
                "html", "css", "javascript"
            },
            sync_install = false,
            highlight = { enable = true },
            indent = { enable = true },
        })
    end
}
