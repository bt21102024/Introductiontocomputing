string = "Python is a case sensitive language"
print("a.) Size of string is:", len(string))
string1 = string[::-1]
print("b.) The reversed string is :", string1)
S = slice(10,26)
print("c.) String after slicing:", string[S])
a = string.replace('a case sensitive' , 'object oriented')
print("d.) Replacing substring:", a)
i = string.index('a')
print("e.) The insex of 'a' is: ", i)
r = string.replace(' ' , '')
print("f.) Removing white spaces:", r, end = "\n")