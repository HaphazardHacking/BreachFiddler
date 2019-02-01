import os
import sys

if len(sys.argv) < 2:
    print("ERROR: Please specify the root directory containing the files you wish to deduplicate")
else:
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print("ERROR: Directory not found.")
    else:
