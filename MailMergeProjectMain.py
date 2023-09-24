
with open("/Users/jerin/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    namesList = names.readlines()
with open("/Users/jerin/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()
    for name in namesList:
        name_without_new_line = name.strip()
        new_letter = letter.replace("[name]", name_without_new_line)
        with open(f"/Users/jerin/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/{name_without_new_line}.txt", mode="w") as output:
            output.write(new_letter)




#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp