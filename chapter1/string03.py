# a string of text 
text = input("Please input anything you like: ")
length = len(text)
# check if the text ends with the period character '.'
if text.endswith('.') == True:
    ans1 = "Yes"
else:
    ans1 = "No"
print("Does it end on a  period?", ans1)
# check if the input contain all alphabetic characters  
if text.isalpha() == True:
    ans2 = "Yes"
else:
    ans2 = "No"
print("Does it contain only alphabetic characters?", ans2)
# check if the input contains "x"
if "x" in text:
    ans3 = "Yes"
else:
    ans3 = "No"
print("Does it contain the letter 'x'?", ans3)
# change all e to E in the input
new_text = text.replace("e", "E")
print("Here is the new text:", new_text)