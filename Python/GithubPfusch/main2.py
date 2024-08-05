import re

import requests
from bs4 import BeautifulSoup

# GitHub API endpoint for repository information
GITHUB_API_URL = "https://api.github.com/repos/"


def get_github_star_count(repo_url, access_token=None):
    """Fetch the star count for a given GitHub repository."""
    # Extract the owner and repo name from the URL
    repo_path = re.search(r"github\.com/([^/]+/[^/]+)", repo_url).group(1)
    # Make a request to the GitHub API
    headers = {}
    if access_token:
        headers['Authorization'] = f'token {access_token}'
    response = requests.get(f"{GITHUB_API_URL}{repo_path}", headers=headers)
    if response.status_code == 200:
        return response.json().get("stargazers_count", 0)
    else:
        return 0


def extract_github_links(html_content):
    """Extract GitHub repository links from HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    github_links = []
    for a_tag in soup.find_all('a', href=True):
        if 'github.com' in a_tag['href']:
            github_links.append(a_tag['href'])
    return github_links


def main(html_content, access_token=None):
    # Extract GitHub links from the HTML content
    github_links = extract_github_links(html_content)

    # Create a dictionary to store repo URLs and their star counts
    repo_star_counts = {}
    for link in github_links:
        star_count = get_github_star_count(link, access_token)
        repo_star_counts[link] = star_count

    # Sort the repositories by star count in descending order
    sorted_repos = sorted(repo_star_counts.items(),
                          key=lambda x: x[1], reverse=True)

    # Print the sorted repositories with their star counts
    for repo, stars in sorted_repos:
        print(f"{repo}: {stars} stars")


if __name__ == "__main__":
    # Example HTML content
    html_content = '''

<div class="markdown-body">
<div class="logo">
<a href="/">
<img src="https://project-awesome.org/images/logo.png" alt="Awesome">
</a>
<h1>
Curated list of awesome lists
</h1>
</div>
<h1>Awesome Neovim <a href="https://github.com/sindresorhus/awesome"><img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome"></a></h1>
<blockquote>
<p>Collections of awesome Neovim plugins. Mostly targeting Neovim specific features.</p>
</blockquote>
<p><a href="https://neovim.io/">Neovim</a> is a Vim-based text editor engineered for extensibility and usability, to encourage new applications and contributions.</p>
<h2>Contents</h2>
<ul>
<li>
<a href="#plugin-manager">Plugin Manager</a>
</li>
<li>
<a href="#lsp">LSP</a>
</li>
<li>
<a href="#completion">Completion</a>
</li>
<li>
<a href="#ai">AI</a>
</li>
<li>
<a href="#programming-languages-support">Programming Languages Support</a>
<ul>
<li>
<a href="#golang">Golang</a>
</li>
<li>
<a href="#yaml">YAML</a>
</li>
<li>
<a href="#web-development">Web Development</a>
</li>
<li>
<a href="#markdown-and-latex">Markdown and LaTeX</a>
</li>
</ul>
</li>
<li>
<a href="#language">Language</a>
</li>
<li>
<a href="#syntax">Syntax</a>
</li>
<li>
<a href="#snippet">Snippet</a>
</li>
<li>
<a href="#register">Register</a>
</li>
<li>
<a href="#marks">Marks</a>
</li>
<li>
<a href="#search">Search</a>
</li>
<li>
<a href="#fuzzy-finder">Fuzzy Finder</a>
</li>
<li>
<a href="#file-explorer">File Explorer</a>
</li>
<li>
<a href="#project">Project</a>
</li>
<li>
<a href="#color">Color</a>
</li>
<li>
<a href="#colorscheme">Colorscheme</a>
<ul>
<li>
<a href="#tree-sitter-supported-colorscheme">Tree-sitter Supported Colorscheme</a>
</li>
<li>
<a href="#lua-colorscheme">Lua Colorscheme</a>
</li>
<li>
<a href="#colorscheme-creation">Colorscheme Creation</a>
</li>
<li>
<a href="#colorscheme-switchers">Colorscheme Switchers</a>
</li>
</ul>
</li>
<li>
<a href="#bars-and-lines">Bars and Lines</a>
<ul>
<li>
<a href="#statusline">Statusline</a>
</li>
<li>
<a href="#tabline">Tabline</a>
</li>
<li>
<a href="#cursorline">Cursorline</a>
</li>
</ul>
</li>
<li>
<a href="#startup">Startup</a>
</li>
<li>
<a href="#icon">Icon</a>
</li>
<li>
<a href="#media">Media</a>
</li>
<li>
<a href="#note-taking">Note Taking</a>
</li>
<li>
<a href="#utility">Utility</a>
</li>
<li>
<a href="#terminal-integration">Terminal Integration</a>
</li>
<li>
<a href="#debugging">Debugging</a>
<ul>
<li>
<a href="#quickfix">Quickfix</a>
</li>
</ul>
</li>
<li>
<a href="#deployment">Deployment</a>
</li>
<li>
<a href="#test">Test</a>
</li>
<li>
<a href="#code-runner">Code Runner</a>
</li>
<li>
<a href="#neovim-lua-development">Neovim Lua Development</a>
</li>
<li>
<a href="#fennel">Fennel</a>
</li>
<li>
<a href="#dependency-management">Dependency Management</a>
</li>
<li>
<a href="#git">Git</a>
<ul>
<li>
<a href="#github">GitHub</a>
</li>
</ul>
</li>
<li>
<a href="#motion">Motion</a>
</li>
<li>
<a href="#keybinding">Keybinding</a>
</li>
<li>
<a href="#mouse">Mouse</a>
</li>
<li>
<a href="#scrolling">Scrolling</a>
<ul>
<li>
<a href="#scrollbar">Scrollbar</a>
</li>
</ul>
</li>
<li>
<a href="#editing-support">Editing Support</a>
<ul>
<li>
<a href="#comment">Comment</a>
</li>
</ul>
</li>
<li>
<a href="#formatting">Formatting</a>
<ul>
<li>
<a href="#indent">Indent</a>
</li>
</ul>
</li>
<li>
<a href="#command-line">Command Line</a>
</li>
<li>
<a href="#session">Session</a>
</li>
<li>
<a href="#remote-development">Remote Development</a>
</li>
<li>
<a href="#split-and-window">Split and Window</a>
<ul>
<li>
<a href="#tmux">Tmux</a>
</li>
</ul>
</li>
<li>
<a href="#game">Game</a>
<ul>
<li>
<a href="#competitive-programming">Competitive Programming</a>
</li>
</ul>
</li>
<li>
<a href="#workflow">Workflow</a>
</li>
<li>
<a href="#preconfigured-configuration">Preconfigured Configuration</a>
</li>
<li>
<a href="#external">External</a>
<ul>
<li>
<a href="#version-manager">Version Manager</a>
</li>
<li>
<a href="#boilerplate">Boilerplate</a>
</li>
<li>
<a href="#os-specific">OS-specific</a>
</li>
</ul>
</li>
<li>
<a href="#wishlist">Wishlist</a>
</li>
<li>
<a href="#ui">UI</a>
</li>
<li>
<a href="#starter-templates">Starter Templates</a>
</li>
<li>
<a href="#vim">Vim</a>
</li>
<li>
<a href="#resource">Resource</a>
</li>
</ul>
<h2 id="plugin-manager">Plugin Manager</h2>
<ul>
<li>
<a href="https://github.com/lewis6991/pckr.nvim">lewis6991/pckr.nvim</a> - Spiritual successor of <code>wbthomason/packer.nvim</code>.</li>
<li>
<a href="https://github.com/savq/paq-nvim">savq/paq-nvim</a> - Neovim package manager written in Lua.</li>
<li>
<a href="https://github.com/NTBBloodbath/cheovim">NTBBloodbath/cheovim</a> - Neovim configuration switcher written in Lua. Inspired by chemacs.</li>
<li>
<a href="https://github.com/chiyadev/dep">chiyadev/dep</a> - An alternative to packer.nvim. It was built to be even better and easier to use. Context can be found <a href="https://chiya.dev/posts/2021-11-27-why-package-manager">here</a>.</li>
<li>
<a href="https://github.com/folke/lazy.nvim">folke/lazy.nvim</a> - A modern plugin manager, featuring a graphical interface, async execution, a lockfile and more 💤.</li>
<li>
<a href="https://github.com/roobert/activate.nvim">roobert/activate.nvim</a> - A plugin installation system designed to complement <code>folke/lazy.nvim</code>.</li>
<li>
<a href="https://github.com/abeldekat/lazyflex.nvim">abeldekat/lazyflex.nvim</a> - An addon for <code>folke/lazy.nvim</code>. Facilitates the testing and troubleshooting of a Neovim configuration.</li>
</ul>
<h2 id="lsp">LSP</h2>
<h3>(requires Neovim 0.5)</h3>
<ul>
<li>
<a href="https://github.com/neovim/nvim-lspconfig">neovim/nvim-lspconfig</a> - Quickstart configurations for the LSP client.</li>
<li>
<a href="https://github.com/nvim-lua/lsp-status.nvim">nvim-lua/lsp-status.nvim</a> - This is a plugin/library for generating statusline components from the built-in LSP client.</li>
<li>
<a href="https://github.com/RishabhRD/nvim-lsputils">RishabhRD/nvim-lsputils</a> - Better defaults for nvim-lsp actions.</li>
<li>
<a href="https://github.com/nvimdev/lspsaga.nvim">nvimdev/lspsaga.nvim</a> - A light-weight LSP plugin based on Neovim's built-in LSP with a highly performant UI.</li>
<li>
<a href="https://github.com/kosayoda/nvim-lightbulb">kosayoda/nvim-lightbulb</a> - The plugin shows a lightbulb in the sign column whenever a <code>textDocument/codeAction</code> is available at the current cursor position.</li>
<li>
<a href="https://github.com/roobert/action-hints.nvim">roobert/action-hints.nvim</a> - Show information about the word under the cursor in the statusline or as virtual text.</li>
<li>
<a href="https://github.com/onsails/lspkind.nvim">onsails/lspkind.nvim</a> - The plugin adds vscode-like icons to Neovim LSP completions.</li>
<li>
<a href="https://github.com/ojroques/nvim-lspfuzzy">ojroques/nvim-lspfuzzy</a> - A small plugin to make the LSP client use FZF.</li>
<li>
<a href="https://github.com/gfanto/fzf-lsp.nvim">gfanto/fzf-lsp.nvim</a> - Enable the power of FZF fuzzy search for the Neovim built in LSP.</li>
<li>
<a href="https://github.com/ray-x/lsp_signature.nvim">ray-x/lsp_signature.nvim</a> - LSP signature hint when you type.</li>
<li>
<a href="https://github.com/smjonas/inc-rename.nvim">smjonas/inc-rename.nvim</a> - Provides an incremental LSP rename command based on Neovim's command-preview feature.</li>
<li>
<a href="https://github.com/rmagatti/goto-preview">rmagatti/goto-preview</a> - Previewing native LSP's goto definition calls in floating windows.</li>
<li>
<a href="https://github.com/jubnzv/virtual-types.nvim">jubnzv/virtual-types.nvim</a> - Show type annotations as virtual text.</li>
<li>
<a href="https://github.com/ray-x/navigator.lua">ray-x/navigator.lua</a> - Learn existing code quickly and navigate code like a breeze. A swiss army knife makes exploring LSP and 🌲Treesitter symbols a piece of 🍰.</li>
<li>
<a href="https://github.com/simrat39/symbols-outline.nvim">simrat39/symbols-outline.nvim</a> - A tree like view for symbols using the Language Server Protocol. Supports all your favourite languages.</li>
<li>
<a href="https://github.com/hedyhli/outline.nvim">hedyhli/outline.nvim</a> - A significantly enhanced and refactored fork of <code>symbols-outline.nvim</code>.</li>
<li>
<a href="https://github.com/stevearc/aerial.nvim">stevearc/aerial.nvim</a> - A code outline window for skimming and quick navigation.</li>
<li>
<a href="https://github.com/SmiteshP/nvim-navbuddy">SmiteshP/nvim-navbuddy</a> - A simple popup display that provides breadcrumbs like navigation features using LSP.</li>
<li>
<a href="https://github.com/tamago324/nlsp-settings.nvim">tamago324/nlsp-settings.nvim</a> - Setup LSP with JSON or YAML files.</li>
<li>
<a href="https://github.com/jakewvincent/texmagic.nvim">jakewvincent/texmagic.nvim</a> - Enhance the lspconfig settings for Texlab by defining any number of custom LaTeX build engines and selecting them with magic comments.</li>
<li>
<a href="https://github.com/nanotee/nvim-lsp-basics">nanotee/nvim-lsp-basics</a> - Basic wrappers for LSP features.</li>
<li>
<a href="https://github.com/weilbith/nvim-code-action-menu">weilbith/nvim-code-action-menu</a> - A floating pop-up menu for code actions to show code action information and a diff preview.</li>
<li>
<a href="https://github.com/aznhe21/actions-preview.nvim">aznhe21/actions-preview.nvim</a> - Fully customizable previewer for LSP code actions.</li>
<li>
<a href="https://github.com/mfussenegger/nvim-lint">mfussenegger/nvim-lint</a> - An asynchronous linter plugin, complementary to the built-in Language Server Protocol support.</li>
<li>
<a href="https://github.com/b0o/SchemaStore.nvim">b0o/SchemaStore.nvim</a> - Provide access to the <a href="https://github.com/SchemaStore/schemastore">SchemaStore</a> catalog.</li>
<li>
<a href="https://github.com/ldelossa/litee.nvim">ldelossa/litee.nvim</a> - Neovim's missing IDE features.</li>
<li>
<a href="https://github.com/j-hui/fidget.nvim">j-hui/fidget.nvim</a> - Standalone UI for LSP progress.</li>
<li>
<a href="https://github.com/scalameta/nvim-metals">scalameta/nvim-metals</a> - Neovim plugin for Metals, the Scala language server, using Neovim's builtin LSP.</li>
<li>
<a href="https://github.com/Junnplus/nvim-lsp-setup">junnplus/nvim-lsp-setup</a> - A simple wrapper for nvim-lspconfig and nvim-lsp-installer to easily setup LSP servers.</li>
<li>
<a href="https://github.com/amrbashir/nvim-docs-view">amrbashir/nvim-docs-view</a> - Display LSP hover documentation in a side panel.</li>
<li>
<a href="https://github.com/roobert/hoversplit.nvim">roobert/hoversplit.nvim</a> - Automatically updated documentation and information about code symbols in a split window.</li>
<li>
<a href="https://github.com/mfussenegger/nvim-jdtls">mfussenegger/nvim-jdtls</a> - Extensions for the built-in LSP support for eclipse.jdt.ls.</li>
<li>
<a href="https://github.com/Kasama/nvim-custom-diagnostic-highlight">Kasama/nvim-custom-diagnostic-highlight</a> - Inline diagnostics popup-highlight much like coc-nvim but based on <code>vim.diagnostic</code>.</li>
<li>
<a href="https://github.com/mrcjkb/haskell-tools.nvim">mrcjkb/haskell-tools.nvim</a> - Seamless integration of Neovim with Haskell development tools like haskell-language-server and Hoogle.</li>
<li>
<a href="https://github.com/ranjithshegde/ccls.nvim">ranjithshegde/ccls.nvim</a> - Use off-spec extensions of ccls LSP and browse AST.</li>
<li>
<a href="https://github.com/idanarye/nvim-buffls">idanarye/nvim-buffls</a> - Add LSP functionality to specific Neovim buffers.</li>
<li>
<a href="https://github.com/DNLHC/glance.nvim">DNLHC/glance.nvim</a> - A pretty window for previewing, navigating and editing your LSP locations.</li>
<li>
<a href="https://github.com/linrongbin16/lsp-progress.nvim">linrongbin16/lsp-progress.nvim</a> - A performant LSP progress status.</li>
<li>
<a href="https://github.com/jinzhongjia/LspUI.nvim">jinzhongjia/LspUI.nvim</a> - A modern and useful UI that wraps LSP operations.</li>
<li>
<a href="https://github.com/VidocqH/lsp-lens.nvim">VidocqH/lsp-lens.nvim</a> - Display function references above function definition like IDEA codelens.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-dr-lsp">chrisgrieser/nvim-dr-lsp</a> - Status line component showing the number of LSP definition and reference of the token under the cursor.</li>
<li>
<a href="https://github.com/Wansmer/symbol-usage.nvim">Wansmer/symbol-usage.nvim</a> - Display references, definitions and implementations of document symbols.</li>
<li>
<a href="https://github.com/creativenull/efmls-configs-nvim">creativenull/efmls-configs-nvim</a> - An unofficial collection of linters and formatters configured for efm-langserver to work with builtin LSP.</li>
<li>
<a href="https://github.com/creativenull/diagnosticls-configs-nvim">creativenull/diagnosticls-configs-nvim</a> - An unofficial collection of linters and formatters configured for diagnostic-languageserver to work with builtin LSP.</li>
<li>
<a href="https://github.com/hinell/lsp-timeout.nvim">hinell/lsp-timeout.nvim</a> - Automatically start/stop idle/unused LSP servers; keeps RAM usage low.</li>
<li>
<a href="https://github.com/nvimtools/none-ls.nvim">nvimtools/none-ls.nvim</a> - Null-ls.nvim reloaded / Use Neovim as a language server to inject LSP diagnostics, code actions, and more via Lua.</li>
<li>
<a href="https://github.com/vxpm/ferris.nvim">vxpm/ferris.nvim</a> - Interact with Rust-Analyzer's LSP extensions.</li>
<li>
<a href="https://github.com/mrcjkb/rustaceanvim">mrcjkb/rustaceanvim</a> - A heavily modified fork of rust-tools.nvim that does not require a <code>setup</code> call and does not depend on nvim-lspconfig.</li>
<li>
<a href="https://github.com/soulis-1256/hoverhints.nvim">soulis-1256/hoverhints.nvim</a> - Mouse-hover LSP hints.</li>
<li>
<a href="https://github.com/stevanmilic/nvim-lspimport">stevanmilic/nvim-lspimport</a> - Automatically resolves imports for undefined terms. Useful with <code>pyright</code> language server.</li>
</ul>
<h4>LSP Installer</h4>
<ul>
<li>
<a href="https://github.com/anott03/nvim-lspinstall">anott03/nvim-lspinstall</a> - Easy to install language servers.</li>
<li>
<a href="https://github.com/alexaandru/nvim-lspupdate">alexaandru/nvim-lspupdate</a> - Updates installed (or auto installs if missing) LSP servers.</li>
<li>
<a href="https://github.com/williamboman/mason.nvim">williamboman/mason.nvim</a> - Portable package manager that runs everywhere Neovim runs. Easily install and manage LSP servers, DAP servers, linters, and formatters.</li>
</ul>
<h4>Diagnostics</h4>
<ul>
<li>
<a href="https://github.com/andrewferrier/textobj-diagnostic.nvim">andrewferrier/textobj-diagnostic</a> - Text object for diagnostics (such as those generated by LSP servers).</li>
<li>
<a href="https://git.sr.ht/~whynothugo/lsp_lines.nvim">~whynothugo/lsp_lines.nvim</a> - Render diagnostics using virtual lines on top of the real line of code.</li>
<li>
<a href="https://github.com/onsails/diaglist.nvim">onsails/diaglist.nvim</a> - Live render workspace diagnostics in quickfix, buffer diagnostics in loclist.</li>
<li>
<a href="https://github.com/folke/trouble.nvim">folke/trouble.nvim</a> - A pretty diagnostics list to help you solve all the trouble your code is causing.</li>
<li>
<a href="https://github.com/piersolenski/wtf.nvim">piersolenski/wtf.nvim</a> - AI powered diagnostic debugging, helps explain complex errors and offers custom tailored solutions.</li>
<li>
<a href="https://github.com/folke/lsp-colors.nvim">folke/lsp-colors.nvim</a> - A plugin that adds missing LSP diagnostics highlight groups for color schemes that don't yet support the builtin LSP client.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-rulebook">chrisgrieser/nvim-rulebook</a> - Add inline-comments to ignore rules, or lookup rule documentation online.</li>
</ul>
<h2 id="completion">Completion</h2>
<ul>
<li>
<a href="https://github.com/ms-jpq/coq_nvim">ms-jpq/coq_nvim</a> - Fast as FUCK Neovim completion. SQLite, concurrent scheduler, hundreds of hours of optimization.</li>
<li>
<a href="https://github.com/hrsh7th/nvim-cmp">hrsh7th/nvim-cmp</a> - A completion plugin written in Lua. New version of nvim-compe.
<ul>
<li>
<a href="https://github.com/lukas-reineke/cmp-under-comparator">lukas-reineke/cmp-under-comparator</a> - A nvim-cmp function for better sorting.</li>
</ul>
</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-completion.md">echasnovski/mini.nvim#mini.completion</a> - Module of <code>mini.nvim</code> for asynchronous two-stage completion. Supports showing completion item info and independent function signature.</li>
<li>
<a href="https://github.com/vigoux/complementree.nvim">vigoux/complementree.nvim</a> - Light and synchronous completion plugin based on tree-sitter and with a functional-programming interface.</li>
<li>
<a href="https://github.com/nvimdev/epo.nvim">nvimdev/epo.nvim</a> - Blazingly fast, minimal LSP auto-completion and snippet engine.</li>
<li>
<a href="https://github.com/simrat39/rust-tools.nvim">simrat39/rust-tools.nvim</a> - Tools for better development in Rust using Neovim's builtin LSP.</li>
<li>
<a href="https://github.com/zbirenbaum/copilot.lua">zbirenbaum/copilot.lua</a> - Fully featured Lua replacement for <a href="https://github.com/github/copilot.vim">GitHub/copilot.vim</a>.</li>
</ul>
<h2 id="ai">AI</h2>
<ul>
<li>
<a href="https://github.com/Robitx/gp.nvim">Robitx/gp.nvim</a> - ChatGPT like sessions and instructable text/code operations in your favorite editor.</li>
<li>
<a href="https://github.com/dpayne/CodeGPT.nvim">dpayne/CodeGPT.nvim</a> - Provides commands to interact with ChatGPT, the focus is around code related usages.</li>
<li>
<a href="https://github.com/jackMort/ChatGPT.nvim">jackMort/ChatGPT.nvim</a> - Effortless Natural Language Generation with OpenAI's ChatGPT API.</li>
<li>
<a href="https://github.com/CamdenClark/flyboy">CamdenClark/flyboy</a> - Simple interaction with ChatGPT in a markdown buffer. Supports GPT-4 and Azure OpenAI.</li>
<li>
<a href="https://github.com/gsuuon/llm.nvim">gsuuon/llm.nvim</a> - Integrate LLM's via a prompt builder interface. Multi-providers including OpenAI (+ compatibles), PaLM, HuggingFace and local engines like llamacpp.</li>
<li>
<a href="https://github.com/dense-analysis/neural">dense-analysis/neural</a> - Integrate LLMs for generating code, interacting with chat bots, and more.</li>
<li>
<a href="https://github.com/jpmcb/nvim-llama">jpmcb/nvim-llama</a> - LLM (Llama 2 and llama.cpp) wrappers.</li>
<li>
<a href="https://github.com/David-Kunz/gen.nvim">David-Kunz/gen.nvim</a> - Generate text using LLMs (via Ollama) with customizable prompts.</li>
</ul>
<h2 id="programming-languages-support">Programming Languages Support</h2>
<ul>
<li>
<a href="https://github.com/Julian/lean.nvim">Julian/lean.nvim</a> - Neovim support for the <a href="https://leanprover.github.io/">Lean Theorem Prover</a>.</li>
<li>
<a href="https://github.com/akinsho/flutter-tools.nvim">akinsho/flutter-tools.nvim</a> - Build Flutter and Dart applications using the native LSP.</li>
<li>
<a href="https://github.com/gbprod/phpactor.nvim">gbprod/phpactor.nvim</a> - Lua version of the Phpactor Vim plugin to take advantage of the latest Neovim features.</li>
<li>
<a href="https://github.com/brendalf/mix.nvim">brendalf/mix.nvim</a> - Mix (from Elixir) wrapper plugin.</li>
<li>
<a href="https://github.com/AckslD/swenv.nvim">AckslD/swenv.nvim</a> - Tiny plugin to quickly switch Python virtual environments without restarting.</li>
<li>
<a href="https://github.com/roobert/f-string-toggle.nvim">roobert/f-string-toggle.nvim</a> - Toggle python f-strings.</li>
<li>
<a href="https://github.com/gennaro-tedesco/nvim-jqx">gennaro-tedesco/nvim-jqx</a> - Interactive interface for JSON files.</li>
<li>
<a href="https://github.com/nanotee/sqls.nvim">nanotee/sqls.nvim</a> - SQL database connection plugin + LSP client.</li>
<li>
<a href="https://github.com/dmmulroy/tsc.nvim">dmmulroy/tsc.nvim</a> - Asynchronous project-wide TypeScript type-checking using the TypeScript compiler (TSC) with results loaded into a quickfix list.</li>
<li>
<a href="https://github.com/chuwy/ucm.nvim">chuwy/ucm.nvim</a> - Navigating <a href="https://unison-lang.org/">Unison</a> projects.</li>
<li>
<a href="https://github.com/niuiic/typst-preview.nvim">niuiic/typst-preview.nvim</a> - Preview typst documents, respond to file changes.</li>
<li>
<a href="https://github.com/simaxme/java.nvim">simaxme/java.nvim</a> - Some utilities regarding Java development (e.g. updating symbol usages when renaming or moving a file in nvim-tree).</li>
</ul>
<h3 id="golang">Golang</h3>
<ul>
<li>
<a href="https://github.com/ray-x/go.nvim">ray-x/go.nvim</a> - Golang plugin based on lsp and Treesitter.</li>
<li>
<a href="https://github.com/crusj/structrue-go.nvim">crusj/structrue-go.nvim</a> - A better structured display of Golang symbols information.</li>
<li>
<a href="https://github.com/crispgm/nvim-go">crispgm/nvim-go</a> - A minimal implementation of Golang development plugin.</li>
<li>
<a href="https://github.com/edolphin-ydf/goimpl.nvim">edolphin-ydf/goimpl.nvim</a> - Generate interface stubs for a type.</li>
<li>
<a href="https://github.com/olexsmir/gopher.nvim/">olexsmir/gopher.nvim</a> - Plugin for making Golang development easiest.</li>
<li>
<a href="https://github.com/rafaelsq/nvim-goc.lua">rafaelsq/nvim-goc.lua</a> - Highlight your buffer with Golang Code Coverage.</li>
<li>
<a href="https://github.com/crusj/hierarchy-tree-go.nvim">crusj/hierarchy-tree-go.nvim</a> - Neovim plugin for Golang, callHierarchy UI tree.</li>
</ul>
<h3 id="yaml">YAML</h3>
<ul>
<li>
<a href="https://github.com/someone-stole-my-name/yaml-companion.nvim">someone-stole-my-name/yaml-companion.nvim</a> - Get, set and autodetect YAML schemas in your buffers.</li>
<li>
<a href="https://github.com/cuducos/yaml.nvim">cuducos/yaml.nvim</a> - Utils to work with YAML files.</li>
</ul>
<h3 id="web-development">Web Development</h3>
<ul>
<li>
<a href="https://github.com/NTBBloodbath/rest.nvim">NTBBloodbath/rest.nvim</a> - A fast Neovim HTTP client written in Lua.</li>
<li>
<a href="https://github.com/ray-x/web-tools.nvim">ray-x/web-tools.nvim</a> - Launch a local development server with live reload feature for static &amp; dynamic pages, HTML &amp; CSS tag rename with LSP.</li>
<li>
<a href="https://github.com/roobert/tailwindcss-colorizer-cmp.nvim">roobert/tailwindcss-colorizer-cmp.nvim</a> - Add vscode-style TailwindCSS completion to nvim-cmp.</li>
</ul>
<h3 id="markdown-and-latex">Markdown and LaTeX</h3>
<ul>
<li>
<a href="https://github.com/ellisonleao/glow.nvim">ellisonleao/glow.nvim</a> - Markdown preview using glow.</li>
<li>
<a href="https://github.com/ellisonleao/dotenv.nvim">ellisonleao/dotenv.nvim</a> - Minimalist .env support.</li>
<li>
<a href="https://github.com/iamcco/markdown-preview.nvim">iamcco/markdown-preview.nvim</a> - Preview markdown on your modern browser with synchronised scrolling and flexible configuration.</li>
<li>
<a href="https://github.com/davidgranstrom/nvim-markdown-preview">davidgranstrom/nvim-markdown-preview</a> - Markdown preview in the browser using pandoc and live-server through Neovim's job-control API.</li>
<li>
<a href="https://github.com/jghauser/auto-pandoc.nvim">jghauser/auto-pandoc.nvim</a> - Easy pandoc conversion leveraging yaml blocks.</li>
<li>
<a href="https://github.com/jghauser/follow-md-links.nvim">jghauser/follow-md-links.nvim</a> - Press enter to follow internal markdown links.</li>
<li>
<a href="https://github.com/jubnzv/mdeval.nvim">jubnzv/mdeval.nvim</a> - Evaluate code blocks inside markdown documents.</li>
<li>
<a href="https://github.com/kdheepak/panvimdoc">kdheepak/panvimdoc</a> - A pandoc to vimdoc GitHub action.</li>
<li>
<a href="https://github.com/frabjous/knap">frabjous/knap</a> - Plugin for creating automatic updating-as-you-type previews for markdown, LaTeX and other documents.</li>
<li>
<a href="https://github.com/jbyuki/carrot.nvim">jbyuki/carrot.nvim</a> - Markdown evaluator Lua code blocks.</li>
<li>
<a href="https://github.com/AckslD/nvim-FeMaco.lua">AckslD/nvim-FeMaco.lua</a> - Catalyze your Fenced Markdown Code-block editing.</li>
<li>
<a href="https://github.com/NFrid/markdown-togglecheck">NFrid/markdown-togglecheck</a> - Simple Neovim plugin for toggling check boxes using Treesitter.</li>
<li>
<a href="https://github.com/toppair/peek.nvim">toppair/peek.nvim</a> - Preview markdown in a webview window.</li>
<li>
<a href="https://github.com/yaocccc/nvim-hl-mdcodeblock.lua">yaocccc/nvim-hl-mdcodeblock.lua</a> - Highlight markdown codeblock using Tree-sitter.</li>
<li>
<a href="https://github.com/kiran94/edit-markdown-table.nvim">kiran94/edit-markdown-table.nvim</a> - Edit Markdown Tables using Tree-sitter.</li>
<li>
<a href="https://github.com/richardbizik/nvim-toc">richardbizik/nvim-toc</a> - Easily generate table of contents for markdown files.</li>
<li>
<a href="https://github.com/Zeioth/markmap.nvim">Zeioth/markmap.nvim</a> - Visualize your Markdown as mindmaps.</li>
<li>
<a href="https://github.com/tadmccorkle/markdown.nvim">tadmccorkle/markdown.nvim</a> - Configurable tools for markdown files, including inline-style, link, and navigation keymaps, table of contents, improved list editing, and more.</li>
</ul>
<h2 id="language">Language</h2>
<ul>
<li>
<a href="https://github.com/potamides/pantran.nvim">potamides/pantran.nvim</a> - Translate your text with an interactive translation window.</li>
<li>
<a href="https://github.com/niuiic/translate.nvim">niuiic/translate.nvim</a> - Invoke any translation engine via shell command.</li>
</ul>
<h2 id="syntax">Syntax</h2>
<ul>
<li>
<a href="https://github.com/nvim-treesitter/nvim-treesitter">nvim-treesitter/nvim-treesitter</a> - Neovim Treesitter configurations and abstraction layer.</li>
<li>
<a href="https://github.com/nvim-treesitter/nvim-treesitter-textobjects">nvim-treesitter/nvim-treesitter-textobjects</a> - Create your own textobjects using tree-sitter queries.</li>
<li>
<a href="https://github.com/RRethy/nvim-treesitter-textsubjects">RRethy/nvim-treesitter-textsubjects</a> - Location and syntax aware text objects which <em>do what you mean</em>.</li>
<li>
<a href="https://github.com/kylechui/nvim-surround">kylechui/nvim-surround</a> - A plugin for adding/changing/deleting surrounding delimiter pairs.</li>
<li>
<a href="https://github.com/roobert/surround-ui.nvim">roobert/surround-ui.nvim</a> - Helper or training aid for kylechui/nvim-surround.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-surround.md">echasnovski/mini.nvim#mini.surround</a> - Module of <code>mini.nvim</code> for working with text surroundings (add, delete, replace, find, highlight). Supports dot-repeat, different search methods, "last"/"next" extended mappings, tree-sitter integration, and more.</li>
<li>
<a href="https://github.com/m-demare/hlargs.nvim">m-demare/hlargs.nvim</a> - Highlight arguments' definitions and usages, using Treesitter.</li>
<li>
<a href="https://github.com/LhKipp/nvim-nu">LhKipp/nvim-nu</a> - Basic editor support for the nushell language.</li>
<li>
<a href="https://github.com/desdic/agrolens.nvim">desdic/agrolens.nvim</a> - Navigate via Tree-sitter nodes using Telescope.</li>
<li>
<a href="https://github.com/IndianBoy42/tree-sitter-just">IndianBoy42/tree-sitter-just</a> - Treesitter grammar for <a href="https://github.com/casey/just">Justfiles</a>.</li>
</ul>
<h2 id="snippet">Snippet</h2>
<ul>
<li>
<a href="https://github.com/norcalli/snippets.nvim">norcalli/snippets.nvim</a> - Snippets in Lua.</li>
<li>
<a href="https://github.com/L3MON4D3/LuaSnip">L3MON4D3/LuaSnip</a> - A snippet engine written in Lua.</li>
<li>
<a href="https://github.com/smjonas/snippet-converter.nvim">smjonas/snippet-converter.nvim</a> - Convert snippets between the most common snippet formats and modify them using a few lines of Lua code.</li>
<li>
<a href="https://github.com/dcampos/nvim-snippy">dcampos/nvim-snippy</a> - Snippet plugin written in Lua with support for <a href="https://github.com/honza/vim-snippets">vim-snippets</a>.</li>
<li>
<a href="https://github.com/ellisonleao/carbon-now.nvim">ellisonleao/carbon-now.nvim</a> - Create beautiful code snippets directly from Neovim.</li>
<li>
<a href="https://github.com/TobinPalmer/rayso.nvim">TobinPalmer/rayso.nvim</a> - Create code snippets in Neovim using <a href="https://ray.so">ray.so</a>.</li>
<li>
<a href="https://github.com/mrcjkb/haskell-snippets.nvim">mrcjkb/haskell-snippets.nvim</a> - Haskell snippets for LuaSnip, powered by Tree-sitter and LSP.</li>
<li>
<a href="https://github.com/rafamadriz/friendly-snippets">rafamadriz/friendly-snippets</a> - Set of preconfigured snippets for different languages.</li>
<li>
<a href="https://github.com/cvigilv/esqueleto.nvim">cvigilv/esqueleto.nvim</a> - Simple templates to use when creating new files.</li>
</ul>
<h2 id="register">Register</h2>
<ul>
<li>
<a href="https://github.com/gennaro-tedesco/nvim-peekup">gennaro-tedesco/nvim-peekup</a> - Dynamically interact with Vim registers.</li>
<li>
<a href="https://github.com/tversteeg/registers.nvim">tversteeg/registers.nvim</a> - Non-obtrusive minimal preview of Vim registers.</li>
<li>
<a href="https://github.com/AckslD/nvim-neoclip.lua">acksld/nvim-neoclip.lua</a> - Clipboard manager Neovim plugin with telescope integration.</li>
<li>
<a href="https://github.com/tenxsoydev/karen-yank.nvim">tenxsoydev/karen-yank.nvim</a> - More intentional register handling with delete, cut and yank mappings.</li>
<li>
<a href="https://github.com/desdic/macrothis.nvim">desdic/macrothis.nvim</a> - Save and load macros/registers.</li>
</ul>
<h2 id="marks">Marks</h2>
<ul>
<li>
<a href="https://github.com/cbochs/grapple.nvim">cbochs/grapple.nvim</a> - Provides tagging, cursor tracking, and immediate navigation to important project files.</li>
<li>
<a href="https://github.com/chentoast/marks.nvim">chentoast/marks.nvim</a> - A better user experience for viewing and interacting with Vim marks.</li>
<li>
<a href="https://github.com/ThePrimeagen/harpoon">ThePrimeagen/harpoon</a> - A per project, auto updating and editable marks utility for fast file navigation.</li>
<li>
<a href="https://github.com/ofirgall/open.nvim">ofirgall/open.nvim</a> - Open the current word with custom openers, GitHub shorthand for example.</li>
<li>
<a href="https://github.com/LeonHeidelbach/trailblazer.nvim">LeonHeidelbach/trailblazer.nvim</a> - TrailBlazer introduces a stack based mark system that enables a completely new dynamic and super fast workflow using project wide marks.</li>
<li>
<a href="https://github.com/tomasky/bookmarks.nvim">tomasky/bookmarks.nvim</a> - Bookmarks with global file storage, written in Lua.</li>
</ul>
<h2 id="search">Search</h2>
<ul>
<li>
<a href="https://github.com/kevinhwang91/nvim-hlslens">kevinhwang91/nvim-hlslens</a> - Helps you better glance searched information, seamlessly jump matched instances.</li>
<li>
<a href="https://github.com/rktjmp/highlight-current-n.nvim">rktjmp/highlight-current-n.nvim</a> - Highlights the current /, ? or * match under your cursor when pressing n or N and gets out of the way afterwards.</li>
<li>
<a href="https://github.com/gaborvecsei/memento.nvim">gaborvecsei/memento.nvim</a> - Keeps track of your visited file history after a buffer is closed. Reopen files more easily.</li>
<li>
<a href="https://github.com/ray-x/sad.nvim">ray-x/sad.nvim</a> - Space Age seD in neovim. Batch file edit tool, a wrapper for <a href="https://github.com/ms-jpq/sad">sad</a>
</li>
<li>
<a href="https://github.com/s1n7ax/nvim-search-and-replace">s1n7ax/nvim-search-and-replace</a> - Search and replace in multiple files at the same time from the current working directory.</li>
<li>
<a href="https://github.com/roobert/search-replace.nvim">roobert/search-replace.nvim</a> - Builds on the native search and replace experience.</li>
<li>
<a href="https://github.com/AckslD/muren.nvim/">AckslD/muren.nvim</a> - Multiple replacements through interactive UI.</li>
<li>
<a href="https://github.com/windwp/nvim-spectre">windwp/nvim-spectre</a> - Search and replace panel.</li>
<li>
<a href="https://github.com/nvimdev/hlsearch.nvim">nvimdev/hlsearch.nvim</a> - Auto remove search highlight and rehighlight when using n or N.</li>
<li>
<a href="https://github.com/mangelozzi/rgflow.nvim">mangelozzi/rgflow.nvim</a> - Quickly get RipGrep results into an editable Quickfix list, while learning RipGrep's CLI.</li>
<li>
<a href="https://github.com/duane9/nvim-rg">duane9/nvim-rg</a> - Run RipGrep asynchronously and see results in a quickfix window.</li>
</ul>
<h2 id="fuzzy-finder">Fuzzy Finder</h2>
<ul>
<li>
<a href="https://github.com/nvim-telescope/telescope.nvim">nvim-telescope/telescope.nvim</a> - Telescope.nvim is a highly <a href="https://github.com/nvim-telescope/telescope.nvim/wiki/Extensions">extendable</a> fuzzy finder over lists. Built on the latest awesome features from Neovim core. Telescope is centered around modularity, allowing for easy customization.</li>
<li>
<a href="https://github.com/vijaymarupudi/nvim-fzf">vijaymarupudi/nvim-fzf</a> - A Lua API for using FZF (Neovim &gt;= 0.5). Allows for full asynchronicity for UI speed and usability.</li>
<li>
<a href="https://github.com/camspiers/snap">camspiers/snap</a> - An extensible fuzzy finder. Similar to Telescope, and optimized for performance, especially when grepping in large codebases.</li>
<li>
<a href="https://github.com/ibhagwan/fzf-lua">ibhagwan/fzf-lua</a> - The Lua version of <code>fzf.vim</code>, high-performance and fully async, supports <code>nvim-web-devicons</code>, git indicators, LSP, quickfix/location lists and more. Also supports <a href="https://github.com/lotabout/skim"><code>skim</code></a> as its fzf binary.</li>
<li>
<a href="https://github.com/jvgrootveld/telescope-zoxide">jvgrootveld/telescope-zoxide</a> - Telescope integration for <a href="https://github.com/ajeetdsouza/zoxide">zoxide</a>, a smart directory picker that tracks your usage.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-fuzzy.md">echasnovski/mini.nvim#mini.fuzzy</a> - Module of <code>mini.nvim</code> with functions to perform fuzzy matching of one string to others along with fast Telescope sorter.</li>
<li>
<a href="https://github.com/axkirillov/easypick.nvim">axkirillov/easypick.nvim</a> - Easypick lets you easily create Telescope pickers from arbitrary console commands.</li>
<li>
<a href="https://github.com/linrongbin16/fzfx.nvim">linrongbin16/fzfx.nvim</a> - E(x)tended commands missing in fzf.vim, a fzf-based fuzzy finder running on the dynamic engine that parsing user query and selection on every keystroke, with friendly features, good performance and maximized customization.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-pick.md">echasnovski/mini.nvim#mini.pick</a> - Module of <code>mini.nvim</code> with general purpose interactive non-blocking picker that has one window design, toggleable preview, flexible and fast default match, and much more.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-extra.md">echasnovski/mini.nvim#mini.extra</a> - Module of <code>mini.nvim</code> with extra functionality for its modules. Contains 20+ 'mini.pick' pickers, 'mini.ai' textobjects, and more.</li>
<li>
<a href="https://github.com/fdschmidt93/telescope-egrepify.nvim">fdschmidt93/telescope-egrepify.nvim</a> - Telescope plugin for better <code>rg</code> flags in <code>live_grep</code>.</li>
</ul>
<h2 id="file-explorer">File Explorer</h2>
<ul>
<li>
<a href="https://github.com/kyazdani42/nvim-tree.lua">kyazdani42/nvim-tree.lua</a> - A simple and fast file explorer tree.</li>
<li>
<a href="https://github.com/luukvbaal/nnn.nvim">luukvbaal/nnn.nvim</a> - File explorer powered by <a href="https://github.com/jarun/nnn">nnn</a> and Lua.</li>
<li>
<a href="https://github.com/tamago324/lir.nvim">tamago324/lir.nvim</a> - Simple file explorer.</li>
<li>
<a href="https://github.com/TimUntersberger/neofs">TimUntersberger/neofs</a> - A file manager written in Lua.</li>
<li>
<a href="https://github.com/kevinhwang91/rnvimr">kevinhwang91/rnvimr</a> - A simple yet amazing file explorer.</li>
<li>
<a href="https://github.com/Xuyuanp/yanil">Xuyuanp/yanil</a> - Yet Another Nerdtree In Lua.</li>
<li>
<a href="https://github.com/ms-jpq/chadtree">ms-jpq/chadtree</a> - File manager. Better than NERDTree.</li>
<li>
<a href="https://github.com/is0n/fm-nvim">is0n/fm-nvim</a> - Neovim plugin that lets you use your favorite terminal file managers (and fuzzy finders).</li>
<li>
<a href="https://github.com/nvim-neo-tree/neo-tree.nvim">nvim-neo-tree/neo-tree.nvim</a> - Neo-tree is a Neovim plugin to browse the file system and other tree like structures in whatever style suits you, including sidebars, floating windows, netrw split style, or all of them at once.</li>
<li>
<a href="https://github.com/elihunter173/dirbuf.nvim">elihunter173/dirbuf.nvim</a> - A file manager which lets you edit your filesystem like you edit text.</li>
<li>
<a href="https://github.com/TheBlob42/drex.nvim">theblob42/drex.nvim</a> - A simple and configurable file explorer written in Lua.</li>
<li>
<a href="https://github.com/SidOfc/carbon.nvim">SidOfc/carbon.nvim</a> - The simple directory tree viewer written in Lua.</li>
<li>
<a href="https://github.com/dinhhuy258/sfm.nvim">dinhhuy258/sfm.nvim</a> - An alternative to Nvim-tree designed to be extensible and minimalist.</li>
<li>
<a href="https://github.com/kiran94/s3edit.nvim">kiran94/s3edit.nvim</a> - Edit files from Amazon S3 directly from Neovim.</li>
<li>
<a href="https://github.com/stevearc/oil.nvim">stevearc/oil.nvim</a> - Edit your filesystem like a buffer.</li>
<li>
<a href="https://github.com/kelly-lin/ranger.nvim">kelly-lin/ranger.nvim</a> - <a href="https://github.com/ranger/ranger">Ranger</a> integration for neovim.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-files.md">echasnovski/mini.nvim#mini.files</a> - Module of <code>mini.nvim</code> providing file explorer with column view capable of manipulating file system by editing text. Can create/delete/rename/copy/move files/directories inside and across directories.</li>
</ul>
<h2 id="project">Project</h2>
<ul>
<li>
<a href="https://github.com/pluffie/neoproj">pluffie/neoproj</a> - Small yet powerful project (and session) manager.</li>
<li>
<a href="https://github.com/shaeinst/penvim">shaeinst/penvim</a> - Project's Root Directory and Documents Indentation detector with project based config loader.</li>
<li>
<a href="https://github.com/nyngwang/NeoRoot.lua">nyngwang/NeoRoot.lua</a> - Change your current working directory to the buffer your cursor is on, and try to go up 2 levels but stop after it encounters one of the project roots you define.</li>
<li>
<a href="https://github.com/windwp/nvim-projectconfig">windwp/nvim-projectconfig</a> - Load Neovim config depend on project directory.</li>
<li>
<a href="https://github.com/ahmedkhalf/project.nvim">ahmedkhalf/project.nvim</a> - An all in one Neovim plugin that provides superior project management.</li>
<li>
<a href="https://github.com/klen/nvim-config-local">klen/nvim-config-local</a> - Secure load local config files from working directories.</li>
<li>
<a href="https://cj.rs/telescope-repo-nvim/">cljoly/telescope-repo.nvim</a> - Telescope picker to jump to any repository (git or other) on the file system.</li>
<li>
<a href="https://github.com/otavioschwanck/telescope-alternate.nvim">otavioschwanck/telescope-alternate.nvim</a> - Alternate between common files using telescope.</li>
<li>
<a href="https://github.com/natecraddock/workspaces.nvim">natecraddock/workspaces.nvim</a> - Manage workspace directories.</li>
<li>
<a href="https://github.com/gnikdroy/projections.nvim">gnikdroy/projections.nvim</a> - Tiny project + session manager.</li>
<li>
<a href="https://github.com/nyngwang/suave.lua">nyngwang/suave.lua</a> - Multi-tabs project session automation.</li>
<li>
<a href="https://github.com/desdic/telescope-rooter.nvim">desdic/telescope-rooter.nvim</a> - Makes sure to always start telescope (and only telescope) from the project/root directory.</li>
<li>
<a href="https://github.com/SalOrak/whaler.nvim">SalOrak/whaler.nvim</a> - Telescope extension to move between directories blazingly fast.</li>
</ul>
<h2 id="color">Color</h2>
<ul>
<li>
<a href="https://github.com/NvChad/nvim-colorizer.lua">NvChad/nvim-colorizer.lua</a> - A high-performance color highlighter which has no external dependencies!.</li>
<li>
<a href="https://github.com/winston0410/range-highlight.nvim">winston0410/range-highlight.nvim</a> - An extremely lightweight plugin (~ 120loc) that highlights ranges you have entered in commandline.</li>
<li>
<a href="https://github.com/xiyaowong/nvim-transparent">xiyaowong/nvim-transparent</a> - Make your Neovim transparent.</li>
<li>
<a href="https://github.com/folke/twilight.nvim">folke/twilight.nvim</a> - Dim inactive portions of the code you're editing using TreeSitter.</li>
<li>
<a href="https://github.com/koenverburg/peepsight.nvim">koenverburg/peepsight.nvim</a> - Focus only the function your cursor is in.</li>
<li>
<a href="https://github.com/uga-rosa/ccc.nvim">uga-rosa/ccc.nvim</a> - Super powerful color picker / colorizer plugin.</li>
<li>
<a href="https://github.com/ziontee113/color-picker.nvim">ziontee113/color-picker.nvim</a> - Plugin that lets users choose &amp; modify RGB/HSL/HEX colors inside Neovim.</li>
<li>
<a href="https://github.com/lcheylus/overlength.nvim">lcheylus/overlength.nvim</a> - A small plugin to highlight too long lines.</li>
<li>
<a href="https://github.com/brenoprata10/nvim-highlight-colors">brenoprata10/nvim-highlight-colors</a> - A plugin to highlight colors with Neovim.</li>
<li>
<a href="https://github.com/nvim-colortils/colortils.nvim">nvim-colortils/colortils.nvim</a> - A plugin providing utils to work with colors (picker, conversion) inside Neovim.</li>
<li>
<a href="https://github.com/Mr-LLLLL/interestingwords.nvim">Mr-LLLLL/interestingwords.nvim</a> - Highlight multiple word same time and navigate word under cursor with scrolling smoothly, display search count in virualtext.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-hipatterns.md">echasnovski/mini.nvim#mini.hipatterns</a> - Module of <code>mini.nvim</code> to highlight patterns in text with configurable highlighters. Works asynchronously with configurable debounce delay.</li>
<li>
<a href="https://github.com/miversen33/sunglasses.nvim">miversen33/sunglasses.nvim</a> - Dynamic Colorscheme/highlight adjuster on window switching.</li>
</ul>
<h2 id="colorscheme">Colorscheme</h2>
<h3 id="tree-sitter-supported-colorscheme">Tree-sitter Supported Colorscheme</h3>
<p>Tree-sitter is a new system introduced in Neovim 0.5 that incrementally parses your code into a tree that works, even with errors in your syntax. These colorschemes have specifically set colors for Tree-sitter highlight groups. Vim colorschemes will work with the new groups out of the box.</p>
<ul>
<li>
<a href="https://github.com/shaeinst/roshnivim-cs">shaeinst/roshnivim-cs</a> - Colorscheme written in Lua, specially made for roshnivim with Tree-sitter support.</li>
<li>
<a href="https://github.com/rafamadriz/neon">rafamadriz/neon</a> - Customizable colorscheme with excellent italic and bold support, dark and light variants. Made to work and look good with Tree-sitter.</li>
<li>
<a href="https://github.com/tomasiser/vim-code-dark">tomasiser/vim-code-dark</a> - A dark color scheme heavily inspired by the look of the Dark+ scheme of Visual Studio Code.</li>
<li>
<a href="https://github.com/Mofiqul/vscode.nvim">Mofiqul/vscode.nvim</a> - A Lua port of vim-code-dark colorscheme with vscode light and dark theme.</li>
<li>
<a href="https://github.com/askfiy/visual_studio_code">askfiy/visual_studio_code</a> - A Neovim theme that highly restores vscode, so that your friends will no longer be surprised that you use Neovim, because they will think you are using vscode.</li>
<li>
<a href="https://github.com/marko-cerovac/material.nvim">marko-cerovac/material.nvim</a> - Material.nvim is a highly configurable colorscheme written in Lua and based on the material palette.</li>
<li>
<a href="https://github.com/bluz71/vim-nightfly-colors">bluz71/vim-nightfly-colors</a> - A dark midnight colorscheme with modern Neovim support including Tree-sitter.</li>
<li>
<a href="https://github.com/bluz71/vim-moonfly-colors">bluz71/vim-moonfly-colors</a> - A dark charcoal colorscheme with modern Neovim support including Tree-sitter.</li>
<li>
<a href="https://github.com/ChristianChiarulli/nvcode-color-schemes.vim">ChristianChiarulli/nvcode-color-schemes.vim</a> - Nvcode, onedark, nord colorschemes with Tree-sitter support.</li>
<li>
<a href="https://github.com/folke/tokyonight.nvim">folke/tokyonight.nvim</a> - A clean, dark and light Neovim theme written in Lua, with support for LSP, Tree-sitter and lots of plugins.</li>
<li>
<a href="https://github.com/sainnhe/sonokai">sainnhe/sonokai</a> - High Contrast &amp; Vivid Color Scheme based on Monokai Pro.</li>
<li>
<a href="https://github.com/nyoom-engineering/oxocarbon.nvim">nyoom-engineering/oxocarbon.nvim</a> - A dark and light Neovim theme written in fennel, inspired by IBM Carbon.</li>
<li>
<a href="https://github.com/kyazdani42/blue-moon">kyazdani42/blue-moon</a> - A dark color scheme derived from palenight and carbonight.</li>
<li>
<a href="https://github.com/mhartington/oceanic-next">mhartington/oceanic-next</a> - Oceanic Next theme.</li>
<li>
<a href="https://github.com/nvimdev/zephyr-nvim">nvimdev/zephyr-nvim</a> - A dark colorscheme with Tree-sitter support.</li>
<li>
<a href="https://github.com/rockerBOO/boo-colorscheme-nvim">rockerBOO/boo-colorscheme-nvim</a> - A colorscheme with handcrafted support for LSP, Tree-sitter.</li>
<li>
<a href="https://github.com/jim-at-jibba/ariake-vim-colors">jim-at-jibba/ariake-vim-colors</a> - A port of the great Atom theme. Dark and light with Tree-sitter support.</li>
<li>
<a href="https://github.com/Th3Whit3Wolf/onebuddy">Th3Whit3Wolf/onebuddy</a> - Light and dark atom one theme.</li>
<li>
<a href="https://github.com/ishan9299/modus-theme-vim">ishan9299/modus-theme-vim</a> - This is a color scheme developed by Protesilaos Stavrou for emacs.</li>
<li>
<a href="https://github.com/sainnhe/edge">sainnhe/edge</a> - Clean &amp; Elegant Color Scheme inspired by Atom One and Material.</li>
<li>
<a href="https://github.com/theniceboy/nvim-deus">theniceboy/nvim-deus</a> - Vim-deus with Tree-sitter support.</li>
<li>
<a href="https://github.com/bkegley/gloombuddy">bkegley/gloombuddy</a> - Gloom inspired theme.</li>
<li>
<a href="https://github.com/Th3Whit3Wolf/one-nvim">Th3Whit3Wolf/one-nvim</a> - An Atom One inspired dark and light colorscheme.</li>
<li>
<a href="https://github.com/PHSix/nvim-hybrid">PHSix/nvim-hybrid</a> - A Neovim colorscheme write in Lua.</li>
<li>
<a href="https://github.com/Th3Whit3Wolf/space-nvim">Th3Whit3Wolf/space-nvim</a> - A spacemacs inspired dark and light colorscheme.</li>
<li>
<a href="https://github.com/yonlu/omni.vim">yonlu/omni.vim</a> - Omni color scheme for Vim.</li>
<li>
<a href="https://github.com/ray-x/aurora">ray-x/aurora</a> - A 24-bit dark theme with Tree-sitter and LSP support.</li>
<li>
<a href="https://github.com/ray-x/starry.nvim">ray-x/starry.nvim</a> - A collection of modern Neovim colorschemes: material, moonlight, dracula (blood), monokai, mariana, emerald, earlysummer, middlenight_blue, darksolar.</li>
<li>
<a href="https://github.com/tanvirtin/monokai.nvim">tanvirtin/monokai.nvim</a> - Monokai theme written in Lua.</li>
<li>
<a href="https://github.com/ofirgall/ofirkai.nvim">ofirgall/ofirkai.nvim</a> - Monokai theme that aims to feel like Sublime Text.</li>
<li>
<a href="https://github.com/savq/melange-nvim">savq/melange-nvim</a> - Warm colorscheme written in Lua with support for various terminal emulators.</li>
<li>
<a href="https://github.com/RRethy/nvim-base16">RRethy/nvim-base16</a> - Neovim plugin for building base16 colorschemes. Includes support for Treesitter and LSP highlight groups.</li>
<li>
<a href="https://github.com/fenetikm/falcon">fenetikm/falcon</a> - A colour scheme for terminals, Vim and friends.</li>
<li>
<a href="https://github.com/andersevenrud/nordic.nvim">andersevenrud/nordic.nvim</a> - A nord-esque colorscheme.</li>
<li>
<a href="https://github.com/AlexvZyl/nordic.nvim">AlexvZyl/nordic.nvim</a> - Nord for Neovim, but warmer and darker. Supports a variety of plugins and other platforms.</li>
<li>
<a href="https://github.com/shaunsingh/nord.nvim">shaunsingh/nord.nvim</a> - Neovim theme based off of the Nord Color Palette.</li>
<li>
<a href="https://github.com/Tsuzat/NeoSolarized.nvim">Tsuzat/NeoSolarized.nvim</a> - NeoSolarized colorscheme with full transparency.</li>
<li>
<a href="https://github.com/svrana/neosolarized.nvim">svrana/neosolarized.nvim</a> - Dark solarized colorscheme using colorbuddy for easy customization.</li>
<li>
<a href="https://github.com/ishan9299/nvim-solarized-lua">ishan9299/nvim-solarized-lua</a> - Solarized colorscheme in Lua (Neovim &gt;= 0.5).</li>
<li>
<a href="https://github.com/shaunsingh/moonlight.nvim">shaunsingh/moonlight.nvim</a> - Port of VSCode's Moonlight colorscheme, written in Lua with built-in support for native LSP, Tree-sitter and many more plugins.</li>
<li>
<a href="https://github.com/navarasu/onedark.nvim">navarasu/onedark.nvim</a> - A One Dark Theme (Neovim &gt;= 0.5) written in Lua based on Atom's One Dark Theme.</li>
<li>
<a href="https://github.com/lourenci/github-colors">lourenci/github-colors</a> - GitHub colors leveraging Tree-sitter to get 100% accuracy.</li>
<li>
<a href="https://github.com/sainnhe/gruvbox-material">sainnhe/gruvbox-material</a> - Gruvbox modification with softer contrast and Tree-sitter support.</li>
<li>
<a href="https://github.com/sainnhe/everforest">sainnhe/everforest</a> - A green based colorscheme designed to be warm, soft and easy on the eyes.</li>
<li>
<a href="https://github.com/neanias/everforest-nvim">neanias/everforest-nvim</a> - A Lua port of the Everforest colour scheme.</li>
<li>
<a href="https://github.com/NTBBloodbath/doom-one.nvim">NTBBloodbath/doom-one.nvim</a> - Lua port of doom-emacs' doom-one.</li>
<li>
<a href="https://github.com/dracula/vim">dracula/vim</a> - Famous beautiful dark powered theme.</li>
<li>
<a href="https://github.com/Mofiqul/dracula.nvim">Mofiqul/dracula.nvim</a> - Dracula colorscheme for neovim written in Lua.</li>
<li>
<a href="https://github.com/yashguptaz/calvera-dark.nvim">yashguptaz/calvera-dark.nvim</a> - A port of <a href="https://github.com/saurabhdaware/vscode-calvera-dark">VSCode Calvara Dark</a> Theme to Neovim with Tree-sitter and many other plugins support.</li>
<li>
<a href="https://github.com/nxvu699134/vn-night.nvim">nxvu699134/vn-night.nvim</a> - A dark Neovim colorscheme written in Lua. Support built-in LSP and Tree-sitter.</li>
<li>
<a href="https://github.com/adisen99/codeschool.nvim">adisen99/codeschool.nvim</a> - Codeschool colorscheme written in Lua with Tree-sitter and built-in lsp support.</li>
<li>
<a href="https://github.com/projekt0n/github-nvim-theme">projekt0n/github-nvim-theme</a> - A GitHub theme, kitty, alacritty written in Lua. Support built-in LSP and Tree-sitter.</li>
<li>
<a href="https://github.com/kdheepak/monochrome.nvim">kdheepak/monochrome.nvim</a> - A 16 bit monochrome colorscheme that uses hsluv for perceptually distinct gray colors, with support for Tree-sitter and other commonly used plugins.</li>
<li>
<a href="https://github.com/rose-pine/neovim">rose-pine/neovim</a> - All natural pine, faux fur and a bit of soho vibes for the classy minimalist.</li>
<li>
<a href="https://github.com/mcchrish/zenbones.nvim">mcchrish/zenbones.nvim</a> - A collection of Vim/Neovim colorschemes designed to highlight code using contrasts and font variations.</li>
<li>
<a href="https://github.com/catppuccin/nvim">catppuccin/nvim</a> - Warm mid-tone dark theme to show off your vibrant self! with support for native LSP, Tree-sitter, and more 🍨!</li>
<li>
<a href="https://github.com/FrenzyExists/aquarium-vim">FrenzyExists/aquarium-vim</a> - A dark, yet vibrant colorscheme.</li>
<li>
<a href="https://github.com/EdenEast/nightfox.nvim">EdenEast/nightfox.nvim</a> - A soft dark, fully customizable Neovim theme, with support for lsp, treesitter and a variety of plugins.</li>
<li>
<a href="https://github.com/kvrohit/substrata.nvim">kvrohit/substrata.nvim</a> - A cold, dark color scheme written in Lua ported from <a href="https://github.com/arzg/vim-substrata">arzg/vim-substrata</a> theme.</li>
<li>
<a href="https://github.com/ldelossa/vimdark">ldelossa/vimdark</a> - A minimal Vim theme for night time. Loosely based on vim-monotonic and chrome's dark reader extension. A light theme is included as well for the day time.</li>
<li>
<a href="https://github.com/Everblush/everblush.nvim">Everblush/everblush.nvim</a> - A dark, vibrant and beautiful colorscheme written in Lua.</li>
<li>
<a href="https://github.com/adisen99/apprentice.nvim">adisen99/apprentice.nvim</a> - Colorscheme written in Lua based on the <a href="https://github.com/romainl/Apprentice">Apprentice</a> color pattete with Tree-sitter and built-in lsp support.</li>
<li>
<a href="https://github.com/olimorris/onedarkpro.nvim">olimorris/onedarkpro.nvim</a> - One Dark Pro theme, written in Lua and based on the VS Code theme. Includes dark and light themes with completely customisable colors, styles and highlights.</li>
<li>
<a href="https://github.com/rmehri01/onenord.nvim">rmehri01/onenord.nvim</a> - A Neovim theme that combines the Nord and Atom One Dark color palettes for a more vibrant programming experience.</li>
<li>
<a href="https://github.com/RishabhRD/gruvy">RishabhRD/gruvy</a> - Gruvbuddy without colorbuddy using Lush.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim#plugin-colorschemes">echasnovski/mini.nvim#colorschemes</a> - Color schemes included in <code>mini.nvim</code> plugin. All of them prioritize high contrast ratio for reading text and computing palettes in perceptually uniform color spaces.</li>
<li>
<a href="https://github.com/luisiacc/gruvbox-baby">luisiacc/gruvbox-baby</a> - A modern gruvbox theme with full treesitter support.</li>
<li>
<a href="https://github.com/titanzero/zephyrium">titanzero/zephyrium</a> - A zephyr-esque theme, written in Lua, with TreeSitter support.</li>
<li>
<a href="https://github.com/rebelot/kanagawa.nvim">rebelot/kanagawa.nvim</a> - Neovim dark colorscheme inspired by the colors of the famous painting by Katsushika Hokusai.</li>
<li>
<a href="https://github.com/tiagovla/tokyodark.nvim">tiagovla/tokyodark.nvim</a> - A clean dark theme written in Lua (Neovim &gt;= 0.5) and above.</li>
<li>
<a href="https://github.com/cpea2506/one_monokai.nvim">cpea2506/one_monokai.nvim</a> - One Monokai theme written in Lua.</li>
<li>
<a href="https://github.com/phha/zenburn.nvim">phha/zenburn.nvim</a> - A low-contrast dark colorscheme with support for various plugins.</li>
<li>
<a href="https://github.com/kvrohit/rasmus.nvim">kvrohit/rasmus.nvim</a> - A dark color scheme written in Lua ported from <a href="https://github.com/rsms/sublime-theme">rsms/sublime-theme</a> theme.</li>
<li>
<a href="https://github.com/chrsm/paramount-ng.nvim">chrsm/paramount-ng.nvim</a> - A dark color scheme written using Lush. Treesitter supported.</li>
<li>
<a href="https://github.com/kaiuri/nvim-juliana">kaiuri/nvim-juliana</a> - Port of Sublime's Mariana Theme to Neovim for short attention span developers with Tree-sitter support.</li>
<li>
<a href="https://github.com/lmburns/kimbox">lmburns/kimbox</a> - A colorscheme with a dark background, and vibrant foreground that is centered around the color brown. A modification of <a href="https://marketplace.visualstudio.com/items?itemName=dnamsons.kimbie-dark-plus">Kimbie Dark</a>.</li>
<li>
<a href="https://github.com/rockyzhang24/arctic.nvim">rockyzhang24/arctic.nvim</a> - A Neovim colorscheme ported from VSCode Dark+ theme with the strict and precise color picking for both the editor and UI.</li>
<li>
<a href="https://github.com/ramojus/mellifluous.nvim">ramojus/mellifluous.nvim</a> - Pleasant and productive colorscheme.</li>
<li>
<a href="https://github.com/yazeed1s/minimal.nvim">Yazeed1s/minimal.nvim</a> - Two tree-sitter supported colorschemes that are inspired by base16-tomorrow-night and monokai-pro.</li>
<li>
<a href="https://github.com/lewpoly/sherbet.nvim">lewpoly/sherbet.nvim</a> - A soothing colorscheme with support for popular plugins and tree-sitter.</li>
<li>
<a href="https://github.com/Mofiqul/adwaita.nvim">Mofiqul/adwaita.nvim</a> - Colorscheme based on GNOME Adwaita syntax with support for popular plugins.</li>
<li>
<a href="https://github.com/olivercederborg/poimandres.nvim">olivercederborg/poimandres.nvim</a> - Neovim port of <a href="https://github.com/drcmda/poimandres-theme">poimandres VSCode theme</a> with Tree-sitter support, written in Lua.</li>
<li>
<a href="https://github.com/kvrohit/mellow.nvim">kvrohit/mellow.nvim</a> - A soothing dark color scheme with tree-sitter support.</li>
<li>
<a href="https://github.com/gbprod/nord.nvim">gbprod/nord.nvim</a> - An arctic, north-bluish clean and elegant Neovim theme, based on Nord Palette.</li>
<li>
<a href="https://github.com/yazeed1s/oh-lucy.nvim">Yazeed1s/oh-lucy.nvim</a> - Two tree-sitter supported colorschemes, inspired by oh-lucy in vscode.</li>
<li>
<a href="https://github.com/embark-theme/vim">embark-theme/vim</a> - A deep inky purple theme leveraging bright colors.</li>
<li>
<a href="https://github.com/nyngwang/nvimgelion">nyngwang/nvimgelion</a> - Neon Genesis Evangelion but for Vimmers.</li>
<li>
<a href="https://github.com/maxmx03/FluoroMachine.nvim">maxmx03/FluoroMachine.nvim</a> - Synthwave x Fluoromachine port.</li>
<li>
<a href="https://github.com/dasupradyumna/midnight.nvim">dasupradyumna/midnight.nvim</a> - A modern black Neovim theme with comfortable color contrast for a pleasant visual experience, with LSP and Tree-sitter support.</li>
<li>
<a href="https://github.com/sonjiku/yawnc.nvim">sonjiku/yawnc.nvim</a> - Theming using pywal, with a Base16 twist.</li>
<li>
<a href="https://github.com/sekke276/dark_flat.nvim">sekke276/dark_flat.nvim</a> - A Neovim colorscheme written in Lua ported from Dark Flat iTerm2 theme, with LSP and Tree-sitter support.</li>
<li>
<a href="https://github.com/zootedb0t/citruszest.nvim">zootedb0t/citruszest.nvim</a> - A colorscheme that features a combination of bright and juicy colors reminiscent of various citrus fruits, with LSP and Tree-sitter support.</li>
<li>
<a href="https://github.com/2nthony/vitesse.nvim">2nthony/vitesse.nvim</a> - Vitesse theme Lua port.</li>
<li>
<a href="https://github.com/xero/miasma.nvim">xero/miasma.nvim</a> - A dark pastel color scheme inspired by the woods. Built using lush and supports Tree-sitter, diagnostics, CMP, Git-Signs, Telescope, Which-key, Lazy, and more.</li>
<li>
<a href="https://github.com/Verf/deepwhite.nvim">Verf/deepwhite.nvim</a> - A light colorscheme inspired by <a href="https://github.com/biletskyy/flatwhite-syntax">flatwhite-syntax</a> and <a href="https://github.com/rougier/elegant-emacs">elegant-emacs</a>.</li>
<li>
<a href="https://github.com/judaew/ronny.nvim">judaew/ronny.nvim</a> - A dark colorscheme, which mostly was inspired by the Monokai originally created by Wimem Hazenberg.</li>
<li>
<a href="https://github.com/ribru17/bamboo.nvim">ribru17/bamboo.nvim</a> - A warm green theme.</li>
<li>
<a href="https://github.com/cryptomilk/nightcity.nvim">cryptomilk/nightcity.nvim</a> - A dark colorscheme inspired by Inkpot, Jellybeans, Gruvbox and Tokyonight with LSP support.</li>
<li>
<a href="https://github.com/polirritmico/monokai-nightasty.nvim">polirritmico/monokai-nightasty.nvim</a> - A dark/light theme based on the Monokai color palette written in Lua, support for LSP, Tree-sitter and lots of plugins.</li>
<li>
<a href="https://github.com/oxfist/night-owl.nvim">oxfist/night-owl.nvim</a> - A <a href="https://github.com/sdras/night-owl-vscode-theme">Night Owl colorscheme port from VSCode</a> with support for Tree-sitter and semantic tokens.</li>
<li>
<a href="https://github.com/svermeulen/text-to-colorscheme">text-to-colorscheme</a> - Dynamically generated colorschemes generated on the fly with a text prompt using ChatGPT.</li>
<li>
<a href="https://github.com/miikanissi/modus-themes.nvim">miikanissi/modus-themes.nvim</a> - Accessible theme, conforming with the highest standard for color contrast (WCAG AAA).</li>
</ul>
<h3 id="lua-colorscheme">Lua Colorscheme</h3>
<p>These colorschemes may not specialize in Tree-sitter directly but are written in Lua.</p>
<ul>
<li>
<a href="https://github.com/tjdevries/gruvbuddy.nvim">tjdevries/gruvbuddy.nvim</a> - Gruvbox colors.</li>
<li>
<a href="https://github.com/ellisonleao/gruvbox.nvim">ellisonleao/gruvbox.nvim</a> - Gruvbox community colorscheme Lua port.</li>
<li>
<a href="https://github.com/metalelf0/jellybeans-nvim">metalelf0/jellybeans-nvim</a> - A port of jellybeans colorscheme.</li>
<li>
<a href="https://github.com/lalitmee/cobalt2.nvim">lalitmee/cobalt2.nvim</a> - A port of cobalt2 colorscheme using colorbuddy.</li>
<li>
<a href="https://github.com/calind/selenized.nvim">calind/selenized.nvim</a> - Lua port of Selenized theme with support for Tree-sitter, nvim-cmp, GitSigns and some more.</li>
</ul>
<h3 id="colorscheme-creation">Colorscheme Creation</h3>
<ul>
<li>
<a href="https://github.com/tjdevries/colorbuddy.nvim">tjdevries/colorbuddy.nvim</a> - A colorscheme helper. Written in Lua! Quick &amp; Easy Color Schemes 😄.</li>
<li>
<a href="https://github.com/norcalli/nvim-base16.lua">norcalli/nvim-base16.lua</a> - Programmatic Lua library for setting base16 themes.</li>
<li>
<a href="https://github.com/rktjmp/lush.nvim">rktjmp/lush.nvim</a> - Define Neovim themes as a DSL in Lua, with real-time feedback.</li>
<li>
<a href="https://github.com/roobert/palette.nvim">roobert/palette.nvim</a> - A beautiful, versatile, systematic, theme system.</li>
<li>
<a href="https://github.com/Iron-E/nvim-highlite">Iron-E/nvim-highlite</a> - A colorscheme generator that is "lite" on logic for the developer.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-base16.md">echasnovski/mini.nvim#mini.base16</a> - Module of <code>mini.nvim</code> with fast implementation of base16 theme for manually supplied palette.</li>
<li>
<a href="https://github.com/themercorp/themer.lua">ThemerCorp/themer.lua</a> - A simple highlighter plugin for neovim. It has a huge collection of colorschemes. It also has ability to create colorschemes for Vim/Neovim and other supported apps (such as kitty and alacritty).</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-colors.md">echasnovski/mini.nvim#mini.colors</a> - Module of <code>mini.nvim</code> to tweak and save any color scheme. Also can animate transition and convert between some color spaces.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-hues.md">echasnovski/mini.nvim#mini.hues</a> - Module of <code>mini.nvim</code> to generate configurable color scheme. Takes only background and foreground colors as required arguments. Can adjust number of hues for non-base colors, saturation, accent color, plugin integration.</li>
</ul>
<h3 id="colorscheme-switchers">Colorscheme Switchers</h3>
<ul>
<li>
<a href="https://github.com/4e554c4c/darkman.nvim">4e554c4c/darkman.nvim</a> - Follow the system dark-mode setting on Linux.</li>
<li>
<a href="https://github.com/f-person/auto-dark-mode.nvim">f-person/auto-dark-mode.nvim</a> - Follow the system appearance on macOS.</li>
<li>
<a href="https://github.com/zaldih/themery.nvim">zaldih/themery.nvim</a> - A new way to change the colorscheme on the fly like in vscode.</li>
<li>
<a href="https://github.com/linrongbin16/colorbox.nvim">linrongbin16/colorbox.nvim</a> - Load all the ultra colorschemes into your Neovim player! It collects all the most popular colorschemes, installs them, and allows you to play them with multiple playback settings.</li>
</ul>
<h2 id="bars-and-lines">Bars and Lines</h2>
<ul>
<li>
<a href="https://github.com/Bekaboo/deadcolumn.nvim">Bekaboo/deadcolumn.nvim</a> - Shows your colorcolumn dynamically.</li>
<li>
<a href="https://github.com/ecthelionvi/NeoColumn.nvim">ecthelionvi/NeoColumn.nvim</a> - Toggleable colorcolumn highlighting specific characters.</li>
<li>
<a href="https://github.com/m4xshen/smartcolumn.nvim">m4xshen/smartcolumn.nvim</a> - Hide your colorcolumn when unneeded.</li>
<li>
<a href="https://github.com/utilyre/barbecue.nvim">utilyre/barbecue.nvim</a> - A VS Code like winbar.</li>
<li>
<a href="https://github.com/Bekaboo/dropbar.nvim">Bekaboo/dropbar.nvim</a> - IDE-like breadcrumbs, out of the box.</li>
<li>
<a href="https://github.com/SmiteshP/nvim-navic">SmiteshP/nvim-navic</a> - A simple statusline/winbar component that uses LSP to show your current code context.</li>
<li>
<a href="https://github.com/luukvbaal/statuscol.nvim">luukvbaal/statuscol.nvim</a> - Configurable 'statuscolumn' with builtin segments and click handlers.</li>
</ul>
<h3 id="statusline">Statusline</h3>
<ul>
<li>
<a href="https://github.com/NTBBloodbath/galaxyline.nvim">NTBBloodbath/galaxyline.nvim</a> - Galaxyline componentizes Vim's statusline by having a provider for each text area. This means you can use the api provided by galaxyline to create the statusline that you want, easily.</li>
<li>
<a href="https://github.com/tjdevries/express_line.nvim">tjdevries/express_line.nvim</a> - Supports co-routines, functions and jobs.</li>
<li>
<a href="https://github.com/sontungexpt/sttusline">sontungexpt/sttusline</a> - Very lightweight, super fast and lazyloading statusline.</li>
<li>
<a href="https://github.com/nvim-lualine/lualine.nvim">nvim-lualine/lualine.nvim</a> - A blazing fast and easy to configure Neovim statusline.</li>
<li>
<a href="https://github.com/adelarsq/neoline.vim">adelarsq/neoline.vim</a> - A light statusline/tabline plugin using Lua.</li>
<li>
<a href="https://github.com/ojroques/nvim-hardline">ojroques/nvim-hardline</a> - A statusline / bufferline. It is inspired by <a href="https://github.com/vim-airline/vim-airline">vim-airline</a> but aims to be as light and simple as possible.</li>
<li>
<a href="https://github.com/beauwilliams/statusline.lua">beauwilliams/statusline.lua</a> - A zero-config minimal statusline written in Lua featuring awesome integrations and blazing speed!</li>
<li>
<a href="https://github.com/tamton-aquib/staline.nvim">tamton-aquib/staline.nvim</a> - A modern lightweight statusline in Lua. Mainly uses unicode symbols for showing info.</li>
<li>
<a href="https://github.com/freddiehaddad/feline.nvim">freddiehaddad/feline.nvim</a> - A minimal, stylish and customizable statusline written in Lua.</li>
<li>
<a href="https://github.com/windwp/windline.nvim">windwp/windline.nvim</a> - The next generation statusline. Animation statusline.</li>
<li>
<a href="https://github.com/konapun/vacuumline.nvim">konapun/vacuumline.nvim</a> - A galaxyline configuration inspired by airline.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-statusline.md">echasnovski/mini.nvim#mini.statusline</a> - Module of <code>mini.nvim</code> for minimal and fast statusline. Supports content change depending on window width.</li>
<li>
<a href="https://github.com/b0o/incline.nvim">b0o/incline.nvim</a> - Lightweight floating statuslines, intended for use with Neovim's new global statusline.</li>
<li>
<a href="https://github.com/rebelot/heirline.nvim">rebelot/heirline.nvim</a> - Heirline.nvim is a no-nonsense Neovim Statusline plugin designed around recursive inheritance to be exceptionally fast and versatile.</li>
<li>
<a href="https://github.com/yaocccc/nvim-lines.lua">yaocccc/nvim-lines.lua</a> - A fast, light, customizable Neovim statusline and tabline(buffers) plugin.</li>
<li>
<a href="https://github.com/MunifTanjim/nougat.nvim">MunifTanjim/nougat.nvim</a> - Hyperextensible Statusline / Tabline / Winbar.</li>
</ul>
<h3 id="tabline">Tabline</h3>
<ul>
<li>
<a href="https://github.com/romgrk/barbar.nvim">romgrk/barbar.nvim</a> - The Neovim tabline plugin.</li>
<li>
<a href="https://github.com/akinsho/bufferline.nvim">akinsho/bufferline.nvim</a> - A snazzy buffer line built using Lua.</li>
<li>
<a href="https://github.com/crispgm/nvim-tabline">crispgm/nvim-tabline</a> - Neovim port of tabline.vim with Lua.</li>
<li>
<a href="https://github.com/alvarosevilla95/luatab.nvim">alvarosevilla95/luatab.nvim</a> - A simple tabline written in Lua.</li>
<li>
<a href="https://github.com/johann2357/nvim-smartbufs">johann2357/nvim-smartbufs</a> - Smart buffer management.</li>
<li>
<a href="https://github.com/kdheepak/tabline.nvim">kdheepak/tabline.nvim</a> - A "buffer and tab" tabline.</li>
<li>
<a href="https://github.com/willothy/nvim-cokeline">willothy/nvim-cokeline</a> - A bufferline for people with addictive personalities.</li>
<li>
<a href="https://github.com/tomiis4/BufferTabs.nvim">tomiis4/BufferTabs.nvim</a> - Simple and Fancy tabline.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-tabline.md">echasnovski/mini.nvim#mini.tabline</a> - Module of <code>mini.nvim</code> for minimal tabline showing listed buffers in case of one tab and falling back to default otherwise.</li>
<li>
<a href="https://github.com/rafcamlet/tabline-framework.nvim">rafcamlet/tabline-framework.nvim</a> - User-friendly framework for building your dream tabline in a few lines of code.</li>
<li>
<a href="https://github.com/nanozuki/tabby.nvim">nanozuki/tabby.nvim</a> - A minimal, configurable, Neovim style tabline. Use your Neovim tabs as workspace multiplexer.</li>
<li>
<a href="https://github.com/roobert/bufferline-cycle-windowless.nvim">roobert/bufferline-cycle-windowless.nvim</a> - A bufferline extension to cycle through windowless buffers to give a more traditional tab based experience.</li>
<li>
<a href="https://github.com/mg979/tabline.nvim">mg979/tabline.nvim</a> - A comprehensive tabline for rendering and managing tabs, buffers or arglist, and featuring buffer filtering, fzf integration and session management.</li>
</ul>
<h3 id="cursorline">Cursorline</h3>
<ul>
<li>
<a href="https://github.com/yamatsum/nvim-cursorline">yamatsum/nvim-cursorline</a> - A plugin that highlights cursor words and lines.</li>
<li>
<a href="https://github.com/xiyaowong/nvim-cursorword">xiyaowong/nvim-cursorword</a> - Part of nvim-cursorline. Highlight the word under the cursor.</li>
<li>
<a href="https://github.com/sontungexpt/stcursorword">sontungexpt/stcursorword</a> - Highlight the word under the cursor (Improved and compact version of nvim-cursorline).</li>
<li>
<a href="https://github.com/RRethy/vim-illuminate">RRethy/vim-illuminate</a> - Highlight the word under the cursor. Neovim's builtin LSP is available, it can be used to highlight more intelligently.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-cursorword.md">echasnovski/mini.nvim#mini.cursorword</a> - Module of <code>mini.nvim</code> for automatic highlighting of word under cursor (displayed after customizable delay).</li>
<li>
<a href="https://github.com/mawkler/modicator.nvim">mawkler/modicator.nvim</a> - Cursor line number mode indicator. Changes the <code>CursorLineNr</code> highlight based on Vim mode.</li>
<li>
<a href="https://github.com/nyngwang/murmur.lua">nyngwang/murmur.lua</a> - Super-fast cursor word highlighting with callbacks(I call them murmurs) included.</li>
</ul>
<h2 id="startup">Startup</h2>
<ul>
<li>
<a href="https://github.com/nvimdev/dashboard-nvim">nvimdev/dashboard-nvim</a> - A minimalist dashboard, inspired by doom-emacs.</li>
<li>
<a href="https://github.com/goolord/alpha-nvim">goolord/alpha-nvim</a> - A fast and highly customizable greeter like <a href="https://github.com/mhinz/vim-startify">vim-startify</a>/dashboard-nvim.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-starter.md">echasnovski/mini.nvim#mini.starter</a> - Module of <code>mini.nvim</code> for start screen. Displayed items are fully customizable, item selection can be done using prefix query with instant visual feedback.</li>
<li>
<a href="https://sr.ht/~henriquehbr/nvim-startup.lua">henriquehbr/nvim-startup.lua</a> - Displays Neovim startup time.</li>
<li>
<a href="https://github.com/startup-nvim/startup.nvim">startup-nvim/startup.nvim</a> - The fully customizable greeter for neovim.</li>
<li>
<a href="https://github.com/willothy/veil.nvim">willothy/veil.nvim</a> - A blazingly fast, animated, and infinitely customizable startup / dashboard plugin.</li>
<li>
<a href="https://github.com/TobinPalmer/Tip.nvim">TobinPalmer/Tip.nvim</a> - Get a simple tip when you launch Neovim.</li>
</ul>
<h2 id="icon">Icon</h2>
<ul>
<li>
<a href="https://github.com/kyazdani42/nvim-web-devicons">kyazdani42/nvim-web-devicons</a> - A Lua fork of <a href="https://github.com/ryanoasis/vim-devicons">vim-devicons</a>.</li>
<li>
<a href="https://github.com/yamatsum/nvim-nonicons">yamatsum/nvim-nonicons</a> - Collection of configurations for nvim-web-devicons.</li>
<li>
<a href="https://github.com/ziontee113/icon-picker.nvim">ziontee113/icon-picker.nvim</a> - Help you pick 𝑨𝕃𝚻 Font Characters, Symbols Σ, Nerd Font Icons  &amp; Emojis ✨.</li>
</ul>
<h2 id="media">Media</h2>
<ul>
<li>
<a href="https://github.com/edluffy/hologram.nvim">edluffy/hologram.nvim</a> - A cross platform terminal image viewer. Works on macOS and Linux.</li>
<li>
<a href="https://github.com/ekickx/clipboard-image.nvim">ekickx/clipboard-image.nvim</a> - Neovim Lua plugin to paste image from clipboard.</li>
<li>
<a href="https://github.com/niuiic/cp-image.nvim">niuiic/cp-image.nvim</a> - Paste image from clipboard and insert the reference code.</li>
<li>
<a href="https://github.com/askfiy/nvim-picgo">askfiy/nvim-picgo</a> - A picgo-core-based Neovim plugin, written in Lua, that allows you to upload images to the image bed, which means you can view your images from anywhere on the internet.</li>
<li>
<a href="https://github.com/gwatcha/reaper-keys">gwatcha/reaper-keys</a> - Modal keybindings for Reaper DAW.</li>
<li>
<a href="https://github.com/madskjeldgaard/reaper-nvim">madskjeldgaard/reaper-nvim</a> - Remote control Reaper DAW from Neovim.</li>
<li>
<a href="https://github.com/davidgranstrom/scnvim">davidgranstrom/scnvim</a> - Neovim frontend for SuperCollider.</li>
<li>
<a href="https://github.com/andweeb/presence.nvim">andweeb/presence.nvim</a> - Fast and lite Discord Rich Presence plugin written in Lua.</li>
<li>
<a href="https://github.com/Chaitanyabsprip/present.nvim">Chaitanyabsrip/present.nvim</a> - A Presentation plugin written in Lua.</li>
<li>
<a href="https://github.com/krady21/compiler-explorer.nvim">krady21/compiler-explorer.nvim</a> - Async Lua plugin for interacting with <a href="https://godbolt.org/">compiler-explorer</a>.</li>
<li>
<a href="https://github.com/samodostal/image.nvim">samodostal/image.nvim</a> - Image Viewer as ASCII Art.</li>
<li>
<a href="https://github.com/adelarsq/image_preview.nvim">adelarsq/image_preview.nvim</a> - Image preview based on terminal's Image Protocol support.</li>
<li>
<a href="https://github.com/niuiic/code-shot.nvim">niuiic/code-shot.nvim</a> - Take a picture of the code.</li>
</ul>
<h2 id="note-taking">Note Taking</h2>
<ul>
<li>
<a href="https://github.com/0styx0/abbreinder.nvim">0styx0/abbreinder.nvim</a> - Abbreviation reminders (Neovim &gt;= 0.5).</li>
<li>
<a href="https://github.com/jakewvincent/mkdnflow.nvim">jakewvincent/mkdnflow.nvim</a> - Fluent markdown notebook navigation &amp; management (create links, follow links, create and manage to-do lists, reference bib files, and more).</li>
<li>
<a href="https://github.com/oberblastmeister/neuron.nvim">oberblastmeister/neuron.nvim</a> - Note taking plugin for neuron that integrates with telescope.nvim.</li>
<li>
<a href="https://github.com/jbyuki/nabla.nvim">jbyuki/nabla.nvim</a> - Take your scientific notes.</li>
<li>
<a href="https://github.com/nvim-neorg/neorg">nvim-neorg/neorg</a> - Modernity meets insane extensibility. The future of organizing your life.</li>
<li>
<a href="https://github.com/nvim-orgmode/orgmode">nvim-orgmode/orgmode</a> - Orgmode clone written in Lua (Neovim &gt;= 0.5).</li>
<li>
<a href="https://github.com/NFrid/due.nvim">NFrid/due.nvim</a> - Displays due for a date string as a virtual text.</li>
<li>
<a href="https://github.com/jbyuki/venn.nvim">jbyuki/venn.nvim</a> - Draw ASCII diagrams.</li>
<li>
<a href="https://github.com/stevearc/gkeep.nvim">stevearc/gkeep.nvim</a> - Google Keep integration.</li>
<li>
<a href="https://github.com/renerocksai/telekasten.nvim">renerocksai/telekasten.nvim</a> - A Neovim (lua) plugin for working with a text-based, markdown zettelkasten / wiki and mixing it with a journal, based on telescope.nvim.</li>
<li>
<a href="https://github.com/mickael-menu/zk-nvim">mickael-menu/zk-nvim</a> - Neovim extension for zk, a plain text note-taking assistant.</li>
<li>
<a href="https://github.com/chrsm/impulse.nvim">chrsm/impulse.nvim</a> - Read Notion.so notes.</li>
<li>
<a href="https://github.com/epwalsh/obsidian.nvim">epwalsh/obsidian.nvim</a> - Plugin for Obsidian, written in Lua.</li>
<li>
<a href="https://github.com/IlyasYOY/obs.nvim">IlyasYOY/obs.nvim</a> - Your Obsidian notes at the speed of thought.</li>
<li>
<a href="https://github.com/jghauser/papis.nvim">jghauser/papis.nvim</a> - Manage your bibliography from within your favourite editor.</li>
<li>
<a href="https://github.com/ostralyan/scribe.nvim">ostralyan/scribe.nvim</a> - Take notes, easily.</li>
<li>
<a href="https://github.com/phaazon/mind.nvim">phaazon/mind.nvim</a> - The power of trees at your fingertips.</li>
<li>
<a href="https://github.com/RutaTang/quicknote.nvim">RutaTang/quicknote.nvim</a> - Quickly take notes, in-place.</li>
<li>
<a href="https://github.com/serenevoid/kiwi.nvim">serenevoid/kiwi.nvim</a> - A stripped down VimWiki with necessary features.</li>
<li>
<a href="https://github.com/ada0l/obsidian">ada0l/obsidian/</a> - Base Obsidian functionality.</li>
<li>
<a href="https://github.com/gsuuon/note.nvim">gsuuon/note.nvim</a> - Daily tasks with deep-linking and project spaces.</li>
</ul>
<h2 id="utility">Utility</h2>
<ul>
<li>
<a href="https://github.com/gaborvecsei/usage-tracker.nvim">gaborvecsei/usage-tracker.nvim</a> - Track your Neovim usage and visualize statistics easily.</li>
<li>
<a href="https://github.com/jghauser/mkdir.nvim">jghauser/mkdir.nvim</a> - Automatically create missing directories when saving files.</li>
<li>
<a href="https://github.com/matbme/JABS.nvim">matbme/JABS.nvim</a> - Pretty and minimal buffer switcher window.</li>
<li>
<a href="https://github.com/j-morano/buffer_manager.nvim">j-morano/buffer_manager.nvim</a> - Add one or more buffers, reorder them, save them inside a file or just delete them very easily from a small floating window.</li>
<li>
<a href="https://github.com/clojure-vim/jazz.nvim">clojure-vim/jazz.nvim</a> - Acid + Impromptu = Jazz.</li>
<li>
<a href="https://github.com/sudormrfbin/cheatsheet.nvim">sudormrfbin/cheatsheet.nvim</a> - Searchable cheatsheet.</li>
<li>
<a href="https://github.com/code-biscuits/nvim-biscuits">code-biscuits/nvim-biscuits</a> - A Neovim port of Assorted Biscuits. Ends up with more supported languages too.</li>
<li>
<a href="https://github.com/kazhala/close-buffers.nvim">kazhala/close-buffers.nvim</a> - Delete multiple Vim buffers based on different conditions.</li>
<li>
<a href="https://github.com/rktjmp/paperplanes.nvim">rktjmp/paperplanes.nvim</a> - Post selections or buffers to online paste bins.</li>
<li>
<a href="https://github.com/rcarriga/nvim-notify">rcarriga/nvim-notify</a> - A fancy, configurable, notification manager.</li>
<li>
<a href="https://github.com/folke/noice.nvim">folke/noice.nvim</a> - Highly experimental plugin that completely replaces the UI for messages, cmdline and the popupmenu.</li>
<li>
<a href="https://github.com/sQVe/bufignore.nvim">sQVe/bufignore.nvim</a> - Unlist hidden buffers matching specified ignore sources.</li>
<li>
<a href="https://github.com/saifulapm/chartoggle.nvim">saifulapm/chartoggle.nvim</a> - Toggle any character at end of line.</li>
<li>
<a href="https://github.com/stevearc/dressing.nvim">stevearc/dressing.nvim</a> - Improve the built-in <code>vim.ui</code> interfaces with telescope, fzf, etc.</li>
<li>
<a href="https://github.com/gaborvecsei/cryptoprice.nvim">gaborvecsei/cryptoprice.nvim</a> - Check the price of the defined cryptocurrencies.</li>
<li>
<a href="https://github.com/jghauser/fold-cycle.nvim">jghauser/fold-cycle.nvim</a> - Cycle folds open or closed.</li>
<li>
<a href="https://github.com/rgroli/other.nvim">rgroli/other.nvim</a> - Open alternative files for the current buffer.</li>
<li>
<a href="https://github.com/toppair/reach.nvim">toppair/reach.nvim</a> - Buffer, mark, tabpage switcher.</li>
<li>
<a href="https://github.com/axieax/urlview.nvim">axieax/urlview.nvim</a> - Browse all URLs in the current buffer.</li>
<li>
<a href="https://github.com/nkakouros-original/numbers.nvim">nkakouros-original/numbers.nvim</a> - Toggle relativenumber whenever it makes sense.</li>
<li>
<a href="https://github.com/ghillb/cybu.nvim">ghillb/cybu.nvim</a> - Displays a notification window with context when cycling buffers.</li>
<li>
<a href="https://github.com/sontungexpt/url-open">sontungexpt/url-open</a> - Open URLs under the cursor and create highlight effects for them.</li>
<li>
<a href="https://github.com/crusj/bookmarks.nvim">crusj/bookmarks.nvim</a> - Remember file locations and sort by time and frequency.</li>
<li>
<a href="https://github.com/xiyaowong/virtcolumn.nvim">xiyaowong/virtcolumn.nvim</a> - Display a line as colorcolumn.</li>
<li>
<a href="https://github.com/m-demare/attempt.nvim">m-demare/attempt.nvim</a> - Manage and run temporary buffers.</li>
<li>
<a href="https://github.com/kevinhwang91/nvim-ufo">kevinhwang91/nvim-ufo</a> - Ultra fold with modern looking and performance boosting.</li>
<li>
<a href="https://github.com/xiyaowong/link-visitor.nvim">xiyaowong/link-visitor.nvim</a> - Let me help you open the links.</li>
<li>
<a href="https://github.com/sitiom/nvim-numbertoggle">sitiom/nvim-numbertoggle</a> - Neovim plugin to automatically toggle between relative and absolute line numbers.</li>
<li>
<a href="https://github.com/anuvyklack/fold-preview.nvim">anuvyklack/fold-preview</a> - Preview closed fold without opening it.</li>
<li>
<a href="https://github.com/nguyenvukhang/nvim-toggler">nguyenvukhang/nvim-toggler</a> - Invert text, such as toggling between <code>true</code> and <code>false</code>.</li>
<li>
<a href="https://github.com/CosmicNvim/cosmic-ui">CosmicNvim/cosmic-ui</a> - Cosmic-UI is a simple wrapper around specific Vim functionality. Built in order to provide a quick and easy way to create a Cosmic UI experience with Neovim!</li>
<li>
<a href="https://github.com/AckslD/messages.nvim">AckslD/messages.nvim</a> - Capture and show any messages in a customisable (floating) buffer.</li>
<li>
<a href="https://github.com/jbyuki/instant.nvim">jbyuki/instant.nvim</a> - A collaborative editing plugin written in Lua with no dependencies.</li>
<li>
<a href="https://github.com/numToStr/BufOnly.nvim">numToStr/BufOnly.nvim</a> - Lua/Neovim port of BufOnly.vim with some changes.</li>
<li>
<a href="https://github.com/zbirenbaum/neodim">zbirenbaum/neodim</a> - Dimming the highlights of unused functions, variables, parameters, and more.</li>
<li>
<a href="https://github.com/bfredl/nvim-miniyank">bfredl/nvim-miniyank</a> - The killring-alike plugin with no default mappings.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-genghis">chrisgrieser/nvim-genghis</a> - Convenience file operations, written in Lua.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-recorder">chrisgrieser/nvim-recorder</a> - Simplifying and improving how you interact with macros.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-animate.md">echasnovski/mini.nvim#mini.animate</a> - Module of <code>mini.nvim</code> to add out of the box animations for common built-in actions (cursor movement, scroll, resize, window open/close).</li>
<li>
<a href="https://github.com/figsoda/nix-develop.nvim">figsoda/nix-develop.nvim</a> - Run <code>nix develop</code> without restarting Neovim.</li>
<li>
<a href="https://github.com/yaocccc/nvim-foldsign">yaocccc/nvim-foldsign</a> - Display folds on sign column.</li>
<li>
<a href="https://github.com/tenxsoydev/nx.nvim">tenxsoydev/nx.nvim</a> - Neovim API utility wrapper for more convenience with Lua keymaps, highlights, autocommands and options.</li>
<li>
<a href="https://github.com/zdcthomas/yop.nvim">zdcthomas/yop.nvim</a> - Easily create your own operators (like <code>d</code> and <code>y</code>).</li>
<li>
<a href="https://github.com/cpea2506/relative-toggle.nvim">cpea2506/relative-toggle.nvim</a> - Toggles smoothly between number and relative numbers, supporting various number combinations, highly customizable.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-early-retirement">nvim-early-retirement</a> - Send buffers into early retirement by automatically closing them after x minutes of inactivity.</li>
<li>
<a href="https://github.com/axkirillov/hbac.nvim">hbac.nvim</a> - Automatically close buffers you are not working on.</li>
<li>
<a href="https://github.com/ecthelionvi/NeoComposer.nvim">ecthelionvi/NeoComposer.nvim</a> - Simplify macro management, enhance productivity, and create harmonious workflows.</li>
<li>
<a href="https://github.com/LukasPietzschmann/telescope-tabs">LukasPietzschmann/telescope-tabs</a> - Quickly navigate between tabs using telescope.</li>
<li>
<a href="https://github.com/RutaTang/compter.nvim">RutaTang/compter.nvim</a> - Power and extend the ability of <code>&lt;C-a&gt;</code> and <code>&lt;C-x&gt;</code> with customized patterns.</li>
<li>
<a href="https://git.sr.ht/~reggie/licenses.nvim">reggie/licenses.nvim</a> - Insert and write license headers and/or files.</li>
<li>
<a href="https://github.com/yagiziskirik/AirSupport.nvim">yagiziskirik/AirSupport.nvim</a> - Searchable reminder window for your custom shortcuts and commands.</li>
<li>
<a href="https://github.com/aPeoplesCalendar/apc.nvim">aPeoplesCalendar/apc.nvim</a> - "On this day" style calendar, which provides information about worldwide history of working class movements and liberation struggles.</li>
<li>
<a href="https://github.com/subnut/nvim-ghost.nvim">subnut/nvim-ghost.nvim</a> - GhostText support with zero dependencies.</li>
<li>
<a href="https://github.com/malbertzard/inline-fold.nvim">malbertzard/inline-fold.nvim</a> - Hide certain elements inline like long CSS classes or <code>href</code> content.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-origami">chrisgrieser/nvim-origami</a> - Fold with relentless elegance.</li>
<li>
<a href="https://github.com/GCBallesteros/NotebookNavigator.nvim">GCBallesteros/NotebookNavigator.nvim</a> - Navigate and execute code cells.</li>
<li>
<a href="https://github.com/LintaoAmons/scratch.nvim">LintaoAmons/scratch.nvim</a> - Create and manage scratch files.</li>
<li>
<a href="https://github.com/luckasRanarison/nvim-devdocs">luckasRanarison/nvim-devdocs</a> - Preview devdocs.io documentations directly in Markdown format.</li>
<li>
<a href="https://github.com/VidocqH/data-viewer.nvim">VidocqH/data-viewer.nvim</a> - Provide a simple table view to inspect data files such as <code>csv</code>, <code>tsv</code>.</li>
<li>
<a href="https://github.com/JMarkin/gentags.lua">JMarkin/gentags.lua</a> - Auto generate tag files by ctags.</li>
<li>
<a href="https://github.com/yutkat/confirm-quit.nvim">yutkat/confirm-quit.nvim</a> - Confirm before quitting Neovim.</li>
<li>
<a href="https://github.com/bgaillard/readonly.nvim">bgaillard/readonly.nvim</a> - Secure edition of files containing sensible / secret information, passwords, API keys, SSH keys, etc.</li>
<li>
<a href="https://github.com/GCBallesteros/jupytext.nvim">GCBallesteros/jupytext.nvim</a> - Edit jupyter notebooks without leaving Neovim.</li>
</ul>
<h2 id="terminal-integration">Terminal Integration</h2>
<ul>
<li>
<a href="https://github.com/LoricAndre/OneTerm.nvim">LoricAndre/OneTerm.nvim</a> - Plugin framework for running commands in the terminal.</li>
<li>
<a href="https://github.com/nikvdp/neomux">nikvdp/neomux</a> - Control Neovim from shells running inside Neovim.</li>
<li>
<a href="https://github.com/willothy/flatten.nvim">willothy/flatten.nvim</a> - Open files from terminal buffers in your current Neovim instance instead of launching a nested instance.</li>
<li>
<a href="https://github.com/willothy/wezterm.nvim">willothy/wezterm.nvim</a> - Functions for interacting with Wezterm.</li>
<li>
<a href="https://github.com/akinsho/nvim-toggleterm.lua">akinsho/nvim-toggleterm.lua</a> - A Neovim Lua plugin to help easily manage multiple terminal windows.</li>
<li>
<a href="https://github.com/norcalli/nvim-terminal.lua">norcalli/nvim-terminal.lua</a> - A high performance filetype mode which leverages conceal and highlights your buffer with the correct color codes.</li>
<li>
<a href="https://github.com/numToStr/FTerm.nvim">numToStr/FTerm.nvim</a> - No nonsense floating terminal written in Lua.</li>
<li>
<a href="https://github.com/pianocomposer321/consolation.nvim">pianocomposer321/consolation.nvim</a> - A general-purpose terminal wrapper and management plugin, written in Lua.</li>
<li>
<a href="https://github.com/jghauser/kitty-runner.nvim">jghauser/kitty-runner.nvim</a> - Poor man's REPL. Easily send buffer lines and commands to a kitty terminal.</li>
<li>
<a href="https://github.com/jlesquembre/nterm.nvim">jlesquembre/nterm.nvim</a> - Interact with the terminal, with notifications.</li>
<li>
<a href="https://github.com/s1n7ax/nvim-terminal">s1n7ax/nvim-terminal</a> - A simple &amp; easy to use multi-terminal plugin.</li>
<li>
<a href="https://github.com/m00qek/baleia.nvim">m00qek/baleia.nvim</a> - Colorize text with ANSI escape sequences (8, 16, 256 or TrueColor).</li>
<li>
<a href="https://github.com/samjwill/nvim-unception">samjwill/nvim-unception</a> - Automatic unnesting of Neovim sessions started from terminal buffers.</li>
<li>
<a href="https://github.com/nyngwang/NeoTerm.lua">nyngwang/NeoTerm.lua</a> - Attach a terminal for each <strong>buffer</strong>, now with stable toggle and astonishing cursor restoring.</li>
<li>
<a href="https://github.com/idanarye/nvim-channelot">idanarye/nvim-channelot</a> - Operate Neovim jobs from Lua coroutines.</li>
<li>
<a href="https://github.com/chomosuke/term-edit.nvim">chomosuke/term-edit.nvim</a> - Allowing you to edit your command in the terminal just like any other buffer.</li>
<li>
<a href="https://github.com/mikesmithgh/kitty-scrollback.nvim">mikesmithgh/kitty-scrollback.nvim</a> - Open your Kitty scrollback buffer. Ameowzing.</li>
<li>
<a href="https://github.com/niuiic/terminal.nvim">niuiic/terminal.nvim</a> - Manage terminal as buffer, multiple terminals support.</li>
</ul>
<h2 id="debugging">Debugging</h2>
<ul>
<li>
<a href="https://github.com/mfussenegger/nvim-dap">mfussenegger/nvim-dap</a> - Debug Adapter Protocol client implementation.</li>
<li>
<a href="https://github.com/sakhnik/nvim-gdb">sakhnik/nvim-gdb</a> - Thin wrapper for GDB, LLDB, PDB/PDB++ and BashDB.</li>
<li>
<a href="https://github.com/rcarriga/nvim-dap-ui">rcarriga/nvim-dap-ui</a> - A UI for nvim-dap.</li>
<li>
<a href="https://github.com/Pocco81/DAPInstall.nvim">Pocco81/DAPInstall.nvim</a> - Manage several debuggers for nvim-dap.</li>
<li>
<a href="https://github.com/Weissle/persistent-breakpoints.nvim">Weissle/persistent-breakpoints.nvim</a> - Persistent breakpoints for nvim-dap.</li>
<li>
<a href="https://github.com/ofirgall/goto-breakpoints.nvim">ofirgall/goto-breakpoints.nvim</a> - Cycle between breakpoints for nvim-dap.</li>
<li>
<a href="https://github.com/andrewferrier/debugprint.nvim">andrewferrier/debugprint.nvim</a> - Debugging the print() way.</li>
<li>
<a href="https://github.com/t-troebst/perfanno.nvim">t-troebst/perfanno.nvim</a> - Annotate your code with callgraph profiling data. Native support for perf, flamegraph and the LuaJit profiler.</li>
<li>
<a href="https://github.com/niuiic/dap-utils.nvim">niuiic/dap-utils</a> - Utilities to provide a better experience for using nvim-dap.</li>
<li>
<a href="https://github.com/theHamsta/nvim-dap-virtual-text">theHamsta/nvim-dap-virtual-text</a> - Virtual text support for nvim-dap.</li>
</ul>
<h3 id="quickfix">Quickfix</h3>
<ul>
<li>
<a href="https://github.com/kevinhwang91/nvim-bqf">kevinhwang91/nvim-bqf</a> - The goal of nvim-bqf is to make Neovim's quickfix window better.</li>
<li>
<a href="https://github.com/yorickpeterse/nvim-pqf">yorickpeterse/nvim-pqf</a> - Prettier quickfix/location list windows.</li>
<li>
<a href="https://github.com/nyngwang/NeoWell.lua">nyngwang/NeoWell.lua</a> - Sometimes you will want to fix some lines later. Store lines into qf with some note so you know what to do when you really want to fix it.</li>
<li>
<a href="https://github.com/ashfinal/qfview.nvim">ashfinal/qfview.nvim</a> - Pretty quickfix/location view with consistent path-shorten and folding.</li>
</ul>
<h2 id="deployment">Deployment</h2>
<ul>
<li>
<a href="https://github.com/coffebar/transfer.nvim">coffebar/transfer.nvim</a> - Sync and diff with remote server using rsync and OpenSSH.</li>
<li>
<a href="https://github.com/OscarCreator/rsync.nvim">OscarCreator/rsync.nvim</a> - Automatically sync up/down project to a remote with rsync.</li>
</ul>
<h2 id="test">Test</h2>
<ul>
<li>
<a href="https://github.com/David-Kunz/jester">David-Kunz/jester</a> - Easily run and debug Jest tests.</li>
<li>
<a href="https://github.com/klen/nvim-test">klen/nvim-test</a> - A Neovim wrapper for running tests.</li>
<li>
<a href="https://github.com/nvim-neotest/neotest">nvim-neotest/neotest</a> - An extensible framework for interacting with tests within Neovim.</li>
<li>
<a href="https://github.com/andythigpen/nvim-coverage">andythigpen/nvim-coverage</a> - Displays coverage information in the sign column.</li>
</ul>
<h2 id="code-runner">Code Runner</h2>
<ul>
<li>
<a href="https://github.com/michaelb/sniprun">michaelb/sniprun</a> - Run parts of code of any language directly from Neovim.</li>
<li>
<a href="https://github.com/pianocomposer321/yabs.nvim">pianocomposer321/yabs.nvim</a> - Yet Another Build System, written in Lua.</li>
<li>
<a href="https://github.com/CRAG666/code_runner.nvim">CRAG666/code_runner.nvim</a> - The best code runner you could have, with super powers.</li>
<li>
<a href="https://github.com/is0n/jaq-nvim">is0n/jaq-nvim</a> - Just Another Quickrun Plugin in Lua.</li>
<li>
<a href="https://github.com/jedrzejboczar/toggletasks.nvim">jedrzejboczar/toggletasks.nvim</a> - Task runner with JSON/YAML configs, using toggleterm.nvim and telescope.nvim.</li>
<li>
<a href="https://github.com/EthanJWright/vs-tasks.nvim">EthanJWright/vs-tasks.nvim</a> - Telescope picker for VSCode style tasks.</li>
<li>
<a href="https://github.com/stevearc/overseer.nvim">stevearc/overseer.nvim</a> - A task runner and job management plugin.</li>
<li>
<a href="https://github.com/smzm/hydrovim">smzm/hydrovim</a> - Run python code inside Neovim.</li>
<li>
<a href="https://github.com/desdic/greyjoy.nvim">desdic/greyjoy.nvim</a> - A modular task runner for Makefiles, vscode tasks, kitchen etc.</li>
<li>
<a href="https://github.com/Shatur/neovim-tasks">Shatur/neovim-tasks</a> - A stateful task manager focused on integration with build systems.</li>
<li>
<a href="https://github.com/milanglacier/yarepl.nvim">milanglacier/yarepl.nvim</a> - Yet Another REPL, flexible, supporting multiple paradigms to interact with REPLs, and native dot repeat without other dependencies.</li>
<li>
<a href="https://github.com/hkupty/iron.nvim">hkupty/iron.nvim</a> - Interactive REPLs of over 30 languages embedded.</li>
<li>
<a href="https://github.com/Civitasv/cmake-tools.nvim">Civitasv/cmake-tools.nvim</a> - CMake integration.</li>
<li>
<a href="https://github.com/idanarye/nvim-moonicipal">idanarye/nvim-moonicipal</a> - Task runner with focus on rapidly changing personal tasks.</li>
<li>
<a href="https://github.com/MarcHamamji/runner.nvim">MarcHamamji/runner.nvim</a> - A customizable Lua code runner.</li>
<li>
<a href="https://github.com/google/executor.nvim">google/executor.nvim</a> - Allows you to run command line tasks in the background and be notified of results.</li>
<li>
<a href="https://github.com/Zeioth/compiler.nvim">Zeioth/compiler.nvim</a> - Compiler for building and running your code without having to configure anything.</li>
<li>
<a href="https://github.com/jaytyrrell13/static.nvim">jaytyrrell13/static.nvim</a> - Run static site generator commands.</li>
<li>
<a href="https://github.com/dasupradyumna/launch.nvim">dasupradyumna/launch.nvim</a> - A simple and quick task launcher which allows dynamically configuring tasks on the fly, with optional support for debugging.</li>
<li>
<a href="https://github.com/benlubas/molten-nvim">benlubas/molten-nvim</a> - Enables running code chunks via the jupyter kernel. Output (including image output) is rendered in a floating window below the code.</li>
<li>
<a href="https://github.com/bfredl/nvim-ipy">bfredl/nvim-ipy</a> - Make interfacing with IPython/Jupyter easier.</li>
</ul>
<h2 id="neovim-lua-development">Neovim Lua Development</h2>
<ul>
<li>
<a href="https://github.com/folke/neodev.nvim">folke/neodev.nvim</a> - Dev setup for init.lua and plugin development with full signature help, docs and completion for the Neovim Lua API.</li>
<li>
<a href="https://github.com/nvim-neorocks/luarocks-tag-release">nvim-neorocks/luarocks-tag-release</a> - A GitHub action that publishes your Neovim plugins to LuaRocks.</li>
<li>
<a href="https://github.com/svermeulen/vimpeccable">svermeulen/vimpeccable</a> - Commands to help write your .vimrc in Lua or any Lua based language.</li>
<li>
<a href="https://github.com/nanotee/nvim-lua-guide">nanotee/nvim-lua-guide</a> - A guide to using Lua in Neovim.</li>
<li>
<a href="https://github.com/rafcamlet/nvim-luapad">rafcamlet/nvim-luapad</a> - Interactive real time Neovim scratchpad for embedded Lua engine - Type and watch!.</li>
<li>
<a href="https://github.com/nvim-lua/plenary.nvim">nvim-lua/plenary.nvim</a> - Plenary: full; complete; entire; absolute; unqualified. All the Lua functions I don't want to write twice.</li>
<li>
<a href="https://github.com/nvim-lua/popup.nvim">nvim-lua/popup.nvim</a> - An implementation of the Popup API from Vim.</li>
<li>
<a href="https://github.com/tjdevries/vlog.nvim">tjdevries/vlog.nvim</a> - Single file, no dependency, easy copy &amp; paste log file to add to your Neovim Lua plugins.</li>
<li>
<a href="https://github.com/bfredl/nvim-luadev">bfredl/nvim-luadev</a> - REPL/debug console Lua plugins. The <code>:Luadev</code> command will open an scratch window which will show output from executing Lua code.</li>
<li>
<a href="https://github.com/jbyuki/one-small-step-for-vimkind">jbyuki/one-small-step-for-vimkind</a> - An adapter for the Neovim Lua language. It allows you to debug any Lua code running in a Neovim instance (A Lua plugin that can debug Neovim Lua plugins).</li>
<li>
<a href="https://github.com/kkharji/sqlite.lua">kkharji/sqlite.lua</a> - SQLite/LuaJIT binding for Lua and Neovim.</li>
<li>
<a href="https://github.com/MunifTanjim/nui.nvim">MunifTanjim/nui.nvim</a> - UI Component Library.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-doc.md">echasnovski/mini.nvim#mini.doc</a> - Module of <code>mini.nvim</code> for generation of help files from EmmyLua-like annotations. Allows flexible customization of output via hook functions.</li>
<li>
<a href="https://github.com/nanotee/luv-vimdocs">nanotee/luv-vimdocs</a> - The luv docs in vimdoc format.</li>
<li>
<a href="https://github.com/milisims/nvim-luaref">milisims/nvim-luaref</a> - A reference for builtin Lua functions.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-test.md">echasnovski/mini.nvim#mini.test</a> - Module of <code>mini.nvim</code> with framework for writing extensive Neovim plugin tests. Supports hierarchical tests, hooks, parametrization, filtering, screen tests, "busted-style" emulation, customizable reporters, and more.</li>
<li>
<a href="https://github.com/miversen33/import.nvim">miversen33/import.nvim</a> - A safe require replacement with niceties.</li>
<li>
<a href="https://github.com/ray-x/guihua.lua">ray-x/guihua.lua</a> - A Lua UI library. Includes a fzy search bar, list view and tree view modules.</li>
<li>
<a href="https://github.com/anuvyklack/animation.nvim">anuvyklack/animation.nvim</a> - Create animations.</li>
<li>
<a href="https://github.com/NFrid/treesitter-utils">NFrid/treesitter-utils</a> - Some useful Treesitter methods.</li>
<li>
<a href="https://github.com/svermeulen/nvim-lusc">nvim-lusc</a> - Adds support for Structured Async/Concurrency in Lua.</li>
</ul>
<h2 id="fennel">Fennel</h2>
<ul>
<li>
<a href="https://github.com/Olical/aniseed">Olical/aniseed</a> - Configure and extend Neovim with Fennel (Lisp to Lua).</li>
<li>
<a href="https://github.com/Olical/nfnl">Olical/nfnl</a> - Streamlined successor to Aniseed, compiling Fennel to Lua on file write.</li>
<li>
<a href="https://github.com/Olical/conjure">Olical/conjure</a> - Interactive evaluation (Clojure, Fennel, Janet, Racket, Hy, MIT Scheme, Guile).</li>
<li>
<a href="https://github.com/rktjmp/hotpot.nvim">rktjmp/hotpot.nvim</a> - Seamless, transparent Fennel inside Neovim.</li>
<li>
<a href="https://github.com/udayvir-singh/tangerine.nvim">udayvir-singh/tangerine.nvim</a> - Sweet :tangerine: Fennel integration, aims to be as fast as possible.</li>
<li>
<a href="https://github.com/udayvir-singh/hibiscus.nvim">udayvir-singh/hibiscus.nvim</a> - Flavored :hibiscus: Fennel macro library.</li>
</ul>
<h2 id="dependency-management">Dependency Management</h2>
<ul>
<li>
<a href="https://github.com/vuki656/package-info.nvim">vuki656/package-info.nvim</a> - Display latest package version as virtual text in package.json.</li>
<li>
<a href="https://github.com/Saecki/crates.nvim">Saecki/crates.nvim</a> - Rust dependency management for <code>Cargo.toml</code>.</li>
<li>
<a href="https://github.com/piersolenski/telescope-import.nvim">piersolenski/telescope-import.nvim</a> - Import modules faster based on what you've already imported in your project.</li>
</ul>
<h2 id="git">Git</h2>
<ul>
<li>
<a href="https://github.com/f-person/git-blame.nvim">f-person/git-blame.nvim</a> - Show git blame info.</li>
<li>
<a href="https://github.com/lewis6991/gitsigns.nvim">lewis6991/gitsigns.nvim</a> - Git integration: signs, hunk actions, blame, etc.</li>
<li>
<a href="https://github.com/NeogitOrg/neogit">NeogitOrg/neogit</a> - A Magit clone that may change some things to fit the Vim philosophy.</li>
<li>
<a href="https://github.com/tveskag/nvim-blame-line">tveskag/nvim-blame-line</a> - A small plugin that uses neovims virtual text to print git blame info at the end of the current line.</li>
<li>
<a href="https://github.com/ruifm/gitlinker.nvim">ruifm/gitlinker.nvim</a> - Generate shareable file permalinks for several git hosts. Inspired by tpope/vim-fugitive's :GBrowse.</li>
<li>
<a href="https://github.com/linrongbin16/gitlinker.nvim">linrongbin16/gitlinker.nvim</a> - Maintained fork of "ruifm's gitlinker", refactored with bug fixes, alias-host, <code>/blame</code> url support and other enhancements.</li>
<li>
<a href="https://github.com/tanvirtin/vgit.nvim">tanvirtin/vgit.nvim</a> - Visual Git Plugin to enhance your git experience.</li>
<li>
<a href="https://github.com/sindrets/diffview.nvim">sindrets/diffview.nvim</a> - Single tabpage interface for easily cycling through diffs for all modified files for any git rev.</li>
<li>
<a href="https://github.com/kdheepak/lazygit.nvim">kdheepak/lazygit.nvim</a> - Plugin for calling lazygit.</li>
<li>
<a href="https://github.com/AckslD/nvim-gfold.lua">AckslD/nvim-gfold.lua</a> - Plugin using <a href="https://github.com/nickgerace/gfold">gfold</a> to switch repo and have statusline component.</li>
<li>
<a href="https://github.com/akinsho/git-conflict.nvim">akinsho/git-conflict.nvim</a> - A plugin to visualise and resolve merge conflicts.</li>
<li>
<a href="https://github.com/aaronhallaert/advanced-git-search.nvim">aaronhallaert/advanced-git-search.nvim</a> - Search your git history by commit content, message and author with Telescope.</li>
<li>
<a href="https://github.com/9seconds/repolink.nvim">9seconds/repolink.nvim</a> - Generate shareable HTTP permalinks for various Git web frontends.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-tinygit">chrisgrieser/nvim-tinygit</a> - Lightweight and nimble git client.</li>
<li>
<a href="https://github.com/niuiic/git-log.nvim">niuiic/git-log.nvim</a> - Check git log of the selected code.</li>
</ul>
<h3 id="github">GitHub</h3>
<ul>
<li>
<a href="https://github.com/pwntester/octo.nvim">pwntester/octo.nvim</a> - Work with GitHub issues and PRs from Neovim. Just edit the issue description.</li>
<li>
<a href="https://github.com/pwntester/codeql.nvim">pwntester/codeql.nvim</a> - Neovim plugin to help writing and testing CodeQL queries.</li>
<li>
<a href="https://github.com/ldelossa/gh.nvim">ldelossa/gh.nvim</a> - A fully featured GitHub integration for performing code reviews.</li>
<li>
<a href="https://github.com/topaxi/gh-actions.nvim">topaxi/gh-actions.nvim</a> - View and dispatch GitHub Actions workflow runs.</li>
</ul>
<h2 id="motion">Motion</h2>
<ul>
<li>
<a href="https://github.com/smoka7/hop.nvim">smoka7/hop.nvim</a> - Hop is an EasyMotion-like plugin allowing you to jump anywhere in a document with as few keystrokes as possible.</li>
<li>
<a href="https://github.com/ggandor/lightspeed.nvim">ggandor/lightspeed.nvim</a> - A Sneak-like plugin offering unparalleled navigation speed via ahead-of-time displayed labels, that eliminate the pause between entering the search pattern and selecting the target.</li>
<li>
<a href="https://github.com/ggandor/leap.nvim">ggandor/leap.nvim</a> - A refined successor of Lightspeed, aiming to establish a widely accepted standard interface extension for moving around in Vim-like editors.</li>
<li>
<a href="https://github.com/ggandor/flit.nvim">ggandor/flit.nvim</a> - Enhanced f/t motions for Leap.</li>
<li>
<a href="https://github.com/ggandor/leap-spooky.nvim">ggandor/leap-spooky.nvim</a> - Spooky (Leap) actions at a distance.</li>
<li>
<a href="https://github.com/folke/flash.nvim">folke/flash.nvim</a> - Navigate your code with search labels, enhanced character motions and Treesitter integration.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-jump.md">echasnovski/mini.nvim#mini.jump</a> - Module of <code>mini.nvim</code> for smarter jumping to a single character.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-jump2d.md">echasnovski/mini.nvim#mini.jump2d</a> - Module of <code>mini.nvim</code> for smarter jumping within visible lines via iterative label filtering. Supports custom jump targets (spots), labels, hooks, allowed windows and lines, and more.</li>
<li>
<a href="https://github.com/rlane/pounce.nvim">rlane/pounce.nvim</a> - An EasyMotion-like plugin for quick cursor movement using fuzzy search.</li>
<li>
<a href="https://github.com/xiaoshihou514/squirrel.nvim">xiaoshihou514/squirrel.nvim</a> - Quickly jump between tree-sitter nodes.</li>
<li>
<a href="https://github.com/gen740/SmoothCursor.nvim">gen740/SmoothCursor.nvim</a> - Add fancy sub-cursor to signcolumn to show your scroll or jump direction.</li>
<li>
<a href="https://github.com/edluffy/specs.nvim">edluffy/specs.nvim</a> - A fast and lightweight Neovim Lua plugin to keep an eye on where your cursor has jumped.</li>
<li>
<a href="https://github.com/abecodes/tabout.nvim">abecodes/tabout.nvim</a> - Jump out of brackets, quotes, objects, etc.</li>
<li>
<a href="https://github.com/roobert/tabtree.nvim">roobert/tabtree.nvim</a> - Jump between significant code elements, such as brackets, quotes, etc.</li>
<li>
<a href="https://github.com/woosaaahh/sj.nvim">woosaaahh/sj.nvim</a> - Search based navigation combined with quick jump features.</li>
<li>
<a href="https://github.com/Weissle/easy-action">Weissle/easy-action</a> - Easily perform an action on where you can see.</li>
<li>
<a href="https://github.com/cbochs/portal.nvim">cbochs/portal.nvim</a> - Build upon and enhance existing jumplist motions (i.e. <code>&lt;c-i&gt;</code> and <code>&lt;c-o&gt;</code>).</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-bracketed.md">echasnovski/mini.nvim#mini.bracketed</a> - Module of <code>mini.nvim</code> to go forward/backward with square brackets.</li>
<li>
<a href="https://github.com/liangxianzhe/nap.nvim">liangxianzhe/nap.nvim</a> - Jump between next/previous buffer, tab, diagnostic, etc, with a single key.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-spider">chrisgrieser/nvim-spider</a> - Use the w, e, b motions like a spider. Considers camelCase and skips insignificant punctuation.</li>
<li>
<a href="https://github.com/gsuuon/tshjkl.nvim">gsuuon/tshjkl.nvim</a> - Toggle to navigate and select tree-sitter nodes with hjkl.</li>
</ul>
<h3>Treesitter Based</h3>
<ul>
<li>
<a href="https://github.com/mfussenegger/nvim-ts-hint-textobject">mfussenegger/nvim-ts-hint-textobject</a> - Region selection with hints on the AST nodes of a document powered by Treesitter.</li>
<li>
<a href="https://github.com/ziontee113/syntax-tree-surfer">ziontee113/syntax-tree-surfer</a> - Navigate and swap Treesitter's AST Nodes. Step into, step out, step over, step back.</li>
<li>
<a href="https://github.com/drybalka/tree-climber.nvim">drybalka/tree-climber.nvim</a> - Easy navigation around the Treesitter's tree that works in multi-language files and in normal mode.</li>
</ul>
<h2 id="keybinding">Keybinding</h2>
<ul>
<li>
<a href="https://github.com/folke/which-key.nvim">folke/which-key.nvim</a> - Neovim plugin that shows a popup with possible keybindings of the command you started typing.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-clue.md">echasnovski/mini.nvim#mini.clue</a> - Module of <code>mini.nvim</code> to show next key clues. Has opt-in triggers, shows next key information after customizable delay, allows hydra-like submodes, and more.</li>
<li>
<a href="https://github.com/mrjones2014/legendary.nvim">mrjones2014/legendary.nvim</a> - Define your keymaps, commands, and autocommands as simple Lua tables, and create a legend for them at the same time (like VS Code's Command Palette), integrates with <code>which-key.nvim</code>.</li>
<li>
<a href="https://github.com/Iron-E/nvim-cartographer">Iron-E/nvim-cartographer</a> - a more convenient <code>:map</code>ping syntax for Lua environments.</li>
<li>
<a href="https://github.com/b0o/mapx.nvim">b0o/mapx.nvim</a> - A simpler key mapping API that mimics Neovim's <code>:map</code>-family of commands. Integrates with which-key.nvim.</li>
<li>
<a href="https://github.com/LionC/nest.nvim">LionC/nest.nvim</a> - Lua utility to map keys concisely using cascading trees. Also allows binding Lua functions to keys.</li>
<li>
<a href="https://github.com/LinArcX/telescope-command-palette.nvim">LinArcX/telescope-command-palette.nvim</a> - Lua plugin to create key-bindings and watch them with telescope.</li>
<li>
<a href="https://github.com/slugbyte/unruly-worker">slugbyte/unruly-worker</a> - A ridiculously fun alternative keymap for the workman keyboard layout with Neovim features like LSP support, built and configured with Lua.</li>
<li>
<a href="https://github.com/FeiyouG/command_center.nvim">FeiyouG/command_center.nvim</a> - Create and manage keybindings and commands in a more organized manner and search them quickly through Telescope.</li>
<li>
<a href="https://github.com/anuvyklack/hydra.nvim">anuvyklack/hydra.nvim</a> - Create custom submodes and menus. Port of Emacs Hydra.</li>
<li>
<a href="https://github.com/anuvyklack/keymap-amend.nvim">anuvyklack/keymap-amend.nvim</a> - Amend the existing keymap.</li>
<li>
<a href="https://github.com/max397574/better-escape.nvim">max397574/better-escape.nvim</a> - Create shortcuts to escape insert mode without getting delay.</li>
<li>
<a href="https://github.com/Nexmean/caskey.nvim">Nexmean/caskey.nvim</a> - Utility to keymappings configuration using declarative cascading trees, optionally integrates with <code>which-key</code>.</li>
<li>
<a href="https://github.com/Wansmer/langmapper.nvim">Wansmer/langmapper.nvim</a> - Auto translating your mappings for non-English input methods.</li>
</ul>
<h2 id="mouse">Mouse</h2>
<ul>
<li>
<a href="https://github.com/notomo/gesture.nvim">notomo/gesture.nvim</a> - Mouse gesture plugin.</li>
</ul>
<h2 id="scrolling">Scrolling</h2>
<ul>
<li>
<a href="https://github.com/karb94/neoscroll.nvim">karb94/neoscroll.nvim</a> - Smooth scrolling.</li>
<li>
<a href="https://github.com/declancm/cinnamon.nvim">declancm/cinnamon.nvim</a> - Smooth scrolling for any movement command.</li>
</ul>
<h3 id="scrollbar">Scrollbar</h3>
<ul>
<li>
<a href="https://github.com/Xuyuanp/scrollbar.nvim">Xuyuanp/scrollbar.nvim</a> - Scrollbar.</li>
<li>
<a href="https://github.com/dstein64/nvim-scrollview">dstein64/nvim-scrollview</a> - Display interactive scrollbars.</li>
<li>
<a href="https://github.com/petertriho/nvim-scrollbar">petertriho/nvim-scrollbar</a> - Extensible scrollbar that shows diagnostics and search results.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-map.md">echasnovski/mini.nvim#mini.map</a> - Module of <code>mini.nvim</code> to show floating window with buffer text overview, scrollbar, and highlights.</li>
<li>
<a href="https://github.com/gorbit99/codewindow.nvim">gorbit99/codewindow.nvim</a> - Minimap plugin, that is closely integrated with treesitter and the builtin LSP to display more information to the user.</li>
<li>
<a href="https://github.com/lewis6991/satellite.nvim">lewis6991/satellite.nvim</a> - Decorate scrollbar.</li>
</ul>
<h2 id="editing-support">Editing Support</h2>
<ul>
<li>
<a href="https://github.com/windwp/nvim-ts-autotag">windwp/nvim-ts-autotag</a> - Use treesitter to autoclose and autorename xml,html,jsx tag.</li>
<li>
<a href="https://github.com/windwp/nvim-autopairs">windwp/nvim-autopairs</a> - A minimalist autopairs written by Lua.</li>
<li>
<a href="https://github.com/ZhiyuanLck/smart-pairs">ZhiyuanLck/smart-pairs</a> - Ultimate smart pairs written by Lua.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-pairs.md">echasnovski/mini.nvim#mini.pairs</a> - Module of <code>mini.nvim</code> for autopairs which has minimal defaults and functionality to do per-key mapping.</li>
<li>
<a href="https://github.com/m4xshen/autoclose.nvim">m4xshen/autoclose.nvim</a> - A minimalist autoclose plugin written in Lua.</li>
<li>
<a href="https://github.com/altermo/ultimate-autopair.nvim">altermo/ultimate-autopair.nvim</a> - Autopair with extensions.</li>
<li>
<a href="https://github.com/utilyre/sentiment.nvim">utilyre/sentiment.nvim</a> - Enhanced matchparen.</li>
<li>
<a href="https://github.com/monaqa/dial.nvim">monaqa/dial.nvim</a> - Extended increment/decrement.</li>
<li>
<a href="https://github.com/HiPhish/rainbow-delimiters.nvim">HiPhish/rainbow-delimiters.nvim</a> - Rainbow delimiters with Tree-sitter.</li>
<li>
<a href="https://github.com/AckslD/nvim-revJ.lua">AckslD/nvim-revJ.lua</a> - Neovim Lua plugin for doing the opposite of join-line (J) for arguments.</li>
<li>
<a href="https://github.com/Pocco81/TrueZen.nvim">Pocco81/TrueZen.nvim</a> - Clean and elegant distraction-free writing.</li>
<li>
<a href="https://github.com/Pocco81/HighStr.nvim">Pocco81/HighStr.nvim</a> - Highlight visual selections like in a normal document editor!</li>
<li>
<a href="https://github.com/Pocco81/AutoSave.nvim">Pocco81/AutoSave.nvim</a> - Save your work before the world collapses or you type :qa!</li>
<li>
<a href="https://github.com/okuuva/auto-save.nvim">okuuva/auto-save.nvim</a> - Automatically saves your work as often as needed and as seldom as possible. Customizable with smart defaults. Maintained fork of Pocco81/auto-save.nvim.</li>
<li>
<a href="https://github.com/tmillr/sos.nvim">tmillr/sos.nvim</a> - Automatically save all your modified buffers according to a predefined timeout value.</li>
<li>
<a href="https://github.com/folke/zen-mode.nvim">folke/zen-mode.nvim</a> - Distraction-free coding.</li>
<li>
<a href="https://github.com/haringsrob/nvim_context_vt">haringsrob/nvim_context_vt</a> - Shows virtual text of the current context.</li>
<li>
<a href="https://github.com/nvim-treesitter/nvim-treesitter-context">nvim-treesitter/nvim-treesitter-context</a> - Shows floating hover with the current function/block context.</li>
<li>
<a href="https://github.com/mizlan/iswap.nvim">mizlan/iswap.nvim</a> - Interactively select and swap function arguments, list elements, and more. Powered by tree-sitter.</li>
<li>
<a href="https://github.com/Wansmer/sibling-swap.nvim">Wansmer/sibling-swap.nvim</a> - Different way to swapping arguments and other siblings with Tree-Sitter.</li>
<li>
<a href="https://github.com/Wansmer/binary-swap.nvim">Wansmer/binary-swap.nvim</a> - Swapping operands and operators in binary expressions: comparison and mathematical operations.</li>
<li>
<a href="https://github.com/nacro90/numb.nvim">nacro90/numb.nvim</a> - Peek lines in a non-obtrusive way.</li>
<li>
<a href="https://github.com/ethanholz/nvim-lastplace">ethanholz/nvim-lastplace</a> - Reopen files at your last edit position.</li>
<li>
<a href="https://github.com/AllenDang/nvim-expand-expr">Allendang/nvim-expand-expr</a> - Expand and repeat expression to multiple lines.</li>
<li>
<a href="https://github.com/h-hg/fcitx.nvim">h-hg/fcitx.nvim</a> - Switching and restoring fcitx state for each buffer separately.</li>
<li>
<a href="https://github.com/keaising/im-select.nvim">keaising/im-select.nvim</a> - Switching and restoring input method automatically depends on Neovim's edit mode.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-trailspace.md">echasnovski/mini.nvim#mini.trailspace</a> - Module of <code>mini.nvim</code> for automatic highlighting of trailing whitespace with functionality to remove it.</li>
<li>
<a href="https://github.com/smjonas/live-command.nvim">smjonas/live-command.nvim</a> - Text editing with immediate visual feedback: preview commands such as <code>:norm</code>, <code>:g</code>, macros and more.</li>
<li>
<a href="https://github.com/filipdutescu/renamer.nvim">filipdutescu/renamer.nvim</a> - VS Code-like renaming UI, written in Lua.</li>
<li>
<a href="https://github.com/gbprod/cutlass.nvim">gbprod/cutlass.nvim</a> - Plugin that adds a 'cut' operation separate from 'delete'.</li>
<li>
<a href="https://github.com/gbprod/substitute.nvim">gbprod/substitute.nvim</a> - Neovim plugin introducing a new operator motions to quickly replace and exchange text.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-operators.md">echasnovski/mini.nvim#mini.operators</a> - Module of <code>mini.nvim</code> with various text edit operators: replace, exchange, multiply, sort, evaluate.</li>
<li>
<a href="https://github.com/gbprod/yanky.nvim">gbprod/yanky.nvim</a> - Improved Yank and Put functionalities.</li>
<li>
<a href="https://github.com/sQVe/sort.nvim">sQVe/sort.nvim</a> - Sorting plugin that intelligently supports line-wise and delimiter sorting.</li>
<li>
<a href="https://github.com/booperlv/nvim-gomove">booperlv/nvim-gomove</a> - A complete plugin for moving and duplicating blocks and lines, with complete fold handling, reindenting, and undoing in one go.</li>
<li>
<a href="https://github.com/hinell/duplicate.nvim">hinell/duplicate.nvim</a> - Duplicate lines &amp; blocks of lines easily; undo &amp; unfolding support; full OOP.</li>
<li>
<a href="https://github.com/hinell/move.nvim">hinell/move.nvim</a> - Move chunks of text around; fork of <a href="https://github.com/fedepujol/move.nvim">fedepujol/move.nvim</a>.</li>
<li>
<a href="https://github.com/willothy/moveline.nvim">willothy/moveline.nvim</a> - Move lines and blocks up and down easily, with indenting handled automatically as you move. Written in Rust.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-move.md">echasnovski/mini.nvim#mini.move</a> - Module of <code>mini.nvim</code> to move any selection (charwise, linewise, blockwise, current line in Normal mode) in any direction. Handles both <code>v:count</code> and undo history.</li>
<li>
<a href="https://github.com/anuvyklack/pretty-fold.nvim">anuvyklack/pretty-fold.nvim</a> - Foldtext customization.</li>
<li>
<a href="https://github.com/bennypowers/nvim-regexplainer">bennypowers/nvim-regexplainer</a> - Explain the regular expression under the cursor.</li>
<li>
<a href="https://github.com/gbprod/stay-in-place.nvim">gbprod/stay-in-place.nvim</a> - Neovim plugin that prevent cursor from moving when using shift and filter actions.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-ai.md">echasnovski/mini.nvim#mini.ai</a> - Module of <code>mini.nvim</code> for extending and creating <code>a</code>/<code>i</code> textobjects. It enhances some builtin textobjects, creates extensive set of new ones (like <code>a*</code>, <code>a&lt;Space&gt;</code>, <code>a?</code>, and more), and allows user to create their own (via Lua patterns or functions). Supports dot-repeat, different search methods, consecutive application, and more.</li>
<li>
<a href="https://github.com/Wansmer/treesj">Wansmer/treesj</a> - Splitting/joining blocks of code like arrays, hashes, statements, objects, dictionaries, etc. Using Tree-Sitter. Inspired by greatest splitjoin.vim.</li>
<li>
<a href="https://github.com/bennypowers/splitjoin.nvim">bennypowers/splitjoin.nvim</a> - Split and join various syntax structures.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-splitjoin.md">echasnovski/mini.nvim#mini.splitjoin</a> - Module of <code>mini.nvim</code> to split and join arguments. Has customizable pre and post hooks. Works inside comments.</li>
<li>
<a href="https://github.com/shortcuts/no-neck-pain.nvim">shortcuts/no-neck-pain.nvim</a> - Center the currently focused buffer to the middle of your terminal.</li>
<li>
<a href="https://github.com/debugloop/telescope-undo.nvim">debugloop/telescope-undo.nvim</a> - A telescope extension to visualize your undo tree and fuzzy-search changes in it.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-various-textobjs">chrisgrieser/nvim-various-textobjs</a> - Bundle of about a dozen custom text objects.</li>
<li>
<a href="https://github.com/XXiaoA/ns-textobject.nvim">XXiaoA/ns-textobject.nvim</a> - Awesome textobject plugin works with nvim-surround.</li>
<li>
<a href="https://git.sr.ht/~nedia/auto-save.nvim">~nedia/auto-save.nvim</a> - Extremely simple auto saving on <code>InsertLeave</code> &amp; <code>TextChanged</code>. Based on Pocco81/AutoSave but lighter.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-basics.md">echasnovski/mini.nvim#mini.basics</a> - Module of <code>mini.nvim</code> with customizable configuration presets for common options, mappings, and autocommands.</li>
<li>
<a href="https://github.com/niuiic/part-edit.nvim">niuiic/part-edit.nvim</a> - Edit a part of a file individually.</li>
<li>
<a href="https://github.com/niuiic/divider.nvim">niuiic/divider.nvim</a> - Custom code divider line.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-alt-substitute">chrisgrieser/nvim-alt-substitute</a> - A substitute of vim's <code>:substitute</code> that uses Lua patterns instead of vim regex. Supports incremental preview.</li>
<li>
<a href="https://github.com/ckolkey/ts-node-action">ckolkey/ts-node-action</a> - A framework for executing functional transformations on Tree-sitter nodes - Has a lot of built-in actions for transforming text.</li>
<li>
<a href="https://github.com/tomiis4/hypersonic.nvim">tomiis4/hypersonic.nvim</a> - Provides explanation for RegExp.</li>
<li>
<a href="https://github.com/00sapo/visual.nvim">00sapo/visual.nvim</a> - Provides keybindings for creating a Kakoune/Helix-like experience: first select and then choose the editing command.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-puppeteer">chrisgrieser/nvim-puppeteer</a> - Automatically convert strings to f-strings or template strings and back.</li>
<li>
<a href="https://github.com/nat-418/boole.nvim">nat-418/boole.nvim</a> - Toggle booleans and common string values.</li>
<li>
<a href="https://github.com/cshuaimin/ssr.nvim">cshuaimin/ssr.nvim</a> - Treesitter-based structural search and replace.</li>
<li>
<a href="https://github.com/Jxstxs/conceal.nvim">Jxstxs/conceal.nvim</a> - Use Tree-sitter to conceal common boilerplate code.</li>
</ul>
<h3 id="comment">Comment</h3>
<ul>
<li>
<a href="https://github.com/numToStr/Comment.nvim">numToStr/Comment.nvim</a> - Smart and Powerful comment plugin. Supports commentstring, motions, dot-repeat and more.</li>
<li>
<a href="https://github.com/b3nj5m1n/kommentary">b3nj5m1n/kommentary</a> - Commenting plugin written in Lua.</li>
<li>
<a href="https://github.com/gennaro-tedesco/nvim-commaround">gennaro-tedesco/nvim-commaround</a> - Fast and light commenting plugin written in Lua.</li>
<li>
<a href="https://github.com/folke/todo-comments.nvim">folke/todo-comments.nvim</a> - Highlight, list and search todo comments in your projects.</li>
<li>
<a href="https://github.com/terrortylor/nvim-comment">terrortylor/nvim-comment</a> - Toggle comments using the built-in commentstring option.</li>
<li>
<a href="https://github.com/winston0410/commented.nvim">winston0410/commented.nvim</a> - A commenting plugin that supports counts and multiple comment patterns and much more.</li>
<li>
<a href="https://github.com/s1n7ax/nvim-comment-frame">s1n7ax/nvim-comment-frame</a> - Adds a comment frame based on the source file.</li>
<li>
<a href="https://github.com/danymat/neogen">danymat/neogen</a> - A better annotation generator. Supports multiple languages and annotation conventions.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-comment.md">echasnovski/mini.nvim#mini.comment</a> - Module of <code>mini.nvim</code> for per-line commenting. Fully supports dot-repeat.</li>
<li>
<a href="https://github.com/LudoPinelli/comment-box.nvim">LudoPinelli/comment-box.nvim</a> - Clarify and beautify your comments using boxes and lines.</li>
<li>
<a href="https://github.com/JoosepAlviste/nvim-ts-context-commentstring">JoosepAlviste/nvim-ts-context-commentstring</a> - Sets the <code>commentstring</code> option based on the cursor location in the file. The location is checked via treesitter queries.</li>
<li>
<a href="https://github.com/LucasTavaresA/SingleComment.nvim">LucasTavaresA/SingleComment.nvim</a> - Always single line, comment sensitive, indentation preserving commenting.</li>
<li>
<a href="https://github.com/Zeioth/dooku.nvim">Zeioth/dooku.nvim</a> - Generate and open your HTML code documentation.</li>
</ul>
<h2 id="formatting">Formatting</h2>
<ul>
<li>
<a href="https://github.com/gpanders/editorconfig.nvim">gpanders/editorconfig.nvim</a> - An EditorConfig plugin written in Fennel.</li>
<li>
<a href="https://github.com/mhartington/formatter.nvim">mhartington/formatter.nvim</a> - A format runner written in Lua.</li>
<li>
<a href="https://github.com/lukas-reineke/lsp-format.nvim">lukas-reineke/lsp-format.nvim</a> - A wrapper around Neovims native LSP formatting.</li>
<li>
<a href="https://github.com/sbdchd/neoformat">sbdchd/neoformat</a> - A (Neo)vim plugin for formatting code.</li>
<li>
<a href="https://github.com/cappyzawa/trim.nvim">cappyzawa/trim.nvim</a> - This plugin trims trailing whitespace and lines.</li>
<li>
<a href="https://github.com/mcauley-penney/tidy.nvim">mcauley-penney/tidy.nvim</a> - Clear trailing whitespace and empty lines at end of file on every save.</li>
<li>
<a href="https://github.com/MunifTanjim/prettier.nvim">MunifTanjim/prettier.nvim</a> - Prettier integration.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-align.md">echasnovski/mini.nvim#mini.align</a> - Module of <code>mini.nvim</code> for aligning text interactively (with or without instant preview).</li>
<li>
<a href="https://github.com/emileferreira/nvim-strict">emileferreira/nvim-strict</a> - Strict, native code style formatting which exposes deep nesting, overlong lines, trailing whitespace, trailing empty lines, todos and inconsistent indentation.</li>
<li>
<a href="https://git.sr.ht/~nedia/auto-format.nvim">~nedia/auto-format.nvim</a> - Does no formatting by itself, but sets up an autocmd to format on save, preferring null-ls over LSP client formatting.</li>
<li>
<a href="https://github.com/tenxsoydev/tabs-vs-spaces.nvim">tenxsoydev/tabs-vs-spaces.nvim</a> - Hint and fix deviating indentation.</li>
<li>
<a href="https://github.com/bennypowers/svgo.nvim">bennypowers/svgo.nvim</a> - Optimize SVG files.</li>
<li>
<a href="https://github.com/niuiic/format.nvim">niuiic/format.nvim</a> - An asynchronous, multitasking, and highly configurable formatting plugin.</li>
<li>
<a href="https://github.com/elentok/format-on-save.nvim">elentok/format-on-save.nvim</a> - A synchronous formatter that combines LSP and non-LSP formatting (e.g. shfmt, stylua, prettier), focused specifically on format-on-save.</li>
<li>
<a href="https://github.com/stevearc/conform.nvim">stevearc/conform.nvim</a> - A lightweight formatting engine that plays nice with LSP.</li>
<li>
<a href="https://github.com/nvimdev/guard.nvim">nvimdev/guard.nvim</a> - Minimalist async formatting and linting plugin.</li>
</ul>
<h3 id="indent">Indent</h3>
<ul>
<li>
<a href="https://github.com/nvimdev/indentmini.nvim">nvimdev/indentmini.nvim</a> - A minimal and blazing fast indentline plugin by using nvim_set_decoration_provide api.</li>
<li>
<a href="https://github.com/lukas-reineke/indent-blankline.nvim">lukas-reineke/indent-blankline.nvim</a> - IndentLine replacement in Lua with more features and treesitter support.</li>
<li>
<a href="https://github.com/LucasTavaresA/simpleIndentGuides.nvim">LucasTavaresA/simpleIndentGuides.nvim</a> - Indentation guides using the builtin variables.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-indentscope.md">echasnovski/mini.nvim#mini.indentscope</a> - Module of <code>mini.nvim</code> for visualizing and operating on indent scope. Supports customization of debounce delay, animation style, and different granularity of options for scope computing algorithm.</li>
<li>
<a href="https://github.com/NMAC427/guess-indent.nvim">NMAC427/guess-indent.nvim</a> - Automatic indentation style detection.</li>
<li>
<a href="https://github.com/Darazaki/indent-o-matic">Darazaki/indent-o-matic</a> - Dumb automatic fast indentation detection written in Lua.</li>
<li>
<a href="https://github.com/Abstract-IDE/penvim">Abstract-IDE/penvim</a> - Project's root directory and documents Indentation detector with project based config loader.</li>
<li>
<a href="https://github.com/yaocccc/nvim-hlchunk">yaocccc/nvim-hlchunk</a> - Highlight a <code>{}</code> chunk.</li>
<li>
<a href="https://github.com/shellRaining/hlchunk.nvim">shellRaining/hlchunk.nvim</a> - A Lua implementation of <code>nvim-hlchunk</code>, contains more features, such as highlight <code>{}</code> chunk, indent line, space blank etc.</li>
<li>
<a href="https://github.com/VidocqH/auto-indent.nvim">VidocqH/auto-indent.nvim</a> - Auto indent cursor when cursor at the first column and press <code>&lt;TAB&gt;</code> key like VSCode.</li>
</ul>
<h2 id="command-line">Command Line</h2>
<ul>
<li>
<a href="https://github.com/notomo/cmdbuf.nvim">notomo/cmdbuf.nvim</a> - Alternative command-line-window plugin.</li>
<li>
<a href="https://github.com/gelguy/wilder.nvim">gelguy/wilder.nvim</a> - A plugin for fuzzy command line autocompletion.</li>
</ul>
<h2 id="session">Session</h2>
<ul>
<li>
<a href="https://github.com/rmagatti/auto-session">rmagatti/auto-session</a> - A small automated session manager.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-sessions.md">echasnovski/mini.nvim#mini.sessions</a> - Module of <code>mini.nvim</code> for session management (read, write, delete).</li>
<li>
<a href="https://github.com/gennaro-tedesco/nvim-possession">gennaro-tedesco/nvim-possession</a> - The no-nonsense session manager.</li>
<li>
<a href="https://github.com/olimorris/persisted.nvim">olimorris/persisted.nvim</a> - Simple session management with git branching, autosave/autoload and Telescope support.</li>
<li>
<a href="https://github.com/Shatur/neovim-session-manager">Shatur/neovim-session-manager</a> - A simple wrapper around :mksession.</li>
<li>
<a href="https://github.com/jedrzejboczar/possession.nvim">jedrzejboczar/possession.nvim</a> - Flexible session management with arbitrary persistent data stored as JSON.</li>
<li>
<a href="https://github.com/niuiic/multiple-session.nvim">niuiic/multiple-session.nvim</a> - Provides multi-session management capabilities.</li>
<li>
<a href="https://github.com/RutaTang/spectacle.nvim">RutaTang/spectacle.nvim</a> - Easily manage multiple sessions with telescope integration.</li>
<li>
<a href="https://github.com/coffebar/neovim-project">coffebar/neovim-project</a> - Declarative project management, automatic saving of sessions, uses Telescope.</li>
</ul>
<h2 id="remote-development">Remote Development</h2>
<ul>
<li>
<a href="https://github.com/chipsenkbeil/distant.nvim">chipsenkbeil/distant.nvim</a> - Edit files, run programs, and work with LSP on a remote machine from the comfort of your local environment.</li>
<li>
<a href="https://github.com/jamestthompson3/nvim-remote-containers">jamestthompson3/nvim-remote-containers</a> - Develop inside docker containers, just like VSCode.</li>
<li>
<a href="https://github.com/esensar/nvim-dev-container">esensar/nvim-dev-container</a> - Neovim devcontainer.json and general development container support.</li>
<li>
<a href="https://github.com/miversen33/netman.nvim">miversen33/netman.nvim</a> - Lua powered Network Resource Manager.</li>
<li>
<a href="https://github.com/niuiic/remote.nvim">niuiic/remote.nvim</a> - Edit remote files with local configuration.</li>
</ul>
<h2 id="split-and-window">Split and Window</h2>
<ul>
<li>
<a href="https://sr.ht/~henriquehbr/ataraxis.lua">~henriquehbr/ataraxis.lua</a> - A zen mode for improving code readability on Neovim.</li>
<li>
<a href="https://github.com/yorickpeterse/nvim-window">yorickpeterse/nvim-window</a> - Easily jump between Neovim windows.</li>
<li>
<a href="https://github.com/sindrets/winshift.nvim">sindrets/winshift.nvim</a> - Rearrange your windows with ease.</li>
<li>
<a href="https://github.com/beauwilliams/focus.nvim">beauwilliams/focus.nvim</a> - Auto-Focusing and Auto-Resizing Splits/Windows written in Lua! Vim splits on steroids.</li>
<li>
<a href="https://github.com/anuvyklack/windows.nvim">anuvyklack/windows.nvim</a> - Automatically expand width of the current window. Maximizes and restore it. And all this with nice animations!</li>
<li>
<a href="https://github.com/nvim-zh/colorful-winsep.nvim">nvim-zh/colorful-winsep.nvim</a> - A configurable color split line.</li>
<li>
<a href="https://github.com/nyngwang/NeoNoName.lua">nyngwang/NeoNoName.lua</a> - Layout preserving buffer deletion.</li>
<li>
<a href="https://github.com/famiu/bufdelete.nvim">famiu/bufdelete.nvim</a> - Delete Neovim buffers without losing your window layout.</li>
<li>
<a href="https://github.com/echasnovski/mini.nvim/blob/main/readmes/mini-bufremove.md">echasnovski/mini.nvim#mini.bufremove</a> - Module of <code>mini.nvim</code> for buffer removing (unshow, delete, wipeout) while saving window layout.</li>
<li>
<a href="https://github.com/jyscao/ventana.nvim">jyscao/ventana.nvim</a> - Convenient flips &amp; shifts for your windows layout.</li>
</ul>
<h3 id="tmux">Tmux</h3>
<ul>
<li>
<a href="https://github.com/aserowy/tmux.nvim">aserowy/tmux.nvim</a> - Tmux integration features pane movement and resizing.</li>
<li>
<a href="https://github.com/danielpieper/telescope-tmuxinator.nvim">danielpieper/telescope-tmuxinator.nvim</a> - Integration for tmuxinator with telescope.nvim.</li>
<li>
<a href="https://github.com/hkupty/nvimux">hkupty/nvimux</a> - Neovim as tmux replacement.</li>
<li>
<a href="https://github.com/numToStr/Navigator.nvim">numToStr/Navigator.nvim</a> - Smoothly navigate between Neovim splits and Tmux panes.</li>
<li>
<a href="https://github.com/declancm/windex.nvim">declancm/windex.nvim</a> - Collection of window functions which includes moving between, closing and maximizing Neovim splits and Tmux panes.</li>
<li>
<a href="https://github.com/otavioschwanck/tmux-awesome-manager.nvim">otavioschwanck/tmux-awesome-manager.nvim</a> - Run your workflow commands like yarn install, rails console, yarn add, bundle install, etc.</li>
</ul>
<h2 id="game">Game</h2>
<ul>
<li>
<a href="https://github.com/ThePrimeagen/vim-be-good">ThePrimeagen/vim-be-good</a> - Vim-be-good is a Neovim plugin designed to make you better at Vim Movements.</li>
<li>
<a href="https://github.com/alec-gibson/nvim-tetris">alec-gibson/nvim-tetris</a> - Bringing emacs' greatest feature to Neovim - Tetris!.</li>
<li>
<a href="https://github.com/seandewar/nvimesweeper">seandewar/nvimesweeper</a> - Play Minesweeper in your favourite text editor.</li>
<li>
<a href="https://github.com/seandewar/killersheep.nvim">seandewar/killersheep.nvim</a> - Neovim port of killersheep.</li>
<li>
<a href="https://github.com/rktjmp/shenzhen-solitaire.nvim">rktjmp/shenzhen-solitaire.nvim</a> - Shenzhen I/O Solitaire port.</li>
<li>
<a href="https://github.com/Eandrju/cellular-automaton.nvim">Eandrju/cellular-automaton.nvim</a> - It lets you execute aesthetically pleasing, cellular automaton animations based on the content of Neovim buffer.</li>
<li>
<a href="https://github.com/alanfortlink/blackjack.nvim">alanfortlink/blackjack.nvim</a> - Classic Black Jack game.</li>
<li>
<a href="https://github.com/jim-fx/sudoku.nvim">jim-fx/sudoku.nvim</a> - Classic sudoku puzzle.</li>
</ul>
<h3 id="competitive-programming">Competitive Programming</h3>
<ul>
<li>
<a href="https://github.com/p00f/cphelper.nvim">p00f/cphelper.nvim</a> - Neovim helper for competitive programming written in Lua.</li>
<li>
<a href="https://github.com/xeluxee/competitest.nvim">xeluxee/competitest.nvim</a> - A plugin to automate testcases management and checking for Competitive Programming contests.</li>
<li>
<a href="https://github.com/Dhanus3133/Leetbuddy.nvim">Dhanus3133/Leetbuddy.nvim</a> - Solve Leetcode problems within Neovim.</li>
</ul>
<h2 id="workflow">Workflow</h2>
<ul>
<li>
<a href="https://github.com/m4xshen/hardtime.nvim">m4xshen/hardtime.nvim</a> - Helping you establish good command workflow and habit.</li>
<li>
<a href="https://github.com/antonk52/bad-practices.nvim">antonk52/bad-practices.nvim</a> - Helping you give up bad practices in Vim.</li>
</ul>
<h2 id="preconfigured-configuration">Preconfigured Configuration</h2>
<ul>
<li>
<a href="https://github.com/sontungexpt/stinvim">sontungexpt/stinvim</a> - Ready Neovim's configuration for fullstack developers.</li>
<li>
<a href="https://github.com/Abstract-IDE/Abstract">Abstract-IDE/Abstract</a> - Abstract, The Neovim configuration to achieve the power of Modern IDE.</li>
<li>
<a href="https://spacevim.org">SpaceVim/SpaceVim</a> - A community-driven modular Vim/Neovim distribution, like spacemacs but for Vim/Neovim.</li>
<li>
<a href="https://github.com/CosmicNvim/CosmicNvim">CosmicNvim/CosmicNvim</a> - CosmicNvim is a lightweight and opinionated Neovim config for web development, specifically designed to provide a 💫 COSMIC programming experience!</li>
<li>
<a href="https://github.com/artart222/CodeArt">artart222/CodeArt</a> - A fast general-purpose IDE written entirely in Lua with an installer for Linux/Windows/macOS and built in <code>:CodeArtUpdate</code> command for updating it.</li>
<li>
<a href="https://github.com/LazyVim/LazyVim">LazyVim/LazyVim</a> - Full-fledged IDE powered by <strong>lazy.nvim</strong> to make it easy to customize and extend your config.</li>
<li>
<a href="https://github.com/NTBBloodbath/doom-nvim">NTBBloodbath/doom-nvim</a> - Port of the doom-emacs framework, its goal is to add useful functions to Neovim to start working in a stable and efficient development environment without spending a lot of time configuring everything.</li>
<li>
<a href="https://github.com/crivotz/nv-ide">crivotz/nv-ide</a> - Neovim custom configuration, oriented for full stack developers (rails, ruby, php, html, css, SCSS, JavaScript).</li>
<li>
<a href="https://github.com/LunarVim/LunarVim">LunarVim/LunarVim</a> - This project aims to help one transition away from VSCode, and into a superior text editing experience.</li>
<li>
<a href="https://github.com/hackorum/VapourNvim">hackorum/VapourNvim</a> - A Neovim config for THE ULTIMATE Vim IDE-like experience.</li>
<li>
<a href="https://github.com/vi-tality/neovitality">vi-tality/neovitality</a> - A full-featured Neovim distribution, packaged with Nix Flake for easy installation and reproducibility.</li>
<li>
<a href="https://github.com/siduck76/NvChad">siduck76/NvChad</a> - An attempt to make Neovim cli as functional as an IDE while being very beautiful and less bloated.</li>
<li>
<a href="https://github.com/nvoid-lua/nvoid">nvoid-lua/nvoid</a> - Simple Neovim config written in Lua with all the modern features available in any <strong>IDE</strong>
</li>
<li>
<a href="https://github.com/cstsunfu/.sea.nvim">cstsunfu/.sea.nvim</a> - A modular Neovim configuration with beautiful UI and some useful features(Pomodoro Clock, Window Number).</li>
<li>
<a href="https://github.com/shaeinst/roshnivim">shaeinst/roshnivim</a> - Roshnivim, can be called neovim's distro, is a predefined configs so that you don't need 1000hr to setup neovim as an IDE.</li>
<li>
<a href="https://github.com/AstroNvim/AstroNvim">AstroNvim/AstroNvim</a> - AstroNvim is an aesthetic and feature-rich Neovim config that is extensible and easy to use with a great set of plugins.</li>
<li>
<a href="https://github.com/shaunsingh/nyoom.nvim">shaunsingh/nyoom.nvim</a> - Blazing fast, configurable, minimal and lispy neovim config written in Fennel. Base config for users to extend and add upon, leading to a more unique editing experience.</li>
<li>
<a href="https://github.com/jrychn/ModuleVim">jrychn/moduleVim</a> - A very easy to use
for backend and frontend, install lsp automatically.</li>
<li>
<a href="https://github.com/askfiy/nvim">askfiy/nvim</a> - An excellent Neovim configuration, which is as powerful as Vscode, is lightning fast ⚡️.</li>
<li>
<a href="https://github.com/imbacraft/dusk.nvim">imbacraft/dusk.nvim</a> - Dusk is a lightweight, aesthetically minimal Neovim config, written in Lua, able to provide for web and Java development.</li>
<li>
<a href="https://github.com/nvim-lua/kickstart.nvim">nvim-lua/kickstart.nvim</a> - A launch point for your personal Neovim configuration.</li>
<li>
<a href="https://github.com/cunderw/nvim">cunderw/nvim</a> - Neovim custom configuration, focused on JS/TS, Go, and Java development. Very IDE like.</li>
<li>
<a href="https://github.com/otavioschwanck/mood-nvim">otavioschwanck/mood-nvim</a> - Ready to use configuration for Ruby on Rails, JavaScript and Typescript.</li>
<li>
<a href="https://github.com/ldelossa/nvim-ide">ldelossa/nvim-ide</a> - A full featured IDE layer heavily inspired by VSCode.</li>
<li>
<a href="https://github.com/jonathandion/web-dev.nvim">jonathandion/web-dev.nvim</a> - Small, simple and flexible configuration for web development ✨.</li>
<li>
<a href="https://github.com/linrongbin16/lin.nvim">linrongbin16/lin.nvim</a> - A highly configured Neovim distribution integrated with tons of utilities for development, inspired by spf13-vim.</li>
<li>
<a href="https://github.com/doctorfree/nvim-lazyman">doctorfree/nvim-lazyman</a> - Neovim configuration manager and modular configuration, supports over 40 preconfigured configurations.</li>
<li>
<a href="https://github.com/NormalNvim/NormalNvim">NormalNvim/NormalNvim</a> - Focused on stability for your daily work. From the creator of Compiler.nvim.</li>
<li>
<a href="https://github.com/chrisgrieser/nvim-kickstart-python">chrisgrieser/nvim-kickstart-python</a> - A launch point for your Neovim configuration for Python.</li>
<li>
<a href="https://github.com/mrcjkb/kickstart-nix.nvim">mrcjkb/kickstart-nix.nvim</a> - A simple <a href="https://nixos.wiki/wiki/Flakes">Nix flake</a> template repo for Neovim derivations, with the goal of simplifying the migration from existing Neovim configurations.</li>
</ul>
<h2 id="external">External</h2>
<p>These tools are used externally to Neovim to enhance the experience.</p>
<h3 id="version-manager">Version Manager</h3>
<ul>
<li>
<a href="https://github.com/MordechaiHadad/bob">MordechaiHadad/bob</a> - A cross platform and easy to use Neovim version manager.</li>
<li>
<a href="https://github.com/NTBBloodbath/nvenv">NTBBloodbath/nvenv</a> - A lightweight and blazing fast Neovim version manager.</li>
<li>
<a href="https://github.com/shohi/neva">shohi/neva</a> - A Neovim version manager written in Lua.</li>
</ul>
<h3 id="boilerplate">Boilerplate</h3>
<ul>
<li>
<a href="https://github.com/gennaro-tedesco/boilit">gennaro-tedesco/boilit</a> - Create boilerplate structure plugins.</li>
<li>
<a href="https://github.com/m00qek/plugin-template.nvim">m00qek/plugin-template.nvim</a> - A plugin template that setups test infrastructure and GitHub Actions.</li>
<li>
<a href="https://github.com/ellisonleao/nvim-plugin-template">ellisonleao/nvim-plugin-template</a> - Another neovim plugin template, using GitHub's template feature.</li>
</ul>
<h3 id="os-specific">OS-specific</h3>
<ul>
<li>
<a href="https://github.com/chrisgrieser/alfred-neovim-utilities">chrisgrieser/alfred-neovim-utilities</a> - Search Neovim plugins and online <code>:help </code>via Alfred (macOS).</li>
</ul>
<h2 id="wishlist">Wishlist</h2>
<p>Have a problem a plugin can solve? Add it to the <a href="https://github.com/nvim-lua/wishlist">nvim-lua wishlist</a>.</p>
<h2 id="ui">UI</h2>
<p>Neovim supports a wide variety of UI's.
You can find them listed on the <a href="https://github.com/neovim/neovim/wiki/Related-projects#gui">Neovim wiki</a></p>
<h2 id="starter-templates">Starter Templates</h2>
<ul>
<li>
<a href="https://github.com/tokiory/neovim-boilerplate">tokiory/neovim-boilerplate</a> - Starter boilerplate for making new configurations.</li>
<li>
<a href="https://github.com/frans-johansson/lazy-nvim-starter">frans-johansson/lazy-nvim-starter</a> - Starter boilerplate with lazy plugin manager.</li>
</ul>
<h2 id="vim">Vim</h2>
<ul>
<li>
<a href="https://vimawesome.com/">Vimawesome</a> - Showcases various plugins for Vim and has a <a href="https://vimawesome.com/?q=tag:neovim">neovim tag</a> for other plugins targeting Neovim.</li>
<li>
<a href="https://github.com/akrawchyk/awesome-vim#tools">awesome-vim</a> - Short list of Vim plugins and helpful guides.</li>
<li>
<a href="https://github.com/altermo/vim-plugin-list">vim-plugin-list</a> - List of Vim and Neovim plugins.</li>
</ul>
<h2 id="resource">Resource</h2>
<ul>
<li>
<a href="https://neovimcraft.com">Neovimcraft</a> - A site dedicated to searching specific plugins and guides for building plugins in Lua.</li>
<li>
<a href="https://dotfyle.com">Dotfyle</a> - Dotfyle is a site for sharing and discovering Neovim configs and plugins.</li>
</ul>
</div>
<script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-17176544-11', 'auto');
    ga('send', 'pageview');
</script>

<script type="text/javascript">
    (function (d, w, c) {
        (w[c] = w[c] || []).push(function() {
            try {
                w.yaCounter45280944 = new Ya.Metrika({
                    id:45280944,
                    clickmap:true,
                    trackLinks:true,
                    accurateTrackBounce:true
                });
            } catch(e) { }
        });

        var n = d.getElementsByTagName("script")[0],
            s = d.createElement("script"),
            f = function () { n.parentNode.insertBefore(s, n); };
        s.type = "text/javascript";
        s.async = true;
        s.src = "https://mc.yandex.ru/metrika/watch.js";

        if (w.opera == "[object Opera]") {
            d.addEventListener("DOMContentLoaded", f, false);
        } else { f(); }
    })(document, window, "yandex_metrika_callbacks");
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/45280944" style="position:absolute; left:-9999px;" alt="" /></div></noscript>


    '''
    # Replace 'your_access_token' with your actual GitHub personal access token
    access_token = ';)'
    main(html_content, access_token)
