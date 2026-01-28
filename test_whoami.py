#!/usr/bin/env python3
"""
Tests for the user identification module
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import whoami
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from whoami import UserIdentity


class TestUserIdentity(unittest.TestCase):
    """Test cases for UserIdentity class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.identity = UserIdentity()
    
    def test_username_not_none(self):
        """Test that username is retrieved"""
        self.assertIsNotNone(self.identity.username)
        self.assertNotEqual(self.identity.username, "")
    
    def test_hostname_not_none(self):
        """Test that hostname is retrieved"""
        self.assertIsNotNone(self.identity.hostname)
        self.assertNotEqual(self.identity.hostname, "")
    
    def test_os_not_none(self):
        """Test that OS information is retrieved"""
        self.assertIsNotNone(self.identity.os)
        self.assertNotEqual(self.identity.os, "")
    
    def test_home_dir_not_none(self):
        """Test that home directory is retrieved"""
        self.assertIsNotNone(self.identity.home_dir)
        self.assertNotEqual(self.identity.home_dir, "")
    
    def test_who_are_you_returns_dict(self):
        """Test that who_are_you returns a dictionary"""
        result = self.identity.who_are_you()
        self.assertIsInstance(result, dict)
    
    def test_who_are_you_has_required_keys(self):
        """Test that who_are_you returns all required keys"""
        result = self.identity.who_are_you()
        required_keys = ["username", "hostname", "operating_system", 
                        "home_directory", "timestamp"]
        for key in required_keys:
            self.assertIn(key, result)
    
    def test_str_representation(self):
        """Test string representation of UserIdentity"""
        str_repr = str(self.identity)
        self.assertIn("User Identity:", str_repr)
        self.assertIn("Username:", str_repr)
        self.assertIn("Hostname:", str_repr)
    
    def test_timestamp_is_set(self):
        """Test that timestamp is properly set"""
        self.assertIsNotNone(self.identity.timestamp)
    
    def test_who_are_you_values_not_unknown(self):
        """Test that basic values are not 'Unknown' (in normal circumstances)"""
        result = self.identity.who_are_you()
        # In a normal environment, username should not be Unknown
        # This might fail in very restricted environments, but should pass normally
        self.assertNotEqual(result["username"], "Unknown")


if __name__ == "__main__":
    unittest.main()
