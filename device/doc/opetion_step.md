1. run into doc dir;
2. sphinx-quickstart
3. conf.py; modify extention to:
   extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax']

4. sphinx-apidoc -o source ../api 