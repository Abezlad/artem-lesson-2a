# --------- 1 ---------
my_list = [ "hello", "world", "bro", "wassup" ]
new_list = []

for index, row in enumerate( my_list ):
    if index % 2 == 1:
        new_list.append( row[::-1] )
    else:
        new_list.append( row )

print( new_list )
#
#
# --------- 2 ---------
#
my_list = [ "aboba", "asffsaaf", "bbbbb", "csrf", "aaaaa" ]
new_list = []

for row in my_list:
    if row[0] == "a" or row[0] == "A":
        new_list.append( row )

print( new_list )
#
# --------- 3 ---------
#
my_list = [  "bbAbb", "csrf", "aaaaa" ]
new_list = []

for row in my_list:
    if "a" in row or "A" in row:
        new_list.append( row )

print( new_list )
#
# --------- 4a ---------
#
peoples = [
    {"name": "Semen", "age": 23},
    {"name": "John", "age": 55},
    {"name": "Jack", "age": 45},
    {"name": "Semen", "age": 23},
]

younger_age = peoples[0]["age"]
younger_list = []

for human in peoples:
    if human["age"] == younger_age:
        younger_list.append( human )
    elif human["age"] < younger_age:
        younger_list = [ human ]
        younger_age = human["age"]

print( younger_age, younger_list )
#
# --------- 4b ---------
#
peoples = [
    {"name": "Semen", "age": 23},
    {"name": "John", "age": 55},
    {"name": "Jack", "age": 45},
    {"name": "Semen", "age": 23},
]

smallest_name = len(peoples[0]["name"])
smallest_list = []

for human in peoples:
    if len(human["name"]) == smallest_name:
        smallest_list.append( human["name"] )
    elif len(human["name"]) < smallest_name:
        smallest_list = [ human["name"] ]
        smallest_name = len(human["name"])

print( smallest_name, smallest_list )
#
# --------- 4в ---------
#
# peoples = [
#     {"name": "Semen", "age": 23},
#     {"name": "John", "age": 55},
#     {"name": "Jack", "age": 45},
#     {"name": "Semen", "age": 23},
# ]
#
# peoples.items() => [ ["Semen", 23], ["John", 55] ]
# peoples.values() => [ 23, 55, 45, 23 ]
# peoples.keys() => ["Semen", "John", "Jack", "Semen"]
#
# total_age = sum(person["age"] for person in peoples)
#
# average_age = total_age / len(peoples)
# print(average_age)
# --------- 4в(2) ---------
def average_age(people_list):
    ages = [person["age"] for person in people_list if "age" in person]
    if ages:
        average = sum(ages) / len(ages)
        return average
    else:
        return None
people = [
    {"name": "John", "age": 15},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Jack", "age": 45}
]
avg_age = average_age(people)
if avg_age is not None:
    print(f"Average age: {avg_age}")
else:
    print("No age data available.")

# --------- 5a ---------
#
my_dict_1 = {
    "value1": 1,
    "value2": 2
}

my_dict_2 = {
    "value1": 1,
    "value3": 3
}

new_list = []

for key in my_dict_1.keys():
    if key in my_dict_2.keys():
        new_list.append( key )

print( new_list )
#
# --------- 5b ---------
#
my_dict_1 = {
    "value1": 1,
    "value2": 2
}

my_dict_2 = {
    "value1": 1,
    "value3": 3
}

s1 = { 1,2,3,4,5 }
s2 = { 4,5,6,7,8,9 }

print( s1 - s2 )
print( s2 - s1 )
print( s2 & s1 )
print( s2 | s1 )

print(  set(my_dict_1.keys()) - set(my_dict_2.keys())   )
#
# --------- 5в ---------
#
my_dict_1 = {
    "value1": 1,
    "value2": 2
}

my_dict_2 = {
    "value1": 1,
    "value3": 3
}

print(  {key: my_dict_1[key] for key in my_dict_1.keys() if key not in my_dict_2}  )
#
# --------- 5г ---------
#
my_dict_1 = {
    "value1": 1,
    "value2": 2
}

my_dict_2 = {
    "value1": 1,
    "value3": 3
}

new_dict = {}

for key in my_dict_1:
    if key not in my_dict_2:
        new_dict[key] = my_dict_1[key]
    elif key in my_dict_2:
        new_dict[key] = [my_dict_1[key], my_dict_2[key]]

print( new_dict )
#
#
