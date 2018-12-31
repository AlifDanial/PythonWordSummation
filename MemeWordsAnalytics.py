# This program converts input alphabets into integers assuming a,b,c and d .. is equal to 1,2,3 and 4 ..
# 30/12/2018

import string
import array as arr

number_list = list(range(1, 27))
alphabet_list = list(string.ascii_lowercase)
'''for x in number_list:
    print("%d : %c" % (x, alphabet_list[x-1]))'''
for x in number_list:
    print(x, end=" ")
print("")
for y in alphabet_list:
    print(y, end=" ")
print("")

a = arr.array('i', [])
word = input("Enter an adjective: ")
word = word.replace(" ", "")
for x in word:
    for y in alphabet_list:
        z = alphabet_list.index(x) + 1
        a.append(z)
        break
print(a)
Sum = sum(a)
print("%s = %d" % (word, Sum))

'''
a = arr.array('i', [])
f1 = open("adjectives.txt", "r")
for w in f1:
    word = w.replace("\n", "")
    for x in word:
        for y in alphabet_list:
            z = alphabet_list.index(x)+1
            a.append(z)
            break
    f = open("WordAnalytics.txt", "a+")
    Sum = sum(a)
    a = []
    word = w.replace("\n", "")
    if Sum != 0:
        f.write("%s = %d \n" % (word, Sum))
    f.close()
    f1.close()'''

