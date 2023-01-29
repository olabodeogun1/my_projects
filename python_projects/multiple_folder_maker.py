# PROGRAM TO GENERATE MULTIPLE FOLDERS TO A PATH

import os

path = os.getcwd()

for i in range(1, 11):
        os.mkdir(path + f"\\{i}")
