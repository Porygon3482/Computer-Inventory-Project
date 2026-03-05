class ComputerSystem:
    """
    Base Class for all computer systems
    """

    def __init__(self, ipAddy, yearPurchased, os):
        self.ipAddy = ipAddy
        self.yearPurchased = yearPurchased
        self.os = os

    def getSpace(self):
        """
        Abstract method - must be overriden by subclasses
        """
        raise NotImplementedError("Subclass must override this method")

    @property
    def yearPurchased(self):
        return self.yearPurchased

    @yearPurchased.setter
    def yearPurchased(self,value):
        if(value < 1970):
            raise ValueError("Invalid year of purchase")
        yearPurchased = value

    def __str__(self):
        return (f"{self.year_purchased:<16} {self.ip_address:<20} "
                f"{self.getSpace():<25} {self.operating_system}")

class Linux(ComputerSystem):
    """
    represents a Linux computer with a filesystem(FS) space property
    """


    def __init__(self, ipAddy, yearPurchased, os):
        super().__init__(ipAddy, yearPurchased, os)
        self.fs = fs_space
        """
        :return: returns the file system space string 
        """
    def getSpace(self):
        return f"Filesystem: {self.fs_space}"

class Windows(ComputerSystem):
    def __init__(self, ipAddy, yearPurchased, os):
        super().__init__(ipAddy, yearPurchased, os)
        self.c_drive_space = c_drive_space

    def getSpace(self):
        """
        :return: returns the C drive space string
        """
        return f"C drive: {self.c_drive_space}"


