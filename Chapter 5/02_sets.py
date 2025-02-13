# Sets in Python
# A set is an unordered collection of unique elements. In a set, there are no duplicate values, and elements are not stored in any specific order.


# Creating an empty set
S = set()
print("Empty Set:", S)  # Output: set()



# Adding elements to the set
S.add(1)
S.add(2)
print("Set after adding elements:", S)  # Output: {1, 2}



# Adding a duplicate element (No repetition allowed!)
S.add(1)  
print("Set after trying to add duplicate:", S)  # Output: {1, 2} (no change)



                                                                        # Methods






S = {1, 8, 2, 33}

# 1. len(S): Get the number of elements in the set
print(len(S))                                                # Output: 4


# 2. remove(element): Removes a specific element from the set
S.remove(8)
print(S)                                                    # Output: {1, 2, 33}


# 3. pop(): Removes and returns an arbitrary element
removed_element = S.pop()
print("Removed element:", removed_element)  
print("Set after pop:", S)                                  # Output: Removed element: 1


# 4. clear(): Removes all elements from the set
S.clear()
print(S)                                                    # Output: set() (empty set)



# 5. union(set2): Returns a new set containing elements from both sets
S1 = {1, 3, 2}
S2 = {3, 11}
result = S1.union(S2)
print(result)                                               # Output: {1, 2, 3, 11}



# 6. intersection(set2): Returns a set containing only the common elements
S1 = {1, 3, 2, 5}
S2 = {3, 11, 5}

intersection_result = S1.intersection(S2)
print("Intersection of S1 and S2:", intersection_result)  # Output: {3, 5}
