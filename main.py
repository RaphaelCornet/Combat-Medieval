import tkinter as tkinter

from weapons import Weapons
from gui import GUI
from character import Character
from peoples import Peoples

if __name__ == '__main__':
    personnage1: Character = Character(
        "Theodore",
        [Weapons.DAGGER, Weapons.SABER],
        Peoples.ELFE,
        10,
        2,
        2,
        150,
    )

    personnage2: Character = Character(
        "Jean-Eudes",
        [Weapons.SHIELD],
        Peoples.TROLL,
        3,
        3,
        0,
        145,
    )

    personnage3: Character = Character(
        "Aldric",
        [Weapons.AXE, Weapons.SPEAR],
        Peoples.HOMME,
        9,
        3,
        3,
        148,
    )

    personnage4: Character = Character(
        "Lyra",
        [Weapons.SWORD],
        Peoples.ELFE,
        11,
        1,
        3,
        152,
    )

    personnage5: Character = Character(
        "Grim",
        [Weapons.HAMMER, Weapons.SHIELD],
        Peoples.NAIN,
        4,
        4,
        1,
        140,
    )

    personnage6: Character = Character(
        "Gregor",
        [Weapons.MACE],
        Peoples.TROLL,
        3,
        4,
        0,
        143,
    )

    fenetre = tkinter.Tk()
    app = GUI(fenetre, personnage1, personnage2)
    fenetre.mainloop()
