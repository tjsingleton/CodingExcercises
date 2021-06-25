# http://www.careercup.com/question?id=12435684
# Generate all the possible substrings of a given string. Write code. 
# i/p: abc
# o/p: { a,b,c,ab,ac,bc,abc}
"""begin
NOTES/DISCUSSION
All substrings is not the same as all combinations
Four distinct patterns comprise all substrings
  1. The original string
  2. Each character in the original string
  3. Two character strings where the first char is the original first char, 
     and the second char is each subsequent char in the original string.
  4. Strings where the original string is reduced, starting with the first char,
     until only two characters remain.
end"""

def findSubstrings(string):
   subArray = []
   length = len(string)
   for char in string:
      subArray.append(char)
   for place in range(0,length):
      for iteration in range(1,length):
         if place < iteration:
            combo = ''
            combo += string[place]
            if combo != string[iteration]:
               combo += string[iteration]
            if combo not in subArray:
               subArray.append(combo)
   subArray.append(string)
   return subArray

print("expected ['a','b','c','ab','ac','bc','abc'] got:", findSubstrings("abc"))
assert findSubstrings("abc") == ['a','b','c','ab','ac','bc','abc'] , "three char string produces correct substrings"