from pydub import AudioSegment
import yaml
import time

while True:

    txt = open("file_read.txt", "r+")
    file_contents = txt.read()
    if file_contents == 'run':
        time.sleep(3)
        with open('communication.yaml', 'r') as file:
            working_file = yaml.safe_load(file)

        og_file_name_type = working_file['file_name']
        og_file_name = og_file_name_type.split('.')[0]
        new_file_format = working_file['new_file_format']
        new_file_name_type = f'{og_file_name}.{new_file_format}'
        working_file['new_file_name_type'] = new_file_name_type

        song = AudioSegment.from_wav(og_file_name_type)
        song.export(f'{og_file_name}.{new_file_format}', new_file_format)

        with open('communication.yaml', 'w', encoding='utf-8') as outfile:
            yaml.dump(working_file, outfile, default_flow_style=False)

        file_contents = open("file_read.txt", 'w+')
        file_contents.write("done")



