all: build install

build:
	python -m build

install: build
	pip install .
uninstall:
	pip uninstall virtual_vehicle

clean:
	rm -fdr build dist virtual_vehicle.egg-info

.PHONY: all build install uninstall clean