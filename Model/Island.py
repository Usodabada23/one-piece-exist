class Island:

    def __init__(self, name:str, location:str, government:str, affiliated_group=None):
        """
        Initialise une île avec les informations de base.

        :param name: Nom de l'île (str)
        :param location: Localisation (ex: Grand Line, East Blue, etc.) (str)
        :param government: Type de gouvernement (ex: monarchie, dictature, etc.) (str)
        :param affiliated_group: Groupe ou faction auquel l'île est associée (ex: Marine, Pirates, etc.) (str, optionnel)
        """
        self.__name = name
        self.__location = location
        self.__government = government
        self.__affiliated_group = affiliated_group