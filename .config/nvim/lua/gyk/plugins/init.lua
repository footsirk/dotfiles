
return {
    -- Displays color codes nicely
    {
        "NvChad/nvim-colorizer.lua",
        opts = {
            filetypes = {"*"},
            mode = "background"
        }
    },

    -- Commenting with gc
    "tpope/vim-commentary",

    -- Treesitter context
    "nvim-treesitter/nvim-treesitter-context",

    -- For viewing project structure
    {
        "nvim-tree/nvim-tree.lua",
        dependencies = {
            "nvim-tree/nvim-web-devicons"
        },
        lazy = false,
        keys = {
            {
                "<leader>e",
                "<cmd>NvimTreeToggle<cr>",
                desc = "Toggle tree"
            }
        },
        config = function()
            require("nvim-tree").setup({})
        end
    },
}

