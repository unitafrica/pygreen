# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pygreen'
copyright = '2025, the PyGreen Team'
author = 'the PyGreen Team'
release = '0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['nbsphinx',
              'sphinxcontrib.bibtex'
              ]

templates_path = ['_templates']

# Avoid some warning messages
exclude_patterns = ["_notebooks/.virtual_documents/*"]


bibtex_bibfiles = ['bibliography.bib']
bibtex_reference_style = "author_year"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_show_sourcelink = False
html_logo = "_images/unitafrica_tra.png"
