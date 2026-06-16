name = "safdar munir"
#capitalize first letter of each word
print(name.capitalize())
#all letters to uppper case
print(name.upper())
#all letters to lower case 
print(name.lower())
#count characters in string
print(name.count("a"))
# Lenght of string
print(len(name))
# Replace a word in string
print(name.replace("munir","king"))
## check if a word is in string
print("safdar" in name)

# split sentence into list of words

sentence = "I am Learning Python and AI skills"
print(sentence.split())
print("total words in sentence =", len(sentence.split()))
 
 # Join back together 
joined = " | ".join(sentence.split())
print(joined)

# string formatting

name = "safdar"
week = 3
day = 16
score = 86

# old way fo string formatting
print("Hello, my name is ",name,". I am in week ",str(week),"day",str(day),"and my score is ",str(score))

# Modern way of string formatting using f-strings
print(f"Hello, my name is {name}. I am in week {week}, day {day}, and my score is {score}")
print(f"day {day}, score {score}/100")
print(f"I am building AI skills from {name} in Lakki marwat.")

#string cleaning 
string = "  Hello, world   "
clean_string = string.strip()
print(len(string), len(clean_string))
print(clean_string)
print(clean_string.startswith("Hello"))
print(clean_string.endswith("world"))

