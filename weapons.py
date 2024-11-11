from enum import Enum


class Weapons(Enum):
    MACE = "Masse", 10, 0.6, 1
    HAMMER = "Marteau", 6, 0.45, 0
    SWORD = "Épée", 7, 0.35, 0
    SPEAR = "Lance", 8, 0.4, 0
    AXE = "Hache", 9, 0.5, 0
    KNIFE = "Couteau", 5, 0.4
    DAGGER = "Dague", 4, 0.3
    SABER = "Sabre", 3, 0.2
    SHIELD = "Bouclier", 0, 0, 3

    def __init__(self, nom: str, damage_point: int, failure_probability: float,
                 defense_points: int = 0):
        self.__name = nom
        self.__damage_points = damage_point
        self.__failure_probability = failure_probability
        self.__defense_points = defense_points

    def __str__(self):
        return (f"     {self.__name} : \n"
                f"      - Points de Dégâts : {self.__damage_points} \n"
                f"      - Probabilité de raté : {int(self.__failure_probability * 100)}%\n"
                f"      - Points de Défense : {self.__defense_points} \n")

    def get_name(self) -> str:
        return self.__name

    def get_damage_points(self) -> int:
        return self.__damage_points

    def get_failure_probability(self) -> float:
        return self.__failure_probability

    def get_defense_points(self) -> int:
        return self.__defense_points
