# p4-auto-lock-and-reopen

`p4-auto-lock-and-reopen` is a Perforce (P4) tool designed to help developers check out files, lock them for exclusive editing, and automatically reopen them for continued editing after submitting a changelist. This tool ensures that once files are checked out, they are locked, preventing other users from modifying them, and when the files are submitted, they are immediately available for further editing.

## Features
- **Check out and lock files**: Lock files immediately after checking them out, ensuring exclusive access for the current user.
- **Automatic reopen after submit**: When files are submitted, they are automatically reopened for continued editing without any manual effort.
- **Locking mechanism**: Lock files using Perforce’s built-in `p4 lock` or through exclusive file types (`+l`), depending on your preferences.
- **Easy integration into P4V**: Easily integrates with P4V via custom tools, allowing you to right-click files/folders to perform the operation.

## Prerequisites
- **Perforce (P4)**: This tool requires an active Perforce server and a client workspace to work with. You should have `P4PORT`, `P4USER`, and `P4CLIENT` environment variables properly set for the tool to function.
- **Python 3**: The tool is written in Python, so you will need to have Python 3 installed on your system.
- **P4Python**: The tool uses P4Python, the Perforce Python API, to interact with the Perforce server.

### Install Dependencies
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/p4-auto-lock-and-reopen.git
   cd p4-auto-lock-and-reopen
