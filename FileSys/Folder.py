from FileSys.File import File

__author__ = 'adri'


class Folder():

    def __init__(self, name, hdd, parent=None, root=None):
        self.name = name
        self.parent = parent
        self.path = self.generate_path()
        self.root = root
        self.folders = []
        self.files = []
        self.hdd = hdd

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

    def add_new_file(self, file_name, inode):
        file_to_save = File(file_name, inode)
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
        fold = next(x for x in self.folders if x.name == folder_name)
        return fold[0]

    def add_folder(self, folder):
        self.folders.append(folder)
        self.hdd.create_inode_for_folder(self.name, folder.name)

    def add_file(self, file):
        self.files.append(file)

    def get_path(self):
        return self.path

    def get_file(self, file_name):
        file = next(f for f in self.files if f.name == file_name)
        return file

    def get_data(self, path):
        path_to_folder = self.split_path(path)
        file_name_with_extension = path_to_folder.pop()
        path_to_folder.append('')
        folder = self.navigate(path_to_folder)
        file_name_without_extension = file_name_with_extension.split('.')
        file = folder.get_file(file_name_without_extension[0])
        return file.inode.pointer