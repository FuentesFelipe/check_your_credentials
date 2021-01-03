import argparse
import sys, mmap
import difflib

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False

my_file = open('rockyou.txt', "r", encoding="ISO-8859-1")
content_list = my_file. readlines()
print("largo: ", len(content_list))

try:

    parser = argparse.ArgumentParser(description='Encuentra tu password en diccionarios públicos')
    parser.add_argument('-p', '--pass', required=True, help=' -p mi_password ')
    parser.add_argument('-d', '--dictio', help=' -d dictionary.txt')

    args = vars(parser.parse_args())
    password = args['pass']

    if args['dictio']:

        dictionary = args['dictio']
            
    else:
        dictionary= 'rockyou.txt'
    
        # Check if string 'is' is found in file 'sample.txt'
    if check_if_string_in_file('rockyou.txt', password):
        result = difflib.get_close_matches(password, content_list)
        print('Yes, string found in file. ', result)
    else:
        print('String not found in file')        
   
except:
        
    print('\n')
    sys.exit(0)
