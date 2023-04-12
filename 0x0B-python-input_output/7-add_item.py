#!/usr/bin/python3
""" A script that adds all arguments to a python list """
import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

del sys.argv[0]
data = sys.argv
data_saver = []
data_saver += data
filename = "add_item.json"
save_to_json_file(data_saver, filename)
load_from_json_file(filename)
