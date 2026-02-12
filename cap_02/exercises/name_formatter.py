'''
Original: '  ada lovelace  '
Formatted: 'Ada Lovelace'
Length difference: 4
 '''

full_name = "  ada lovelace  "
formatted_name = full_name.strip().title()
length_difference = len(full_name) - len(formatted_name)
#length_difference = full_name.__len__() - formatted_name.__len__() 


print(f"Original: '{full_name}'")
print(f"Formatted: '{formatted_name}'")
print(f"Length difference: {length_difference}")