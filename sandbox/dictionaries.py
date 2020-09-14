# dictionaries are part of the standard library so we don't need an import
# create an instance of a dictionary

dictionary_instance = {
    "key": "value",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
}

print(dictionary_instance)

# access a value
print(dictionary_instance.get("key"))

# or this way with a runtime error if a key doesn't exist
print(dictionary_instance['key'])

# dictionaries are dynamic in memory which means we can change the values during runtime/exectution of files
# not static and we can change the value

dictionary_instance['key3'] = "value_new "
print(dictionary_instance)

# prints all the keys
for x in dictionary_instance:
    print(x)

# we can print the values too 
for x in dictionary_instance:
    print(dictionary_instance.get(x))

# shortand version
for x in dictionary_instance.values():
    print(x)

# key and values
for key, value in dictionary_instance.items():
    print(key)
    print(value)

# check if key exists
if "key3" in dictionary_instance:
    print("Yes 'key', is in the dictionary_instance")
else:
    print("Not found in dictionary")

if "key" in dictionary_instance:
    dictionary_instance['key'] = "key 1 new"

print(dictionary_instance)

# we can print length of dictionary -> returns the number of key value pairs (number of rows)
print(len(dictionary_instance))

# remove item from dictionary
# Good to check if the key exists first
if "key3" in dictionary_instance:
    print(dictionary_instance.pop('key3'))

print(dictionary_instance)

# remove the last item in dictionary

dictionary_instance.popitem()
print(dictionary_instance)

# we can empy an dictionary
dictionary_instance.clear()

# we can delete a dictionary
# del dictionary_instance

# copy a dictionary 

x = dictionary_instance
a = x
x["key3"] = "new key 3 value"

print(x ,"this is x")
print(a , "this is a")

# Both key3 in x and a will be assigned the new value as they are both pointing to the same object in memory 
# Since we change x ->key3 and a reference x then a key3 is also changed

# if we want to change the x key3 only then we can use copy() as
# a will get a new object in memory, a new dictionary instance


y = dictionary_instance
b = y.copy()
y["key3"] = "new key 3 value"

print(y ,"this is y")
print(b , "this is b")