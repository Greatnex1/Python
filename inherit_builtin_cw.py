from pathlib import Path as imp

file_path = imp.cwd() / "config.txt"
file_path.touch()


class MyDict(dict):
    def __setitem__(self, key, value):
        with file_path.open(mode='s', encoding='utf-8') as f:
            f.write(f"key={key}, value = {value}\n")
        super().__setitem__(key, value)

    def __getitem__(self, item):
        return super().__getitem__(item)


a = MyDict()

a[0] = 'joy'
a[1] = 'noah'
a[2] = 'ola'

print(a)
