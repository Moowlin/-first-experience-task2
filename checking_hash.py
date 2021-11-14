#!/usr/bin/python3

"""Программа читает файл,содержащий имена файлов, алгоритм хэширования и соответсввующие им хэш-суммы, и проверяет
целостность указанных файлов.
Пример вызова программы: <script.py> <path to the input file> <path to the directory containing files to check>"""

# ---------------------------------------------------------------
# Program by Olga N.
#
# Vesion     Date      Info
# 1.0       11/13/21    Lesson
#
# ---------------------------------------------------------------

import hashlib      # for to calculate hash sums
import os           # for to connect paths and check if a file exists
import sys          # for CLI Arguments

# Check of command:
if len(sys.argv) < 3:
    print('Missing arguments: Usage is <script.py> <path to the input file> <path to the directory containing files to check>')

InputFile = sys.argv[1]         # get control file
PathToCheckFile = sys.argv[2]   # get path to  check files

# ============================================= FUNCTIONS =============================================================

def computation_hash(path_file, hashAlgorithm):

    """Функция вычисления хэша по заданному алгоритму. Функция вовзращает результат как строковой объект, содержащий
     только шестнадцатеричные цифры"""

    with open(path_file, 'rb') as file:
        hsh = hashlib.new(hashAlgorithm)
        while True:
            data = file.read(2048)
            if not data:
                break
            hsh.update(data)
        return(hsh.hexdigest())


def comparisonHashs(ControlHash, HashFile):

    """Функция сравнения значений хэш-сумм"""

    if ControlHash == HashFile:
        return "OK"
    else:
        return "FAIL"


# ============================================ MAIN ==================================================================

with open(InputFile, 'r') as control_file:
    for line in control_file:
        if line.isspace():
            continue                                                        # skip blank lines
        else:
            line = line.strip().split()
            WorkFile = line[0]                                              # get file's name
            HashAlgorithm = line[1].lower()                                 # get algorithm's name
            HashFromControlFile = line[2]                                   # get hash value
            PathFile = os.path.join(PathToCheckFile, WorkFile)              # get full path of the file

            if os.path.isfile(PathFile) == True:                            # checking for file existence
                HashFile = computation_hash(PathFile, HashAlgorithm)        # calculate the hash
                result = comparisonHashs(HashFromControlFile, HashFile)     # comparison hashs
                print(f'{WorkFile} {result}')
            else:
                print(f'{WorkFile} NOT FOUND')