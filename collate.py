import os
import sys
import funcs

if len(sys.argv) < 2:
    print("Please specify the root directory containing the files you wish to collate")
else:
    size_buffer = 0
    file_num_count = 0
    root_dir = sys.argv[1]
    for root, dirs, files in os.walk(root_dir, onerror=None):  
        for filename in files:  
            unsorted_file = os.path.join(root, filename)
            file_size = os.path.getsize(unsorted_file)
            size_buffer = size_buffer + file_size
            file_num_count_str = str(file_num_count)
            out = os.path.join(root,file_num_count_str)
            with open(out, "a") as out_file: 
                if size_buffer < 1073741824:
                    #do stuff and write into file 
                else:
                    size_buffer = file_size
                try:
                    with open(unsorted_file, "rb") as in_file:
                        count = 0
                        for line in in_file:  
                            try:
                                line = line.decode("utf-8")  
                            except ValueError:  
                                continue
                except(IOError, OSError):
                    pass