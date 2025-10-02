import P4
import sys

p4 = P4.P4()
p4.connect()

def lock_files(files):
    for f in files:
        try:
            p4.run("edit", "-l", f)
            print(f"Locked {f}")
        except P4.P4Exception as e:
            print(f"Error locking {f}: {e}")


changelist = sys.argv[1] 

files = [f['depotFile'] for f in p4.run("describe", "-s", changelist)['depotFile']]

lock_files(files)
p4.disconnect()
