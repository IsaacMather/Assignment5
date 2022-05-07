from HashQP import HashQP, HashEntry
from Employee import Employee

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_hash_table = HashQP()
    employees = []
    employees.append(Employee("mike", 123456789))
    employees.append(Employee("fred", 987654321))
    employees.append(Employee("rick", 555555555))

    print("Hash Table Size:", my_hash_table.size)
    for i in range(3):
        print("Adding", employees[i].name, "twice")
        my_hash_table.insert(employees[i])
        my_hash_table.insert(employees[i])

    print("Hash Table Size (should be 3):", my_hash_table.size)

    for i in range(3):
        if employees[i] in my_hash_table:
            print("Verified that", employees[i].name, "is in the table")
        else:
            print("oops,", employees[i].name, "was not found")

    my_hash_table_two = HashQP()

    substrate = "asdlkfj asdoiBIUYVuwer slkdjLJfwoe89)B)(798rjMG0293lkJLJ42lk3j)(*"

    substrate = substrate + substrate
    string_list = [substrate[k:k + 5] for k in range(len(substrate) - 5)]

    my_hash_table_two.max_lambda = .5
    inserted = 0
    for k in range(len(substrate) - 5):
        if my_hash_table_two.insert(string_list[k]):
            print("Inserted string", k, ":", string_list[k])
            inserted += 1

        else:
            print("Did not insert", k, ":", string_list[k])
    print("Strings inserted:", inserted)
    print("Size of table:", my_hash_table_two.size)
    print("Number of buckets:", my_hash_table_two._table_size)
    print("\nFind the strings:")
    for k in range(len(substrate) - 5):
        if string_list[k] in my_hash_table_two:
            print("Found string", k, ":", string_list[k])
        else:
            print("Did not find", k, ":", string_list[k])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
