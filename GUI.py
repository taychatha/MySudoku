from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style
import Tkinter
from Tkinter import *
import sudokuGen
import tkMessageBox
from tkFileDialog import askopenfilename
from datetime import datetime
import math
import copy
import time


__author__ = 'Taimoor Chatha'

class GUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
        self.n = 0
        self.difficulty = "E"
        self.cells = []
        self.puzzle = []
        self.sudokuGrid = Frame(self)
        self.sudokuGrid.grid(row=2, column=0, pady=5)

    def initUI(self):

        self.parent.title("Sudoku")
        Style().configure("TButton", padding=(0, 5, 0, 5),
                          font='serif 10')
        #
        #
        # RWidth=self.parent.winfo_screenwidth()
        # RHeight=self.parent.winfo_screenheight()
        # self.parent.geometry(("%dx%d")%(RWidth,RHeight))
        self.parent.geometry("1000x800")

        menubar = Menu(self)
        titlePhotoFrame = Frame(self)
        titlePhotoFrame.grid(row = 4, column = 0)
        frame = Frame(self)
        frame.grid(row=0, column=0, padx=5)
        space = Frame(self)
        space.grid(row=1, column=0, pady=5)
        timer_frame = Frame(self)
        timer_frame.grid(row=2, column=0, pady=5)



        # cells = [] # A list of variables tied to entries
        # for i in range(9):
        #     cells.append([])
        #     for j in range(9):
        #         cells[i].append(StringVar())
        #
        # for i in range(9):
        #     for j in range(9):
        #         Entry(sudokuGrid, width = 3, justify = RIGHT,
        #               textvariable = cells[i][j]).grid(
        #             row = i+1, column = j+1)

        drag1 = PhotoImage(file = "animated-dragon-image-0031.gif")
        label = Label(frame, image = drag1)
        label.photo = drag1
        label.pack(side = "right", fill = "both", expand = "yes")

        titlePhoto = PhotoImage(file = "SudokuTitl.gif")
        label = Label(titlePhotoFrame, image = titlePhoto)
        label.photo = titlePhoto
        label.pack(side = "right", fill = "both", expand = "yes")

        photo = PhotoImage(file = "dragon4.gif")
        label = Label(frame, image = photo)
        label.photo = photo
        label.pack(side = "left", fill = "both", expand = "yes")

        generate = Tkinter.Button(frame, height = 2, width = 6, text = "Generate", command = self.newPuzzle)
        solvePuzzle = Tkinter.Button(frame, height = 2, width = 5, text = "Solve", command = self.solvePuzzle)
        importPuzzle = Tkinter.Button(frame, height = 2, width = 5, text = "Import", command = self.readPuzzle)
        #code to add widgets will go here...
        generate.pack(side = RIGHT)


        solvePuzzle.pack(side = RIGHT)
        importPuzzle.pack(side = RIGHT)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label="Generate Puzzle", command=self.newPuzzle)
        filemenu.add_command(label="Import Puzzle", command=self.readPuzzle)
        filemenu.add_command(label="Solve Puzzle", command=self.solvePuzzle)
        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.parent.config(menu = menubar)
        self.pack()

    def printN(self):
        print self.n

    def readPuzzle(self):
        filename = askopenfilename()
        if filename != "":
            strGrid = ""
            try:
                with open(filename) as f:
                    for line in f:
                        strGrid = strGrid+ (line)
                f.close
            except OSError:
                print "Daha"

            self.cells = []
            grid = strGrid.splitlines()


            self.n = len(grid)
            print self.n


            grid = [[0 for x in range(self.n)] for x in range(self.n)]
            row = 0
            col = 0
            for i, v in enumerate(strGrid.splitlines()):
                for j, w in enumerate(v.split()):
                    if w != " " and w != "\n" and w != "." :
                        print w
                        if col == self.n:
                            row += 1
                            col = 0
                        if row == self.n:
                            break
                        grid[row][col] = int(w)
                        col+=1

            self.puzzle = grid
            print self.puzzle
            for i in range((self.n)):
                self.cells.append([])
                for j in range((self.n)):
                    self.cells[i].append(StringVar())
            for child in self.sudokuGrid.winfo_children():
                child.destroy()
            for i in range((self.n)):
                for j in range((self.n)):
                    self.cells[i][j].set(self.puzzle[i][j])
            for i in range((self.n)):
                for j in range(self.n):
                    Entry(self.sudokuGrid, width=3, justify=RIGHT,
                          textvariable=self.cells[i][j]).grid(
                        row=i+1, column=j+1)
            tkMessageBox.showinfo( "Generated!", ("Valid Sudoku Puzzle Imported"))




            print grid


    def solvePuzzle(self):
        if self.n == 0:
            print "No grid. Generate a grid, or import one."

        elif self.n == 6 or self.n == 8 or self.n == 10 or self.n == 12:
            statement = TRUE
            for i in self.puzzle:
                if i != 0:
                    statement == FALSE
                    break
            if statement == TRUE:
                startTime = datetime.now()
                sudokuGen.evenRecSolve(self.puzzle)
                print self.puzzle
                for i in range(int(self.n)):
                    for j in range(int(self.n)):
                        self.cells[i][j].set(self.puzzle[i][j])
                tkMessageBox.showinfo( "Solved!", ("It took this long to solve the puzzle: ",(datetime.now()-startTime)))

        elif self.n == 4 or self.n == 9 or self.n == 16 or self.n == 25:
            statement = TRUE
            for i in self.puzzle:
                if i != 0:
                    statement == FALSE
                    break
            if statement == TRUE:
                startTime = datetime.now()
                sudokuGen.recSolve(self.puzzle)
                print self.puzzle
                for i in range(int(self.n)):
                    for j in range(int(self.n)):
                        self.cells[i][j].set(self.puzzle[i][j])
                tkMessageBox.showinfo( "Solved!", ("It took this long to solve the puzzle: ",(datetime.now()-startTime)))
            else:
                print "Already solved!"




    def newPuzzle(self):
        # sudokuGrid = Frame(self)
        # sudokuGrid.grid(row=2, column=0, pady=5)
        generator = Toplevel(self)
        inst = Label(generator, text="Enter your n")
        inst.grid(row=0, column=1)
        L1 = Label(generator, text="n")
        L1.grid(row=1, column=0)
        v = IntVar()
        j = StringVar()
        j.set("E")
        E1 = Entry(generator, bd=3, textvariable=v)
        D = Entry(generator, bd = 3, textvariable = j)
        E1.grid(row=1, column=1)
        E1.config(state = DISABLED)
        D.grid(row=2, column=1)
        D.config(state = DISABLED)
        v.set(4)
        radiobuttons = Frame(generator)
        radiobuttons.grid(row = 4, column =0)
        difficultButtons = Frame(generator)
        difficultButtons.grid(row = 4, column = 1)

        grids = [
            ("4x4", 4),
            ("6x6",  6),
            ("8x8", 8),
            ("9x9", 9),
            ("10x10", 10),
            ("12x12", 12),
            ("16x16", 16)]
        difficulties = [
            ("Hard", "H"),
            ("Medium", "M"),
            ("Easy", "E"),
        ]



        for text, n in grids:
            b = Radiobutton(difficultButtons, text=text,
                            variable=v, value=n)
            b.pack(anchor=E)
        for text, d in difficulties:
            q = Radiobutton(radiobuttons, text=text,
                            variable=j, value=d)
            q.pack(anchor=E)

        self.difficulty = j.get()
        self.n = v.get()

        def setN():

            self.cells = []
            self.n = int(E1.get())

             # A list of variables tied to entries
            if self.n == 4 or self.n == 9 or self.n == 16 or self.n == 25:
                self.n == int(math.sqrt(self.n))

                for i in range(self.n):
                    self.cells.append([])
                    for j in range(self.n):
                        self.cells[i].append(StringVar())
                grid = []
                startTime = datetime.now()
                stats = True
                while stats == True:
                    grid = sudokuGen.generator(int(math.sqrt(self.n)))
                    self.puzzle = sudokuGen.createPuzzle(grid, self.difficulty)
                    answer = copy.deepcopy(self.puzzle)
                    sudokuGen.recSolve(answer)
                    if answer != self.puzzle:
                        stats = False

                for child in self.sudokuGrid.winfo_children():
                    child.destroy()

                for i in range(self.n):
                    for j in range(self.n):
                        self.cells[i][j].set(self.puzzle[i][j])
                for i in range(self.n):
                    for j in range(self.n):
                        Entry(self.sudokuGrid, width=3, justify=RIGHT,
                              textvariable=self.cells[i][j]).grid(
                            row=i+1, column=j+1)
                tkMessageBox.showinfo( "Generated!", ("It took this long to make the puzzle: ",(datetime.now()-startTime)))
                print sudokuGen.toString(self.puzzle)
            elif self.n == 6 or self.n == 8 or self.n == 10 or self.n == 12:
                print "yes"
                print int(math.sqrt(self.n))
                self.n == int(self.n)
                for i in range(self.n):
                    self.cells.append([])
                    for j in range(self.n):
                        self.cells[i].append(StringVar())
                stats = True
                grid = []
                startTime = datetime.now()
                while stats == True:
                    grid = sudokuGen.altGenrator(self.n)
                    self.puzzle = sudokuGen.createPuzzle(grid, self.difficulty)
                    answer = copy.deepcopy(self.puzzle)
                    sudokuGen.evenRecSolve(answer)
                    print answer
                    print self.puzzle
                    print answer == self.puzzle
                    if answer != self.puzzle:
                        stats = False

                for child in self.sudokuGrid.winfo_children():
                    child.destroy()

                for i in range(self.n):
                    for j in range(self.n):
                        self.cells[i][j].set(self.puzzle[i][j])
                for i in range(self.n):
                    for j in range(self.n):
                        Entry(self.sudokuGrid, width=3, justify=RIGHT,
                              textvariable=self.cells[i][j]).grid(
                            row=i+1, column=j+1)
                tkMessageBox.showinfo( "Generated!", ("It took this long to make the puzzle: ",(datetime.now()-startTime)))
                print sudokuGen.toString(self.puzzle)


        def exitWind():
            generator.destroy()
        def two():
            setN()
            exitWind()
        ok = Tkinter.Button(generator, text = "OK", command = two)
        ok.grid(row = 3, column = 1)





    def disable(self, event):
        event.widget["state"] = "disabled"
        event.widget[""]

    def donothing(self):
        pass
    def importPuzzle(self):
        pass
        self.pack()

def main():

    root = Tk()
    app = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()