Profile = {
    "name":"safdar",
    "age": 20,
    "city": "Lakki Marwat",
    "week":3,
    "score":86
}

print(Profile["name"])
print(Profile["city"])
print(Profile["score"])

#add a new key
Profile["goal"]= "billionaire"
print(Profile["goal"])

#Loop throgh Dictionaries
for key,value in Profile.items():
    print(key, ":" , value)

#list of automation projects as dictionary

Projects = [
    {"name":"form to Gmail", "Tool":"Zapier", "day": 8},
    {"name":"make automation", "Tool":"make.com", "day": 10},
    {"name":"Lead collection", "Tool":"Zapier", "day":12},
    {"name":"Task Remider ", "Tool": "Zapier","day":13}

]

for project in Projects :
  print("Project:", project["name"], "| Tool:", project["Tool"], "| Day:", project["day"])

