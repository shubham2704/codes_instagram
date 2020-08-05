"""
Description 
An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are anagram of each other.

"""

s1 = input('Enter first string')
s2 = input('Enter seconf string')

if sorted(s1)==sorted(s2):
    print('Strings are anagrams')
else:
    print('Strings are not annagrams')

"""
scaler hiring challenge ref link
https://www.scaler.com/contest/scalerhiring?rcy=1&rce=bcdae13f6629
"""