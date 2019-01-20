import os
import sys

if len(sys.argv) < 2:
    print("Requires at least one argument to be specified. e.g. domaindumpcheck <domainlist.csv> <start_directory>(optional)")
else:
    domain_list = sys.argv[1]
    if len(sys.argv) > 2:
        root_dir = sys.argv[2]
    else:
        root_dir = "/"
    with open(domain_list,r) as domain:
        for line in domains:
            keyword = line
            for root, dirs, files in os.walk(root_dir, onerror=None):  
                for filename in files:  
                    file_path = os.path.join(root, filename)  
                    try:
                        with open(file_path, "rb") as f:  
                            for line in f:  
                                try:
                                    line = line.decode("utf-8")  
                                except ValueError:  
                                    continue
                                if keyword in line:
                                    print(file_path)  
                                    break  
                    except (IOError, OSError):
                        pass