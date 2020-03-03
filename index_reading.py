
path = "term_index.txt"
file = None
try:
    file = open(path , "r")
except IOError:
    print("File Error occurred!")


content = file.read().split('\n')
# print(content)
id = 101
print(content[id-100])
# for line in content:
#     if not line:
#         break
#     parsed = line.split()
#     print(parsed[0] +" : "+ parsed[1] + " : " + parsed[2])

file.close()
