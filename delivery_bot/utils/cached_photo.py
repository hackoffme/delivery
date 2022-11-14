from aiogram import types


class CachedPhoto():
    def __init__(self):
        self._data = {}

    def get(self, url):
        if url in self._data:
            return self._data[url]
        try:
            photo = types.URLInputFile(url)
        except:
            return None
        return photo

    def update(self, url, id):
        if url not in self._data:
            self._data.update({url: id})


cache_photo = CachedPhoto()
