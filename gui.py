import tkinter as tk
from tkinter import ttk

from fight import Fight


class GUI:
    def __init__(self, root, combattant1, combattant2):
        self.__root = root
        self.__combat: Fight = Fight(combattant1, combattant2, self)
        self.__root.title("Combat")

        # Frame pour le combattant 1
        self.__combattant1_frame = ttk.Frame(root)
        self.__combattant1_frame.grid(row=0, column=0, padx=10, pady=10)
        self.__combattant1_label = ttk.Label(self.__combattant1_frame,
                                             text=str(self.__combat.get_fighter1()))
        self.__combattant1_label.grid(row=0, column=0)

        # Frame pour le combattant 2
        self.__combattant2_frame = ttk.Frame(root)
        self.__combattant2_frame.grid(row=0, column=1, padx=10, pady=10)
        self.__combattant2_label = ttk.Label(self.__combattant2_frame,
                                             text=str(self.__combat.get_fighter2()))
        self.__combattant2_label.grid(row=0, column=0)

        # Zone d'affichage des actions
        self.__log_text = tk.Text(root, width=80, height=15, state='disabled')
        self.__log_text.grid(row=1, column=0, columnspan=2, pady=10)
        self.__log_text.tag_configure("center", justify='center')

        # Bouton pour démarrer le tour
        self.__tour_button = ttk.Button(root, text="Prochain Tour", command=self.__next_turn)
        self.__tour_button.grid(row=2, column=0, padx=10, pady=10)

        # Bouton pour aller à la fin du combat
        self.__skip_button = ttk.Button(root, text="Skipper le combat", command=self.__skip)
        self.__skip_button.grid(row=2, column=1, padx=10, pady=10)

    def log(self, text):
        self.__log_text.config(state='normal')
        self.__log_text.insert(tk.END, text + "\n")
        self.__log_text.config(state='disabled')
        self.__log_text.see(tk.END)

    def __next_turn(self):
        self.__combat.next_turn()
        self.__update_display()
        if self.__combat.is_finished():
            self.__tour_button.grid_forget()

    def __skip(self):
        self.__tour_button.grid_forget()
        self.__skip_button.grid_forget()
        while not self.__combat.is_finished():
            self.__combat.next_turn()
            self.__update_display()

    def __update_display(self):
        self.__combattant1_label.config(text=str(self.__combat.get_fighter1()))
        self.__combattant2_label.config(text=str(self.__combat.get_fighter2()))
