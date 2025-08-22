import sys
from P4 import P4, P4Exception

p4 = P4()

def lock_checked_out_files():
    """Locks all checked-out files."""
    try:
        opened_files = p4.run("opened")  # Get opened (checked-out) files
        if not opened_files:
            print("No files are currently checked out.")
            return

        for file in opened_files:
            file_path = file['file']
            print(f"Locking {file_path}")
            p4.run("lock", file_path)
    except P4Exception as e:
        print(f"Error locking files: {e}")

def unlock_files_in_changelist(changelist_id):
    """Unlocks files that were part of the specified changelist."""
    try:
        submitted_files = p4.run("describe", changelist_id)  # Get the files submitted in the changelist
        if not submitted_files:
            print(f"No files found for changelist {changelist_id}.")
            return

        # Assuming the first entry contains the file information
        for file in submitted_files[0].get('depotFile', []):
            print(f"Unlocking {file}")
            p4.run("unlock", file)
    except P4Exception as e:
        print(f"Error unlocking files: {e}")

def disconnect() -> None:
    """Disconnects from the Perforce server."""
    if p4.connected():
        p4.disconnect()

def init(username=None, port=None, password=None):
    """Initialize the P4 connection and log in."""
    if port and p4.port != port:
        disconnect()
        p4.port = port or p4.port
    
    p4.user = username or p4.user
    if not p4.connected():
        p4.connect()
    try:
        p4.run_login("-s")  # Login using saved credentials
    except P4Exception as e:
        if not password:
            raise e
        p4.password = password
        try:
            p4.run_login()  # Attempt login with the password
        except P4Exception as e:
            if "invalid or unset" in e.args[0]:
                raise e

    return True

def main(*paths):
    """Main function to control locking and unlocking based on paths."""
    if not paths:
        print("Please provide depot paths or changelist IDs.")
        return

    for path in paths:
        if path.startswith("//"):  # If it's a depot path, lock checked out files
            lock_checked_out_files()
        else:  # Otherwise, it's assumed to be a changelist ID, unlock files in changelist
            unlock_files_in_changelist(path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: p4-lock-unlock <depot_path_or_changelist_id>")
        sys.exit(1)

    try:
        init(username="your-username", password="your-password", port="perforce-server:1666")
        main(*sys.argv[1:])  # Pass the arguments to the main function
    except P4Exception as e:
        print(f"Error: {e}")
    finally:
        disconnect()