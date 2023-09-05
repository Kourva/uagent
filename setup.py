#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Resources
import shutil
import os
import sys

# Raise root exception if file not executed with root
def check_root() -> None | Exception:
    if os.geteuid() != 0:
        raise PermissionError("You must run this tool as root!")

# Print error if user is running this code on Windows
def Check_OS() -> None | Exception:
    if os.name == 'posix' and os.uname().sysname.lower() == 'linux':
        print("Operation System: Linux")
    else:
        raise OSError("This tool is only compatible with Linux!")
        

# Installer
def uagent_installer() -> None:
    # Define the source and destination paths
    source_useragents = 'uagent.txt'
    destination_useragents = '/etc/uagent/uagent.txt'
    man_file = "uagent.1.gz"

    # Create the /etc/uagent directory if it doesn't exist
    try:
        os.makedirs('/etc/uagent')
    except FileExistsError:
        pass  # Directory already exists

    # Copy uagent.txt to /etc/uagent
    shutil.copy2(source_useragents, destination_useragents)

    # Make sure the copied file has the correct permissions (adjust as needed)
    os.chmod(destination_useragents, 0o644)

    # Copy main script to /usr/local/bin
    shutil.copy2('uagent', '/usr/local/bin/uagent')

    # Make the copied script executable
    os.chmod('/usr/local/bin/uagent', 0o755)

    # Copy man file
    shutil.copy2(man_file, "/usr/local/share/man/man1")

    # Print a message indicating successful installation
    print("uagent has been successfully installed!")

# Uninstaller
def uagent_uninstaller() -> None:
    # Define the paths to remove
    script_path = '/usr/local/bin/uagent'
    useragents_path = '/etc/uagent/uagent.txt'
    man_file = "/usr/local/share/man/man1/uagent.1.gz"

    # Remove the script from /usr/local/bin
    if os.path.exists(script_path):
        os.remove(script_path)
        print(f"Removed {script_path}")

    # Remove the uagent.txt file
    if os.path.exists(useragents_path):
        os.remove(useragents_path)
        print(f"Removed {useragents_path}")

    # Remove the man file
    if os.path.exists(man_file):
        os.remove(man_file)
        print(f"Removed {man_file}")

    # Remove the /etc/uagent directory if it's empty
    try:
        os.rmdir('/etc/uagent')
        print("Removed /etc/uagent directory")
    except OSError:
        pass  # Directory may not be empty

    # Print a message indicating successful uninstallation
    print("uagent has been successfully uninstalled!")

# Run installer
if __name__ == "__main__":

    # Check OS
    Check_OS()

    # Check root privilege
    check_root()
    
    try:
        # Run installer
        if sys.argv[1] == "install":
            uagent_installer()
        
        # Run uninstaller
        elif sys.argv[1] == "uninstall":
            uagent_uninstaller()

        else:
            raise IndexError
    
    except IndexError:
        # Print usage for user
        print("Usage: python3 setup.py [install/uninstall]")