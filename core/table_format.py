grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

def formatted_grades(students):
    beautiful_table_lines = []
    count = 0
    for stud in students.keys():
        count += 1
        beautiful_table_lines.append(
            "{:>4}|{:<10}|{:^5}|{:^3}".format(count, stud, students[stud], grades[students[stud]]))
    return beautiful_table_lines


for el in formatted_grades(students):
    print(el)
