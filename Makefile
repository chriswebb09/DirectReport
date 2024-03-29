TMPREPO=/tmp/docs/DirectReport

#########
# BUILD #
#########
develop:  ## install dependencies and build library
	python3 -m pip install Flask --user
	python3 -m pip install Flask-Login --user
	python3 -m pip install flask_httpauth --user
	python3 -m pip install -e .[develop]

build:  ## build the python library
	python3 setup.py build build_ext --inplace

install:  ## install library
	python3 -m pip install --user .

#########
# LINTS #
#########
lint:  ## run static analysis with flake8
	python3 -m black --check DirectReport setup.py
	python3 -m flake8 DirectReport setup.py --ignore=E501,F401,F403

# Alias
lints: lint

format:  ## run autoformatting with black
	python3 -m black DirectReport/ setup.py

# alias
fix: format

check:  ## check assets for packaging
	check-manifest -v

# Alias
checks: check

annotate:  ## run type checking
	python3 -m mypy ./DirectReport

#########
# TESTS #
#########
test:
    ## clean and run unit tests
	python3 -m pytest -v DirectReport/tests/

coverage:  ## clean and run unit tests with coverage
	python3 -m pytest -v DirectReport/tests --cov=DirectReport --cov-branch --cov-fail-under=5 --cov-report term-missing

# Alias
tests: clean develop build test

###########
# VERSION #
###########
show-version:
	bump2version --dry-run --allow-dirty setup.py --list | grep current | awk -F= '{print $2}'

patch:
	bump2version patch

minor:
	bump2version minor

major:
	bump2version major

########
# DIST #
########
dist-build:  # Build python dist
	python3 setup.py sdist bdist_wheel

dist-check:
	python3 -m twine check dist/*

dist: clean build dist-build dist-check  ## Build dists

publish:  # Upload python assets
	echo "would usually run python -m twine upload dist/* --skip-existing"
	
########
# PAGES #
########

docs:
	$(MAKE) -C docs/ clean
	$(MAKE) -C docs/ html

pages:
	rm -rf $(TMPREPO)
	git clone -b gh-pages git@github.com:chriswebb09/DirectReport.git $(TMPREPO)
	rm -rf $(TMPREPO)/*
	cp -r docs/source/html/* $(TMPREPO)
	cd $(TMPREPO);\
	git add -A ;\
	git commit -a -m 'auto-updating docs' ;\
	git push

serve:
	cd docs/source/html; \
	python3 -m http.server 9087

#########
# CLEAN #
#########

clean: ## clean the repository
	rm -rf .coverage coverage cover htmlcov logs build dist *.egg-info .pytest_cache

############################################################################################

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: develop build install lint lints format fix check checks annotate test coverage show-coverage tests show-version patch minor major dist-build dist-check dist publish deep-clean clean help
