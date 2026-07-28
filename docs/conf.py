from datetime import UTC, datetime

# 1. Basic Project Info
project = "apple-maps-api"
copyright = f"{datetime.now(UTC).year}, Michael Bianco"
author = "Michael Bianco"

# 2. Extensions
# AutoAPI is the sole API generator (AST-based; avoids importing patched modules).
# autodoc/napoleon/autodoc-typehints/paramlinks are intentionally omitted.
extensions = [
    "myst_parser",  # Enable Markdown
    "sphinx_design",  # UI Components (Grids/Cards)
    "sphinx_copybutton",  # Code copy button
    "sphinx.ext.viewcode",  # View source code
    "sphinx.ext.intersphinx",  # Link to external docs
    "autoapi.extension",  # Auto-generate API reference
    "sphinx_llm.txt",  # LLM-friendly documentation (llms.txt / llms-full.txt)
]

# Configure AutoAPI
autoapi_dirs = ["../apple_maps_api"]
autoapi_type = "python"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
]
autoapi_keep_files = False

# Scraped Apple developer docs are reference material, not Sphinx pages
exclude_patterns = [
    "apple_maps_documentation",
    "_build",
]

# Intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pydantic": (
        "https://docs.pydantic.dev/latest/",
        "https://pydantic.dev/docs/validation/latest/objects.inv",
    ),
}
intersphinx_timeout = 10

# sphinx-llm runs a nested markdown build; keep it sequential for clearer errors
llms_txt_build_parallel = False

# 3. Markdown Support Configuration
source_suffix = {
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",  # Use ::: for directives (much cleaner MD)
    "deflist",  # Support for definition lists
    "substitution",  # Use {{ variables }} in Markdown
    "tasklist",  # Enable GitHub-style checkboxes
    "attrs_block",  # CSS classes directly in markdown
    "attrs_inline",  # CSS classes inline
    "smartquotes",  # Typographic curly quotes
]

# Support heading anchors in MyST for README includes
myst_heading_anchors = 3

# 4. Theme & Appearance (Shibuya)
html_theme = "shibuya"
html_baseurl = "https://iloveitaly.github.io/python-apple-maps-api/"
html_static_path = ["_static"]
html_extra_path = [".nojekyll"]
html_css_files = ["custom.css"]

html_theme_options = {
    "accent_color": "blue",
    "github_url": "https://github.com/iloveitaly/python-apple-maps-api",
    "nav_links": [
        {"title": "API Reference", "url": "autoapi/index"},
    ],
}

# 5. sphinx-llm: publish machine-readable docs alongside HTML
llms_txt_enabled = True
llms_txt_full_build = True
llms_txt_description = (
    "apple-maps-api: A modern Python client for the Apple Maps Server API with "
    "automatic JWT management, Pydantic models, and type-safe geocoding/search helpers."
)
