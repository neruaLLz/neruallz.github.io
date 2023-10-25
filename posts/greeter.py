name = input("Please enter your name: ")
print(f"\nHello, {name}!")


prompt = "If you share your name, we can personalize the meassages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# This example shows one way to build a multiline string. 
# The first line assigns the first part of the message to the variable prompt. 
# In the second line, the operator += takes the string that was assigned to prompt 
# and adds the new string onto the end. 
# The prompt now spans two lines, again with space after the question mark for clarity.