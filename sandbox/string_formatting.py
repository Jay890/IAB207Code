print("Hello World")

x = 10
a = x
x = 20

print(x)


name = "John Smith"
points = 10
str = " Hello {}, You have won {} points today!!"
print(str.format(name, points))
# the parameter passed will be based on the position and number of {}

# String formatting help provide more information in a cleaner way.
# We also don't need to run format method either
name2 = "Bob Bob"
points2 = 5
str2 = f"Hello {name2}, You have won {points2} today!!"
print(str2)


# Most programming languages in most cases have concepts of value types and reference types
# So value types are things you can create copies off
x = 10
a = x
x = 20

print(a)
print(x)
# a will be 10
# x will be 20
# In this scenario, for value types. for python we got a copy of 10 in the assignment not the 10 that x has.
# In python strings are value types too so it will be same

x = "foobar"
a = x
x = "barfoo"

print(a)
print(x)

# In a lot of other languages strings are reference types

# Reference type can be an array/list
c = [10, 20, 30]
d = c
c[0] = 50

print(c)
print(d)

# In this case for reference types we get the same value as c and d hold the same valye
# So when a = x we don't get a copy like the value type we get the exact array/list
# So when we change the list we also change a
# Both print
# c - [50, 20,30]
# d - [50, 20,30]
