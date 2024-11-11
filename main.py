import tkinter as tkinter

from arme import Arme
from gui import GUI
from personnage import Personnage
from race import Race

if __name__ == '__main__':
    personnage1: Personnage = Personnage(
        "Theodore",
        [Arme.DAGUE, Arme.SABRE],
        Race.ELFE,
        10,
        2,
        2,
        150,
    )

    personnage2: Personnage = Personnage(
        "Jean-Eudes",
        [Arme.BOUCLIER],
        Race.TROLL,
        3,
        3,
        0,
        145,
    )

    personnage3: Personnage = Personnage(
        "Aldric",
        [Arme.HACHE, Arme.LANCE],
        Race.HOMME,
        9,
        3,
        3,
        148,
    )

    personnage4: Personnage = Personnage(
        "Lyra",
        [Arme.EPEE],
        Race.ELFE,
        11,
        1,
        3,
        152,
    )

    personnage5: Personnage = Personnage(
        "Grim",
        [Arme.MARTEAU, Arme.BOUCLIER],
        Race.NAIN,
        4,
        4,
        1,
        140,
    )

    personnage6: Personnage = Personnage(
        "Gregor",
        [Arme.MASSE],
        Race.TROLL,
        3,
        4,
        0,
        143,
    )

    fenetre = tkinter.Tk()
    app = GUI(fenetre, personnage1, personnage2)
    fenetre.mainloop()
