#!/usr/local/bin/python3

# Python file for generating a table of contents

import glob
import re
import sys 
import ntpath

def path_leaf(path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

def first_parent(path):
    parent = re.search("([^/]*)\/", path)
    if not parent:
        re
    return parent.group(0) or ""

def main_folders():
    paths = {}
    for path in glob.glob('*/'):
        paths[path] = []
    return paths

def generate_table(paths_dict):
    output = ""
    for directory, files in paths_dict.items():
        output += "\n### " + directory + "\n"
        for f in files:
            output += "* ["+list(f.keys())[0]+"](" +list(f.values())[0]+ ")\n" 

    return output

def main():
    paths = main_folders()
    paths['Miscellaneous'] = []
    for filename in glob.glob('**/*.md', recursive=True):
            if (filename.find('/') > 0):
                first_dir = re.search("([^/]*)\/", filename).group(0)
                file_name = path_leaf(filename)
                paths[first_dir].append({file_name: filename})
            else:
                paths['Miscellaneous'].append({filename: filename})
    paths = {k:v for k,v in paths.items() if len(v) > 0}
    output_file = sys.argv[1] 
    between = ['<!--TABLE-->', '<!--/TABLE-->']
    file = open(output_file, 'r')
    table = generate_table(paths).splitlines()
    l = file.readlines()
    next_replace = False
    for line in list(l):
        if between[0] in line:
            next_replace = True
            continue
        elif between[1] in line:
            next_replace = False
        elif next_replace:
            l.remove(line)
    for index, line in enumerate(list(l)):
        if between[0] in line:
            for new_line in reversed(table):
                l.insert(index+1, new_line)
    file.close()
    file = open(output_file, 'w')
    for line in l:
        if line is not "\n":
            file.write(line+"\n")
    file.close()


if __name__ == '__main__':
    main()
