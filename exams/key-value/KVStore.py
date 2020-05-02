class KVStore:
    """Simple key-value store using dict
    kinda crap
    """

    def __init__(self):
        """Initially empty"""
        self.__store = {}

    def insert(self, key, value):
        """Insert or replace value"""
        self.__store[key] = value

    def get(self, key):
        """Get value; returns None if not present"""
        try:
            return self.__store[key]
        except KeyError:
            return None

    def set(self, key, value):
        """Replace value"""
        self.__store[key] = value

    def delete(self, key):
        """remove value at key"""
        try:
            del self.__store[key]
        except KeyError:
            pass

    def __iter__(self):
        # use the items tuple-list of dict!
        # (this is a rather expensive & lazy way to do it...)
        self.iterable = list(self.__store.items())
        self.pointer = 0
        return self

    def __next__(self):
        # raise StopIteration when exhausted
        if self.pointer >= len(self.iterable):
            raise StopIteration
        ret = self.iterable[self.pointer]
        self.pointer += 1
        return ret

if __name__ == '__main__':
    # Example usage from exam
    db = KVStore() # Create and initialise a new kv-store
    obj = {'hi': 44} # Arbitrary object (can be any data type)
     
    db.insert("name", "Rick Astley")
    db.insert("object", obj)
     
    name = db.get("name")
    print(name)
     
    # Iteration
    for key, value in db:
        print(key, ":", value)

    print('delete obj')
    db.delete("object")

    for key, value in db:
        print(key, ":", value)
