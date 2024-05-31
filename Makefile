all: build install

build:
	python -m build

install: build
	pip install .
uninstall:
	pip uninstall docKar

clean:
	rm -fdr build dist docKar.egg-info

.PHONY: all build install uninstall clean