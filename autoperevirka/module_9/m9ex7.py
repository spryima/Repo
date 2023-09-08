def normal_name(list_name):
    cap_names = map(lambda name: name.capitalize(), list_name)
    return list(cap_names)
    

names = ["dan", "jane", "steve", "mike"]
print(normal_name(names))