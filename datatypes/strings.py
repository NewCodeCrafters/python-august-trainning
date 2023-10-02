# string manipulation
# str_mani.py

# len, chr, ord

name = "Bello AbdulHakeem"
name = "Olamide"

name = "Zubair"
sname = "Mr. Ibraheem"
fname = "Bello AbdulHakeem"
new_name = "Abubakar Yakub"  # fname = name  #Zubair
# sname = name  # Zubair
name = sname  # Zubair

# sentence = Bello AbdulHakeem is 17 characters long.
sentence = f'{fname} is {len(fname)} characters long.'
print(sentence)

# len()
# print()
sentence = f"{sname} is {len(sname)} characters long."
print(sentence)

sentence = f"{new_name} is {len(new_name)} characters long."
print(sentence)
