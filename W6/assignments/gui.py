'''
J Austin Hutchinson
CSE 111
Week #
Assignment Name
'''

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    '''
    FOR:    x 
    PARAM:  x
    RETURN: x
    '''
    # Create Window
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.option_add("Font", "Helvetica 16")
    frm_main.master.title("title")
    frm_main.pack(padx=3, pady=3,fill=tk.BOTH,expand=True)
    
    # create elements
    lbl_height = Label(frm_main,text="What is your rectangles height?")
    lbl_height.grid(row=0, column=0)
    ent_height = IntEntry(frm_main,lower_bound=0,width=3)
    ent_height.grid(row=0, column=1)

    
    lbl_width = Label(frm_main,text="What is your rectangles width?")
    lbl_width.grid(row=1, column=0)
    ent_width = IntEntry(frm_main,lower_bound=0,width=3)
    ent_width.grid(row=1, column=1)

    btn_calc = Button(frm_main,text="Calculate Area")
    btn_calc.grid(row=2, column=0)
    lbl_result = Label(frm_main,text="")
    lbl_result.grid(row=3, column=0)

    # button action
    def btn_actn_calc():
        try:
            height = ent_height.get()
            width = ent_width.get()
            area = f"Area: {height*width}"
            lbl_result.config(text=area)
        except ValueError:
            lbl_result.config(text="Enter a valid value")
            return False
            
    
    btn_calc.config(command = btn_actn_calc)
    
    # start GUI
    frm_main.mainloop()
    
    return 0

# Helper Functions
def helper():
    '''
    FOR:    x 
    PARAM:  x
    RETURN: x
    '''
    # step 1

    return 0
# Main call
if __name__ == "__main__":
    main()