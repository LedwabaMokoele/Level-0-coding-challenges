import string
def print_Common(word_i, word_ii):
    common = "Common letters: "
    common_letters = []
    temp_string_i = word_i.lower()  #temporary strings 
    temp_string_ii = word_ii.lower() #to store the variables passed
    for i in temp_string_ii:  
        if(temp_string_i.count(i) > 0 and common_letters.count(i) == 0):
            if(i != " "):
                common_letters.append(i)
    for i in common_letters:
        common += str(i)+", "
    common = common[:-2] #Remove the extra comma and space at the end
    return common

print(print_Common("Fearers","Terry")) 