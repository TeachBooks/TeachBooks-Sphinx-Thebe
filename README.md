*For IT2901 evaluation:* 
The only change we have made to the original repo made by TeachBooks (https://github.com/TeachBooks/Sphinx-Thebe), is to add the configuration `"mathjaxUrl": "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"` to lines 48 and 182 in `src/sphinx_thebe/__init__.py`.

# sphinx-thebe

[![Documentation](https://readthedocs.org/projects/sphinx-thebe/badge/?version=latest)](https://sphinx-thebe.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/sphinx-thebe.svg)](https://pypi.org/project/sphinx-thebe)

Integrate interactive code blocks into your documentation with Thebe and Binder.

See [the sphinx-thebe documentation](https://sphinx-thebe.readthedocs.io/en/latest/) for more details!

## Install

To install `sphinx-thebe` first install it:

```
pip install git+https://github.com/TeachBooks/Sphinx-Thebe
```

Then, add it to your Sphinx site's `conf.py` file:

```
extensions = [
    ...
    "sphinx_thebe"
    ...
]
```

See [the sphinx-thebe documentation](https://sphinx-thebe.readthedocs.io/en/latest/) for more details!
