from aiogram import types

class CachedPhoto():
    def __init__(self):
        self._data = {}

    def get(self, url):
        if url in self._data:
            return self._data[url]
        return types.URLInputFile(url)

    def update(self, url, id):
        if url not in self._data:
            self._data.update({url: id})

cache_photo = CachedPhoto()

