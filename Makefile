dist/logtimes: logtimes/__init__.py cli.py Makefile
	pyinstaller -F ./cli.py -n logtimes
