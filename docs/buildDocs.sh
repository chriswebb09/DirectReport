#####################
# DECLARE VARIABLES #
#####################

pwd
ls -lah
export SOURCE_DATE_EPOCH=$(git log -1 --pretty=%ct)

##############
# BUILD DOCS #
##############

# build our documentation with sphinx (see docs/conf.py)
# * https://www.sphinx-doc.org/en/master/usage/quickstart.html#running-the-build
make -C docs clean
make -C docs html

#######################
# Update GitHub Pages #
#######################

docroot=$(mktemp -d)
rsync -av "build/html/" "${docroot}/"

pushd "${docroot}"

git config --global user.name "chriswebb09"
git config --global user.email "chris.webb5249@gmail.com"

git remote set-url origin  "https://token:${GITHUB_TOKEN}@github.com/chriswebb09/DirectReport.git"

git config --global --add safe.directory '*'

# don't bother maintaining history; just generate fresh
git init
git remote add deploy "https://token:${GITHUB_TOKEN}@github.com/chriswebb09/DirectReport.git"
git checkout -b gh-pages


# add .nojekyll to the root so that github won't 404 on content added to dirs
# that start with an underscore (_), such as our "_content" dir..
touch .nojekyll

# copy the resulting html pages built from sphinx above to our new git repo
git add .

# commit all the new files
msg="Updating Docs for commit ${GITHUB_SHA} made on $(date -u +%FT%T%z"@${SOURCE_DATE_EPOCH}") from ${GITHUB_REF} by ${GITHUB_ACTOR}"
git commit -am "${msg}"

# overwrite the contents of the gh-pages branch on our github.com repo
git push deploy gh-pages --force

popd # return to main repo sandbox root

# exit cleanly
exit 0
