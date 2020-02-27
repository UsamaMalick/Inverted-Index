

import os

def doc_ids():
    try:
        doc_id_file = open("doc_ids.txt", "w")
    except IOError:
        print("File Error occurred!")
        return

    path = 'alldocs/'
    files = []
    ids = 100
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
            document = str(ids) + '\t' + str(file) + '\n'
            ids = ids + 1
            doc_id_file.write(document)

    # for f in files:
    #     print(f)

    # print(str(len(files)))



doc_ids()
