# SPDX-FileCopyrightText: None
# SPDX-License-Identifier: None
#
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import datetime
import shutil
import pathlib

import pyvista
from pyvista.plotting.utilities.sphinx_gallery import DynamicScraper
from sphinx_gallery.sorting import FileNameSortKey

sys.path.insert(0, os.path.abspath('../src/esprsim'))
sys.path.insert(0, os.path.abspath('../src'))

# When building the docs, ensure example runner sees the example `cfg` folder
# so examples that open config files run correctly during `make html`.
try:
    docs_dir = pathlib.Path(__file__).resolve().parent
    repo_root = docs_dir.parent
    cfg_dir = repo_root / 'examples' / 'ex1' / 'cfg'
    if cfg_dir.exists():
        os.chdir(str(cfg_dir))
        print(f"Sphinx: changed working directory to {cfg_dir}")
except Exception:
    pass

# examples_src = pathlib.Path(__file__).resolve().parent.parent / 'examples'
# examples_dst = pathlib.Path(__file__).resolve().parent / '_examples'
# if examples_src.exists():
#     if examples_dst.exists():
#         shutil.rmtree(examples_dst)
#     shutil.copytree(examples_src, examples_dst)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "esprsim"
year = datetime.date.today().year
copyright = f"2022-{year}, Achim Geissler"
author = "Achim Geissler"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    # "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_codeautolink",
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
    "gallery_dirs": ["examples"],
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
intersphinx_mapping = {
    "esprsim": ("https://esprsim.readthedocs.io/en/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "python": ("https://docs.python.org/3/", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_title = "esprsim"

html_static_path = ['_static']
html_css_files = ["custom.css"]

html_theme_options = {
    "icon_links": [
        # {
        #     "name": "Discussions",
        #     "url": "https://github.com/AGeissler/esprsim/discussions",
        #     "icon": "fa-solid fa-comment",
        #     "type": "fontawesome",
        # },
        {
            "name": "GitHub",
            "url": "https://github.com/AGeissler/esprsim",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        {
            "name": "Read the Docs",
            # "url": "https://readthedocs.org/projects/esprsim",
            "url": "https://esprsim.readthedocs.io/en/latest",
            "icon": "fa-solid fa-book",
            "type": "fontawesome",
        },
    ],
    "logo": {
        "text": "esprsim",
        "image_light": "_static/esplogosmall.bmp",
        "image_dark": "_static/esplogosmall.bmp",
    },
    "use_edit_page_button": True,
}

html_context = {
    "github_user": "AGeissler",
    "github_repo": "esprsim",
    "github_version": "master",
    "doc_path": "docs/",
}

html_build_dir = os.environ.get('READTHEDOCS_OUTPUT', 'docs/en/build/html')
