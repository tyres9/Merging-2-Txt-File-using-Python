"""Merging 2 text file """


search_text = "[name]"
with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    letter_to_all = starting_letter.read()


with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    for name in invited_names:
        output_letter = letter_to_all
        new_output_letter = output_letter.replace(search_text, name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode= 'w') as letter_to_send:
            letter_to_send.write(new_output_letter)






