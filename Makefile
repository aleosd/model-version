test:
	pytest --cov=model_version --showlocals -v

fmt:
	black ./ -l 99
	isort .
