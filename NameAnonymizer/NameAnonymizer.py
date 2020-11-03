import nltk
import os
import docx

def preprocess(text):
    outputFile = "outputFile" + fileExtension

    ne_person = []
    ne_person_list = []
    ne_name = ''

    ne_tree = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))) # Chunk, tokenize and label text
    print(ne_tree)

    for subtree in ne_tree.subtrees(filter=lambda t: t.label() == 'PERSON'): # Filter every instance of the named entity with tag PERSON
        # print(subtree)
        for leaf in subtree.leaves():
            ne_person.append(leaf[0]) # Append part of full name with title
            # print (ne_person)
        for part in ne_person:
            ne_name += part + ' ' # Add part of persons name to complete it
            #print(part)
        if ne_name[:-1] not in ne_person_list:
            ne_person_list.append(ne_name[:-1]) # Append full name to person list
            #print (ne_name)
        ne_name = ''
        ne_person = []
        for ne_full_name in ne_person_list: # Replace all full name occurances with a tag 'person' // Change to unique ID
            text = text.replace(ne_full_name, 'PERSON')

    print(ne_person_list) # Print names for DEBUG PURPOSES

    newPathOut = os.path.relpath('..\\dataSet\\' + outputFile , curPath) # Make new relative path to file
    if fileExtension == ".txt":
        with open(newPathOut, 'w', encoding = 'utf-8') as outputFile: # Open file
            outputFile.write(text)
            outputFile.close()
    elif fileExtension == ".docx":
        output = docx.Document()
        output.add_paragraph(text)
        output.save(newPathOut)


text = ""
fileExtension = ".docx"
curProjectFile = "NameAnonymizer.sln"
inputFile = "inputFile" + fileExtension
curPath = os.path.dirname(curProjectFile) # Point to the current project folder

newPathIn = os.path.relpath('..\\dataSet\\' + inputFile , curPath)
if fileExtension == ".txt":
    with open(newPathIn, 'r', encoding = 'utf-8') as inputFile:
        text = inputFile.read()
        inputFile.close()
elif fileExtension == ".docx":
    document = docx.Document(newPathIn)
    for paragraph in document.paragraphs: 
        paragraph = paragraph.text
        text = text + paragraph

preprocess(text)