import math
import copy
from enum import Enum


class HashEntry:
    class State(Enum):
        ACTIVE = 0
        EMPTY = 1
        DELETED = 2

    def __init__(self, data=None):
        self._data = data
        self._state = HashEntry.State.EMPTY


class HashQP:
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
        # loop doesn't work for 2 or 3
        if floor <= 2:
            return 2
        elif floor == 3:
            return 3
        if floor % 2 == 0:
            candidate = floor + 1
        else:
            candidate = floor

        while True:
            # we know candidate is odd.  check for divisibility by 3
            if candidate % 3 != 0:
                loop_lim = int((math.sqrt(candidate) + 1) / 6)
                # now we can check for divisibility by 6k +/- 1 up to sqrt
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

        #can just use find, and return true or false instead of an object

    #is this the correct implementation of the find method? #nah it needs
    # the overloaded __eq__ operator from KeywordEntry, because that's what
    # we're gonna be using for line 84 here (cuz it needs strings, plus data_
    def find(self, data):
        data = data.upper()
        bucket = self._find_pos(data)
        #do i need to access the data item of the HashEntry class?
        if self._buckets[bucket]._state == HashEntry.State.ACTIVE and self._buckets[bucket]._data == data:
            return self._buckets[bucket]._data #i think here we're returning
            # the
            # whole object, because the example test code shows us calling
            # the .sites property on the returned object of the .find()
            # method, so i assume it's the KeywordEntry object being returned
        else:
            raise HashQP.NotFoundError

    def remove(self, data):
        data = data.upper()
        bucket = self._find_pos(data)
        if self._buckets[bucket]._state != HashEntry.State.ACTIVE:
            # f'did not remove {self._buckets[bucket]._data._word}'
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