all: test run

clean:
	@find . -name '*.pyc' -delete

test:
	@echo "Running unit + functional tests ..."
	@nosetests -s --with-coverage --cover-package=macherie tests/unit tests/functional
	@echo "Done."
	@make acceptance
unit:
	@echo "Running unit tests ..."
	@nosetests -s --with-coverage --cover-package=macherie tests/unit
	@echo "Done."

functional:
	@echo "Running functional tests ..."
	@nosetests -s --with-coverage --cover-package=macherie tests/functional
	@echo "Done."

acceptance:
	@echo "Running acceptance tests ..."
	@pyccuracy_console -u http://localhost:8080 -d `pwd`/tests/acceptance -v 1
	@echo "Done."

run:
	@echo "Running server ..."
	@python macherie/__init__.py
	@echo "Done."