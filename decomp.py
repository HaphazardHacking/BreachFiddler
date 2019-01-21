import os
import sys
import tarfile

if len(sys.argv) < 2:
    print("Please specify the root directory containing the files you wish to organise")
else:
    root_dir = sys.argv[1]
    os.chdir(root_dir)
    for root, dirs, files in os.walk(root_dir, onerror=None):  
        for filename in files: 
            unsorted_file = os.path.join(root, filename)  
            if unsorted_file.endswith(".tar.gz"):
                try:
                    with tarfile.open(unsorted_file) as in_tar_file:
                        print("Uncompressing: " + unsorted_file)
                        in_tar_file.extractall()
                        print("Successfully Extracted: " + unsorted_file)
                    os.remove(unsorted_file)
                    print("Cleaned up: " + unsorted_file)
                except (IOError, OSError):
                    print("Unable to read: " + unsorted_file)
                    pass