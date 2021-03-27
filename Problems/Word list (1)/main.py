text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
z = int(input())
new_list = []      
for i in text:
        for x in i:
                if len(x) <= z:
                        new_list.append(x)
                
print(new_list)
