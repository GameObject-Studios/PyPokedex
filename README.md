# Source code for PyPokédex by Kyle Pummell

I created this project as practice of my learning of Python programming.<br>
    Topics covered include:<br>
        - Creating a GUI application using the Tkinter library<br>
        - Reading from a file<br>
        - Accessing and manipulating .CSV data<br>
        - Displaying images using Tkinter<br>
        - Using custom fonts in a Tkinter application<br>
        - Updating data shown in various labels on Tkinter GUI<br>
        - Building an executable using pyinstaller<br>
        - Web scraping, APIs and creating images from raw text data<br>
<br>
Fonts:<br>
To use the fonts provided in the 'Fonts' folder, they must be properly installed.<br>
In most modern Windows Operating Systems, you should be able to right-click the font file and<br>
    select 'Install' from the menu. For other operating systems, I found the following resources:<br>
    - For Linux: https://www.unixtutorial.org/how-to-install-ttf-fonts-in-linux/<br>
    - For Mac OS: https://support.apple.com/guide/font-book/install-and-validate-fonts-fntbk1000/mac<br>
<br>
Sprites:<br>
    Most of the sprites used were created from data provided by the pokebase API at https://pokeapi.co/<br>
    The alternate forms and megas sprites were found at the sites mentioned in the credits.txt file.<br>
<br>
Application:<br>
This program can be run directly from source code if you have the latest Python interpreter installed(3.10+) by running<br>
the main.py file.<br>
<br>
Build:<br>
It is also possible to build the project to a standalone executable(.exe) using the package 'pyinstaller'<br>

    directions:
        1. In a command prompt/terminal run the following command (Requires Python 3.10 or higher):
        
            pip install pyinstaller
        
        2. Run the following command:
        
            pyinstaller --onefile --noconsole main.py
        
        3. If successful, the executable should be in the "dist" folder, for the program to find the assets, 
           the executable must be in the same folder as the assets, which should be in there respective folders 
           as seen in the source code. It is recommended to put the created 'build' folder inside the "dist" folder,
           and also  copy/move the "Sprites" and "Data" folders, and the "main.spec" file to the "dist" folder with the 
           executable. Once that has been done, you may rename the "dist" folder to whatever you'd like and put that 
           folder wherever you want it.
        
        4. NOTE: These instructions may not be completely accurate for every OS so please refer to the following site:
        
            https://pyinstaller.org/en/stable/usage.html

<br>
<br>
Other Resources:<br>
    - Install Python Interpreter: https://www.python.org/downloads/

*** !!! Disclaimer !!! ***
** Pokémon is copyright protected by Nintendo, Game Freak, and Creatures.
** I claim NO rights over any images or fonts used in this project.
** I am providing the source code, build(s) and assets for educational purposes only.
** ABSOLUTELY NO money or goods will be exchanged for the code and/or files.
