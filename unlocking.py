import P4
import sys

p4 = P4.P4()
p4.connect()

def unlock_files(files):
    for f in files:
        try:
            p4.run("revert", "-k", f)
            print(f"Unlocked {f}")
        except P4.P4Exception as e:
            print(f"Error unlocking {f}: {e}")

changelist = sys.argv[1]

files = [f['depotFile'] for f in p4.run("describe", "-s", changelist)['depotFile']]

unlock_files(files)
p4.disconnect()