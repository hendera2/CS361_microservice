import yaml
import time

with open('communication.yaml', 'r') as file:
    working_file = yaml.safe_load(file)

working_file['file_name'] = 'StarWars3.wav'
working_file['new_file_format'] = 'mp3'

with open('communication.yaml', 'w', encoding='utf-8') as outfile:
    yaml.dump(working_file, outfile, default_flow_style=False)

file_contents = open("file_read.txt", 'w+')
file_contents.write("run")
file_contents.close()

with open('communication.yaml', 'r') as file:
    working_file = yaml.safe_load(file)

new_file_name = working_file['new_file_name_type']
print(new_file_name)

working_file['file_name'] = None
working_file['new_file_format'] = None
working_file['new_file_name_type'] = None

with open('communication.yaml', 'w', encoding='utf-8') as outfile:
    yaml.dump(working_file, outfile, default_flow_style=False)




