class smartDict:

    def __init__(self, value_list):
        self.index = 0
        self.value_list = value_list

    def __setattr__(self, key, value):
        print('----')
        print("key", key)
        print("value", value)
        self.__dict__[key] = value

    def __getattr__(self, key):
        print(key)
        print("key", key)
        return self.__dict__[key]

    def __iter__(self):
        return self

    def __next__(self):
        keys_self = list(self.value_list)
        if self.index == len(keys_self):
            # self.index = 0
            raise StopIteration
        self.index += 1
        return self.value_list[self.index]

    def _func(self):
        print('_func')
        print(list(self.__dict__.keys()))

smarty = smartDict([])
smarty.__setattr__('name1', 'value1')
smarty.__setattr__('name2', 'value2')
smarty.__setattr__('name3', 'value3')
# print(smarty.__dict__)
# smarty._func()

for key, value in smarty:
    print(key)
    print(value)

