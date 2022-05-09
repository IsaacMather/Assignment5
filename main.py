from HashQP import HashQP, HashEntry
from KeywordEntry import KeywordEntry
from Employee import Employee

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_hash_table = HashQP()
    obj_one = KeywordEntry("one", "foothill.edu", 4)
    obj_two = KeywordEntry("two", "foothill.edu", 5)
    obj_three = KeywordEntry("as", "foothill.edu", 6)

    keyword_entry_list = [
        KeywordEntry("one", "foothill.edu", 4),
        KeywordEntry("as", "foothillcollege.instructure.com/", 1),
        KeywordEntry("written", "foothillcollege.instructure.com/", 2),
        KeywordEntry("the", "foothill.edu",5),
        KeywordEntry("class", "foothillcollege.instructure.com/",10),
        KeywordEntry("does", "foothill.edu", 11),
        KeywordEntry("not", "foothill.edu", 7),
        KeywordEntry("have", "foothill.edu", 3),
        KeywordEntry("valid", "foothill.edu", 8),
        KeywordEntry("comparison", "foothill.edu", 9),

    ]
    for keyword_entry in keyword_entry_list:
        my_hash_table.insert(keyword_entry)

    #running find on key words that are loaded in to the HashQP should
    # return a list. Are we returning a list?

    my_hash_table.find("ONE")
    my_hash_table.find("as")
    my_hash_table.find("aS")
    my_hash_table.find("wriTTen")
    my_hash_table.find("the")
    my_hash_table.find("tHE")
    my_hash_table.find("class")
    my_hash_table.find("does")
    my_hash_table.find("not")
    my_hash_table.find("have")
    my_hash_table.find("valid")
    my_hash_table.find("comparison")

    #run find on some keys that you did not load, to ensure that an
    # exception is raised.

    #lets put these in a try/except block
    my_hash_table.find("computer")
    my_hash_table.find("tree")

    # Remove all but one of the nodes and run find() on the remaining node and a
    # removed node, verifying that you get the correct behavior.

    #remove the final node and check again

    #anything else you can thing of!

    #add doc strings and commentary, emulate that example code!



#checking if the base stuff is working
    # my_hash_table = HashQP()
    # employees = []
    # employees.append(Employee("mike", 123456789))
    # employees.append(Employee("fred", 987654321))
    # employees.append(Employee("rick", 555555555))
    #
    # print("Hash Table Size:", my_hash_table.size)
    # for i in range(3):
    #     print("Adding", employees[i].name, "twice")
    #     my_hash_table.insert(employees[i])
    #     my_hash_table.insert(employees[i])
    #
    # print("Hash Table Size (should be 3):", my_hash_table.size)
    #
    # for i in range(3):
    #     if employees[i] in my_hash_table:
    #         print("Verified that", employees[i].name, "is in the table")
    #     else:
    #         print("oops,", employees[i].name, "was not found")
    #
    # my_hash_table_two = HashQP()
    #
    # substrate = "asdlkfj asdoiBIUYVuwer slkdjLJfwoe89)B)(798rjMG0293lkJLJ42lk3j)(*"
    #
    # substrate = substrate + substrate
    # string_list = [substrate[k:k + 5] for k in range(len(substrate) - 5)]
    #
    # my_hash_table_two.max_lambda = .5
    # inserted = 0
    # for k in range(len(substrate) - 5):
    #     if my_hash_table_two.insert(string_list[k]):
    #         print("Inserted string", k, ":", string_list[k])
    #         inserted += 1
    #
    #     else:
    #         print("Did not insert", k, ":", string_list[k])
    # print("Strings inserted:", inserted)
    # print("Size of table:", my_hash_table_two.size)
    # print("Number of buckets:", my_hash_table_two._table_size)
    # print("\nFind the strings:")
    # for k in range(len(substrate) - 5):
    #     if string_list[k] in my_hash_table_two:
    #         print("Found string", k, ":", string_list[k])
    #     else:
    #         print("Did not find", k, ":", string_list[k])