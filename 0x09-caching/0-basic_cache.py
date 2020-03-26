#!/usr/bin/python3
'''BasicCache module'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache classs'''

    def put(self, key, item):
        '''add item to the cache'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''get item from the cache'''
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
