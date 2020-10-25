import nltk
import os

def preprocess(text):
    outputFile = "outputFile.txt"

    ne_person = []
    ne_person_list = []
    ne_name = ''

    ne_tree = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))) # Chunk, tokenize and label text

    for subtree in ne_tree.subtrees(filter=lambda t: t.label() == 'PERSON'): # Filter every instance of the named entity with tag PERSON
        for leaf in subtree.leaves():
            ne_person.append(leaf[0]) # Append part of full name with title
        for part in ne_person:
            ne_name += part + ' ' # Add part of persons name to complete it
        if ne_name[:-1] not in ne_person_list:
            ne_person_list.append(ne_name[:-1]) # Append full name to person list
        ne_name = ''
        ne_person = []
        for ne_full_name in ne_person_list: # Replace all full name occurances with a tag 'person' // Change to unique ID
            text = text.replace(ne_full_name, 'PERSON')

    print(ne_person_list) # Print names for DEBUG PURPOSES

    newPathOut = os.path.relpath('..\\dataSet\\' + outputFile , curPath)
    with open(newPathOut, 'w', encoding = 'utf-8') as outputFile:
        outputFile.write(text)

curProjectFile = "NameAnonymizer.sln"
inputFile = "inputFile.txt"
curPath = os.path.dirname(curProjectFile) # Point to the current project folder

newPathIn = os.path.relpath('..\\dataSet\\' + inputFile , curPath)
with open(newPathIn, 'r', encoding = 'utf-8') as inputFile:
    text = inputFile.read()

preprocess(text)