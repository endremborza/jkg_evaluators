import subprocess
import os
import glob


project_name = 'jkg_evaluators'
include_api_docs = False

doc_dir_name = 'docs'
author_name = 'Endre Márk Borza'
doc_notebooks_dir = 'notebooks'
doc_reqs = ['sphinx', 'graphviz', 'sphinx-automodapi', 'pygments', 'jupyter']

subprocess.call(['rm', '-rf', doc_dir_name])

doc_notebooks = sorted(glob.glob('{}/*.ipynb'.format(doc_notebooks_dir)))

subprocess.call(['sphinx-quickstart',
                 doc_dir_name,
                 '-p',
                 project_name,
                 '-a',
                 author_name,
                 '-q',
                 '--ext-autodoc'])

subprocess.call(['jupyter',
                 'nbconvert',
                 '--to',
                 'rst',
                 *doc_notebooks,
                 '--output-dir={}/notebooks'.format(doc_dir_name)])

extensions = ['sphinx.ext.autosummary',
              'sphinx_automodapi.automodapi',
              'sphinx_automodapi.smart_resolver',
              'sphinx.ext.graphviz']
with open(os.path.join(doc_dir_name, 'conf.py'), 'a') as fp:
    fp.write('\n')
    for ext in extensions:
        fp.write("extensions.append('{}')".format(ext))
        fp.write('\n')

    fp.write('import os, sys')
    fp.write('\n')
    fp.write('sys.path.insert(0, os.path.abspath(".."))')
    fp.write('\n')
    fp.write('master_doc = "index"')
    fp.write('\n')

toc_nbs = ['   notebooks/{}'.format(np.split('/')[-1].split('.')[0])
           for np in doc_notebooks]

index_rst = """
Welcome to {}'s documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   {}
{}


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
""".format('api' if include_api_docs else '',
           project_name, '\n'.join(toc_nbs))

autosumm_rst = """

API
===

.. automodapi:: {}

""".format(project_name)

with open(os.path.join(doc_dir_name, 'index.rst'), 'w') as fp:
    fp.write(index_rst)

with open(os.path.join(doc_dir_name, 'api.rst'), 'w') as fp:
    fp.write(autosumm_rst)

with open(os.path.join(doc_dir_name, 'requirements.txt'), 'w') as fp:
    fp.write('\n'.join(doc_reqs))
