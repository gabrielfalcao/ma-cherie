all: test run

clean:
	@find . -name '*.pyc' -delete

test:
	@echo "Running unit + functionial tests ..."
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
	@echo "Done."

run:
	@echo "Running server ..."
	@python macherie/__init__.py
	@echo "Done."