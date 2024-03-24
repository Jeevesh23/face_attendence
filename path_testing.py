import os

# Path to the XML file
xml_file_path = r"C:\Jeevesh\me\face_attendenc\data"

# Check if the file exists
if os.path.isfile(xml_file_path):
    print("XML file exists at the specified path.")
else:
    print("XML file does not exist at the specified path.")
