
explainer::
	pip install -e .

autodoc::
	sphinx-apidoc -o /tmp explainer

docs::
	jupyter-book build --all docs/


docs-serve::
	python -m http.server --directory docs/_build/html 9009


docs-build::
	pip install -U -r docs/requirements.txt


clean::
	rm -rf docs/_build
