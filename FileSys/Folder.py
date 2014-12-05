from FileSys.File import File

__author__ = 'adri'


class Folder():

    def __init__(self, name, parent=None, root=None):
        self.name = name
        self.parent = parent
        self.path = self.generate_path()
        self.root = root
        self.folders = []
        self.files = []

    def generate_path(self):
        if self.parent is None:
            return '/'
        else:
            return self.parent.path + self.name + '/'

    def ls(self):
        ret = []
        for folder in self.folders:
            ret.append(folder.name)
        for file in self.files:
            ret.append(file)
        return ret

    def add_new_file(self, file_name, data):
        file_to_save = File(file_name)
        self.files.append(file_to_save)
        return file_to_save

    def cd(self, path):
        path_list = self.split_path(path)
        return self.navigate(path_list)

    def navigate(self, path_list):
        if path_list[0] == '':
            return self
        else:
            first_path = path_list.pop(0)
            folder = self.find_folder(first_path)
            return folder.navigate(path_list)

    def split_path(self, path):
        return path.split('/')

    def find_folder(self, folder_name):
        fold = filter(lambda x: x.name == folder_name, self.folders)
        return fold[0]

    def add_folder(self, folder):
        self.folders.append(folder)

    def add_file(self, file):
        self.files.append(file)

    def get_path(self):
        return self.path

