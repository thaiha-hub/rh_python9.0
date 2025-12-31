# Program that counts the number of a character in a string
text = input("Enter a string: ")
first_char = text[0]
count1 = 0
for char in text:
    if char == first_char.lower() or char == first_char.upper():
        count1 += 1
last_char = text[-1]
count2 = 0

if char == ".":
    last_char = text[-2]
    
for char in text:
    if char == last_char.lower() or char == last_char.upper():
        count2 += 1

print(f"The first character '{first_char}' occurs {count1} times.")
print(f"The last character '{last_char}' occurs {count2} times.")   