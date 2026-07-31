# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

import pyvista
from pyvista.plotting.utilities.sphinx_gallery import DynamicScraper
from sphinx_gallery.sorting import FileNameSortKey

sys.path.insert(0, os.path.abspath('../src/esprsim'))
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'esprsim'
copyright = '2026, Achim Geissler'
author = 'Achim Geissler'
release = '0.8.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_gallery.gen_gallery",
    "myst_parser",
    "matplotlib.sphinxext.plot_directive",
    "pyvista.ext.plot_directive",
    "pyvista.ext.viewer_directive",
]
source_suffix = {
    ".rst": "restructuredtext",
}
sphinx_gallery_conf = {
    "examples_dirs": ["../examples"],
    # "gallery_dirs": ["examples", "tutorial"],
    "image_scrapers": (DynamicScraper(), "matplotlib"),
    "download_all_examples": False,
    "remove_config_comments": True,
    "reset_modules_order": "both",
    "filename_pattern": "ex.*\\.py",
    "backreferences_dir": None,
    "pypandoc": True,
    "capture_repr": ("_repr_html_",),
    "within_subsection_order": FileNameSortKey,
}

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
#html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_build_dir = os.environ.get('READTHEDOCS_OUTPUT', 'docs/en/build/html')
