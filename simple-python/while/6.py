i = 0 
word = "Hello"

#print all letters except e and o

while i < len(word):
    if word[i] == "e" or word[i] =="o":
        i += 1
        continue

    print("Returned letter",word[i])
    i += 1