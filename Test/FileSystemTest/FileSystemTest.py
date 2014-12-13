import unittest
from FileSys.File import File, INode
from FileSys.Folder import Folder
from HardWare.HardDisk import HardDisk


class FileSystemTest(unittest.TestCase):

    def setUp(self):
        self.hdd = HardDisk()
        self.root = Folder('root')
        self.folder1 = Folder('pepe', self.root, self.root)
        self.folder2 = Folder('carlos', self.folder1, self.root)
        self.folder3 = Folder('juan', self.folder2, self.root)
        self.inode = INode('text')
        self.file1 = File('text', self.inode)
        self.root.add_folder(self.folder1)
        self.folder1.add_folder(self.folder2)
        self.folder2.add_folder(self.folder3)
        self.folder3.add_file(self.file1)

    def find_folder_test(self):
        ass = self.folder1.find_folder('juan')
        self.assertEqual(ass, self.folder3)

    def ls_test(self):
        ls = self.folder3.ls()
        self.assertEqual(ls, [self.file1])

    def cd_test(self):
        folder = self.root.cd('pepe/carlos/juan/')
        l = folder.ls()
        self.assertEqual(l, [self.file1])

    def generate_path_test(self):
        p = self.folder3.get_path()
        self.assertEqual(p, '/pepe/carlos/juan/')
