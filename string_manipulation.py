# String Manipulation

input_string = input("\nEnter String: ")
input_string = input_string.lower().split()
output_string = str()
output_list = list()
for word in input_string:
    word = word[::-1]
    if ord(word[0]) >= 97 and ord(word[0]) <= 122:
        new_char = chr(ord(word[0]) - 32)
        word = word.replace(word[0], new_char, 1)
        output_list.append(word)
output_string = " ".join(output_list)
print("\nResult output: {}".format(output_string))
