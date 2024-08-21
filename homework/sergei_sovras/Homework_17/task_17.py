import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("fp", help="File path")
parser.add_argument("sw", help="Search word")
parser.add_argument("-full", help="Yes for full, No fo short")
args = parser.parse_args()

folder_path = args.fp
word = args.sw
full = args.full
search_word = word.lower()
file_name = ''
flag = False

files = os.listdir(folder_path)
for file in files:
    file_path = os.path.join(folder_path, file)

    with open(file_path, 'r') as log_file:

        for line in log_file:
            line = line.lower()
            splited_line = line.split()
            if search_word in splited_line:
                flag = True

                if full == 'Yes':
                    print(f'The file {os.path.basename(file_path)} contains: {line} ')

                else:
                    place = splited_line.index(search_word)
                    if place < 5:
                        substring = ' '.join(splited_line[: place + 6])
                    else:
                        substring = ' '.join(splited_line[place - 5: place + 6])
                    print(place)
                    print(f'The file {os.path.basename(file_path)} contains subline: {substring} ')

if not flag:
    print(f'There is no includes the word {word}')
