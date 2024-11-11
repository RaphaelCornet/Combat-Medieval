from random import random

from personnage import Personnage


class Combat:
    def __init__(self, combattant1: Personnage, combattant2: Personnage, gui):
        # Le combattant 1 sera toujours celui avec le plus de points actions
        if combattant1.get_point_action() > combattant2.get_point_action():
            self.__combattant1: Personnage = combattant1
            self.__combattant2: Personnage = combattant2
        else:
            self.__combattant1: Personnage = combattant2
            self.__combattant2: Personnage = combattant1
        self.__fini: bool = False
        self.__compteur_tour: int = 0
        self.__gui = gui

    def get_combattant1(self) -> Personnage:
        return self.__combattant1

    def get_combattant2(self) -> Personnage:
        return self.__combattant2

    def get_gagnant(self) -> Personnage:
        return self.__gagnant

    def get_perdant(self) -> Personnage:
        return self.__perdant

    def est_fini(self):
        return self.__fini

    def __str__(self):
        combattant1: str = self.__combattant1.get_nom()
        combattant2: str = self.__combattant2.get_nom()
        return f"Combat opposant {combattant1} à {combattant2} :"

    @staticmethod
    def __calcul_degats(combattant1: Personnage, combattant2: Personnage) -> int:
        """
        Fonction statique qui renvoie les dégats que va infliger le combattant 1 sur le combattant 2.
        """
        return (combattant1.get_arme_actuel().get_point_degats() +
                combattant1.get_point_attaque() -
                combattant2.get_point_defense() -
                combattant2.get_arme_actuel().get_point_defense())

    def __attaque(self, combattant1: Personnage, combattant2: Personnage):
        """
        Gère la logique de l'attaque du combattant 1 sur le combattant 2.
        """
        if combattant1.get_arme_actuel().get_proba_rate() >= random():
            self.__gui.log(f"{combattant1.get_nom()} a loupé {combattant2.get_nom()}.")
            return

        degats: int = self.__calcul_degats(combattant1, combattant2)
        if degats <= 0:
            self.__gui.log(f"{combattant1.get_nom()} a touché {combattant2.get_nom()} "
                           f"mais n'est pas parvenu à lui faire des dégâts.")
            return

        combattant2.decrement_point_de_vie(degats)
        self.__gui.log(f"{combattant1.get_nom()} a infligé {degats} points de dégâts "
                       f"à {combattant2.get_nom()} ({combattant2.get_point_de_vie()} pv).")

    def __fin_de_combat(self, perdant: Personnage, gagnant: Personnage):
        """
        Gère la logique de la fin de partie quand, perdant perd et gagnant gagne.
        """
        self.__fini = True
        self.__gagnant = gagnant
        self.__perdant = perdant
        self.__gui.log(f"\n------ Fin de Combat ------" +
                       f"{"-" * (len(str(self.__compteur_tour)) + 1)}\n"
                       f"{perdant.get_nom()} est mort. \n"
                       f"{gagnant.get_nom()} l'emporte avec encore "
                       f"{gagnant.get_point_de_vie()} points de vie restants !\n"
                       f"------ Fini en {self.__compteur_tour} tours ------\n")

    def tour(self):
        """
        Gère la logique d'un tour (combattant1 attaque combattant 2 puis l'inverse),
        entrecoupé de vérification de si la partie est finie ou non.
        """
        self.__compteur_tour += 1
        self.__gui.log(f"\n------ Tour n°{self.__compteur_tour} ------")
        self.__attaque(self.__combattant1, self.__combattant2)
        if self.__combattant2.get_point_de_vie() == 0:
            self.__fin_de_combat(self.__combattant2, self.__combattant1)
            return
        self.__attaque(self.__combattant2, self.__combattant1)
        if self.__combattant1.get_point_de_vie() == 0:
            self.__fin_de_combat(self.__combattant1, self.__combattant2)
            return
