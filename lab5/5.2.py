sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

print(sample_dict.items())

for k in sample_dict.keys():
  print(k,sample_dict[k])

list = ["name","age","city","salary"]
s2 = {}
for k in sample_dict.keys():
 if k in list:
  s2[k] = sample_dict[k]

print(s2)

for k in sample_dict.keys():
 if k in list:
  del s2[k]

print(s2)

if "Jones" in sample_dict.values():
 print("występuje")

sample_dict2 = sample_dict
sample_dict2["location"] = sample_dict2.pop("city")
print(sample_dict2)