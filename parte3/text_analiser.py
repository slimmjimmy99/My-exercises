name = input("Input you full name, please ")
print("Your name in Uppercase letters, {}".format(name.upper()))
print("Your name in Lowercase letters, {}".format(name.lower()))
name_count = name.strip().replace(" ", "")
print("This name have {} caraters length".format(len(name_count)))
splited_names = name.split()
print("The first name has {} caraters length".format(len(splited_names[0])))

