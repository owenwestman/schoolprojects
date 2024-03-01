# Made by Owen Eastman, Feb 15
# init list
fastfood = ["Mc. Donalds", "Wendy's", "Burger King", "Taco Bell", "Chick-Fil-A", "Popeyes", "Carl Jr.", "Dairy Queen", "KFC", "Arby's", "Pizza Hut"]
print(fastfood)
# return item at index 1
print(fastfood[1] + "  is the best fast food resteraunt")
# return number of times "KFC" appears in the list
print(str(fastfood.count("KFC")) + " KFCs in the list")
# sorts the list alphabetically
fastfood.sort()
print(fastfood)
# adds subway to the end of the list
fastfood.append("Subway")
print(fastfood)
# remove Chik-Fil-A
fastfood.remove("Chick-Fil-A")
print(fastfood)
# return and remove the item at index 1
print(fastfood.pop(9))
# add Arby's and Krusty Burger to the end of the list
fastfood.extend(["Arby's","Krusty Burger"])
print(fastfood)
# insert Wendy's before index 0
fastfood.insert(0,"Wendy's")
print(fastfood)
