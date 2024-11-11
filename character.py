from weapons import Weapons
from peoples import Peoples


class Character:
    def __init__(self, name: str, weapons: list[Weapons], people: Peoples, action_points: int,
                 damage_points: int, defense_points: int, health_points: int):
        self.__current_weapon: Weapons = weapons[0]
        self.__weapons: list[Weapons] = weapons
        self.__name: str = name
        self.__action_points: int = action_points
        self.__damage_points: int = damage_points
        self.__defense_points: int = defense_points
        self.__health_points: int = health_points
        self.__people: Peoples = people

    def __str__(self):
        if self.__current_weapon is None:
            current_weapon_description: str = "X"
        else:
            current_weapon_description: str = f"\n" + str(self.__current_weapon)

        inventory_description: str = ""
        for arme in self.__weapons:
            inventory_description += arme.get_name() + ", "
        if inventory_description == "":
            inventory_description = "X  "

        return ("--------------------------------------------\n"
                f"{self.__name} ({self.__people})\n"
                f"Statistiques : \n"
                f" - Points Action : {self.__action_points}\n"
                f" - Points Attaque : {self.__damage_points}\n"
                f" - Points Défense : {self.__defense_points}\n"
                f" - Points de Vie : {self.__health_points}\n"
                f"Inventaire : \n" +
                f" - Arme Actuelle : {current_weapon_description}\n"
                f" - Armes : "
                f"{inventory_description[:-2]}\n"
                "--------------------------------------------\n")

    def get_weapons(self) -> list[Weapons]:
        return self.__weapons

    def get_current_weapon(self) -> Weapons:
        return self.__current_weapon

    def get_name(self) -> str:
        return self.__name

    def get_action_points(self) -> int:
        return self.__action_points

    def get_damage_points(self) -> int:
        return self.__damage_points

    def get_defense_points(self) -> int:
        return self.__defense_points

    def get_health_points(self) -> int:
        return self.__health_points

    def get_people(self) -> Peoples:
        return self.__people

    def add_weapon(self, weapon: Weapons):
        self.__weapons.append(weapon)

    def set_current_weapon(self, current_weapon: Weapons):
        self.__current_weapon = current_weapon

    def set_action_points(self, action_points: int):
        self.__action_points = action_points

    def set_damage_points(self, damage_points: int):
        self.__damage_points = damage_points

    def set_defense_points(self, defense_points: int):
        self.__defense_points = defense_points

    def set_people(self, people: Peoples):
        self.__people = people

    def decrement_health_points(self, health_points: int):
        self.__health_points -= health_points
        if self.__health_points < 0:
            self.__health_points = 0
