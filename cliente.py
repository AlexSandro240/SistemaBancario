class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property   #propriedade que fará o metodo ser acessado sem necessidade do ()
    def nome(self):
        print("Chamando Getter @propety nome()")
        return self.__nome.capitalize()

    @nome.setter
    def nome(self, nome):
        print("Chamando Setter @propety nome()")
        self.__nome = nome
