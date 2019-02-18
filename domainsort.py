import os
import sys
import funcs
import time
import datetime


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

        domain_list = funcs.file_to_list(domain_list_file)
        prefix = "@"
        domain_list = [prefix + x for x in domain_list]
        line_total = 0
        match_total = 0
        time_total = 0
        for root, dirs, files in os.walk(root_dir, onerror=None):
            for filename in files:
                if "_sorted_" not in filename:
                    start = time.time()
                    
                    unsorted_file = os.path.join(root, filename)
                    in_file = funcs.file_to_list(unsorted_file)
                    line_count = len(in_file)
                    line_total += line_count
                    
                    print("\nProcessing {}...".format(filename))
                    matches = [s for s in in_file if any(xs in s for xs in domain_list)]
                    match_total += len(matches)
                    
                    end = time.time()
                    time_taken_int = int(end - start)
                    time_taken = str(datetime.timedelta(seconds=time_taken_int))
                    time_total += time_taken_int

                    print("\nTime taken: {}".format(time_taken))
                    print("Combos processed: {}".format(line_count))
                    print("Number of matches: {}".format(len(matches)))
                    print("\nWriting results to output directories...")
                    
                    for match in matches:
                        domain = funcs.between(match,"@",":")
                        if domain == "":
                            domain = funcs.between(match,"@",";")
                        if domain == "":
                            continue
                        filename = ("_sorted_" + domain)
                        out_file_name = os.path.join(output_dir,filename)
                        with open(out_file_name, "a") as out_file:
                            out_file.write(match + "\n")
                    print("Done!")

        time_taken = str(datetime.timedelta(seconds=time_total))
        
        out_files_total = 0
        for root, dirs, files in os.walk(output_dir):
            out_files_total += len(files)
        
        print("\n\n****************************************")
        print("Total time taken: {}".format(time_taken))
        print("Total combos processed: {}".format(line_total))
        print("Total matches found: {}".format(match_total))
        print("****************************************")