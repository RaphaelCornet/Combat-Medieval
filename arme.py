from enum import Enum


class Arme(Enum):
    MASSE = "Masse", 10, 0.6, 1
    MARTEAU = "Marteau", 6, 0.45, 0
    EPEE = "Épée", 7, 0.35, 0
    LANCE = "Lance", 8, 0.4, 0
    HACHE = "Hache", 9, 0.5, 0
    COUTEAU = "Couteau", 5, 0.4
    DAGUE = "Dague", 4, 0.3
    SABRE = "Sabre", 3, 0.2
    BOUCLIER = "Bouclier", 0, 0, 3

    def __init__(self, nom: str, point_degats: int, proba_rate: float,
                 point_defense: int = 0):
        self.__nom = nom
        self.__point_degats = point_degats
        self.__proba_rate = proba_rate
        self.__point_defense = point_defense

    def __str__(self):
        return (f"     {self.__nom} : \n"
                f"      - Points de Dégâts : {self.__point_degats} \n"
                f"      - Probabilité de raté : {int(self.__proba_rate * 100)}%\n"
                f"      - Points de Défense : {self.__point_defense} \n")

    def get_nom(self) -> str:
        return self.__nom

    def get_point_degats(self) -> int:
        return self.__point_degats

    def get_proba_rate(self) -> float:
        return self.__proba_rate

    def get_point_defense(self) -> int:
        return self.__point_defense
