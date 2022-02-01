# This is for a demonstration of my skills
from tkinter import *

# ----------------------  CONSTANTS  ---------------------- #
BACKGROUND = "#44c7da"
LIGHTBLUE = "#a4dae5"
DARKGRAY = "#3d424a"
KEYCOLOR = "#2596be"
RESETCOLOR = "#2596be"
FONT_NAME = "Courier"


# ----------------------  UI Setup  ---------------------- #
class Dashboard:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")

        # the width, height and colors are temp
        displayPanel = Frame(root, background=DARKGRAY, width=300, height=100)
        buttonPanel = Frame(root, background=BACKGROUND, width=300, height=200)
        displayPanel.pack(side="top", fill="both")
        buttonPanel.pack(side="bottom", fill="both", expand=True)

        # fill in the two areas
        self._create_buttons(buttonPanel)
        self._create_display(displayPanel)

        # Place the window in the center of the monitor
        root.eval('tk::PlaceWindow . center')

        # Set the minsize and maxsize of the window
        root.minsize(150, 300)
        root.maxsize(450, 900)

    def _create_buttons(self, parent):
        clear_button = Button(parent, text="Clr", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        all_clear_button = Button(parent, text="AC", bd=4, height=5, width=5, justify=CENTER,
                                  font=(FONT_NAME, 18, "bold"))
        seven_button = Button(parent, text="7", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        eight_button = Button(parent, text="8", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        nine_button = Button(parent, text="9", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        multiply_button = Button(parent, text="X", bd=4, height=5, width=5, justify=CENTER,
                                 font=(FONT_NAME, 18, "bold"))
        four_button = Button(parent, text="4", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        five_button = Button(parent, text="5", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        six_button = Button(parent, text="6", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        subtract_button = Button(parent, text="-", bd=4, height=5, width=5, justify=CENTER,
                                 font=(FONT_NAME, 18, "bold"))
        one_button = Button(parent, text="1", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        two_button = Button(parent, text="2", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        three_button = Button(parent, text="3", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        divide_button = Button(parent, text="\u00F7", bd=4, height=5, width=5, justify=CENTER,
                               font=(FONT_NAME, 18, "bold"))
        dot_button = Button(parent, text=".", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        zero_button = Button(parent, text="0", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        equal_button = Button(parent, text="=", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))
        add_button = Button(parent, text="+", bd=4, height=5, width=5, justify=CENTER, font=(FONT_NAME, 18, "bold"))

        # Set the Grid config/weights
        Grid.rowconfigure(parent, 0, weight=1)
        Grid.rowconfigure(parent, 1, weight=1)
        Grid.rowconfigure(parent, 2, weight=1)
        Grid.rowconfigure(parent, 3, weight=1)
        Grid.rowconfigure(parent, 4, weight=1)
        Grid.rowconfigure(parent, 5, weight=1)

        Grid.columnconfigure(parent, 0, weight=1)
        Grid.columnconfigure(parent, 1, weight=1)
        Grid.columnconfigure(parent, 2, weight=1)
        Grid.columnconfigure(parent, 3, weight=1)

        seven_button.grid(column=0, row=2, padx=5, pady=5, sticky=NSEW)
        eight_button.grid(column=1, row=2, padx=5, pady=5, sticky=NSEW)
        nine_button.grid(column=2, row=2, padx=5, pady=5, sticky=NSEW)
        multiply_button.grid(column=3, row=2, padx=5, pady=5, sticky=NSEW)
        clear_button.grid(column=0, columnspan=2, row=1, padx=5, pady=5, sticky=NSEW)
        all_clear_button.grid(column=2, columnspan=2, row=1, padx=5, pady=5, sticky=NSEW)
        four_button.grid(column=0, row=3, padx=5, pady=5, sticky=NSEW)
        five_button.grid(column=1, row=3, padx=5, pady=5, sticky=NSEW)
        six_button.grid(column=2, row=3, padx=5, pady=5, sticky=NSEW)
        subtract_button.grid(column=3, row=3, padx=5, pady=5, sticky=NSEW)
        one_button.grid(column=0, row=4, padx=5, pady=5, sticky=NSEW)
        two_button.grid(column=1, row=4, padx=5, pady=5, sticky=NSEW)
        three_button.grid(column=2, row=4, padx=5, pady=5, sticky=NSEW)
        divide_button.grid(column=3, row=4, padx=5, pady=5, sticky=NSEW)
        dot_button.grid(column=0, row=5, padx=5, pady=5, sticky=NSEW)
        zero_button.grid(column=1, row=5, padx=5, pady=5, sticky=NSEW)
        equal_button.grid(column=2, row=5, padx=5, pady=5, sticky=NSEW)
        add_button.grid(column=3, row=5, padx=5, pady=5, sticky=NSEW)

    def _create_display(self, parent):
        output_display = Label(parent, text="test me", fg="white", bg=DARKGRAY, font=(FONT_NAME, 24, "bold"))
        output_display.pack(padx=25, pady=5, side=RIGHT)


if __name__ == '__main__':
    root = Tk()
    board = Dashboard(root)
    root.mainloop()
