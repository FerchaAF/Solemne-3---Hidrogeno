class HidroCalculo():
    def __init__(self, da3, da4):
        self.__datoHydro1 = da3
        self.__datoHydro2 = da4

    ## SETTER

    def setHydro1(self, da3):
        self.__datoHydro1 = da3

    def setHydro2(self, da4):
        self.__datoHydro2 = da4

    ## GETTER

    def getHydroDato1(self):
        return self.__datoHydro1
    def getHydroDato2(self):
        return self.__datoHydro2
    
    ### METODO DE CALCULO ##

    def EficienciaElectrolisis(self, da3, da4):
        Ef = (da3/da4)*100
        self.setHydro1(Ef)
        print(self.getHydroDato1())