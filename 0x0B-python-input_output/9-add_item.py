#!/usr/bin/python3
from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
count = 0

with open(filename, "r", encoding='utf8') as f:
    for line in f:
        count += 1
    f.close()
        
if (count > 0):
    old_list = load_from_json_file(filename)
else:
    old_list = []

i = 1
while i < (len(argv)):
    old_list.append(argv[i])
    i += 1

save_to_json_file(old_list, filename)
