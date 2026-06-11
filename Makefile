# Run a solution with the repo root on PYTHONPATH, so `from helpers...` resolves.
# Usage: make run FILE=patterns/<pattern>/<problem>/solution.py

export PYTHONPATH := $(CURDIR)

.PHONY: run
run:
	python3 $(FILE)
