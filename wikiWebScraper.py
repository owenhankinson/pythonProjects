import os
from bs4 import BeautifulSoup
import requests.exceptions
import requests


url = input('Insert Wikipedia Page ')     # The User inputs a Wikipedia Page

s = url.rfind('/')

subject_matter = url[s + 1:]             # The system parses out the subject of the page from the link


response = requests.get(url)             # A request is sent to the server for information
# Not My work (Down)-----------------------------
try:
    soup = BeautifulSoup(response.text, features="html.parser")                 # Beutiful Soup calls an html parser to use on the specified page.
except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
    pass
# End of not my work ----------------------------
link = ''
for a in soup.find_all("a"):                                                    # Finds all HTML <a> tags and makes a list of all the links using the "href" identifier
    link += a.attrs['href'] + "\n" if 'href' in a.attrs else '' + '\n'


f1 = link.split()

new_string = []

for word in f1[:]:               #Getting rid of files and junk links
    if word.find("#") >= 0:
            f1.remove(word)
    elif word.find('File:') >= 0:
            f1.remove(word)
    elif word.find('ex.php') >= 0:
            f1.remove(word)
    elif word.find('1889') >= 0:
            f1.remove(word)
    elif word.startswith("//"):
            f1.remove(word)





subjects = []
new = []
for string in f1:                         # Making the links more readable
    f2 = string.replace(string[0:5 + 1], '')
    subjects.append(f2)

for string in subjects[:]:
    if string.startswith("/"):
        subjects.remove(string)
    elif string.find('%',0, 17) >= 0:
        f4 = string.replace(string[:string.find('_') +1], '')
        new.append(f4)
        subjects.remove(string)


big_list = subjects + new                               #Making new list and sorting
new.sort()
big_list.sort()
subjects.sort()


bigger_list = []
for i in big_list[:]:
    f5 = i.replace('_', " ")
    bigger_list.append(f5)

del bigger_list[:2]

doupLess = list(dict.fromkeys(bigger_list))                 #Taking out doups

numberOfLInks = len(doupLess)


try:                                                        # Writing it on a text doc
    with open(f'{subject_matter}.txt', 'w') as document:
        document.write("All link subjects for the " + f'{subject_matter}'+ ' WikiPidia page: ' + '\n' *2)
        document.write("There are " + str(numberOfLInks) + " links on the "f'{subject_matter} WikiPedia page.' + '\n'*3)
        print(f'Writing {subject_matter}.txt...')
        print('File is located here: ', os.path.abspath(f'{subject_matter}.txt'))
        for link in doupLess:
            document.write(link + '\n')


except IOError:
    print(f'{subject_matter}.txt cannot be opened for output')

finally:
    document.close()

