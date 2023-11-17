COMMUNICATION CONTRACT:

A. Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call:
1. Open the "communication.yaml" file and write over the following variables:
- [file_name] (the full file name--including the type--that is being converted)
- [new_file_format] (the new format desired for the conversion)

2. Open the "file_read.txt" file, clear the current contents, and write "run" to the file

EXAMPLE CALL:

    with open('communication.yaml', 'r') as file:
        working_file = yaml.safe_load(file)
    
    working_file['file_name'] = 'StarWars3.wav'
    working_file['new_file_format] = 'mp3'

    with open('communication.yaml', 'w', encoding='utf-8') as outfile:
        yaml.dump(working_file, outfile, default_flow_style=False)

    file_contents = open("file_read.txt", 'w+')
    file_contents.write("run")


B. Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.
1. The main program can recieve data from the microservice by opening the .yaml file and reading the [new_file_name_type] variable from the file AFTER requesting data from the microservice to get the new file's name.
The new, converted file itself will be saved in the same directory as the original file and can be accessed from there.

EXAMPLE CALL:

    with open('communication.yaml', 'r') as file:
        working_file = yaml.safe_load(file)
    
    new_file_name = working_file['new_file_name_type']


C. UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your partner (and your grader) will understand

![UML_sequence_diagarm](https://github.com/hendera2/CS361_microservice/assets/102428207/e2e23df1-fe86-4821-9a73-20778fc43f0a)

