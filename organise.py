import os
import sys
import funcs
import gzip

if len(sys.argv) < 2:
    print("Please secify the root directory containing the files you wish to organise")
else:
    #step 1 - organise infile files based on domain name. max file size - 4GB
    #step 2 - compress all original files with gzip
    # with zip.open as newfile
    # size_buffer = 0
    #for each unsorted file
    # file_size = os.path.getsize(file)
    # if (size_buffer + file_size) > 1073741824:
    #   break, 
    #else
    root_dir = sys.argv[1]
    for root, dirs, files in os.walk(root_dir, onerror=None):  
        for filename in files:  
            unsorted_file = os.path.join(root, filename)  
            try:
                with open(unsorted_file, "rb") as in_file:
                    count = 0
                    for line in in_file:  
                        try:
                            line = line.decode("utf-8")  
                        except ValueError:  
                            continue
                        domain = funcs.between(line,"@",":")
            except (IOError, OSError):
                pass