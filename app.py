import sys
import re
filename = sys.argv[-1]                                                     #Allow argument in standard input terminal


def clean_words(words):            
    return (' '.join(re.sub("[^a-zA-Z0-9]+"," ",words).split()))            #Regex that removes wild and special characters

def word_occurence(file):
    try:
        with open(file, encoding="utf-8", errors="strict" ) as f:
            data = f.read()
            if(not data):
                return "Empty file, no words found."                        

            if(data.isspace()):                                             #Check if file contains only whitespaces
                return "File contains only spaces, no words"

            words = data.split(" ")                                         #Separate words based on spaces
            wordcount = len(words)
            

            checkwords = clean_words(data).split(" ")                       #Call function to remove wild characters
            counts = dict()
            for word in checkwords:                             
                if word in counts:                                          #Dictionary based key:value counter increment if word found
                    counts[word] += 1
                else:
                    counts[word] = 1

        # Sort dictionary items based on the x[1] position in dict which is the value
        # Since we require the largest/most common value, reverse the dict items
        counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)[:10]    
        return wordcount,counts                                             

    except FileNotFoundError as not_found:
        return ("File not found")



def main():
    word_search = word_occurence(filename)
    print("The total number of words in the text file are: ", word_search[0])
    print("The 10 most common words and their occurences are: ",word_search[1])

if __name__ == "__main__":
    main()

