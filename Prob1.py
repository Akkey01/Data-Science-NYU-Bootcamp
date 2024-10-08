def count_vowels(word):
    d=0
    l=list(word)
    for c in l:
        if c in ['a','e','i','o','u','A','E','I','O','U'] :
            d=d+1
    return d
    
word=input("Enter your Word : ")
print(count_vowels(word))