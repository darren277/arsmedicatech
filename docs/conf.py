# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ArsMedicaTech'
copyright = '2025, Darren MacKenzie'
author = 'Darren MacKenzie'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # for Google/Numpy style docstrings
    "sphinx_autodoc_typehints",
    "myst_parser", #enable Markdown support
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'src/*',
    'k8s/*',
    'static/*',
    'emr/*',
    'config/*',
    '.vscode/*',
    '.venv/*',
    '.idea/*',
    '.github/*',
    'data/*',
    'coverage/*',
    'playright-report/*',
    'node_modules/*',
    'stuff/*',
    'test/*',
    'test-results/*',
    'venv/*',
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
