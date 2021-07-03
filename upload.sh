pelican content -t Hola -o output -s publishconf.py
ghp-import output -b master
git push -f origin master
