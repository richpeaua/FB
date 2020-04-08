import glob
import os

dir_entries = glob.glob("*")

for entry in dir_entries:
    if '.py' in entry:
        st = os.stat(entry)
        print(st.st_uid)