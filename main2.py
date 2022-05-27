# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
#import string
def read_file_content(filename):
    # [assignment] Add your code here 
  with open ("C:/Users/Admin/Downloads/Reading-Text-Files/story.txt") as f:
     file=f.read()
  return file
result=read_file_content("C:/Users/Admin\Downloads/Reading-Text-Files/story.txt")
print(result)
def count_words(str):
     result= read_file_content("C:/Users/Admin\Downloads/Reading-Text-Files/story.txt")
    # [assignment] Add your code here
      # Create an empty dictionary
     counts = dict()
     words = str.split()

    # Loop through each line of the file
     for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
     return counts


print( count_words(result))
    #return {"as": 10, "would": 20}
