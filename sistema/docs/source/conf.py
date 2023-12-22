# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Biblioteca_SanMarcosApostol'
copyright = '2023, Diego Hernandez - Marialejandra Holguin - Catalina Fabres'
author = 'Diego Hernandez - Marialejandra Holguin - Catalina Fabres'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'sistema.settings'
django.setup()


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary', 
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',  # Para admitir docstrings en formato Google
    'sphinx_rtd_theme',  # Agregar el tema para el PDF
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
}

master_doc = 'index'  # Define master_doc

latex_documents = [
    (master_doc, 'Biblioteca_SanMarcosApostol.tex', 'Biblioteca San Marcos Apostol Documentation',
     'Diego Hernandez - Marialejandra Holguin - Catalina Fabres', 'manual'),
]


# -- Autodoc configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

autodoc_member_order = 'bysource'
autodoc_default_options = {
    'member-order': 'bysource',
    'undoc-members': True,
    'show-inheritance': True,
}

# -- Napoleon extension configuration ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html

napoleon_google_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
