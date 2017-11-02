# -*- coding: utf-8 -*-

# -- General configuration -----------------------------------------------------

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'Blanc Basic Assets'
copyright = u'2014, Developer Society Ltd'

# The short X.Y version.
version = '0.3'
# The full version, including alpha/beta/rc tags.
release = '0.3'

exclude_patterns = ['_build']
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'blanc-basic-assetsdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
    ('index', 'blanc-basic-assets.tex', 'Blanc Basic Assets Documentation',
     'Developer Society Ltd', 'manual'),
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    ('index', 'blanc-basic-assets', 'Blanc Basic Assets Documentation',
     ['Developer Society Ltd'], 1)
]

# -- Options for Texinfo output ------------------------------------------------

texinfo_documents = [
    ('index', 'blanc-basic-assets', 'Blanc Basic Assets Documentation',
     'Developer Society Ltd', 'blanc-basic-assets', 'One line description of project.',
     'Miscellaneous'),
]
