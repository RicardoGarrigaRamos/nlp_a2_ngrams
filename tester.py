"""
Runs ngram.py with random presets
"""


import random
import re

import sys


"""print("This program generates random sentences based on an Ngram model.")
args = ""
for arg in sys.argv:
    args = args + arg + " "
print("Command line settings : " +args)

file = open("testfile.txt")
list = re.findall(r"[\w']+|[.,!?;]", file.read().lower())

print(list)
"""
"""dict = {"key": {"word":"frequency"}}

"""
"""lis = [2,2,3,3,3,4]
for word in range(len(lis)-1):
    print (lis[word],lis[word+1])"""


"""print(dict.get("key").get("word"))
print(dict)"""

"""

print(bool(re.search("[.?!]", "!")))"""

"""ngrams = {"cur_n1gram":{}}

for i in range(4):
    if "words" in ngrams["cur_n1gram"].keys():

        ngrams["cur_n1gram"]["words"] = ngrams["cur_n1gram"]["words"]+1
    else:
        ngrams["cur_n1gram"]= {"words" : 1}


print(ngrams["cur_n1gram"]["words"])"""



ngrams = {"<n-1gram>":{"<some_word>": 1}}
if "<n-1gram>" in ngrams.keys():
    if "<next_word>" in ngrams["<n-1gram>"].keys():
        ngrams["<n-1gram>"]["<next_word>"] = ngrams["<n-1gram>"]["<next_word>"]+1
    else:
        ngrams["<n-1gram>"]["<next_word>"] = 1

print (ngrams)

# python ngram.py 2 1 sotiw.txt