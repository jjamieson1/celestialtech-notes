# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CelestialTech-Notes'
copyright = '2024, James Jamieson'
author = 'James Jamieson'
release = 'R1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_dark_mode','sphinxcontrib.mermaid']
pygments_style = ('solarized-dark')
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx-rtd-dark-mode'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']