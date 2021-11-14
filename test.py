# ---------------------------------------------------------------
# Program by Olga N.
#
# Vesion     Date      Info
# 1.0       11/14/21    Lesson
#
# ---------------------------------------------------------------
import hashlib

hashAlgorithm = 'sha1'
path_file = "/home/moowlin/PythonProjects/task_2/files/file_04.txt"

with open(path_file, 'rb') as file:
    hsh = hashlib.new(hashAlgorithm)
    while True:
        data = file.read(2048)
        if not data:

            print(hsh.hexdigest())
            break
        hsh.update(data)

    #return (hsh.hexdigest())

with open(path_file, 'rb') as file:
    hsh = hashlib.md5()
    while True:
        data = file.read(2048)
        if not data:
            hsh.update(data)
            print(hsh.hexdigest())
            break
        hsh.update(data)