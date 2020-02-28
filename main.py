import os

def doc_ids():
    try:
        doc_id_file = open("doc_ids.txt", "w")
    except IOError:
        print("File Error occurred!")
        return -1 #return -1 if error occurs
    path = 'alldocs/'
    files = []
    ids = 100

    for r, d, f in os.walk(path): # r=root, d=directories, f = files
        for file in f:
            files.append(os.path.join(r, file))
            document = str(ids) + '\t' + str(file) + '\n'
            ids = ids + 1
            doc_id_file.write(document)

    doc_id_file.close()
    return files



def term_ids(files_path):
    try:
        term_id_file = open("term_ids.txt", "w")
    except IOError:
        print("File Error occurred!")
        return -1  #return -1 if error occurs
    ids = 100 #ids start from 100

    for path in files_path:
        print (path)
        file = open(path , "r")
        for word in file.read().split():
            print(word.lower())
        break


    # for r, d, f in os.walk(path): # r=root, d=directories, f = files
    #     for file in f:
    #         term_with_id = str(ids) + '\t' + str(file) + '\n'
    #         ids = ids + 1
    #         term_id_file.write(term_with_id)


files_path = doc_ids() # file mapping a document's filename (without path) to a unique integer

if(files_path is not -1):
    term_ids(files_path)
