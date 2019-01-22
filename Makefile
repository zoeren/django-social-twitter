coverage:
	python --version
	coverage erase
	DJANGO_SETTINGS_MODULE=tests.settings \
		coverage run -m django test -v2 $${TEST_ARGS:-tests}
	coverage report
	coverage html