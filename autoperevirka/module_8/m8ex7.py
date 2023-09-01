import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    cats_list = []

    if isinstance(cats[0], Cat):
        for _ in range(len(cats)):
            cats_list.append({
                "nickname": cats[_].nickname, 
                "age": cats[_].age, 
                "owner": cats[_].owner
            })
        return cats_list
    else:
        for _ in cats:
            cats_list.append(
                Cat(nickname= _["nickname"], 
                    age= _["age"], 
                    owner= _["owner"])
                )
        return cats_list
    
       

print(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))
print("+++")
print(convert_list([
                    {"nickname": "Mick", "age": 5, "owner": "Sara"},
                    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
                    {"nickname": "Simon", "age": 3, "owner": "Yura"},
                    ]))