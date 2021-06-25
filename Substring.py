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
