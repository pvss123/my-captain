#1)Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#2)Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#3)Return the third, fourth, and fifth item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#4)This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#5)This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#6)Specify negative indexes if you want to start the search from the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#7)Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
###
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
##
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
####
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
##
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
##
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
##
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
##
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
##
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
##
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
##
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
##
thislist = ["apple", "banana", "cherry"]
del thislist
##
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
##
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
##
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  ###
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
##
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
##
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
##
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
##
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
##
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
##
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
##
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
##
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
##
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
##
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
##'
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
   