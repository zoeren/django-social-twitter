coverage:
	python --version
	coverage erase
	coverage run -m django test tests --settings=tests.settings
	coverage report
	coverage html