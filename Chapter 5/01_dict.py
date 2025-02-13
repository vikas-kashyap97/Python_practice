# marks = {
#     "vikas": 100,
#     "sachin": 90,
#     "rahul": 80,
#     "shubham": 70,
#     "saurav": 60
# }
# print(marks, type(marks))  # Output: {'vikas': 100, 'sachin': 90, 'rahul': 80, 'shubham': 70, 'saurav': 60} <class 'dict'>

# print(marks["vikas"])      # Output: 100

                                                                        # It is a collection of key-value pairs 



                                                                        # Methods



marks = {
    "vikas": 100,
    "sachin": 90,
    "rahul": 80,
    "shubham": 70,
    "saurav": 60
}



# 1. items() - Returns a list of (key, value) tuples
print("items() ->", marks.items())                        # Output: dict_items([('vikas', 100), ('sachin', 90), ('rahul', 80), ('shubham', 70), ('saurav', 60)])



# 2. keys() - Returns a list containing dictionary's keys
print("keys() ->", marks.keys())                            # Output: dict_keys(['vikas', 'sachin', 'rahul', 'shubham', 'saurav'])



# 3. update() - Updates the dictionary with the supplied key-value pairs
marks.update({"friend": "Sam"})
print("update() ->", marks)                                 # Output: {'vikas': 100, 'sachin': 90, 'rahul': 80, 'shubham': 70, 'saurav': 60, 'friend': 'Sam'}



# 4. get() - Returns the value of the specified key
name_value = marks.get("vikas")
print("get('vikas') ->", name_value)                       # Output: 100



# If key doesn't exist, get() will return None or a default value (if specified)
friend_value = marks.get("friend")
print("get('friend') ->", friend_value)                    # Output: Sam