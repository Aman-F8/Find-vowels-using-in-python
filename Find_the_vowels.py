#Find the vowels in given string
vowels = "aeiou"
values = "Guvi Geeks Network Private Limited"
a = list(values) #string convert into list
print(a)
for i in a: #list are iterating
    if i in vowels: #vowels are compared to iterative list
        print(list(i)) #it will print the matching characters.

#Find the string without vowels
vowels = "aeiou"
values = "Guvi Geeks Network Private Limited"
a = list(values) #string convert into list
print(a)
for i in a: #vowels are compared to iterative list
    if i not in vowels: #it will print the without matching characters.
        print(list(i))

values1 = "Guvi Geeks Network Private Limited"
b = list(values1)
print(set(b))

#return the number of word
values3 = "Guvi Geeks Network Private Limited"
print(len(values3.split()))




