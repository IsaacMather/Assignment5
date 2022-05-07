class KeywordEntry:

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

    #are greater than and less than overloaded string comparison operators?

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        if isinstance(other, str):
            other = other.upper()
            return self._word == other

        elif isinstance(other, KeywordEntry):
            self._word == other._word

    def __hash__(self):
        pass


    #The comparison functions will be acting on strings, a we will sort and
    # hash on self._word. The comparison functions should allow a
    # KeywordEntry object to be compared to either another KeywordEntry
    # object (using self._word for comparison) or a string (again compring
    # the string to self._word). When implemeting the string comparison,
    # remember that self_word has been converted to uppercase, so the string
    # on the right side of the comparison needs to be converted as well.