import subprocess
import os
from shutil import copyfile
from shutil import rmtree


def change_name(name, post):
    s = name.split('.')
    return s[0] + post + '.' + s[1]


file_name = "cesare_code.py"
directory = "example"
current = os.getcwd()

if not os.path.exists(os.path.join(current, directory)):
    os.makedirs(os.path.join(current, directory))

copyfile(os.path.join(current, file_name), os.path.join(current, directory, file_name))

os.system(
    'pyminifier ' + os.path.join(current, directory, file_name)
    + ' >> ' + os.path.join(current, directory, change_name(file_name, '_min')))
os.system(
    'pyminifier -O ' + os.path.join(current, directory, file_name)
    + ' >> ' + os.path.join(current, directory, change_name(file_name, '_min_obf')))