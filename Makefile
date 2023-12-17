default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: test
test: # Run tests (using pytest) with coverage
	pytest --cov=model_version --showlocals -v

.PHONY: fmt
fmt: # Format code with black and isort
	black ./ -l 99
	isort .
