# Declare variabkes
string1 = "Thirty"
string2 = "Days"
string3 = "Of"
string4 = "Python"
concatenated_string1 = f"{string1} {string2} {string3} {string4}"
print(concatenated_string1)

string5 = "Coding"
string6 = "For"
string7 = "All"
concatenated_string2 = f"{string5} {string6} {string7}"
print(concatenated_string2)

company = "Coding for all"
print(company)

print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

sliced_word = company[7:]
print(sliced_word)
print(company[0:7])
print(company.replace("Coding for all","Python"))

libraries = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_libraries = libraries.split(', ')
print(split_libraries) 


first_character = company[0]
print(first_character) 


last_index = len(company) - 1
print(last_index) 

character_at_index_10 = company[10]
print(character_at_index_10)  

starts_with_coding = company.startswith('Coding')
print(starts_with_coding) 

ends_with_coding = company.endswith('coding')
print(ends_with_coding) 

libraries_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = '#'.join(libraries_list)
print(joined_libraries)