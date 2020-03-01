import os , re , string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


class doc_term:
    def __init__(self, doc_id , term_pos):
        self.doc_id = doc_id
        self.term_pos = term_pos

class index:
    def __init__(self, term_id):
        self.term_id = term_id
        self.count = 0
        self.total_doc = 0
        self.list = []



def load_dictionary():
    corpus = {}
    path = "term_ids.txt"
    try:
        file = open(path , "r")
    except IOError:
        print("File Error occurred!")
        return -1  # return -1 if error occurs

    content = file.read().split()
    for i in range(0, len(content) , 2):
        # print(str(i) + " " + content[i] + " " + content[i+1])
        corpus[content[i+1]] = content[i]

    return corpus


def load_doc_ids():
    doc_ids = {}
    path = "doc_ids.txt"
    try:
        file = open(path , "r")
    except IOError:
        print("File Error occurred!")
        return -1  # return -1 if error occurs

    content = file.read().split()
    for i in range(0, len(content) , 2):
        # print(str(i) + " " + content[i] + " " + content[i+1])
        doc_ids[content[i+1]] = content[i]

    return doc_ids


def inverted_index(corpus , doc_ids):
    try:
        term_index_file = open("term_index.txt", "w")
    except IOError:
        print("File Error occurred!")
        return -1  # return -1 if error occurs
    ids = 100 # ids start from 100

    inverted_index = {}

    for key , value in doc_ids.items():
        path = "alldocs/" +  key
        print (path)
        try:
            file = open(path , "r")
        except IOError:
            print("File Error occurred!")
            return -1  # return -1 if error occurs
        content = file.read().lower() # converting to lower case
        content = re.sub(r'\w*\d\w*', '', content) #removing numeric entries
        content = content.translate(str.maketrans('','', string.punctuation)) # removing punctuation and symbols
        stop_words = stopwords.words('english') # loading stopwords from nltk
        content = content.split()
        terms = [word for word in content if word not in stop_words] # removing stop words
        ps = PorterStemmer()
        terms = [ps.stem(word) for word in terms] # stemming words

        word_in_doc = {} # copy term as key into word_in_doc key and initialise its default value not_present

        for word in terms:
            if word in corpus:

                word_id = corpus[word]
                document_id = value
                word_position = terms.index(word)
                # make a single object of document_id and word_position and store it in the list of numpy array
                # increment word Occurrence Count in numpy array of specific term.

                if word_in_doc[word] == "not_present":
                    word_in_doc[word] = "is_present"
                    # increment total Document Count in numpy array of specific term.
                    pass
            else:
                print("Word Conflict in in Document : " + key)

        # the question is do I have to remove stoping words or not  because removing
        # them will actually disturb the position of other terms
        # do i have to remove numeric values as well?

    term_index_file.close()
    # write data into term_index.txt according to the specific order given in the document


corpus = load_dictionary()
doc_ids = load_doc_ids()
inverted_index(corpus , doc_ids)

word = 	"without"
if word in corpus:
    print("Given Word ID is : " + corpus[word])
else:
    print("Word out if scope")
