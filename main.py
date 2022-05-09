import math
import copy
from enum import Enum


class HashEntry:
    """Used to store data, and store the state of the data in the Hash Table

        Args:
            data (): any object which has active or overloaded comparison
            operators
    """
    class State(Enum):
        ACTIVE = 0
        EMPTY = 1
        DELETED = 2

    def __init__(self, data=None):
        self._data = data
        self._state = HashEntry.State.EMPTY


class HashQP:
    """Quadratic probing hash table that stores HashEntry objects

        Args:
            table_size (int): initial size of the table
    """
    class NotFoundError(Exception):
        pass

    INIT_TABLE_SIZE = 97
    INIT_MAX_LAMBDA = .49

    def __init__(self, table_size=None):

        if table_size is None or table_size < HashQP.INIT_TABLE_SIZE:
            self._table_size = self._next_prime(HashQP.INIT_TABLE_SIZE)
        else:
            self._table_size = self._next_prime(table_size)
        self._buckets = [HashEntry() for _ in range(self._table_size)]
        self._max_lambda = HashQP.INIT_MAX_LAMBDA
        self._size = 0
        self._load_size = 0

    def _internal_hash(self, item):
        return hash(item) % self._table_size

    def _next_prime(self, floor):
        if floor <= 2:
            return 2
        elif floor == 3:
            return 3
        if floor % 2 == 0:
            candidate = floor + 1
        else:
            candidate = floor

        while True:
            if candidate % 3 != 0:
                loop_lim = int((math.sqrt(candidate) + 1) / 6)
                for k in range(1, loop_lim + 1):
                    if candidate % (6 * k - 1) == 0:
                        break
                    if candidate % (6 * k + 1) == 0:
                        break
                    if k == loop_lim:
                        return candidate
            candidate += 2

    def _find_pos(self, data):
        kth_odd_number = 1
        bucket = self._internal_hash(data)
        while self._buckets[bucket]._state != HashEntry.State.EMPTY and \
                self._buckets[bucket]._data != data:
            bucket += kth_odd_number
            kth_odd_number += 2
            if bucket >= self._table_size:
                bucket -= self._table_size
        return bucket

    def __contains__(self, data):
        bucket = self._find_pos(data)
        return self._buckets[bucket]._state == HashEntry.State.ACTIVE

    def find(self, data):
        data = data.upper()
        bucket = self._find_pos(data)
        if self._buckets[bucket]._state == HashEntry.State.ACTIVE and \
                self._buckets[bucket]._data == data:
            print(f'successfully found {data}')
            return self._buckets[bucket]._data
        else:
            raise HashQP.NotFoundError

    def remove(self, data):
        data = data.upper()
        bucket = self._find_pos(data)
        if self._buckets[bucket]._state != HashEntry.State.ACTIVE:
            return False
        else:
            print(f'successfully removed {self._buckets[bucket]._data._word}')
            self._buckets[bucket]._state = HashEntry.State.DELETED
            self._size -= 1
            return True

    def insert(self, data):
        bucket = self._find_pos(data)
        if self._buckets[bucket]._state == HashEntry.State.ACTIVE:
            return False
        elif self._buckets[bucket]._state == HashEntry.State.EMPTY:
            self._load_size += 1
        self._buckets[bucket]._data = data
        self._buckets[bucket]._state = HashEntry.State.ACTIVE
        self._size += 1
        if self._load_size > self._max_lambda * self._table_size:
            self._rehash()
        print(f' Successfully inserted {data._word}')
        return True

    def _rehash(self):
        old_table_size = self._table_size
        self._table_size = self._next_prime(2 * old_table_size)
        old_buckets = copy.copy(self._buckets)
        self._buckets = [HashEntry() for _ in range(self._table_size)]
        self._size = 0
        self._load_size = 0
        for k in range(old_table_size):
            if old_buckets[k]._state == HashEntry.State.ACTIVE:
                self.insert(old_buckets[k]._data)

    @property
    def size(self):
        return self._size

class KeywordEntry:
    """Stores information about a specific word on a webpage

        Args:
            word (str): the word we're storing info about
            url (str): the url the word is located on
            location (int): location, where the word is on the page
    """

    def __init__(self, word: str, url: str = None, location: int = None):
        self._word = word.upper()
        if url:
            self._sites = {url: [location]}
        else:
            self._sites = {}

    def add(self, url: str, location: int) -> None:
        if url in self._sites:
            self._sites[url].append(location)
        else:
            self._sites[url] = [location]

    def get_locations(self, url: str) -> list:
        try:
            return self._sites[url]
        except IndexError:
            return []

    @property
    def sites(self) -> list:
        return [key for key in self._sites]

    def __lt__(self, other):
        if isinstance(other, str):
            other = other.upper()
            return self._word < other

        elif isinstance(other, KeywordEntry):
            return self._word < other._word

        else:
            print("Error, incorrect data type passed to __lt__")

    def __gt__(self, other):
        if isinstance(other, str):
            other = other.upper()
            return self._word > other

        elif isinstance(other, KeywordEntry):
            return self._word > other._word

        else:
            print("Error, incorrect data type passed to __gt__")

    def __eq__(self, other):
        if isinstance(other, str):
            other = other.upper()
            return self._word == other

        elif isinstance(other, KeywordEntry):
            return self._word == other._word

        else:
            print("Error, incorrect data type passed to __eq__")

    def __hash__(self):
        return hash(self._word)


def testing_code():
    # Instantiate a HashQP object.
    my_hash_table: HashQP = HashQP()

    print('Create at least ten KeywordEntry objects and load them in to your '
          'hash table.')
    keyword_entry_list = [
        KeywordEntry("one", "foothill.edu", 4),
        KeywordEntry("as", "foothillcollege.instructure.com/", 1),
        KeywordEntry("written", "foothillcollege.instructure.com/", 2),
        KeywordEntry("the", "foothill.edu", 5),
        KeywordEntry("class", "foothillcollege.instructure.com/", 10),
        KeywordEntry("does", "foothill.edu", 11),
        KeywordEntry("not", "foothill.edu", 7),
        KeywordEntry("have", "foothill.edu", 3),
        KeywordEntry("valid", "foothill.edu", 8),
        KeywordEntry("comparison", "foothill.edu", 9),
    ]

    for keyword_entry in keyword_entry_list:
        my_hash_table.insert(keyword_entry)

    print("\nRun find() on each key to make sure they can all be found.  Make "
          "sure ase doesnt matter, so using the example above, both of these "
          "calls:")
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

    print('\nRun find on some keys that you did not load, to ensure that an '
          'exception is raised.')
    try:
        my_hash_table.find("computer")
    except HashQP.NotFoundError:
        print("Successfully did not find computer")

    try:
        my_hash_table.find("tree")
    except HashQP.NotFoundError:
        print("Successfully did not find tree")

    print('\nRemove all but one of the nodes')
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

    print('\nRun find() on the remaining '
          'node and a removed node, verifying that you get the correct '
          'behavior.')
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

    print('\nRemove the final node and check again')
    my_hash_table.remove('comparison')

    print('\nAfter removing all but one removed node, run find on a removed '
          'node verifying that you get the correct behavior.')
    try:
        my_hash_table.find("COMPARISON")
        print('oops found comparison')
    except HashQP.NotFoundError:
        print("Successfully did not find comparison")

if __name__ == '__main__':
   testing_code()


# Sample output
"""/Users/isaacmather/PycharmProjects/Assignment5/venv/bin/python /Users/isaacmather/PycharmProjects/Assignment5/main.py
Create at least ten KeywordEntry objects and load them in to your hash table.
 Successfully inserted ONE
 Successfully inserted AS
 Successfully inserted WRITTEN
 Successfully inserted THE
 Successfully inserted CLASS
 Successfully inserted DOES
 Successfully inserted NOT
 Successfully inserted HAVE
 Successfully inserted VALID
 Successfully inserted COMPARISON

Run find() on each key to make sure they can all be found.  Make sure ase doesnt matter, so using the example above, both of these calls:
successfully found ONE
successfully found AS
successfully found WRITTEN
successfully found THE
successfully found CLASS
successfully found DOES
successfully found NOT
successfully found HAVE
successfully found VALID
successfully found COMPARISON

Run find on some keys that you did not load, to ensure that an exception is raised.
Successfully did not find computer
Successfully did not find tree

Remove all but one of the nodes
successfully removed ONE
successfully removed AS
successfully removed WRITTEN
successfully removed THE
successfully removed CLASS
successfully removed DOES
successfully removed NOT
successfully removed HAVE
successfully removed VALID

Run find() on the remaining node and a removed node, verifying that you get the correct behavior.
successfully found COMPARISON
successfully found comparison
Successfully did not find oNe
Successfully did not find HaVe

Remove the final node and check again
successfully removed COMPARISON

After removing all but one removed node, run find on a removed node verifying that you get the correct behavior.
Successfully did not find comparison

Process finished with exit code 0"""

