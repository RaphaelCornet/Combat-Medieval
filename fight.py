from random import random

from character import Character


class Fight:
    def __init__(self, fighter1: Character, fighter2: Character, gui):
        if fighter1.get_action_points() > fighter2.get_action_points():
            self.__fighter1: Character = fighter1
            self.__fighter2: Character = fighter2
        else:
            self.__fighter1: Character = fighter2
            self.__fighter2: Character = fighter1
        self.__finished: bool = False
        self.__turn_count: int = 0
        self.__gui = gui

    def get_fighter1(self) -> Character:
        return self.__fighter1

    def get_fighter2(self) -> Character:
        return self.__fighter2

    def get_winner(self) -> Character:
        return self.__winner

    def get_looser(self) -> Character:
        return self.__looser

    def is_finished(self):
        return self.__finished

    def __str__(self):
        fighter1: str = self.__fighter1.get_name()
        fighter2: str = self.__fighter2.get_name()
        return f"Combat opposant {fighter1} à {fighter2} :"

    @staticmethod
    def __damage_calculation(fighter1: Character, fighter2: Character) -> int:
        return (fighter1.get_current_weapon().get_damage_points() +
                fighter1.get_damage_points() -
                fighter2.get_defense_points() -
                fighter2.get_current_weapon().get_defense_points())

    def __attack(self, fighter1: Character, fighter2: Character):
        if fighter1.get_current_weapon().get_failure_probability() >= random():
            self.__gui.log(f"{fighter1.get_name()} a loupé {fighter2.get_name()}.")
            return

        damage: int = self.__damage_calculation(fighter1, fighter2)
        if damage <= 0:
            self.__gui.log(f"{fighter1.get_name()} a touché {fighter2.get_name()} "
                           f"mais n'est pas parvenu à lui faire des dégâts.")
            return

        fighter2.decrement_health_points(damage)
        self.__gui.log(f"{fighter1.get_name()} a infligé {damage} points de dégâts "
                       f"à {fighter2.get_name()} ({fighter2.get_health_points()} pv).")

    def __fight_end(self, looser: Character, winner: Character):
        self.__finished = True
        self.__winner = winner
        self.__looser = looser
        self.__gui.log(f"\n------ Fin de Combat ------" +
                       f"{"-" * (len(str(self.__turn_count)) + 1)}\n"
                       f"{looser.get_name()} est mort. \n"
                       f"{winner.get_name()} l'emporte avec encore "
                       f"{winner.get_health_points()} points de vie restants !\n"
                       f"------ Fini en {self.__turn_count} tours ------\n")

    def next_turn(self):
        self.__turn_count += 1
        self.__gui.log(f"\n------ Tour n°{self.__turn_count} ------")
        self.__attack(self.__fighter1, self.__fighter2)
        if self.__fighter2.get_health_points() == 0:
            self.__fight_end(self.__fighter2, self.__fighter1)
            return
        self.__attack(self.__fighter2, self.__fighter1)
        if self.__fighter1.get_health_points() == 0:
            self.__fight_end(self.__fighter1, self.__fighter2)
            return
