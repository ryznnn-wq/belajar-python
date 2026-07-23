#program deksripsi password untuk melewati level 6 dari hackthissite

myString = '6e445>i:' #ganti dengan password yang terenkripsi yang diberikan

for i, j in enumerate(myString):
    c=ord(j) - i 
    print(chr(c), end="")