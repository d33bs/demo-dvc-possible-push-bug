"""
Generate zen of python text file and zip it for demonstration purposes.
"""

import pathlib
import zipfile
import codecs
import shutil

# Get the zen of python text.
import this

# referenced from: https://stackoverflow.com/a/50987949
zen_text = codecs.encode(this.s, "rot13")

# Create the data directory.
data_dir = pathlib.Path("data")
data_dir.mkdir(parents=True, exist_ok=True)

# Create the zip file.
zip_file = zipfile.ZipFile(data_dir / "zen.zip", "w")

# Write the zen text to a file.
with (data_dir / "zen.txt").open("w") as f:
    f.write(zen_text)

# Add the file to the zip file.
zip_file.write(data_dir / "zen.txt", "zen.txt")

# Close the zip file.
zip_file.close()

# copy the files to a sub dir
shutil.copytree(src="data", dst="data/data_sub_dir")
