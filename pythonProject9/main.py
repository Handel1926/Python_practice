# FileNotFoundError
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdhdks"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key{error_message} doesnt exist")
# else: # works only if try works
#     content = file.read()
#     print(content)
# finally: # occors wether code succeeds or fails
#     file.close()
#     print("file was closed")

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key]

# IndexError
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text * 5)

height = float(input("height: "))
weight = int(input("weight: "))
if height > 3:#meters:
    raise ValueError("Human heigt cant be greater than 3meters")

bmi = weight/height**2
print(bmi)
