def num2words(num):
	under_20 = ['Zero','One','Two','Three','Four','Five',
                'Six','Seven','Eight','Nine','Ten','Eleven',
                'Twelve','Thirteen','Fourteen','Fifteen',
                'Sixteen','Seventeen','Eighteen','Nineteen']

	tens = ['Twenty','Thirty','Forty','Fifty','Sixty',
            'Seventy','Eighty','Ninety']

	above_100 = {100: 'Hundred',
                1000:'Thousand', 
                1000000:'Million', 
                1000000000:'Billion'
                }
 
	if num < 20:
		 return under_20[num]
	
	if num < 100:
		return tens[(int)(num/10)-2] + ('' if num%10==0 else ' ' + under_20[num%10])
 
	# find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
	pivot = max([key for key in above_100.keys() if key <= num])
 
	return num2words((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + num2words(num%pivot))

print(num2words(17141918))

#using inflict library

import inflect
p = inflect.engine()
 
words = p.number_to_words(1234)
# Prints “one thousand, two hundred and thirty-four”
print(words) 
 
words = p.number_to_words(p.ordinal(1234))
 
# Prints “one thousand, two hundred and thirty-forth”
print(words)
 
# You can also convert individual digit 
# into word using “group” parameter 
 
words = p.number_to_words(1234, group=1)
# Prints “one, two, three, four”
print(words)
 
words = p.number_to_words(1234, group=2)
# Prints “twelve, thirty-four”
print(words)