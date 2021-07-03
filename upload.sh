pelican content -t Hola -o output -s publishconf.py
ghp-import output -b gh-pages
git push -f origin gh-pages
