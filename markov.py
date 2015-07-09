import random

class SimpleMarkovGenerator(object):


    def process_file(self): #METHOD NOT MODULE
        """ Open file and turn file into list of words in order
            Strip punctuation from ends of text seperate by blank space.
        """

        file_prompt = str(raw_input('What File?')) # promt user to input file name
        opened_file = open(file_prompt) 

    # import sys
        split_words = [] # list of words from file we have opened after stripped and split
        #convert file into list
        for line in opened_file: # for every line in opened_file,
            words = line.rstrip( ).split(" ") # we split the line into strings called words
            for word in words: # Strip punctuation and make lower case
                word = word.lower()
                word = word.strip('\"')
                word = word.rstrip(".")
                word = word.rstrip("--")
                word = word.rstrip(",")
                word = word.strip()
                split_words.append(word) # append word to split_words

        self.split_words = split_words # attribute!


    def make_chains(self, split_words):
        """Takes input text as a list; returns dictionary of markov chains."""
        
        lined_to_corpus = {}
        for index in range(len(self.split_words)-2):  
            key1 = self.split_words[index]
            key2 = self.split_words[index +1]
            key = (key1, key2)
            value_added = self.split_words[index +2]
            if (key1, key2) in lined_to_corpus:
                lined_to_corpus[(key1, key2)].append(value_added)
                list_of_words = lined_to_corpus[(key1, key2)]
                list_of_words.append(value_added)
            else:
                lined_to_corpus[(key1, key2)] = [value_added]
        
        self.lined_to_corpus = lined_to_corpus #attribute!



    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""
        #finds random key,
        
        tweet_list = []

        initial_key = []

        current_key = []
     
        for keys, values in chains.items():
            if len(tweet_list) <200:
                if tweet_list ==  []:
                    initial_key = random.choice(chains.keys())
                    tweet_list.extend(initial_key)
                    values = chains[initial_key]
                    value = random.choice(values)
                # print initial_key
              
                # print value
                    tweet_list.append(value)
                # print tweet_list
                    current_key = (initial_key[1], value)     
                    # print tweet_list
                    # print current_key   
                else:
                    if current_key not in chains.keys():    
                        break 
                    else:
                        values = chains[current_key]
                        value = random.choice(values)
                        tweet_list.append(value)
                        # print tweet_list
                        current_key = (current_key[1], value)
               
        tweet_string = " ".join(tweet_list)
        return tweet_string
        print len(tweet_string)



# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)


if __name__ == "__main__":

    new_markov = SimpleMarkovGenerator()


    input_text = new_markov.process_file()

    # Get a Markov chain
    chain_dict = new_markov.make_chains(input_text)

    # Produce random text
    random_text = new_markov.make_text(chain_dict)

    print random_text
    print len(random_text)

    # print make_text(chain_dict)
