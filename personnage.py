from arme import Arme
from race import Race


class Personnage:
    def __init__(self, nom: str, armes: list[Arme], race: Race, point_action: int,
                 point_attaque: int, point_defense: int, point_de_vie: int):
        self.__arme_actuel: Arme = armes[0]
        self.__armes: list[Arme] = armes
        self.__arme_actuel: Arme
        self.__nom: str = nom
        self.__point_action: int = point_action
        self.__point_attaque: int = point_attaque
        self.__point_defense: int = point_defense
        self.__point_de_vie: int = point_de_vie
        self.__race: Race = race

    def __str__(self):
        if self.__arme_actuel is None:
            description_arme_actuel: str = "X"
        else:
            description_arme_actuel: str = f"\n" + str(self.__arme_actuel)

        description_inventaire: str = ""
        for arme in self.__armes:
            description_inventaire += arme.get_nom() + ", "
        if description_inventaire == "":
            description_inventaire = "X  "

        return ("--------------------------------------------\n"
                f"{self.__nom} ({self.__race})\n"
                f"Statistiques : \n"
                f" - Points Action : {self.__point_action}\n"
                f" - Points Attaque : {self.__point_attaque}\n"
                f" - Points Défense : {self.__point_defense}\n"
                f" - Points de Vie : {self.__point_de_vie}\n"
                f"Inventaire : \n" +
                f" - Arme Actuelle : {description_arme_actuel}\n"
                f" - Armes : "
                f"{description_inventaire[:-2]}\n"
                "--------------------------------------------\n")

    def get_armes(self) -> list[Arme]:
        return self.__armes

    def get_arme_actuel(self) -> Arme:
        return self.__arme_actuel

    def get_nom(self) -> str:
        return self.__nom

    def get_point_action(self) -> int:
        return self.__point_action

    def get_point_attaque(self) -> int:
        return self.__point_attaque

    def get_point_defense(self) -> int:
        return self.__point_defense

    def get_point_de_vie(self) -> int:
        return self.__point_de_vie

    def get_race(self) -> Race:
        return self.__race

    def add_arme(self, arme: Arme):
        self.__armes.append(arme)

    def set_arme_actuel(self, arme_actuel: Arme):
        self.__arme_actuel = arme_actuel

    def set_point_action(self, point_action: int):
        self.__point_action = point_action

    def set_point_attaque(self, point_attaque: int):
        self.__point_attaque = point_attaque

    def set_point_defense(self, point_defense: int):
        self.__point_defense = point_defense

    def set_race(self, race: Race):
        self.__race = race

    def decrement_point_de_vie(self, point_de_vie: int):
        self.__point_de_vie -= point_de_vie
        if self.__point_de_vie < 0:
            self.__point_de_vie = 0

    MASSE = "Masse", 10, 0.6, 0
