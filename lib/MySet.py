# class MySet:
#     def first_repeated_value(list):
#         #create a Set to keep track of values we've seen
#         number_set = set()
#         #iterate over each element from the list
#         for i in range(0, len(list)):
#                 #if we've already seen a value, we've found the duplicate!
#                 if list[i] in number_set:
#                     return list[i]
#                 #otherwise, add the value to our set
#                 number_set.add(list[i])
#             #return None if we reach the end and haven't found our value    
#         return None        

#     print(first_repeated_value([1,2,3,3,4,4]))
#     pass

class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

    def add(self, value):
        self.dictionary[value] = True 
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()
