from HashQP import HashQP, HashEntry
from KeywordEntry import KeywordEntry
from Employee import Employee

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Instantiate a HashQP object.
    my_hash_table: HashQP = HashQP()

    # Create at least ten KeywordEntry objects and load them in to your hash table.
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

    # Run find() on each key to make sure they can all be found.  Make sure case doesn't matter, so using the example above, both of these calls:
    my_hash_table.find("ONE")
    my_hash_table.find("aS")
    my_hash_table.find("wriTTen")
    my_hash_table.find("tHE")
    my_hash_table.find("class")
    my_hash_table.find("does")
    my_hash_table.find("not")
    my_hash_table.find("have")
    my_hash_table.find("valid")
    my_hash_table.find("comparison")

    #run find on some keys that you did not load, to ensure that an
    # exception is raised.

    try:
        my_hash_table.find("computer")
    except HashQP.NotFoundError:
        print("Successfully did not find computer")

    try:
        my_hash_table.find("tree")
    except HashQP.NotFoundError:
        print("Successfully did not find tree")


    # Remove all but one of the nodes and run find() on the remaining node
    my_hash_table.remove("ONE")
    my_hash_table.remove("aS")
    my_hash_table.remove("wriTTen")
    my_hash_table.remove("the")
    my_hash_table.remove("tHE")
    my_hash_table.remove("class")
    my_hash_table.remove("does")
    my_hash_table.remove("nOt")
    my_hash_table.remove("have")
    my_hash_table.remove("valId")

    # Remove all but one of the nodes and run find() on the remaining node and
    # a removed node, verifying that you get the correct behavior.
    if my_hash_table.find("comparison"):
        print('successfully found comparison')
    else:
        print('Did not find comparison')

    try:
        my_hash_table.find("oNe")
    except HashQP.NotFoundError:
        print("Successfully did not find oNe")

    try:
        my_hash_table.find("HaVe")
        print('oops found have')
    except HashQP.NotFoundError:
        print("Successfully did not find HaVe")


    #remove the final node and check again
    my_hash_table.remove('comparison')


    # after removing all but one removed node, run find on a removed
    # node verifying that you get the correct behavior.
    try:
        my_hash_table.find("COMPARISON")
        print('oops found comparison')
    except HashQP.NotFoundError:
        print("Successfully did not find comparison")








    #anything else you can thing of!




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