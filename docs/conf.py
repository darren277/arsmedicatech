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

    # Exclude project root dirs
    '../src/*',
    '../k8s/*',
    '../static/*',
    '../emr/*',
    '../config/*',
    '../data/*',
    '../node_modules/*',
    '../test/*',
    '../test-results/*',
    '../coverage/*',
    '../stuff/*',
    '../playright-report/*',

    # Exclude dev env and tooling
    '../.vscode/*',
    '../.idea/*',
    '../.github/*',
    '../.venv/*',
    '../venv/*',
]





# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


import os
import sys

# Add the project root directory to sys.path
print("[DEBUG] __file__:", __file__)
print("[DEBUG] cwd:", os.getcwd())

lib_path = os.path.abspath('../../lib')
print("[DEBUG] Adding to sys.path:", lib_path)
sys.path.insert(0, lib_path)

import db  # Should not throw an error
