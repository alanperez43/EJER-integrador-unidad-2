class Proyecto ():
    __IdProyecto = None
    __Titulo = None
    __Palabra_Clave = None
    def __init__ (self,IdP,titulo,palabra):
        self.__IdProyecto = IdP
        self.__Titulo = titulo
        self.__Palabra_Clave = palabra
    
    def getIdProyecto (self):
        return self.__IdProyecto