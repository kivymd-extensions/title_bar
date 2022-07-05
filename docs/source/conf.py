# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("_extensions"))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath("."))))

import autoapi_title_bar  # NOQA. from _extensions

# -- Project information -----------------------------------------------------

project = 'MDTitleBar'
copyright = '2022, Neizvestnyj'
author = 'Neizvestnyj'

# The full version, including alpha/beta/rc tags
release = '0.1'
version = '0.1'


# -- General configuration ---------------------------------------------------
master_doc = "index"
locale_dirs = ["_locales"]
language = "Python"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "autoapi_title_bar",
    "sphinx.ext.intersphinx",
    "kivy_lexer",
    "toctree_with_sort",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_favicon = "_static/kivymd_logo.png"
html_logo = "_static/kivymd_logo.png"
html_theme_options = {
    "canonical_url": "https://kivymd.readthedocs.io/en/latest/",
    "navigation_depth": 2,
    "collapse_navigation": False,
    "titles_only": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# AutoAPI configuration
autoapi_dirs = ["../../kivymd_extensions/title_bar"]
autoapi_template_dir = os.path.abspath("_templates")
autoapi_type = "python"
autoapi_file_patterns = ["*.py"]
autoapi_generate_api_docs = True
autoapi_options = ["members", "undoc-members"]
autoapi_root = "api"
autoapi_add_toctree_entry = False
autoapi_include_inheritance_graphs = False
autoapi_include_summaries = True
autoapi_python_class_content = "class"
autoapi_python_use_implicit_namespaces = False
autoapi_keep_files = False  # True for debugging

# InterSphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "kivy": ("https://kivy.org/doc/stable/", None),
}