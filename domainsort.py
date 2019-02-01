import os
import sys

if len(sys.argv) < 3:
    print("ERROR: Two arguments required: domainsort.py <root_directory_of_files_to_sort> <file_containing_list_of_domains>")
else:
    
    root_dir = sys.argv[1]
    domain_list = sys.argv[2]
    if not os.path.isdir(root_dir):
        print("ERROR: Directory not found.")
    elif not os.path.exists(domain_list):
        print("ERROR: List of domains not found.")
    else:

        output_dir = os.path.join(root_dir,"_domain_sort_output")
        if not os.path.isdir(output_dir):
            print("Creating output directory...")
            os.makedirs(output_dir)
        for root, dirs, files in os.walk(root_dir, onerror=None):
            for filename in files:
                if "domain_sort_output" in filename:
                    continue