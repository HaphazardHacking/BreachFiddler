import os
import sys
import funcs
import time
         
if len(sys.argv) < 3:
    print("ERROR: Two arguments required: domainsort.py <root_directory_of_files_to_sort> <file_containing_list_of_domains>")
else:
    root_dir = sys.argv[1]
    domain_list_file = sys.argv[2]
    if not os.path.isdir(root_dir):
        print("ERROR: Directory not found.")
    elif not os.path.exists(domain_list_file ):
        print("ERROR: List of domains not found.")
    else:
        output_dir = os.path.join(root_dir,"_domain_sort_output")
        if not os.path.isdir(output_dir):
            print("Creating output directory...")
            os.makedirs(output_dir)
        with open(domain_list_file) as domain_list:
            start = time.time()
            line_total = 0
            match_total = 0
            for root, dirs, files in os.walk(root_dir, onerror=None):
                for filename in files:
                    if "domain_sort_output" in filename:
                        continue
                    unsorted_file = os.path.join(root, filename)
                    with open(unsorted_file, "r") as in_file:
                        print("Using {} as infile".format(unsorted_file))
                        match_count = 0
                        line_count = 0
                        for line in in_file:
                            line_count += 1
                            domain = funcs.between(line,"@",":")
                            if domain == "":
                                domain = funcs.between(line,"@",";")
                            if domain == "":
                                continue
                            for domain_line in domain_list:
                                print("Checking {} against {}".format(domain,domain_line))
                                if domain == domain_line.strip('\n'):
                                    match_count += 1
                                    out_file_name = os.path.join(output_dir,domain)
                                    with open(out_file_name, "a") as out_file:
                                        out_file.write(line)
                            domain_list.seek(0)
                        match_total += match_count
                        end = time.time()
                        time_taken = end - start
                        
                        print("Time taken: {}".format(time_taken))
                        print("Line processed: {}".format(line_count))
                        print("Number of matches: {}".format(match_total))

                        #print("Found {} matches from {} lines in {}. Total matches: {}".format(match_count,line_count,filename,match_total))