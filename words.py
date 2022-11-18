def print_upper_words(words):
    """ Print out each word on a seperate line, but in all uppercase.
    
   for example: 
        print_upper_words("Hello", "Hi", "Bye")
            //HELLO
            //HI
            //BYE
    
    """

    for word in words: 
        print(word.upper())


def print_words_starting_with(words):
    """ Only print words that start with the letter 'e'
        Print either uppercase or lowercase

    for example: 
        print_words_starting_with(["ego", "Egg", "popsicle", "yellow"])
            //ego
            //egg
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word)


def print(words, must_start_with):
    """ Print the words that start with the letter being declared in the second argument
        Should be able to pass in a set of letters
        It should only print out words that start with that letter

    for example:
        print(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
    """
  
    for word in words: 
        for letter in must_start_with:
            if word.startswith(letter):
                print(word)
       
        


print(["hello", "hey", "goodbye", "yo", "yes", "egg", "eat"],["h", "y"])