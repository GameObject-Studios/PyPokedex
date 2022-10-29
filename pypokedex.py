# import pokebase as pb
from tkinter import *
from tkinter import ttk

import pandas as pd

# CONSTANTS
DARK_RED = "#de0100"

NAVY_BLUE = "#0000b6"

pkmn = "Pokémon"

INFO_BG = 'LightGray'

CATEGORY_FONT = ('Arial', 12, 'bold')

VALUE_FONT = ('Arial', 10)

type_colors = {"grass": 'green',
               "water": '#0094ff',
               "fire": 'red',
               "normal": 'white',
               "rock": '#b1804d',
               "ground": '#c88100',
               "bug": '#958941',
               "dark": 'black',
               "dragon": '#8e9fd4',
               "electric": 'yellow',
               "fairy": 'magenta',
               "fighting": '#ee9d64',
               "flying": '#08deff',
               "ghost": '#8b5985',
               "ice": '#80ffff',
               "poison": '#ac49ff',
               "psychic": '#dc80ff',
               "steel": '#beb6b6',
               "nan": 'black'}


class Dex(Tk):
    def __init__(self):
        super().__init__()
        # Default settings
        self.title('PyDex')
        self.__to_center()
        self.resizable(False, False)
        self.__data = pd.read_csv("Data\\pokedex_(Update_05.20).csv")
        self.__all_pokemon = self.__data.to_dict(orient='records')
        self.config(bg=DARK_RED, padx=130, pady=25)

        label_width = 17

        # ----------------------GUI Components-------------------- #
        #
        self.__title_frame = Frame(self, bg=DARK_RED)
        self.__title_frame.grid(row=0, column=0)
        self.__title_text = Label(self.__title_frame,
                                  text="PyDex:\nThe Python-Powered Pokédex",
                                  font=("Pokemon Solid", 22),  # TODO: use from local font instead of system-installed?
                                  fg='yellow',
                                  bg=DARK_RED)
        self.__title_text.grid(row=0, column=0)
        self.__title_text2 = Label(self.__title_frame,
                                   text="Select a Pokémon below to view their data.",
                                   font=("Pokemon Solid", 12),
                                   bg=DARK_RED,
                                   fg='yellow')
        self.__title_text2.grid(row=1, column=0)
        self.__selected = StringVar(self)
        self.__pokemon_names = [i['name'] for i in self.__all_pokemon]
        self.__selected.set(self.__pokemon_names[0])
        self.__pokemon_list = ttk.Combobox(self, textvariable=self.__selected, values=self.__pokemon_names, width=35)
        self.__pokemon_list.bind('<<ComboboxSelected>>', self.__selection_changed)
        self.__pokemon_list.grid(row=1, column=0)

        # Dex data
        self.__info_frame = Frame(self, border=6, bg=INFO_BG, width=54, bd=6)
        self.__info_frame.grid(row=3, column=0, columnspan=6)
        self.__species_label = Label(self.__info_frame, text='Species: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__species_label.grid(row=0, column=0, sticky=W)
        self.__species = Label(self.__info_frame, bg=INFO_BG, font=VALUE_FONT, width=label_width)
        self.__species.grid(row=0, column=1, sticky=W)
        self.__type1_label = Label(self.__info_frame, text='Type 1: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__type1_label.grid(row=1, column=0, sticky=W)
        self.__type1 = Label(self.__info_frame, bg=INFO_BG, font=('Arial', 10, 'bold'), width=label_width)
        self.__type1.grid(row=1, column=1, sticky=W)
        self.__type2_label = Label(self.__info_frame, text='Type 2: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__type2_label.grid(row=1, column=2, sticky=W)
        self.__type2 = Label(self.__info_frame, bg=INFO_BG, font=('Arial', 10, 'bold'), width=label_width)
        self.__type2.grid(row=1, column=3, sticky=W)
        self.__height_label = Label(self.__info_frame, text="Height: ", bg=INFO_BG, font=CATEGORY_FONT)
        self.__height_label.grid(row=2, column=0, sticky=W)
        self.__height = Label(self.__info_frame, bg=INFO_BG, font=VALUE_FONT, width=label_width)
        self.__height.grid(row=2, column=1, sticky=W)
        self.__weight_label = Label(self.__info_frame, text='Weight: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__weight_label.grid(row=2, column=2, sticky=W)
        self.__weight = Label(self.__info_frame, bg=INFO_BG, font=VALUE_FONT, width=label_width)
        self.__weight.grid(row=2, column=3, sticky=W)
        self.__ability1_label = Label(self.__info_frame, text='Ability 1: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__ability1_label.grid(row=3, column=0, sticky=W)
        self.__ability1 = Label(self.__info_frame, bg=INFO_BG, font=VALUE_FONT, width=label_width)
        self.__ability1.grid(row=3, column=1, sticky=W)
        self.__ability2_label = Label(self.__info_frame, text='Ability 2: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__ability2_label.grid(row=3, column=2, sticky=W)
        self.__ability2 = Label(self.__info_frame, bg=INFO_BG, font=VALUE_FONT, width=label_width)
        self.__ability2.grid(row=3, column=3, sticky=W)
        self.__ability_hidden_label = Label(self.__info_frame, text='Hidden Ability: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__ability_hidden_label.grid(row=3, column=4, sticky=W)
        self.__ability_hidden = Label(self.__info_frame, bg=INFO_BG, font=VALUE_FONT, width=label_width)
        self.__ability_hidden.grid(row=3, column=5, sticky=W)

        # Base Stats
        self.__base_stat_frame = Frame(self, border=4, bg=INFO_BG, bd=3)
        self.__base_stat_frame.grid(row=4, column=0)
        self.__stats_title = Label(self.__base_stat_frame, text='Base Stats', bg=INFO_BG, font=('Arial', 16, 'bold'),
                                   width=54)
        self.__stats_title.grid(row=0, column=0, columnspan=2)
        self.__hp_label = Label(self.__base_stat_frame, text='HP: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__hp_label.grid(row=1, column=0, sticky=E)
        self.__hp = Label(self.__base_stat_frame, bg=INFO_BG, font=VALUE_FONT, width=5)
        self.__hp.grid(row=1, column=1, sticky=W)
        self.__attack_label = Label(self.__base_stat_frame, text='ATTACK: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__attack_label.grid(row=2, column=0, sticky=E)
        self.__attack = Label(self.__base_stat_frame, bg=INFO_BG, font=VALUE_FONT, width=5)
        self.__attack.grid(row=2, column=1, sticky=W)
        self.__defense_label = Label(self.__base_stat_frame, text='DEFENSE: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__defense_label.grid(row=3, column=0, sticky=E)
        self.__defense = Label(self.__base_stat_frame, bg=INFO_BG, font=VALUE_FONT, width=5)
        self.__defense.grid(row=3, column=1, sticky=W)
        self.__special_atk_label = Label(self.__base_stat_frame, text='SPECIAL ATTACK: ', bg=INFO_BG,
                                         font=CATEGORY_FONT)
        self.__special_atk_label.grid(row=4, column=0, sticky=E)
        self.__special_atk = Label(self.__base_stat_frame, bg=INFO_BG, font=VALUE_FONT, width=5)
        self.__special_atk.grid(row=4, column=1, sticky=W)
        self.__special_def_label = Label(self.__base_stat_frame, text='SPECIAL DEFENSE: ', bg=INFO_BG,
                                         font=CATEGORY_FONT)
        self.__special_def_label.grid(row=5, column=0, sticky=E)
        self.__special_def = Label(self.__base_stat_frame, bg=INFO_BG, font=VALUE_FONT, width=5)
        self.__special_def.grid(row=5, column=1, sticky=W)
        self.__speed_label = Label(self.__base_stat_frame, text='SPEED: ', bg=INFO_BG, font=CATEGORY_FONT)
        self.__speed_label.grid(row=6, column=0, sticky=E)
        self.__speed = Label(self.__base_stat_frame, bg=INFO_BG, font=VALUE_FONT, width=5)
        self.__speed.grid(row=6, column=1, sticky=W)

        # Sprite display
        self.__sprite_canvas = Canvas(self, width=96, height=96, bg=DARK_RED, highlightthickness=0)
        self.__sprite_canvas.grid(row=2, column=0)
        self.__sprites = {str: PhotoImage}
        # Create sprite image objects and store for runtime use
        for i in self.__pokemon_names:
            new_path = f'Sprites/{i}.png'
            self.__sprites[i] = PhotoImage(file=new_path)
            # print(new_path)
        self.__shown_sprite = self.__sprite_canvas.create_image(48, 48, image=self.__sprites["Bulbasaur"])
        self.__selection_changed()

        # The following code only to be used to create the sprites from the pokebase API data, do not include in builds
        # for i in self.__pokemon_names:
        #     pokemn = pb.SpriteResource('pokemon', self.__all_pokemon[self.__pokemon_names.index(i)]['pokedex_number'])
        #     try:
        #         p = f"Sprites/{i}.png"
        #         if not os.path.exists(p):
        #             print(p)
        #             with open(p, 'wb') as pokemon:
        #                 pokemon.write(pokemn.img_data)
        #     except IndexError:
        #         continue

    # noinspection PyUnusedLocal
    def __selection_changed(self, event=None):
        self.view_info = None
        pkmn_name = self.__selected.get()
        dex_no = 0
        for i in self.__all_pokemon:
            n = i['name']
            if n == pkmn_name:
                try:
                    dex_no = i['pokedex_number']
                except KeyError or dex_no == 0:
                    return
                else:
                    # Update displayed information and image
                    self.__update_info(i)
                    # print(dex_no, n)
                    break

    def __update_info(self, pokemon):
        t1_color = type_colors[pokemon['type_1'].lower()]
        t2_color = type_colors[str(pokemon['type_2']).lower()]
        # set info label texts
        self.__species.config(text=f"{pokemon['species']}")
        self.__type1.config(text=f'{pokemon["type_1"]}', bg=t1_color)
        t1 = str(pokemon['type_1']).lower()
        if t1 == 'dark' or t1 == 'grass' or t1 == 'poison' or t1 == 'ghost':
            self.__type1.config(fg='white')
        else:
            self.__type1.config(fg='black')
        self.__type2.config(text=f'{str(pokemon["type_2"]).replace("nan", "None")}', bg=t2_color)
        self.__ability1.config(text=f'{str(pokemon["ability_1"]).replace("nan", "None")}')
        self.__ability2.config(text=f'{str(pokemon["ability_2"]).replace("nan", "None")}')
        self.__ability_hidden.config(text=f'{str(pokemon["ability_hidden"]).replace("nan", "None")}')
        self.__height.config(text=f'{pokemon["height_m"]}m'.replace("nanm", "None"))
        self.__weight.config(text=f'{pokemon["weight_kg"]}kg'.replace('nankg', "None"))
        self.__hp.config(text=f'{pokemon["hp"]}')
        self.__attack.config(text=f'{pokemon["attack"]}')
        self.__defense.config(text=f'{pokemon["defense"]}')
        self.__special_atk.config(text=f"{pokemon['sp_attack']}")
        self.__special_def.config(text=f"{pokemon['sp_defense']}")
        self.__speed.config(text=f"{pokemon['speed']}")
        t2 = str(pokemon['type_2']).lower()
        if t2 == 'dark' or t2 == 'grass' or t2 == 'poison' or t2 == 'ghost':
            self.__type2.config(fg='white')
        elif self.__type2.cget('text') == "None":
            self.__type2.config(fg='black', bg=INFO_BG)
        else:
            self.__type2.config(fg='black')
        self.__update_sprite(pokemon['name'])

    def __update_sprite(self, name: str):
        self.__sprite_canvas.itemconfig(self.__shown_sprite, image=self.__sprites[name])

    def __to_center(self):
        width = 970
        height = 700
        self.__center_window(self, width, height)

    @staticmethod
    def __center_window(window, x, y):
        width = x
        height = y
        screen_width = window.winfo_screenwidth()  # Width of the screen
        screen_height = window.winfo_screenheight()  # Height of the screen
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))
