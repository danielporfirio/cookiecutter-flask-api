all: test

clean:
	rm -rf /tmp/your_project

test: clean
	cookiecutter . --output-dir /tmp --no-input && \
	cd /tmp/your_project