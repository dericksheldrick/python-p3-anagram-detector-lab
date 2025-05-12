# your code goes here!

#Pseudocode 
#create a class called Anagram and should take word on the intialization
#we will loop through the word to se if the letters matches the word given
#Return a list of all matches, otherWise retrn an empty array

class Anagram:
    def __init__(self, word):
        self.word_letters = sorted( letter for letter in word)

    def match(self, word_list):
        match_word_list = []

        for word in word_list:
            if sorted ([letter for letter in word]) == self.word_letters:
                match_word_list.append(word)

        return match_word_list
