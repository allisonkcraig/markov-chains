import random

opened_file = open("green-eggs.txt") 

# import sys



split_words = []
#convert file into list
for line in opened_file:
    word = line.rstrip( ).split(" ")
    split_words.extend(word) 

# print split_words
#convert list into string
corpus_string = " ".join(split_words)

# print corpus_string
# print corpus_string


def make_chains(corpus_string):
    # """Takes input text as string; returns dictionary of markov chains."""
    # for word in corpus_string:
    #     key = (word, word +1)
    #     if key == a key in dictionary: 

#     #     value += (word + 2)
# lined_to_corpus.items() 
    lined_to_corpus = {}
    for index in range(len(split_words)-2):  
        key1 = split_words[index]
        key2 = split_words[index +1]
        value_added = split_words[index +2]
        if (key1, key2) in lined_to_corpus:
            lined_to_corpus[(key1, key2)].append(value_added)
        else:
            lined_to_corpus[(key1, key2)] = [value_added]


        # for key , value in lined_to_corpus.items(): 
            # print key
            # print value
            # if (key1, key2) == key:
            #     lined_to_corpus[key] = value.extend(split_words[index+ 2])
            # else:
            #     lined_to_corpus[split_words[index],split_words[index+1]] = [split_words[index+2]]
    



    
    return lined_to_corpus


make_chains(corpus_string)

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    for keys in chains:
        print chains.random()


    return "Here's some random text."




# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = split_words

# Get a Markov chain
chain_dict = make_chains(input_text)

# Produce random text
random_text = make_text(chain_dict)

print random_text


print make_text(chain_dict)