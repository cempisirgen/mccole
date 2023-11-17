"""Ark configuration file for testing mccole theme."""

title = "McCole Test"
repo = "https://github.com/gvwilson/mccole"
author = "Greg Wilson"

chapters = [
    "first",
    "second",
    "license",
    "bib",
    "syllabus",
]

theme = "mccole"

copy = [
    "*.svg",
]

exclude = copy + [
    "*.py",
    "*.tbl",
    "*~",
    "CODE_OF_CONDUCT.md",
    "LICENSE.md",
    "README.md",
    "__pycache__",
    "pyproject.toml",
]

markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}

src_dir = "src"
out_dir = "docs"

extension = "/"
