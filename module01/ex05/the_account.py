class Account():
    
    __ID_COUNT = 1
    __id: int
    __name: str
    __value: float
    zip = 1
    addr: str
    
    def __init__(self, name, **kwargs):
        """
            Initialization
        """
        
        self.__dict__.update(kwargs)
        self.__id = self.__ID_COUNT
        Account.__ID_COUNT += 1
        self.__name = name
  
        if not hasattr(self, "value"):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.__name, str):
            raise AttributeError("Attribute name must be a str object.")
        self.addr = str(self.__id) + self.__name
        self.zip = str(self.__id) + self.__name



    def get_id(self):
        return self.__id

    def get_accounts(self):
        return self.__ID_COUNT

    def get_value(self):
        return self.__value

    def get_name(self):
        return self.__name

    def transfer(self, amount):
        self.value += amount