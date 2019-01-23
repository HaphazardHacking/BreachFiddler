import os
import sys
import shutil
import fnmatch

def file_write():
    try:
        with open(unsorted_file, "rb") as in_file:
            with open(out, "ab") as out_file:
                shutil.copyfileobj(in_file, out_file, 1024*1024*10)
                out_file_size = os.path.getsize(out)
                print("Successfully added {0} into {1}. Output file size is now {2} bytes.".format(filename,file_num_count_str,out_file_size))
    except(IOError, OSError):
        print("ERROR: Unable to read {}, skipping.".format(filename))
        pass

if len(sys.argv) < 2:
    print("Please specify the root directory containing the files you wish to collate")
else:
    size_buffer = 0
    file_num_count = 0
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print("ERROR: Directory not found.")
    else:
        output_dir = os.path.join(root_dir,"_collation_output")
        if not os.path.isdir(output_dir):
            print("Creating output directory...")
            os.makedirs(output_dir)
        for root, dirs, files in os.walk(root_dir, onerror=None):  
            file_num_count_str = "_collation_output_{}.txt".format(str(file_num_count))
            for filename in files:
                #if fnmatch.fnmatch(filename,"*collation_output*"):
                if "collation_output" in filename:
                    continue
                unsorted_file = os.path.join(root, filename)
                file_size = os.path.getsize(unsorted_file)
                size_buffer = size_buffer + file_size
                out = os.path.join(output_dir,file_num_count_str)
                if file_size < 1024*1024*1024:
                    if size_buffer < 1024*1024*1024:
                        file_write()
                    else:
                        size_buffer = file_size
                        file_num_count += 1
                        file_num_count_str = "_collation_output_{}.txt".format(str(file_num_count))
                        file_write()
                else:
                    shutil.move(unsorted_file,out)
                    file_num_count += 1