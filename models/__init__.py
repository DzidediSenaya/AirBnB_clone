#!/usr/bin/python3
"""
Creates a unique FileStorage instance for the application.
"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Call the reload() method on the storage variable
storage.reload()
