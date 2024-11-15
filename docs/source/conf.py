# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DREAMS'
copyright = '2024, DREAMS collaboration'
author = 'DREAMS collaboration'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_tabs.tabs",
    "nbsphinx",
    "sphinx_gallery.load_style",
    "sphinx_rtd_theme",
    "sphinxcontrib.googleanalytics",
    "sphinx_sitemap"
]

googleanalytics_id = 'G-XRRM15GMS9'
googleanalytics_enabled = True

html_baseurl = 'https://dreams-project.readthedocs.io/en/latest/'

templates_path = ['_templates']
exclude_patterns = []

pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
#html_static_path = ['_static']

html_logo = 'Images/logo.png'

html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

html_extra_path = ["robots.txt"]
