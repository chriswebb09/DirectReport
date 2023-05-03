# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DirectReport'
copyright = '2023, Christopher Webb-Orenstein'
author = 'Christopher Webb-Orenstein'
release = '1.0.0'
import sphinx_rtd_theme
import os               # line 13
import sys              # line 14
sys.path.insert(0, os.path.abspath('../../../DirectReport'))
sys.path.insert(1, os.path.abspath('../../DirectReport'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'sphinx.ext.autosummary'
]

templates_path = ['_templates']
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = 'sphinx_rtd_theme'

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
#

#html_sidebars = {'searchbox.htm'}
#
#project = "DirectReport"
#version = "0.1.0"
#
## Include results from subprojects by default.
#rtd_sphinx_search_default_filter = f"subprojects:{project}/{version}"
