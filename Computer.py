"""
Name:
Assignment: Project 2, Computer.py
Date: 3/4/2026
Summary:
This file defines the base class ComputerSystem and its two subclasses Linux
and Windows. ComputerSystem contains common properties and an abstract getSpace()
method that must be overridden by each subclass. The year of purchase is hidden
using a property decorator to protect it from invalid values.
"""


class ComputerSystem:
    """
    Base class for all computer systems in the inventory.
    Contains common properties shared by all computers: IP address,
    year purchased, and operating system. Defines an abstract getSpace()
    method that subclasses must override to return their storage space.
    """

    def __init__(self, ipAddy, yearPurchased, os):
        """
        Initializes a ComputerSystem object with the given properties.
        :param ipAddy: the IP address of the computer (string)
        :param yearPurchased: the year the computer was purchased (int)
        :param os: the operating system installed on the computer (string)
        """
        self.ipAddy = ipAddy
        self.yearPurchased = yearPurchased  # uses the property setter
        self.os = os

    @property
    def yearPurchased(self):
        """
        Getter for the hidden _yearPurchased attribute.
        :return: the year the computer was purchased (int)
        """
        return self._yearPurchased

    @yearPurchased.setter
    def yearPurchased(self, value):
        """
        Setter for the hidden _yearPurchased attribute.
        Validates that the year is 1970 or later before saving.
        :param value: the year to set (int)
        :raises ValueError: if the year is before 1970
        """
        if value < 1970:
            raise ValueError("Invalid year of purchase")
        self._yearPurchased = value

    def getSpace(self):
        """
        Abstract method that must be overridden by subclasses.
        Returns the storage space of the computer as a formatted string.
        :raises NotImplementedError: if called directly on ComputerSystem
        """
        raise NotImplementedError("Subclass must override this method")

    def __str__(self):
        """
        Returns a formatted string representation of the computer,
        used when printing a row in the inventory table.
        :return: formatted string with year, IP, storage space, and OS
        """
        return (f"{self.yearPurchased:<16} {self.ipAddy:<20} "
                f"{self.getSpace():<25} {self.os}")


class Linux(ComputerSystem):
    """
    Represents a Linux computer in the inventory.
    Inherits from ComputerSystem and adds a filesystem (FS) space property.
    Overrides getSpace() to return the filesystem space.
    """

    def __init__(self, ipAddy, yearPurchased, os, fs_space):
        """
        Initializes a Linux computer with all ComputerSystem properties
        plus the filesystem space.
        :param ipAddy: the IP address of the computer (string)
        :param yearPurchased: the year the computer was purchased (int)
        :param os: the operating system installed on the computer (string)
        :param fs_space: the filesystem storage capacity (string, e.g. "750 GB")
        """
        super().__init__(ipAddy, yearPurchased, os)
        self.fs_space = fs_space

    def getSpace(self):
        """
        Overrides the abstract getSpace() method from ComputerSystem.
        :return: a formatted string showing the filesystem capacity
        """
        return f"Filesystem: {self.fs_space}"


class Windows(ComputerSystem):
    """
    Represents a Windows computer in the inventory.
    Inherits from ComputerSystem and adds a C drive space property.
    Overrides getSpace() to return the C drive space.
    """

    def __init__(self, ipAddy, yearPurchased, os, c_drive_space):
        """
        Initializes a Windows computer with all ComputerSystem properties
        plus the C drive space.
        :param ipAddy: the IP address of the computer (string)
        :param yearPurchased: the year the computer was purchased (int)
        :param os: the operating system installed on the computer (string)
        :param c_drive_space: the C drive storage capacity (string, e.g. "500 GB")
        """
        super().__init__(ipAddy, yearPurchased, os)
        self.c_drive_space = c_drive_space

    def getSpace(self):
        """
        Overrides the abstract getSpace() method from ComputerSystem.
        :return: a formatted string showing the C drive capacity
        """
        return f"C drive: {self.c_drive_space}"