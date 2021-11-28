"""Sphinx configuration."""
from datetime import datetime


project = "Job Application"
author = "Juan Henao"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
autodoc_typehints = "description"
