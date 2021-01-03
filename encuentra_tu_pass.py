import argparse
import sys, mmap
import difflib
import requests
import os
from tqdm import tqdm

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print(bcolors.WARNING + "saving as " + bcolors.OKBLUE + filename)
        total_size_in_bytes= int(r.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                progress_bar.update(len(chunk))
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))

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

parser = argparse.ArgumentParser(description='Encuentra tu password en diccionarios públicos')
parser.add_argument('-p', '--pass', required=True, help=' -p mi_password ')
parser.add_argument('-d', '--download', action="store_true" ,help=' Usa la flag -d si quieres descargar los wordlists')
args = vars(parser.parse_args())

password = args['pass']
download_param = args['download']
path_wordlist = "Wordlists"

try:

    query = '"' + str(password) + '"wordlist" "filetype:txt'

    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
        print(bcolors.OKGREEN + "URL ->",j) 
        if download_param:
                
            if j.find('/'):
                filename = j.rsplit('/', 1)[1]
                download(j, dest_folder=path_wordlist)
    
        
    #my_file = open('rockyou.txt', "r", encoding="ISO-8859-1")
    #content_list = my_file. readlines()
    #print("largo: ", len(content_list))
    
    # Check if string 'is' is found in file 'sample.txt'
    #if check_if_string_in_file('rockyou.txt', password):
    #    result = difflib.get_close_matches(password, content_list)
    #    print('Yes, string found in file. ', result)
    #else:
    #    print('String not found in file')        
   
except:
        
    print('\n')
    sys.exit(0)
