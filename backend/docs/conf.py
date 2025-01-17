# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django

sys.path.insert(0, os.path.abspath(".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
django.setup()

project = 'BAI_PRO_DEMO'
copyright = '2023, Patryk Jaworski, Jakub Jach'
author = 'Patryk Jaworski, Jakub Jach'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


language = 'pl'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    "preamble": r"""
    \usepackage{listings}
    \lstset{
        language=Python,
        title=\lstname
    }
    """
}
