import os

# base_dir = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(base_dir, "Modals/TMS.db")
data_file_path = os.path.join(os.path.dirname(__file__), 'Modals/TMS.db')


from PyInstaller.building.datastruct import TOC


def Datafiles(*filenames, **kw):
    import os

    def datafile(path, strip_path=True):
        parts = path.split('/')
        path = name = os.path.join(*parts)
        if strip_path:
            name = os.path.basename(path)
        return name, path, 'DATA'

    strip_path = kw.get('strip_path', True)
    return TOC(
        datafile(filename, strip_path=strip_path)
        for filename in filenames
        if os.path.isfile(filename))


dbfile = Datafiles('Modals/TMS.db', strip_path=False)  # keep the path of this file
