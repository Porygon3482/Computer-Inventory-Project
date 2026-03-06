"""
Computer.py
Base and subclasses for the computer inventory system.
"""

class ComputerSystem:
    """
    Base Class for all computer systems
    """

    def __init__(self, ipAddy, yearPurchased, os):
        self.ipAddy = ipAddy
        self.yearPurchased = yearPurchased  # uses the property setter
        self.os = os

    @property
    def yearPurchased(self):
        return self._yearPurchased

    @yearPurchased.setter
    def yearPurchased(self, value):
        if value < 1970:
            raise ValueError("Invalid year of purchase")
        self._yearPurchased = value

    def getSpace(self):
        """Abstract method - must be overridden by subclasses"""
        raise NotImplementedError("Subclass must override this method")

    def __str__(self):
        return (f"{self.yearPurchased:<16} {self.ipAddy:<20} "
                f"{self.getSpace():<25} {self.os}")


class Linux(ComputerSystem):
    """
    Represents a Linux computer with a filesystem (FS) space property
    """

    def __init__(self, ipAddy, yearPurchased, os, fs_space):
        super().__init__(ipAddy, yearPurchased, os)
        self.fs_space = fs_space

    def getSpace(self):
        """Returns the filesystem space string"""
        return f"Filesystem: {self.fs_space}"


class Windows(ComputerSystem):
    """
    Represents a Windows computer with a C drive space property
    """

    def __init__(self, ipAddy, yearPurchased, os, c_drive_space):
        super().__init__(ipAddy, yearPurchased, os)
        self.c_drive_space = c_drive_space

    def getSpace(self):
        """Returns the C drive space string"""
        return f"C drive: {self.c_drive_space}"