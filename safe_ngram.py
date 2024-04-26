"""
ngram.py
Ricardo Garriga-Ramos
CMSC-416-001 - INTRO TO NATURAL LANG PROCESS - feb 12 Spring 2024

Uses an ngram modle to generate sentences.
Runs with python n m file.txt ...
it handles numaric vaues of n and m where n is the size of the ngram and m is the number of sentences as well as any number of subsiquent text file names


This program uses regex to break a selection of text files into a list of words and punctuation 
then creates an n-1 gram which contains all n-1  grams and thier frequencies as a dictionary
and creates an ngram dictionary which contains all n-1 grams as well as the following word and it's frequency as a dictionary
using these two tables it uses the marcov assumtion and chain rule to determin probiblities for the posible next word of a sentence
using the formula P(word|n-1gram) = frq(ngram)/frq(n1gram) and continues to randomly select words until it selects punctuation m time
"""


import sys
import random
import re

def start():
    n = 0
    m = 0
    files = []

    print("This program generates random sentences based on an Ngram model.")
    args = ""
    for arg in sys.argv:
        args = args + arg + " "
    print("Command line settings : " +args)

    # posible error in arguments
    if len(sys.argv) > 3:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                if i == 1:
                    n = arg
                    if not n.isnumeric():
                        print("n is not an int.")
                        return
                    elif not (int(n) > 0):
                        print("n must be atleast 1")
                        return
                elif i == 2:
                    m = arg
                    if not m.isnumeric():
                        print("m is not an int.")
                        return
                    elif not (int(m) > 0):
                        print("m must be atleast 1")
                        return
                else:
                    files.append(arg)
    else:
        print("Not enough arguments.")
        return
    

    # main activity
    ngrams,n1grams = build_n_gram(int(n),files)
    print_m_sentences(int(n), int(m), ngrams, n1grams)


def build_n_gram(n, files):

    # ngrams dictionary of ever n-1gram : [{word:frequncy},{word:frequncy},...]
    # n1grams dictionary of unique n-1gram : frequecy in corpus
    
    
    num_start_markers = (n-1)
    start_marker = "<s> "
    n1grams = {"<n-1gram>": -1}
    ngrams = {"<n-1gram>":{"<next_word>": -1}}
    saw_punctuation = False
    #for each file add to gram dictionaries
    for file_name in files :
        with open(file_name, encoding='utf8') as file:
            
            # create tokens
            words = re.findall(r"[\w']+|[.,!?;:]", file.read().lower())
            
            # find frequencies of n and n-1
            for i in range(len(words)-(n-1)):

                # creat ngrams at start of sentences
                if saw_punctuation or i == 0:
                    saw_punctuation = False
                    
                    num_start_markers = (n-1)
                    cur_n1gram = (start_marker * num_start_markers).strip()
                    




                    # add n1gram and ngram
                    if cur_n1gram in n1grams.keys():
                        n1grams[cur_n1gram] = n1grams[cur_n1gram]+1
                        
                        if cur_n1gram in ngrams.keys():
                            if words[i-num_start_markers+(n-1)] in ngrams[cur_n1gram].keys():
                                ngrams[cur_n1gram][words[i-num_start_markers+(n-1)]] = ngrams[cur_n1gram][words[i-num_start_markers+(n-1)]]+1

                            else:
                                ngrams[cur_n1gram][words[i-num_start_markers+(n-1)]] =  1
                    else:
                        n1grams[cur_n1gram] = 1
                        
                        ngrams[cur_n1gram]= {words[i-num_start_markers+(n-1)] : 1}

                    num_start_markers = num_start_markers-1


                # create ngrams not at start of sentence    
                else:
                    cur_n1gram = ""

                    if bool(re.search("[.?!]", words[i])):
                        
                        saw_punctuation = True

                    if num_start_markers > 0:
                        # we are at the near the start of a sentence
                        cur_n1gram = start_marker * num_start_markers
                        
                        
                        back_track_index = (n-1)-(num_start_markers)
                        
                        for j in range(back_track_index):
                            cur_n1gram = cur_n1gram + words[i-(back_track_index-j)] +" "
                        
                        cur_n1gram = cur_n1gram.strip()





                        # add n1gram and ngram
                        if cur_n1gram in n1grams.keys():
                            n1grams[cur_n1gram] = n1grams[cur_n1gram]+1
                            
                            if cur_n1gram in ngrams.keys():
                                if words[i] in ngrams[cur_n1gram].keys():
                                    ngrams[cur_n1gram][words[i]] = ngrams[cur_n1gram][words[i]]+1

                                else:
                                    ngrams[cur_n1gram][words[i]] =  1
                        else:
                            n1grams[cur_n1gram] = 1
                            
                            ngrams[cur_n1gram]= {words[i] : 1}


                        # set up next iteration
                        num_start_markers = num_start_markers-1
                    



                    else:
                        #we in the middle of a sentence
                        back_track_index = (n-1)-(num_start_markers)

                        for j in range(back_track_index):
                            cur_n1gram = cur_n1gram + words[i-(back_track_index-j)] +" "
                        
                        cur_n1gram = cur_n1gram.strip()
                        
                        cur_n1gram = cur_n1gram.strip()





                        # add n1gram and ngram
                        if cur_n1gram in n1grams.keys():
                            n1grams[cur_n1gram] = n1grams[cur_n1gram]+1
                            
                            if cur_n1gram in ngrams.keys():
                                if words[i] in ngrams[cur_n1gram].keys():
                                    ngrams[cur_n1gram][words[i]] = ngrams[cur_n1gram][words[i]]+1

                                else:
                                    ngrams[cur_n1gram][words[i]] =  1
                        else:
                            n1grams[cur_n1gram] = 1
                            
                            ngrams[cur_n1gram]= {words[i] : 1}

                


                
                

                
                
        




    return ngrams, n1grams

def print_m_sentences(n, m, ngram, n1gram):
    import random
    import re
    punctuation_found = 0
    num_start_markers = (n-1)
    start_marker = "<s> "

    cur_n1gram = (start_marker*num_start_markers).strip()
    sentence = ""
    sentences = []
    while punctuation_found < m:
        
        
        if cur_n1gram in ngram.keys():
            words = ngram[cur_n1gram].keys()
            probs = ngram[cur_n1gram].values()
        
            # produce probibility of next word

            selection = random.randint(0, sum(probs))
            i = 0
            while (selection > list(probs)[i]) and (i<len(list(probs))):
                selection = selection - list(probs)[i]
                i += 1
            



            if bool(re.search("[.?!]", list(words)[i])):
                # publish a sentence
                sentences.append((sentence+list(words)[i]))
                cur_n1gram = (start_marker*num_start_markers).strip()
                sentence = ""
                punctuation_found += 1

            else:
                #add to sentence 
                if bool(re.search("[,;:]", list(words)[i])):
                    sentence += list(words)[i]
                else : sentence += " "+list(words)[i]

                temp = cur_n1gram.split()
                cur_n1gram = ""
                for j in range(len(temp)):
                    if j > 0:
                        cur_n1gram += temp[j]+" "
                cur_n1gram += list(words)[i]
            
            
        else:
            print("There was an error in ngram Construction.")
            punctuation_found += 1


    output = ""
    for i in range(len(sentences)):
        output += str(sentences[i]).strip().capitalize()

    print(output)

start()


