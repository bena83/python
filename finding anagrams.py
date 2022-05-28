# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(s1, s2):


   if len(s1) != len(s2):
      return False
 
   s1 = sorted(s1)
   s2 = sorted(s2)
 
   return s1 == s2

s1 = "bite"
s2 = "biet"
print(find_anagram(s1, s2))

    
         

    

