from tkinter import *
import login

#main method
def main():
    root = Tk()
    root.title("GAYATRI's DANCE ACADEMY")
    root.geometry("1400x930+100+50")
    root.resizable(False, True)

    #Parsing the root window to the Login class
    #Initiating the System
    login.Login(root)

    root.mainloop()

if __name__ == '__main__':
    main()
