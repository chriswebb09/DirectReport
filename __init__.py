#!/usr/bin/env python
from commandline import storage
from browserview import app

def test():
    store = storage.DataStorage()
    store.makeDBConnection()
    #LINK - app()


if __name__ == "__main__":
    test()