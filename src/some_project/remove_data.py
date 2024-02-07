"""
Remove the demonstrational data dir and contents.
"""

import pathlib
import shutil

# Get the data directory.
data_dir = pathlib.Path("data")

# Remove the data directory
shutil.rmtree(data_dir, ignore_errors=True)
