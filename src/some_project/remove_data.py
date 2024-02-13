"""
Remove the demonstrational data dir and contents.
"""

import pathlib

# Get the data directory.
data_dir = pathlib.Path("data")

# list of files to individually remove
files_to_remove = [
    data_dir / "zen.txt",
    data_dir / "zen.zip",
    data_dir / "data_sub_dir" / "zen.txt",
    data_dir / "data_sub_dir" / "zen.zip",
]

# Remove the data directory
for file in files_to_remove:
    pathlib.Path(file).unlink()
