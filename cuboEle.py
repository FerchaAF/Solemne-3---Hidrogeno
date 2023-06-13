class ElevadoCua():
    def __init__(self, da1, da2): ##, Resu1, Resu2):
        self.__dato1 = da1
        self.__dato2 = da2

        ## self.__Resultado1 = Resu1
        ## self.__Resultado2 = Resu2


    ## SETTERS

    def setDato1(self, da1):
        self.__dato1 = da1

    def setDato2(self, da2):
        self.__dato2 = da2
    
    ## def setResultado1(self, Resu1):
        ## self.__resultado1 = Resu1
    
    ## def setResultado2(self, Resu2):
        ## self.__resultado2 = Resu2

    ## GETTERS

    def getDato1(self):
        return self.__dato1
    def getDato2(self):
        return self.__dato2
    ## def setResultado1(self):
        ## return self.__Resultado1
    ## def setResultado2(self):
        ## return self.__Resultado2

    ### METODOS ###

    def ElevarAlCubo(self, da1, da2):
        Res1 = da1 * da1 * da1
        Res2 = da2 * da2 * da2
        self.setDato1(Res1)
        self.setDato2(Res2)
        print(self.getDato1())
        print(self.getDato2())

        ## pass