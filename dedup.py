import os
import sys

if len(sys.argv) < 2:
    print("ERROR: Please specify the root directory containing the files you wish to deduplicate")
else:
    lines_seen = set()
    file_num_count = 0
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print("ERROR: Directory not found.")
    else:
        output_dir = os.path.join(root_dir,"_dedup_output")
        if not os.path.isdir(output_dir):
            print("Creating output directory...")
            os.makedirs(output_dir)
        out_file_name = "_dedup_output_.txt"
        dedup_file = os.path.join(output_dir,out_file_name)
        dupe_count = 0
        for root, dirs, files in os.walk(root_dir, onerror=None):  
            with open(dedup_file, 'a') as out_file:
                for filename in files:
                    if "dedup_output" in filename:
                        continue
                    collated_file = os.path.join(root, filename)
                    with open(collated_file, 'r') as in_file:
                        line_count = 0
                        for line in in_file:
                            if line not in collated_file:
                                out_file.write(line)
                                line_count =+ 1
                            else:
                                dupe_count =+ 1
                        print("Found {0} unique entries in {1}. Ingored {2} duplicates.".format(line_count,filename,dupe_count))
                                