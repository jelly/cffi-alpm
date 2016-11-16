from alpm._alpm import ffi, lib

class AlpmList():
    def __init__(self, alpm_list=None):
        if alpm_list:
            self.list = alpm_list
        else:
            self.list = ffi.cast('alpm_list_t *', ffi.NULL)
            self.head = self.list

    def add(self, item):
        self.list = lib.alpm_list_add(self.list, item)

    def next(self):
        res = lib.alpm_list_next(self.list)
        if res:
            self.list = res
            return res
        return None

    def __iter__(self):
        class AlpmListIterator():
            def __init__(self, alpm_list):
                self.list = alpm_list

            def __next__(self):
                if self.list:
                    result = self.list.data
                else:
                    raise StopIteration

                self.list = lib.alpm_list_next(self.list)
                return result

        return AlpmListIterator(self.list)
