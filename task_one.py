import os , re , string
# Load library

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

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

    dict_terms = []
    for path in files_path:
        print (path)
        file = open(path , "r")
        content = file.read().lower() #converting to lower case
        content = re.sub(r'\w*\d\w*', '', content) #removing numeric entries
        content = content.translate(str.maketrans('','', string.punctuation)) #removing punctuation and symbols
        stop_words = stopwords.words('english') #loading stopwords from nltk
        content = content.split()
        words = [word for word in content if word not in stop_words] #removing stop words
        terms = list(dict.fromkeys(words)) #remmoving duplicates
        ps = PorterStemmer()
        terms = [ps.stem(word) for word in terms] #stemming words
        terms = list(dict.fromkeys(terms)) #removing duplicate words
        dict_terms = list(set(dict_terms) | set(terms))

    for final_term in dict_terms:
        id_with_term = str(ids) + '\t' + str(final_term) + '\n'
        ids = ids + 1
        term_id_file.write(id_with_term)

    term_id_file.close()
    return dict_terms


files_path = doc_ids() # file mapping a document's filename (without path) to a unique integer

dictionary = 0
if(files_path is not -1):
    dictionary = term_ids(files_path)

print(len(dictionary))
