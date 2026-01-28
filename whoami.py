#!/usr/bin/env python3
"""
User identification module that answers "Who are you?"
"""

import getpass
import socket
import os
import platform
from datetime import datetime


class UserIdentity:
    """Class to represent user identity information"""
    
    def __init__(self):
        self.username = self._get_username()
        self.hostname = self._get_hostname()
        self.os = self._get_os()
        self.home_dir = self._get_home_dir()
        self.timestamp = datetime.now()
    
    def _get_username(self):
        """Get the current username"""
        try:
            return getpass.getuser()
        except Exception:
            return "Unknown"
    
    def _get_hostname(self):
        """Get the hostname"""
        try:
            return socket.gethostname()
        except Exception:
            return "Unknown"
    
    def _get_os(self):
        """Get the operating system information"""
        try:
            return f"{platform.system()} {platform.release()}"
        except Exception:
            return "Unknown"
    
    def _get_home_dir(self):
        """Get the home directory"""
        try:
            return os.path.expanduser("~")
        except Exception:
            return "Unknown"
    
    def who_are_you(self):
        """Answer the question: Who are you?"""
        return {
            "username": self.username,
            "hostname": self.hostname,
            "operating_system": self.os,
            "home_directory": self.home_dir,
            "timestamp": self.timestamp.isoformat()
        }
    
    def __str__(self):
        """String representation of user identity"""
        info = self.who_are_you()
        return f"""User Identity:
  Username: {info['username']}
  Hostname: {info['hostname']}
  OS: {info['operating_system']}
  Home Directory: {info['home_directory']}
  Timestamp: {info['timestamp']}"""


def main():
    """Main function to demonstrate user identification"""
    identity = UserIdentity()
    print("Who are you?\n")
    print(identity)
    print("\n" + "=" * 50)
    print("JSON format:")
    import json
    print(json.dumps(identity.who_are_you(), indent=2))


if __name__ == "__main__":
    main()
