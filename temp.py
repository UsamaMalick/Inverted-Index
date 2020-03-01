
import os , re , string

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

    def doc_term_listing(self , doc_term):
        self.list.append(doc_term)



invert_index = []
doc = doc_term(100 , 10)

temp_index = index(100)
temp_index.doc_term_listing(doc)

invert_index.append(temp_index)

# print(temp_index)
# print(doc)


