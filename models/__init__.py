#!/usr/bin/python3
"""instantiates the storge engin either DBStorage or FileStorage"""
from os import getenv


storage_base = getenv("HBNB_TYPE_STORAGE")

if storage_base == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
