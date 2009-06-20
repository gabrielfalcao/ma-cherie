all: test

clean:
	@find . -name '*.pyc' -delete

test: unit functional acceptance

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