import os , re , string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


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
        doc_ids[content[i+1]] = content[i]

    return doc_ids


def inverted_index(corpus , doc_ids):
    try:
        term_index_file = open("term_index.txt", "w")
    except IOError:
        print("File Error occurred!")
        return -1  # return -1 if error occurs

    inverted_index = {}

    for key, value in corpus.items():
        inverted_index[value] = {"total_doc":0,
                                 "count":0,
                                 "doc_pos":[]}

    for key , value in doc_ids.items():
        document_id = value
        path = "alldocs/" +  key
        print (key)
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

        for key, value in corpus.items():
            word_in_doc[key] = "not_present"

        for word in terms:
            if word in corpus:

                word_id = corpus[word]
                word_position = terms.index(word)
                terms[word_position] = None

                # make a single object of document_id and word_position and store it in the list
                doc_pos_temp = [document_id , word_position]

                # increment word Occurrence Count in numpy array of specific term.
                inverted_index[word_id]["count"] = inverted_index[word_id]["count"] + 1
                inverted_index[word_id]["doc_pos"].append(doc_pos_temp)


                if word_in_doc[word] == "not_present":
                    word_in_doc[word] = "is_present"
                    # increment total Document Count in numpy array of specific term.
                    inverted_index[word_id]["total_doc"] = inverted_index[word_id]["total_doc"] + 1
            else:
                print("Word Conflict in in Document : " + key)


        # the question is do I have to remove stopping words or not  because removing
        # them will actually disturb the position of other terms
        # do i have to remove numeric values as well?

    print ("Starting building term_index")
    for key , value in inverted_index.items():
        total_count = inverted_index[key]["count"]
        doc_count = inverted_index[key]["total_doc"]
        lists = inverted_index[key]["doc_pos"]
        index_item = str(key) + " " + str(total_count) + " " + str(doc_count)
        sum_term = 0
        sum_doc = 0

        for item in lists:
            docID = item[0]
            termID = item[1]
            deltaCode_doc = int(docID) - sum_doc
            sum_doc = sum_doc + deltaCode_doc
            if docID is not sum_term:
                sum_term = 0
            deltaCode_term = termID - sum_term
            sum_term = sum_term + deltaCode_term
            index_item = index_item + " " + str(deltaCode_doc) + "," + str(deltaCode_term)

            # index_item = index_item + " " + str(docID) + "," + str(termID)
        index_item = index_item + '\n'
        term_index_file.write(index_item)

    term_index_file.close()
    return inverted_index
    # write data into term_index.txt according to the specific order given in the document


corpus = load_dictionary()
doc_ids = load_doc_ids()
index_inverted = inverted_index(corpus , doc_ids)
