fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[1])   # Output: Banana

#  Unlike strings lists are mutable
fruits[1] = "Grapes"
print(fruits[1])  # Output: Grapes


# Creating a list  
numbers = [8, 1, 15, 7, 2, 21]  
print("Original List:", numbers)  


# 1. sort() - Sorts the list in ascending order  
numbers.sort()  
print("sort() ->", numbers)  # Output: [1, 2, 7, 8, 15, 21]  



# 2. reverse() - Reverses the order of the list  
numbers.reverse()  
print("reverse() ->", numbers)  # Output: [21, 15, 8, 7, 2, 1]  



# 3. append(8) - Adds 8 at the end of the list  
numbers.append(8)  
print("append(8) ->", numbers)  # Output: [21, 15, 8, 7, 2, 1, 8]  



# 4. insert(3, 8) - Inserts 8 at index 3  
numbers.insert(3, 8)  
print("insert(3, 8) ->", numbers)  # Output: [21, 15, 8, 8, 7, 2, 1, 8]  



# 5. pop(2) - Removes the element at index 2 and returns its value  
removed_element = numbers.pop(2)  
print("pop(2) -> Removed:", removed_element, "Updated List:", numbers)  
# Output: Removed: 8, Updated List: [21, 15, 8, 7, 2, 1, 8]  



# 6. remove(21) - Removes the first occurrence of 21 from the list  
numbers.remove(21)  
print("remove(21) ->", numbers)  # Output: [15, 8, 7, 2, 1, 8]  
