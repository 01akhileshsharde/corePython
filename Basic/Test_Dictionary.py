# Dictionary : it is a key-value pair
# key is unique
# value can be duplicate
# empty dict:
d = {}
d1 = dict()
print(type(d))
print(type(d1))

data = {"id" : 1,
        "Name" : "Akhilesh",
        "Score" : 90
        }
print(data)

# Add pair
data["Mobile"] =8770253771
print(data)

# get
print(data.get("Name"))

# remove
# pop()
print(data.pop("Name")) # remove specified value

# Value , key and items of dict
print(data.values())
print(data.keys())
print(data.items()) # in the tuple form
