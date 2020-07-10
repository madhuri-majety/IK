"""
K-V Store++
PUT(K, V), DELETE(K), GET(K), GETRANDOM()-> return a value but with a probability of 1/size of the store

Design a data structure that supports following operations in O(1) time.

insert/put(x): Inserts an item x to the data structure if not already present.

remove/delete(x): Removes an item x from the data structure if present.

search/get(x): Searches an item x in the data structure.

getRandom(): Returns a random element from current set of elements

https://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-delete-search-and-getrandom-in-constant-time/

Notes:
Just to ensure that often problems will require auxiliary structures
Delete from the middle of the array can be done in O(1) ==> Swap with last element of the array and decrease the size of array by 1
When using 2 data structures, ensure that there are 2 pointers, forward pointer and backward pointer
    Hash map will have a pointer pointing to index of an array
    Array will have the index element pointing to hash map keys


"""

import random

class MagicMap(object):
    def __init__(self):
        self.hashmap = {}
        self.list_keys = list()
        self.index = 0

    def put(self,key,value):
        if key not in self.hashmap:
            self.hashmap[key] = {}
            self.hashmap[key]['value_stored'] = [value]
            self.list_keys.insert(self.index, key)
            self.hashmap[key]['key_idx'] = self.index
            self.index += 1
            return True
        else:
            if value not in self.hashmap[key]['value_stored']:
                self.hashmap[key]['value_stored'].append(value)
                return True
        return False

    def get(self,key):
        if key in self.hashmap.keys():
            return self.hashmap[key]['value_stored']
        return None

    def delete(self,key):
        if key in self.hashmap.keys():
            del_idx = self.hashmap[key]['key_idx']
            del self.hashmap[key]
            print("****Hashmap:{}".format(self.hashmap))

            update_key = self.list_keys[self.index-1]
            print("****Update Key:{}".format(update_key))

            self.list_keys[del_idx], self.list_keys[-1] = self.list_keys[-1], self.list_keys[del_idx]
            print("****Swapped List:{}".format(self.list_keys))

            self.list_keys.pop()
            print("****Deleted List:{}".format(self.list_keys))

            print("****Self Index:{}".format(self.index))
            self.index -= 1

            self.hashmap[update_key]['key_idx'] = del_idx
            return True
        return False

    def get_random(self):
        idx = random.randint(0, self.index-1)
        hash_key = self.list_keys[idx]
        if hash_key in self.hashmap:
            return self.hashmap[hash_key]['value_stored']
        return None

    def print_magic_map(self):
        print("Printing Hash Map")
        for k,v in self.hashmap.items():
            print("{} : {}".format(k,v))
        print("Printing auxillary DS list")
        print(self.list_keys)
        print("Global Index at {}".format(self.index))
        print("#######################################")


def main():
    mm = MagicMap()
    mm.put("Madhu","408-431-0737")
    mm.put("Madhu","408-338-6382")
    mm.put("Sumanth","650-759-0291")
    mm.print_magic_map()
    print("Madhu has {}".format(mm.get("Madhu")))
    mm.delete("Suman")
    mm.print_magic_map()
    mm.put("Sumanth", "650-759-0291")
    mm.print_magic_map()
    mm.put("Rithika", "408-338-6382")
    mm.put("Someone", "408-338-6388")
    mm.print_magic_map()
    print(mm.get_random())
    mm.delete("Sumanth")
    mm.print_magic_map()
    print(mm.get('Rithika'))
    print(mm.get_random())
    mm.put("Sumanth", "650-759-0291")
    mm.print_magic_map()

if __name__ == '__main__':
    main()


