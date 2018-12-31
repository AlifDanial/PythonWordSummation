# This program converts input alphabets into integers assuming a,b,c and d .. is equal to 1,2,3 and 4 ..
# 30/12/2018

import string
import array as arr

number_list = list(range(1, 27))
print(number_list)
alphabet_list = list(string.ascii_lowercase)
print(alphabet_list)
a = arr.array('i', [])

word = input("Enter an adjective: ")
word = word.replace(" ", "")

for x in word:
    for y in alphabet_list:
        z = alphabet_list.index(x)+1
        a.append(z)
        break

Sum = sum(a)
print("%s = %d" % (word, Sum))








