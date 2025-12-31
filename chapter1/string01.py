# The program would ask an input of text & should print the original text followed on the 2nd line in the output by the number of characters entered.
text = input("Enter a string of text:")
length = len(text)
print(length, text.capitalize(), sep="\n")

# sep="\n" is used to print the outputs on separate lines.
# #!/usr/bin/env python3 is used to specify the interpreter for executing the script.