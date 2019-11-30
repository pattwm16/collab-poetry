# LITR 0110D Final Project
import textract
import os
import re

# open a file to write the corpus
corpus = open("/Users/Will/Desktop/myfile1.txt","w")

# for each collected file in the test folder, get path and textract
list_of_files = os.listdir('/Users/Will/Desktop/test')
list_of_files.remove(".DS_Store")
list_of_files.sort()
for file in list_of_files:
    # listing file
    print("Starting file {}".format(file))
    # collect the extension, needed for textract
    ext = os.path.splitext(file)[-1].lower()
    # concatenate to get path
    path = str("/Users/Will/Desktop/test/" + file)
    # extract text from file
    text_to_write = textract.process(path, extension=ext).splitlines()
    text_to_write = list(map(lambda x: x.strip().decode("utf-8") , text_to_write))
    text_to_write = [i for i in text_to_write if i]
    # write the text to the corpus file
    # corpus.writelines(list(map(lambda x: x.strip(), str(text_to_write).splitlines())))
    text_to_write = re.sub(r'[^\x00-\x7f]',r'', "\n".join(text_to_write))
    corpus.writelines(text_to_write.splitlines())

# remember to close out the file
corpus.close()
