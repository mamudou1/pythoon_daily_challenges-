"""people = ["jc", "malieu","joe",39,True]
print(people[-1])
print(people[1:3])
people[2]="jerreh"
print(people)
"""

number=[2,4,3,5,65,66,43]
friend=["kelvin", "karen", "jim", "oscar"]
friend.extend(number)
friend.append("maka")
friend.insert(2,"bojang")
friend.remove("kelvin")
friend.clear()
friend.pop() #remove last element
print(friend.index("jim"))
print(friend.count("jim"))
friend.sort()
number.reverse()
number1=number.copy()
print(friend)




