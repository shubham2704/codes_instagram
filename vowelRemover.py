# naive method
def vowel_Remover1(s,v):
    for i in s.lower():
        if i in v:
            s = s.replace(i,"")
    return s

# one liner list compherihension
def vowel_Remover2(s,v):
    return "".join("" if x in v else x for x in s.lower())

# using regex 
import re
def vowel_Remover3(s):
    return (re.sub("[AEIOUaeiou]","",s))

s = 'shubham'
v = ['a','e','i','o','u']
print(vowel_Remover1(s,v))
print(vowel_Remover2(s,v))
print(vowel_Remover3(s))