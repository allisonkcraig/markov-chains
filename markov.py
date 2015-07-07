opened_file = open("green-eggs.txt") 

# import sys

lined_to_corpus = {}

split_words = []
#convert file into list
for line in opened_file:
    word = line.rstrip( ).split(" ")
    split_words.extend(word) 

# print split_words
#convert list into string
corpus_string = " ".join(split_words)

# print corpus_string



def make_chains(corpus_string):
    # """Takes input text as string; returns dictionary of markov chains."""
    # for word in corpus_string:
    #     key = (word, word +1)
    #     if key == a key in dictionary:

    #     value += (word + 2)
    for word in range(len(split_words)):    
        if word +1 == len(split_words):
            lined_to_corpus[split_words[word],split_words[word+1]] = split_words[split_words[0]]
            break
        else:
            lined_to_corpus[split_words[word],split_words[word+1]] = split_words[word+2]
        # if split_words[word +1] != len(split_words):
        #     lined_to_corpus[(split_words[word],split_words[word+1])] = split_words[word+2]
        # else:
        #     lined_to_corpus[(split_words[word],split_words[word+1])] = split_words[split_words[0]]
        #     break




print lined_to_corpus
    # return {}

make_chains(corpus_string)

# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# # Change this to read input_text from a file, deciding which file should
# # be used by examining the `sys.argv` arguments (if neccessary, see the
# # Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
