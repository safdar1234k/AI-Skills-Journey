#Lists
skills = ["Python ", "zapier", "make.com", "AI", "Automation"]
print(skills)
#print specefic skill
print(skills[3])

#Add new skill 
 
skills.append("Github")
print(skills)

#Remove a skill
skills.remove("make.com")
print(skills)
#change a skill 
skills[2] = "Notion"
print(skills)
#Length of the list 
print(len(skills))
#Loop throgh the list 
for skill in skills:
    print("I am learning",skill)
    
   
