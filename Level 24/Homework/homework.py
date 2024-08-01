# Task1.

def manual_count():
    string = input("Enter your name: ")
    x = 0
    for i in string:
        if i == "e":
            x += 1
        else:
            pass
    print(x)



manual_count()

# Task2.

print("__________________Task2__________________")

sentence = "simple sentence"

print(sentence.islower())  # every character is in lower case

print(sentence.isupper()) # every character is in upper case

print(sentence.isnumeric()) # every character is numeric {0,1,2,3...}

print(sentence.isalpha()) # every character is alphabet {a,b,c...z,A,B,C...Z}

print(sentence.istitle()) # every word starts with an upper case character