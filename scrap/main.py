say = "how are you"
words = say.split(" ")
for word in words:
    a, *b = word
    print(a)
    print(b)
    b.append(a)
    print(b)
    new_string = ""
    new_strings = ""
    for i in b:
        new_string += i + "ay"
    print(new_string)
  