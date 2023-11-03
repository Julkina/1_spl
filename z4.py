my_dict = {'a': 12, 'b': 12, 'c': 56, 'd': 400, 'e': 58, 'f': 20}
sorted_dict=sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
top_dict=[key for key, value in sorted_dict[:3]]
print(sorted_dict)
print(top_dict)
