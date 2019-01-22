coverage:
	python --version
	coverage erase
	coverage run -m django test $${TEST_ARGS:-tests} --settings=tests.settings
	coverage report
	coverage html