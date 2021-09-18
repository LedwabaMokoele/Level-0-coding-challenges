import string
def print_Common(word_i, word_ii):
    common = "Common letters: "
    temp_string_i = word_i.lower()  #temporary strings 
    temp_string_ii = word_ii.lower() #to store the variables passed
    for i in temp_string_ii:  
        if(temp_string_i.count(i) > 0):
            if(i != " "):
                common+=i+", "
    common= common[:-2] #Remove the extra comma and space at the end
    return common

print(print_Common("house","computers")) 