class actionbar:
    def __init__(self):
        self.__keybinds = {}
        self.__x_coordiante = 0
        self.__y_coordiante = 0
        self.__width = 0
        self.__height = 0
        self.__orintation = ""
        
    def get_x_coordinate(self):
        return self.__x_coordiante
    
    def set_x_coordinate(self,x):
        self.__x_coordinate = x
        
    def get_y_coordinate(self):
        return self.__y_coordiante
    
    def set_y_coordinate(self,y):
        self.__y_coordinate = y
        
    def getWidth(self):
        return self.__width
    
    def set_width(self,x):
        self.__width = x

    def getHeight(self):
        return self.__height
    
    def setHeight(self,x):
        self.__height = x

    def getOrientation(self):
        return self.__orintation
    
    def setOrientation(self,x):
        self.__orientation = x

    def addKeybind(self,key,ability):
        if len(self.__keybinds) <= 14:
            self.__keybinds[key] = ability
    
    def RemoveKeybind(self,x):
        try:
            del self.__keybinds[x]
        except KeyError:
            pass
    def getAbility(self,key):
        try:
            return self.__keybinds[key]
        except KeyError:
            pass

    def getKeys(self):
        return self.__keybinds
    
        
    

    
