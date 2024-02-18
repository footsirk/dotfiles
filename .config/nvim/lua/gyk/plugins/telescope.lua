
return {
    'nvim-telescope/telescope.nvim',
    tag = '0.1.3',
    dependencies = { 'nvim-lua/plenary.nvim' },
    keys = {
        {
            "<leader>f",
            function()
                require("telescope.builtin").find_files()
            end,
            desc = "Toggle Telescope find files"
        },
        {
            "<leader>s",
            function()
                require("telescope.builtin").grep_string({
                    search = vim.fn.input("Grep > ")
                })
            end,
            desc = "Toggle Telescope find files"
        },
    }
}
