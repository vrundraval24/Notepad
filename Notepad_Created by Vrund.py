from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import font , colorchooser, filedialog, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from posixpath import split
import os

root = Tk()
root.attributes('-fullscreen', True)

root.title("Notepad")
# root.wm_iconbitmap("C:\\Program Files\\Notepad Created by Vrund\\Notepad-icon.ico")

root.config(bg="grey10")

theme_color = "deep sky blue"

file = None

back_file = '''
'''

def on_enter(event):
    close_button.config(background='firebrick3', foreground= "white")
    
def on_leave(event):
    close_button.config(background='grey30', foreground= "grey70")

def on_enter1(event):
    min_button.config(background='grey40', foreground= "white")
    
def on_leave1(event):
    min_button.config(background='grey30', foreground= "grey70")

statusbar_label = Label(root, text='Words : 0     Characters : 0         ', bg="grey20", fg="grey70", font=("",11,""), anchor=E)

statusbar_var = IntVar()

def statusbar(event):

    if statusbar_var.get() == 0:
        statusbar_label.pack(side=BOTTOM, fill=X)
        statusbar_var.set(1)
        text_area.pack_forget()
        text_area.pack(side=LEFT, fill=Y)

    elif statusbar_var.get() == 1:
        statusbar_label.pack_forget()
        statusbar_var.set(0)

    func_r7(event)

title_bar = Frame(root, bg="grey30") 
menu_bar = Frame(root, bg="grey20") 

label0 = Label(title_bar, text="  Notepad", bg="grey30", fg=theme_color, font=("",11,""), anchor=CENTER, height=1)
label0.pack(side=LEFT, fill=Y)

# label00 = Label(title_bar, text="•", bg="grey30", fg="grey70", font=("",11,""), anchor=CENTER, height=1)
# label00.pack(side=LEFT, fill=Y)

f_name = "Untitled"

if len(f_name) > 100:
    f_name = "*"

file_name = Label(title_bar, text=f"{f_name}.txt", bg="grey30", fg="grey70", font=("",11,""), anchor=CENTER, height=1)
file_name.pack(side=LEFT, fill=X, expand=True)

main_space_f = Frame(title_bar, bg="grey30", width=5)
main_space_f.pack(side=LEFT)

global close_button

close_button = Button(title_bar, text='X',bg="grey30",width=3,
fg="grey70",font=("",13,""), relief=FLAT, bd=-2,
activebackground='firebrick3', activeforeground='white')

min_button = Button(title_bar, text='_',bg="grey30",width=3,
fg="grey70",font=("",13,""), relief=FLAT, bd=-2,
activebackground='grey50', activeforeground='white')

file_button = Button(menu_bar, text="File", bg="grey20",width=5,
fg="grey65",font=("",10,""), relief=FLAT, bd=-2,
activebackground='grey25', activeforeground='white')
file_button.pack(side=LEFT)

edit_button = Button(menu_bar, text="Edit", bg="grey20",width=5,
fg="grey65",font=("",10,""), relief=FLAT, bd=-2,
activebackground='grey25', activeforeground='white')
edit_button.pack(side=LEFT)

format_button = Button(menu_bar, text="Format", bg="grey20",width=7,
fg="grey65",font=("",10,""), relief=FLAT, bd=-2,
activebackground='grey25', activeforeground='white')
format_button.pack(side=LEFT)

view_button = Button(menu_bar, text="View", bg="grey20",width=5,
fg="grey65",font=("",10,""), relief=FLAT, bd=-2,
activebackground='grey25', activeforeground='white')
view_button.pack(side=LEFT)

help_button = Button(menu_bar, text="Help", bg="grey20",width=5,
fg="grey65",font=("",10,""), relief=FLAT, bd=-2,
activebackground='grey25', activeforeground='white')
help_button.pack(side=LEFT)

def on_enter0(event):
    file_button.config(background='grey25', foreground= "white")
def on_leave0(event):
    file_button.config(background='grey20', foreground= "grey65") 

def on_enter3(event):
    edit_button.config(background='grey25', foreground= "white")
def on_leave3(event):
    edit_button.config(background='grey20', foreground= "grey65") 

def on_enter5(event):
    format_button.config(background='grey25', foreground= "white")
def on_leave5(event):
    format_button.config(background='grey20', foreground= "grey65") 

def on_enter7(event):
    view_button.config(background='grey25', foreground= "white")
def on_leave7(event):
    view_button.config(background='grey20', foreground= "grey65")

def on_enter8(event):
    help_button.config(background='grey25', foreground= "white")
def on_leave8(event):
    help_button.config(background='grey20', foreground= "grey65")

def newFile(event):
    global file
    f_name = "Untitled"

    if len(f_name) > 100:
        f_name = "*"

    file_name.configure(text=f"{f_name}.txt")
    file = None
    text_area.delete(1.0, END)

def openFile(event):
    global file
    global back_file

    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.txt"), ("Text Documents", "*.txt")])
    
    if file == "":
        file = None
            
    else:
        text_area.delete(1.0, END)
        f = open(file, "r")
        text_area.insert(1.0, f.read())
        f.close()

        back_file = text_area.get(1.0, END)


        f_name = os.path.basename(file)[:-4]

        if len(f_name) > 100:
            f_name = "*"

        file_name.configure(text=f"{f_name}.txt")

def saveFile(event):
    global file
    global back_file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.txt"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            f = open(file, 'r')
            back_file = f.read()
            f.close()
            f_name = os.path.basename(file)[:-4]

            if len(f_name) > 100:
                f_name = "*"

            file_name.configure(text=f"{f_name}.txt")
    else:
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()
        f = open(file, 'r')
        back_file = f.read()
        f.close()

def save_asFile(event):
    global file
    global back_file
    file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.txt"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()
        f = open(file, "r")
        back_file = f.read()
        f.close()
        f_name = os.path.basename(file)[:-4]

        if len(f_name) > 100:
            f_name = "*"

        file_name.configure(text=f"{f_name}.txt")

root.bind("<Control-n>", newFile)
root.bind("<Control-o>", openFile)
root.bind("<Control-s>", saveFile)
root.bind("<Control-Shift-S>", save_asFile)

def File_menu(event):
    global newFile
    global openFile
    global saveFile
    global save_asFile

    try:
        top2.destroy()
        edit_button.bind('<Enter>', on_enter3)
        edit_button.bind('<Leave>', on_leave3)
        edit_button.bind("<Button-1>", Edit_menu)        
        edit_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top5.destroy()
        top6.destroy()
        format_button.bind('<Enter>', on_enter5)
        format_button.bind('<Leave>', on_leave5)
        format_button.bind("<Button-1>", Format_menu)
        format_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top7.destroy()
        view_button.bind('<Enter>', on_enter7)
        view_button.bind('<Leave>', on_leave7)
        view_button.bind("<Button-1>", View_menu)
        view_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top8.destroy()
        help_button.bind('<Enter>', on_enter8)
        help_button.bind('<Leave>', on_leave8)
        help_button.bind("<Button-1>", Help_menu)
        help_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    global top
    top = Toplevel()
    top.overrideredirect(True)
    top.geometry("190x155+0+53")
    top.config(bg="grey15")
    

    space = Frame(top, bg="grey15", height=8)
    space.pack()

    def newFile(event):
        global file
        global f_name

        f_name = "Untitled"

        if len(f_name) > 100:
            f_name = "*"

        file_name.configure(text=f"{f_name}.txt")

        file = None
        text_area.delete(1.0, END)

        func_r(event)

    def openFile(event):
        global file
        global back_file
        global f_name
        file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.txt"), ("Text Documents", "*.txt")])
        func_r(event)

        if file == "":
            file = None
            
        else:
            text_area.delete(1.0, END)
            f = open(file, "r")
            text_area.insert(1.0, f.read())
            f.close()

            back_file = text_area.get(1.0, END)

            f_name = os.path.basename(file)[:-4]

            if len(f_name) > 100:
                f_name = "*"

            file_name.configure(text=f"{f_name}.txt")

    def saveFile(event):
        global file
        global back_file
        global f_name
        if file == None:
            file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.txt"), ("Text Documents", "*.txt")])

            if file == "":
                file = None
            else:
                f = open(file, "w")
                f.write(text_area.get(1.0, END))
                f.close()
                f = open(file, "r")
                back_file = f.read()
                f.close()
                f_name = os.path.basename(file)[:-4]

                if len(f_name) > 100:
                    f_name = "*"

                file_name.configure(text=f"{f_name}.txt")

        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            f = open(file, "r")
            back_file = f.read()
            f.close()

        func_r(event)

    def save_asFile(event):
        global file
        global back_file
        global f_name
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.txt"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            f = open(file, 'r')
            back_file = f.read()
            f.close()
            f_name = os.path.basename(file)[:-4]

            if len(f_name) > 100:
                f_name = "*"

            file_name.configure(text=f"{f_name}.txt")
        func_r(event)

    def exitFile(event):
        func_r(event)
        global file
        global back_file

        a = text_area.get(1.0, END)

        if a == back_file:
            root.destroy()

        else:

            top3 = Toplevel()
            top3.grab_set()
            top3.overrideredirect(True)
            top3.geometry("450x160+445+250")

            top3.configure(bg="grey20")
            global close_notepad_label

            # if theme_var.get() == 1:
            close_notepad_label = Label(top3, text="    Notepad", font=("",12,""), bg="grey20", fg=theme_color, anchor=W)
            close_notepad_label.pack(fill=X, pady=5)

            can_wid = Canvas(top3, bg="grey20", height=50, width=200, bd=-2)
            can_wid.pack(fill=X)
            can_wid.create_line(10, 1, 439, 1, fill="grey50")
            can_wid.create_text(222, 35, fill="grey90", text="Do you want to save the changes you made to this file?", font=("",11,""))

            f = Frame(top3, bg="grey20")
            f.pack(fill=BOTH, expand=True)

            def on_enterClose1(event):
                b1.config(background='dodgerblue4', foreground= "white")
            def on_leaveClose1(event):
                b1.config(background='grey40', foreground= "white")

            def on_enterClose2(event):
                b2.config(background='dodgerblue4', foreground= "white")
            def on_leaveClose2(event):
                b2.config(background='grey40', foreground= "white")

            def on_enterClose3(event):
                b3.config(background='dodgerblue4', foreground= "white")
            def on_leaveClose3(event):
                b3.config(background='grey40', foreground= "white")

            b1 = Button(f, text='Save',bg="grey40",width=7,
            fg="white",font=("",11,""), relief=FLAT, bd=-2,
            activebackground='dodgerblue4', activeforeground='white')
            b1.pack(side=LEFT,padx=50)

            b2 = Button(f, text="Don't Save",bg="grey40",width=10,
            fg="white",font=("",11,""), relief=FLAT, bd=-2,
            activebackground='dodgerblue4', activeforeground='white')
            b2.pack(side=LEFT,padx=10)

            b3 = Button(f, text='Cancle',bg="grey40",width=7,
            fg="white",font=("",11,""), relief=FLAT, bd=-2,
            activebackground='dodgerblue4', activeforeground='white')
            b3.pack(side=LEFT,padx=50)

            def func_c1(event):
                global file
                global back_file
                global f_name

                top3.destroy()

                if file == None:
                    file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.txt"), ("Text Documents", "*.txt")])

                    if file == "":
                        file = None

                    else:
                        f = open(file, "w")
                        f.write(text_area.get(1.0, END))
                        f.close()
                        f = open(file, 'r')
                        back_file = f.read()
                        f.close()
                        f_name = os.path.basename(file)[:-4]

                        if len(f_name) > 100:
                            f_name = "*"

                        file_name.configure(text=f"{f_name}.txt")
                        root.destroy()


                else:
                    f = open(file, "w")
                    f.write(text_area.get(1.0, END))
                    f.close()
                    f = open(file, 'r')
                    back_file = f.read()
                    f.close()
                    root.destroy()

            def func_c2(event):
                top3.destroy()
                root.destroy()

            def func_c3(event):
                top3.destroy()

            b1.bind('<Enter>', on_enterClose1)
            b1.bind('<Leave>', on_leaveClose1)
            b1.bind('<Button-1>', func_c1)

            b2.bind('<Enter>', on_enterClose2)
            b2.bind('<Leave>', on_leaveClose2)
            b2.bind('<Button-1>', func_c2)

            b3.bind('<Enter>', on_enterClose3)
            b3.bind('<Leave>', on_leaveClose3)
            b3.bind('<Button-1>', func_c3)

            top3.mainloop()


    new_button = Button(top, text="      New                Ctrl + N", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    new_button.pack(fill=X)

    open_button = Button(top, text="      Open              Ctrl + O", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    open_button.pack(fill=X)

    save_button = Button(top, text="      Save               Ctrl + S", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    save_button.pack(fill=X)

    save_as_button = Button(top, text="      Save as...", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    save_as_button.pack(fill=X)

    can = Canvas(top, width=190, height=20, bg="grey15", bd=-2)
    can.pack()

    can.create_line(10,10,180,10, fill="grey30")

    exit_button = Button(top, text="      Exit", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    exit_button.pack(fill=X)

    def func2(name, func_name):
        def on_enter2(event):
            name.config(background='dodgerblue4', foreground= "white")
        def on_leave2(event):
            name.config(background='grey15', foreground= "grey70")

        name.bind('<Enter>', on_enter2)
        name.bind('<Leave>', on_leave2)
        name.bind("<Button-1>", func_name)
    

    

    func2(new_button, newFile)
    func2(open_button, openFile)
    func2(save_button, saveFile)
    func2(save_as_button, save_asFile)
    func2(exit_button, exitFile)

    def func_r(event):

        try:
            text = event.widget.cget("text")


            if text == "File":
            
                file_button.configure(bg="grey25", fg="white")

                file_button.bind('<Enter>', on_enter0)
                file_button.bind('<Leave>', on_leave0)
                file_button.bind("<Button-1>", File_menu)

                top.destroy()

            else:
                file_button.configure(bg="grey20", fg="grey65")

                file_button.bind('<Enter>', on_enter0)
                file_button.bind('<Leave>', on_leave0)
                file_button.bind("<Button-1>", File_menu)
                

                top.destroy()

        except:
            file_button.configure(bg="grey20", fg="grey65")

            file_button.bind('<Enter>', on_enter0)
            file_button.bind('<Leave>', on_leave0)
            file_button.bind("<Button-1>", File_menu)
            
            top.destroy()



    file_button.bind('<Enter>', on_enter0)
    file_button.bind('<Leave>', on_leave0)
    file_button.bind("<Button-1>", func_r)

    file_button.configure(bg="grey25",fg="white")    
    file_button.unbind('<Enter>')
    file_button.unbind('<Leave>')


    root.bind('<Button-1>', func_r)





    top.mainloop()

def Edit_menu(event):

    try:
        top5.destroy()
        top6.destroy()
        format_button.bind('<Enter>', on_enter5)
        format_button.bind('<Leave>', on_leave5)
        format_button.bind("<Button-1>", Format_menu)
        format_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top.destroy()
        file_button.bind('<Enter>', on_enter0)
        file_button.bind('<Leave>', on_leave0)
        file_button.bind("<Button-1>", File_menu)
        file_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top7.destroy()
        view_button.bind('<Enter>', on_enter7)
        view_button.bind('<Leave>', on_leave7)
        view_button.bind("<Button-1>", View_menu)
        view_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top8.destroy()
        help_button.bind('<Enter>', on_enter8)
        help_button.bind('<Leave>', on_leave8)
        help_button.bind("<Button-1>", Help_menu)
        help_button.configure(bg="grey20", fg="grey65")
    except:
        pass


    global top2
    top2 = Toplevel()
    top2.overrideredirect(True)
    top2.geometry("220x267+46+53")
    top2.config(bg="grey15")

    space = Frame(top2, bg="grey15", height=8)
    space.pack()

    def undo_0(event):
        func_r3(event)       
        try:
            text_area.edit_undo()
        except:
            pass
        
    def redo_0(event):
        func_r3(event)
        try:
            text_area.edit_redo()
        except:
            pass
        
    def cut_0(event):
        text_area.event_generate(("<<Cut>>"))
        func_r3(event)


    def copy_0(event):
        text_area.event_generate(("<<Copy>>"))
        func_r3(event)
        
    def paste_0(event):
        text_area.event_generate(("<<Paste>>"))
        func_r3(event)

    def findandreplace_0(event=None):

        func_r3(event)

        def find():
            word = find_input.get()
            text_area.tag_remove('match','1.0',END)
            matches = 0
            if word :
                start_pos = '1.0'
                while True :
                    start_pos = text_area.search(word,start_pos,stopindex=END)
                    if(not start_pos):
                        break
                    end_pos = f'{start_pos}+{len(word)}c'
                    text_area.tag_add('match',start_pos,end_pos)
                    matches +=1
                    start_pos=end_pos
                    text_area.tag_config('match',foreground='red',background='')

        def replace():
            word = find_input.get()
            replace_text = replace_input.get()
            content = text_area.get(1.0,END)
            new_content = content.replace(word,replace_text)
            text_area.delete(1.0,END)
            text_area.insert(1.0,new_content)

        find_dialogue = Toplevel()
        find_dialogue.geometry('300x160+500+200')
        find_dialogue.resizable(0,0)

        ## frame
        find_frame = LabelFrame(find_dialogue, text ='Find and Replace')
        find_frame.pack(pady=20)

        ## labels 
        text_find_label = Label(find_frame,text ='Find ')
        text_replace_label = Label(find_frame,text ='Replace ')

        ##entry boxes 
        find_input = Entry(find_frame,width=30)
        replace_input = Entry(find_frame,width=30)

        ## Button
        find_button = Button(find_frame,text ='Find',command=find)
        replace_button = Button(find_frame,text ='Replace',command=replace)

        ##label grid
        text_find_label.grid(row=0,column=0,padx=4,pady=4)
        text_replace_label.grid(row=1,column=0,padx=4,pady=4)

        ##entry grid
        find_input.grid(row=0, column=1,padx=4,pady=4)
        replace_input.grid(row=1, column=1,padx=4,pady=4)

        ##button grid
        find_button.grid(row=2 ,column=0 ,padx=8,pady=4)
        replace_button.grid(row=2 ,column=1 ,padx=8,pady=4)

        find_dialogue.mainloop()
        
    def selectall_0(event):
        text_area.tag_add('sel', 1.0, END)
        func_r3(event)

    def clearall_0(event):
        text_area.delete(1.0, END)
        func_r3(event)

    undo_button = Button(top2,         text="      Undo                      Ctrl + Z", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    undo_button.pack(fill=X)

    redo_button = Button(top2,         text="      Redo                      Ctrl + Y", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    redo_button.pack(fill=X)

    can = Canvas(top2, width=220, height=20, bg="grey15", bd=-2)
    can.pack()
    can.create_line(10,10,210,10, fill="grey30")

    cut_button = Button(top2,          text="      Cut                        Ctrl + X", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    cut_button.pack(fill=X)

    copy_button = Button(top2,         text="      Copy                      Ctrl + C", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    copy_button.pack(fill=X)

    paste_button = Button(top2,        text="      Paste                     Ctrl + V", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    paste_button.pack(fill=X)

    can = Canvas(top2, width=220, height=20, bg="grey15", bd=-2)
    can.pack()
    can.create_line(10,10,210,10, fill="grey30")

    findandreplace_button = Button(top2,         text="      Find and Replace", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    findandreplace_button.pack(fill=X)

    can = Canvas(top2, width=220, height=20, bg="grey15", bd=-2)
    can.pack()
    can.create_line(10,10,210,10, fill="grey30")

    selectall_button = Button(top2,    text="      Select All                Ctrl + A", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    selectall_button.pack(fill=X)

    clearall_button = Button(top2,     text="      Clear All ", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    clearall_button.pack(fill=X)

    def func3(name3, func_name3):
        def on_enter3(event):
            name3.config(background='dodgerblue4', foreground= "white")
        def on_leave3(event):
            name3.config(background='grey15', foreground= "grey70")

        name3.bind('<Enter>', on_enter3)
        name3.bind('<Leave>', on_leave3)
        name3.bind("<Button-1>", func_name3)

    func3(undo_button, undo_0)
    func3(redo_button, redo_0)
    func3(cut_button, cut_0)
    func3(copy_button, copy_0)
    func3(paste_button, paste_0)
    func3(findandreplace_button, findandreplace_0)
    func3(selectall_button, selectall_0)
    func3(clearall_button, clearall_0)

    def func_r3(event):
        
        try:
            text = event.widget.cget("text")

            if text == "Edit":
            
                edit_button.configure(bg="grey25", fg="white")

                edit_button.bind('<Enter>', on_enter3)
                edit_button.bind('<Leave>', on_leave3)
                edit_button.bind("<Button-1>", Edit_menu)

                top2.destroy()

            else:

                edit_button.configure(bg="grey20", fg="grey65")

                edit_button.bind('<Enter>', on_enter3)
                edit_button.bind('<Leave>', on_leave3)
                edit_button.bind("<Button-1>", Edit_menu)

                top2.destroy()

        except:

            edit_button.configure(bg="grey20", fg="grey65")

            edit_button.bind('<Enter>', on_enter3)
            edit_button.bind('<Leave>', on_leave3)
            edit_button.bind("<Button-1>", Edit_menu)

            top2.destroy()

    edit_button.bind('<Enter>', on_enter3)
    edit_button.bind('<Leave>', on_leave3)
    edit_button.bind("<Button-1>", func_r3)

    edit_button.configure(bg="grey25",fg="white")    
    edit_button.unbind('<Enter>')
    edit_button.unbind('<Leave>')

    root.bind('<Button-1>', func_r3)

    top2.mainloop()

def Format_menu(event):
    try:
        top2.destroy()
        edit_button.bind('<Enter>', on_enter3)
        edit_button.bind('<Leave>', on_leave3)
        edit_button.bind("<Button-1>", Edit_menu)        
        edit_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top.destroy()
        file_button.bind('<Enter>', on_enter0)
        file_button.bind('<Leave>', on_leave0)
        file_button.bind("<Button-1>", File_menu)
        file_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top7.destroy()
        view_button.bind('<Enter>', on_enter7)
        view_button.bind('<Leave>', on_leave7)
        view_button.bind("<Button-1>", View_menu)
        view_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top8.destroy()
        help_button.bind('<Enter>', on_enter8)
        help_button.bind('<Leave>', on_leave8)
        help_button.bind("<Button-1>", Help_menu)
        help_button.configure(bg="grey20", fg="grey65")
    except:
        pass
    
    global top5
    top5 = Toplevel()
    
    top5.overrideredirect(True)
    top5.geometry("200x64+92+53")
    top5.config(bg="grey15")

    space1 = Frame(top5, bg="grey15", height=8)
    space1.pack()

    def open_fontdialogbox(event):
        func_r5(event)
        func()

    font_button = Button(top5,         text="      Font... ", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    font_button.pack(fill=X)

    theme_button = Button(top5,         text="      Theme ", bg="grey15",width=5,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    theme_button.pack(fill=X)


    space2 = Frame(top5, bg="grey15", height=8)
    space2.pack(fill=BOTH, expand= True)


    def on_enter4(event):
        try:
            top6.withdraw()
        except:
            pass
        font_button.config(background='dodgerblue4', foreground= "white")
    def on_leave4(event):
        font_button.config(background='grey15', foreground= "grey70")
    

    def on_enter44(event):
        theme_button.config(background='dodgerblue4', foreground= "white")
        try:
            top6.state('normal')
        except:
            pass
    def on_leave44(event):
        theme_button.config(background='grey15', foreground= "grey70")

    def hower_close(event):
        try:
            top6.withdraw()
        except:
            pass

    space2.bind('<Enter>', hower_close)

    root.bind('<Enter>', hower_close)

    font_button.bind('<Enter>', on_enter4)
    font_button.bind('<Leave>', on_leave4)
    font_button.bind("<Button-1>", open_fontdialogbox)

    theme_button.bind('<Enter>', on_enter44)
    theme_button.bind('<Leave>', on_leave44)

   

    def func_r5(event):

        try:
            text = event.widget.cget("text")


            if text == "Format":
            
                format_button.configure(bg="grey25", fg="white")

                format_button.bind('<Enter>', on_enter5)
                format_button.bind('<Leave>', on_leave5)
                format_button.bind("<Button-1>", Format_menu)

                top5.destroy()
                top6.destroy()


            else:
                format_button.configure(bg="grey20", fg="grey65")

                format_button.bind('<Enter>', on_enter5)
                format_button.bind('<Leave>', on_leave5)
                format_button.bind("<Button-1>", Format_menu)
                

                top5.destroy()
                top6.destroy()


        except:
            format_button.configure(bg="grey20", fg="grey65")

            format_button.bind('<Enter>', on_enter5)
            format_button.bind('<Leave>', on_leave5)
            format_button.bind("<Button-1>", Format_menu)
            
            top5.destroy()
            top6.destroy()


    format_button.bind('<Enter>', on_enter5)
    format_button.bind('<Leave>', on_leave5)
    format_button.bind("<Button-1>", func_r5)

    format_button.configure(bg="grey25",fg="white")    
    format_button.unbind('<Enter>')
    format_button.unbind('<Leave>')

    root.bind('<Button-1>', func_r5)

    global top6
    top6 = Toplevel()
    top6.overrideredirect(True)
    top6.withdraw()
    top6.geometry("200x90+292+85")
    top6.config(bg="red")

    global theme_var

    theme_var = IntVar()
    # theme_var.set(0)

    if theme_color == 'deep sky blue':
        theme_var.set(0)

    elif theme_color == 'orange':
        theme_var.set(1)

    space3 = Frame(top6, bg="grey20", height=8)
    space3.pack(fill=BOTH, expand= True)

    radiobtn_1 = Radiobutton(top6, text="Light Blue       ", variable=theme_var, value=0, bg="grey20", fg="deep sky blue", activeforeground="deep sky blue", activebackground="grey20", selectcolor="grey20", font=("",12,""), pady=5)
    radiobtn_1.pack(fill=X)
   
    radiobtn_2 = Radiobutton(top6, text="Orange           ", variable=theme_var, value=1, bg="grey20", fg="orange", activeforeground="orange", activebackground="grey20", selectcolor="grey20",font=("",12,""), pady=5)
    radiobtn_2.pack(fill=X)



        
    space4 = Frame(top6, bg="grey20", height=8)
    space4.pack(fill=BOTH, expand= True)
    



    def push_btn_hower(event):
        format_button.configure(bg="grey20", fg="grey65")

        format_button.bind('<Enter>', on_enter5)
        format_button.bind('<Leave>', on_leave5)
        format_button.bind("<Button-1>", Format_menu)

        root.unbind('<Enter>')

        top5.destroy()
        top6.destroy()
        
        
    def func_rb0(event):

        text = event.widget.cget("text")

        if text == "Light Blue       ":
            text0 = "deep sky blue" 
        elif text == "Orange           ":
            text0 = "orange"     

        root.bind('<Enter>', push_btn_hower)

        global theme_color
        global theme_var

        if text0 == theme_color:
            pass
        else:
            if theme_var.get() == 1:
                theme_color = "deep sky blue"
                label0.config(fg=theme_color)
                text_area.config(insertbackground=theme_color)
                try:
                    label_font.config(fg=theme_color)
                except:
                    pass

            elif theme_var.get() == 0:
                theme_color = "orange"
                label0.config(fg=theme_color)
                text_area.config(insertbackground=theme_color)
                try:
                    label_font.config(fg=theme_color)
                except:
                    pass
            

    radiobtn_1.bind('<Button-1>', func_rb0)
    radiobtn_2.bind('<Button-1>', func_rb0)

    top6.bind('<Enter>', on_enter44)
    top6.bind('<Leave>', on_leave44)

    def on_enter_rb007(event):
        radiobtn_1.config(background='grey30', foreground= "deep sky blue")
    def on_leave_rb007(event):
        radiobtn_1.config(background='grey20', foreground= "deep sky blue")

    def on_enter_rb0077(event):
        radiobtn_2.config(background='grey30', foreground= "orange")
    def on_leave_rb0077(event):
        radiobtn_2.config(background='grey20', foreground= "orange")

    radiobtn_1.bind('<Enter>', on_enter44)
    radiobtn_1.bind('<Leave>', on_leave44)

    radiobtn_2.bind('<Enter>', on_enter44)
    radiobtn_2.bind('<Leave>', on_leave44)

    radiobtn_1.bind('<Enter>', on_enter_rb007)
    radiobtn_1.bind('<Leave>', on_leave_rb007)

    radiobtn_2.bind('<Enter>', on_enter_rb0077)
    radiobtn_2.bind('<Leave>', on_leave_rb0077)

    top6.mainloop()

    

    top5.mainloop()

def View_menu(event):
    
    try:
        top2.destroy()
        edit_button.bind('<Enter>', on_enter3)
        edit_button.bind('<Leave>', on_leave3)
        edit_button.bind("<Button-1>", Edit_menu)        
        edit_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top5.destroy()
        top6.destroy()
        format_button.bind('<Enter>', on_enter5)
        format_button.bind('<Leave>', on_leave5)
        format_button.bind("<Button-1>", Format_menu)
        format_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top.destroy()
        file_button.bind('<Enter>', on_enter0)
        file_button.bind('<Leave>', on_leave0)
        file_button.bind("<Button-1>", File_menu)
        file_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top8.destroy()
        help_button.bind('<Enter>', on_enter8)
        help_button.bind('<Leave>', on_leave8)
        help_button.bind("<Button-1>", Help_menu)
        help_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    global top7
    top7 = Toplevel()
    top7.overrideredirect(True)
    top7.geometry("200x38+154+53")
    top7.config(bg="grey15")

    space = Frame(top7, bg="grey15", height=8)
    space.pack()

    statusbar_button = Checkbutton(top7,         text="  Statusbar             ", bg="grey15", variable=statusbar_var,
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=CENTER, selectcolor="gray15")
    statusbar_button.pack(fill=X)
    
    def on_enter77(event):
        statusbar_button.config(background='dodgerblue4', foreground= "white")
    def on_leave77(event):
        statusbar_button.config(background='grey15', foreground= "grey70")

    statusbar_button.bind('<Enter>', on_enter77)
    statusbar_button.bind('<Leave>', on_leave77)
    statusbar_button.bind("<Button-1>", statusbar)

    global func_r7

    def func_r7(event):
        
        try:
            text = event.widget.cget("text")

            if text == "View":
            
                view_button.configure(bg="grey25", fg="white")

                view_button.bind('<Enter>', on_enter7)
                view_button.bind('<Leave>', on_leave7)
                view_button.bind("<Button-1>", View_menu)

                top7.destroy()

            else:

                view_button.configure(bg="grey20", fg="grey65")

                view_button.bind('<Enter>', on_enter7)
                view_button.bind('<Leave>', on_leave7)
                view_button.bind("<Button-1>", View_menu)

                top7.destroy()

        except:

            view_button.configure(bg="grey20", fg="grey65")

            view_button.bind('<Enter>', on_enter7)
            view_button.bind('<Leave>', on_leave7)
            view_button.bind("<Button-1>", View_menu)

            top7.destroy()

    view_button.bind('<Enter>', on_enter7)
    view_button.bind('<Leave>', on_leave7)
    view_button.bind("<Button-1>", func_r7)

    view_button.configure(bg="grey25",fg="white")    
    view_button.unbind('<Enter>')
    view_button.unbind('<Leave>')

    root.bind('<Button-1>', func_r7)

    top7.mainloop()

def Help_menu(event):

    try:
        top2.destroy()
        edit_button.bind('<Enter>', on_enter3)
        edit_button.bind('<Leave>', on_leave3)
        edit_button.bind("<Button-1>", Edit_menu)        
        edit_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top5.destroy()
        top6.destroy()
        format_button.bind('<Enter>', on_enter5)
        format_button.bind('<Leave>', on_leave5)
        format_button.bind("<Button-1>", Format_menu)
        format_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top.destroy()
        file_button.bind('<Enter>', on_enter0)
        file_button.bind('<Leave>', on_leave0)
        file_button.bind("<Button-1>", File_menu)
        file_button.configure(bg="grey20", fg="grey65")
    except:
        pass

    try:
        top7.destroy()
        view_button.bind('<Enter>', on_enter7)
        view_button.bind('<Leave>', on_leave7)
        view_button.bind("<Button-1>", View_menu)
        view_button.configure(bg="grey20", fg="grey65")

    except:
        pass

    global top8
    top8 = Toplevel()
    top8.overrideredirect(True)
    top8.geometry("200x38+200+53")
    top8.config(bg="grey15")

    space = Frame(top8, bg="grey15", height=8)
    space.pack()

    def about(event):

        func_r8(event)

        top9 = Toplevel()
        top9.grab_set()
        top9.overrideredirect(True)
        top9.geometry("432x320+470+180")
        top9.config(bg="grey")

        about_can = Canvas(top9, bg="grey20", bd=-2, height=220)
        about_can.pack(fill=X)

        about_notepad_text = '''Notepad is a simple text editor for Microsoft Windows and 
a basic text-editing program which enables computer users
to create documents.'''

        about_can.create_text(120, 50, fill=theme_color, text="Notepad", font=("",30,"bold"))
        about_can.create_text(250, 57, fill="grey50", text="0.0.1", font=("",15,"bold"))
        about_can.create_text(215, 130, fill="grey70", text=about_notepad_text, font=("",10,""))
        about_can.create_text(210, 206, fill="grey50", text="Created by", font=("",15,"bold"))
        about_can.create_text(330, 200, fill="grey55", text="Vrund", font=("",30,"bold"))

        about_frame = Frame(top9, bg="grey20") 
        about_frame.pack(fill=BOTH, expand=True)

        ab_Ok_btn = Button(about_frame, text='Ok',bg="grey40",width=7,
        fg="white",font=("",11,""), relief=FLAT, bd=-2,
        activebackground='dodgerblue4', activeforeground='white')
        ab_Ok_btn.pack(side=RIGHT,padx=47, anchor=S, pady=30)

        def ab_close(event):
            top9.destroy()

        def on_enterOk(event):
            ab_Ok_btn.config(background='dodgerblue4', foreground= "white")
        def on_leaveOk(event):
            ab_Ok_btn.config(background='grey40', foreground= "white")

        ab_Ok_btn.bind('<Enter>', on_enterOk)
        ab_Ok_btn.bind('<Leave>', on_leaveOk)
        ab_Ok_btn.bind("<Button-1>", ab_close)

    about_button = Button(top8,         text="      About Notepad", bg="grey15",
    fg="grey70",font=("",10,""), relief=FLAT, bd=-2,
    activebackground='dodgerblue4', activeforeground='white', anchor=NW)
    about_button.pack(fill=X)

    def on_enter88(event):
        about_button.config(background='dodgerblue4', foreground= "white")
    def on_leave88(event):
        about_button.config(background='grey15', foreground= "grey70")

    about_button.bind('<Enter>', on_enter88)
    about_button.bind('<Leave>', on_leave88)
    about_button.bind("<Button-1>", about)

    def func_r8(event):
        
        try:
            text = event.widget.cget("text")

            if text == "Help":
            
                help_button.configure(bg="grey25", fg="white")

                help_button.bind('<Enter>', on_enter8)
                help_button.bind('<Leave>', on_leave8)
                help_button.bind("<Button-1>", Help_menu)

                top8.destroy()

            else:

                help_button.configure(bg="grey20", fg="grey65")

                help_button.bind('<Enter>', on_enter8)
                help_button.bind('<Leave>', on_leave8)
                help_button.bind("<Button-1>", Help_menu)

                top8.destroy()

        except:

            help_button.configure(bg="grey20", fg="grey65")

            help_button.bind('<Enter>', on_enter8)
            help_button.bind('<Leave>', on_leave8)
            help_button.bind("<Button-1>", Help_menu)

            top8.destroy()

    help_button.bind('<Enter>', on_enter8)
    help_button.bind('<Leave>', on_leave8)
    help_button.bind("<Button-1>", func_r8)

    help_button.configure(bg="grey25",fg="white")    
    help_button.unbind('<Enter>')
    help_button.unbind('<Leave>')

    root.bind('<Button-1>', func_r8)

    top8.mainloop()



file_button.bind('<Enter>', on_enter0)
file_button.bind('<Leave>', on_leave0)
file_button.bind("<Button-1>", File_menu)

edit_button.bind('<Enter>', on_enter3)
edit_button.bind('<Leave>', on_leave3)
edit_button.bind("<Button-1>", Edit_menu)

format_button.bind('<Enter>', on_enter5)
format_button.bind('<Leave>', on_leave5)
format_button.bind("<Button-1>", Format_menu)

view_button.bind('<Enter>', on_enter7)
view_button.bind('<Leave>', on_leave7)
view_button.bind("<Button-1>", View_menu)

help_button.bind('<Enter>', on_enter8)
help_button.bind('<Leave>', on_leave8)
help_button.bind("<Button-1>", Help_menu)

title_bar.pack(fill=X, anchor=N)
menu_bar.pack(fill=X, anchor=N)
close_button.pack(side=RIGHT)
min_button.pack(side=RIGHT)

def close(event):

    global file
    global back_file

    a = text_area.get(1.0, END)

    if a == back_file:
        root.destroy()

    else:

        top3 = Toplevel()
        top3.grab_set()
        top3.overrideredirect(True)
        top3.geometry("450x160+445+250")
        top3.configure(bg="grey20")

        global close_notepad_label


        close_notepad_label = Label(top3, text="    Notepad", font=("",12,""), bg="grey20", fg=theme_color, anchor=W)
        close_notepad_label.pack(fill=X, pady=5)

        can_wid = Canvas(top3, bg="grey20", height=50, width=200, bd=-2)
        can_wid.pack(fill=X)
        can_wid.create_line(10, 1, 439, 1, fill="grey50")
        can_wid.create_text(222, 35, fill="grey90", text="Do you want to save the changes you made to this file?", font=("",11,""))

        f = Frame(top3, bg="grey20")
        f.pack(fill=BOTH, expand=True)

        def on_enterClose1(event):
            b1.config(background='dodgerblue4', foreground= "white")
        def on_leaveClose1(event):
            b1.config(background='grey40', foreground= "white")

        def on_enterClose2(event):
            b2.config(background='dodgerblue4', foreground= "white")
        def on_leaveClose2(event):
            b2.config(background='grey40', foreground= "white")

        def on_enterClose3(event):
            b3.config(background='dodgerblue4', foreground= "white")
        def on_leaveClose3(event):
            b3.config(background='grey40', foreground= "white")

        b1 = Button(f, text='Save',bg="grey40",width=7,
        fg="white",font=("",11,""), relief=FLAT, bd=-2,
        activebackground='dodgerblue4', activeforeground='white')
        b1.pack(side=LEFT,padx=50)

        b2 = Button(f, text="Don't Save",bg="grey40",width=10,
        fg="white",font=("",11,""), relief=FLAT, bd=-2,
        activebackground='dodgerblue4', activeforeground='white')
        b2.pack(side=LEFT,padx=10)

        b3 = Button(f, text='Cancle',bg="grey40",width=7,
        fg="white",font=("",11,""), relief=FLAT, bd=-2,
        activebackground='dodgerblue4', activeforeground='white')
        b3.pack(side=LEFT,padx=50)

        def func_c1(event):
            global file
            global back_file
            global f_name

            top3.destroy()

            if file == None:
                file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.txt"), ("Text Documents", "*.txt")])
                
                if file == "":
                    file = None

                else:
                    f = open(file, "w")
                    f.write(text_area.get(1.0, END))
                    f.close()
                    f = open(file, 'r')
                    back_file = f.read()
                    f.close()
                    f_name = os.path.basename(file)[:-4]

                    if len(f_name) > 100:
                        f_name = "*"

                    file_name.configure(text=f"{f_name}.txt")
                    root.destroy()

                    
            else:
                f = open(file, "w")
                f.write(text_area.get(1.0, END))
                f.close()
                f = open(file, 'r')
                back_file = f.read()
                f.close()
                root.destroy()

        def func_c2(event):
            top3.destroy()
            root.destroy()

        def func_c3(event):
            top3.destroy()

        b1.bind('<Enter>', on_enterClose1)
        b1.bind('<Leave>', on_leaveClose1)
        b1.bind('<Button-1>', func_c1)

        b2.bind('<Enter>', on_enterClose2)
        b2.bind('<Leave>', on_leaveClose2)
        b2.bind('<Button-1>', func_c2)

        b3.bind('<Enter>', on_enterClose3)
        b3.bind('<Leave>', on_leaveClose3)
        b3.bind('<Button-1>', func_c3)

        top3.mainloop()

# Minimize Function
def minimize(event):

    root.iconify()


side_bar_frame = Frame(root, bg="grey10")
side_bar_frame.pack(fill=Y, side=RIGHT)

def on_enter_showbar(event):
    scroll_bar.pack(side=RIGHT, fill=Y)    

def on_leave_hidebar(event):
    scroll_bar.pack_forget()

side_bar_frame.bind('<Enter>', on_enter_showbar)

scroll_bar = Scrollbar(root)

text_area = Text(root, bg="grey10", bd=-2, fg="grey85", font=("Arial",12,""), padx=15, pady=10, undo=True, width=147)
text_area.pack(side=LEFT, fill=Y)
text_area.config(insertbackground=theme_color)
text_area.focus_set()

scroll_bar.config(command=text_area.yview)
text_area.config(yscrollcommand= scroll_bar.set)
text_area.bind('<Enter>', on_leave_hidebar)
menu_bar.bind('<Enter>', on_leave_hidebar)
statusbar_label.bind('<Enter>', on_leave_hidebar)

text_changed = False

def changed(event=None):

    global text_changed

    if text_area.edit_modified(): # checks if any character is added or not

        text_changed = True
        words = len(text_area.get(1.0, 'end-1c').split()) # it even counts new line character so end-1c subtracts one char
        straight_text = text_area.get(1.0,'end-1c').replace('''\n''', "")
        characters = len(straight_text.replace(" ", ""))
        
        # curser_location = text_area.index(INSERT)
        # for i in range(0, len(curser_location)):
        #     if curser_location[i] == ".":
        #         line = curser_location[:i]
        #         column = curser_location[i+1:]
        #         line = int(line)
        #         column = int(column)

        statusbar_label.config(text=f'Words : {words}     Characters : {characters}         ')

    text_area.edit_modified(False)
text_area.bind('<<Modified>>',changed)

close_button.bind('<Enter>', on_enter)
close_button.bind('<Leave>', on_leave)
close_button.bind("<Button-1>", close)

min_button.bind('<Enter>', on_enter1)
min_button.bind('<Leave>', on_leave1)
min_button.bind("<Button-1>", minimize)

###########################################       START       ############################################

global func

def func():
    
    top4.lift()
    top4.state('normal')
    top4.grab_set()
    
    global a
    global b
    global c
    global d

    a = current_font_family
    b = current_font_size
    c = font_style
    d = f_color


top4 = Toplevel()
top4.overrideredirect(True)
top4.geometry("450x320+450+180")
top4.withdraw()

# make a frame for the title bar
title_bar = Frame(top4, bg="grey30")

label_font = Label(title_bar, text="  Font", bg="grey30", fg=theme_color, font=("times new roman",15,"bold"), anchor=NW, height=1)
label_font.pack(side=LEFT)

def start_move(event):
    top4.x = event.x
    top4.y = event.y

def stop_move(event):
    top4.x = None
    top4.y = None

def do_move(event):
    deltax = event.x - top4.x
    deltay = event.y - top4.y
    x = top4.winfo_x() + deltax
    y = top4.winfo_y() + deltay
    top4.geometry(f"+{x}+{y}")


title_bar.pack(expand=1, fill=X, anchor=N)

title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", do_move)

label_font.bind("<ButtonPress-1>", start_move)
label_font.bind("<ButtonRelease-1>", stop_move)
label_font.bind("<B1-Motion>", do_move)

##Frames
f1 = Frame(top4)
f1.pack(fill=BOTH,expand=True)

f4 = Frame(top4)
f4.pack(fill=BOTH,expand=True,side=BOTTOM, pady=5)

f2 = Frame(top4, width=100)
f2.pack(side=LEFT, pady=10)

f3 = Frame(top4)
f3.pack(fill=BOTH,expand=True, pady=10)

##font box
font_tuple = font.families()
font_family = StringVar()
font_box = ttk.Combobox(f1, width=45,textvariable=font_family,state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.pack(side=LEFT, anchor=NW, pady=10, padx=10)

##size box
size_var = IntVar()
font_size=ttk.Combobox(f1,width=25,textvariable = size_var,state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(2)
font_size.pack(side=LEFT, anchor=NW, pady=10, padx=10)

font_color_btn = ttk.Button(f2, text="Font Color", takefocus=0)
font_color_btn.pack(pady=20, padx=33, anchor=W)

global f_color
f_color = "#d8d8d8"

##font color functionality
def change_font_color():
    global f_color
    global color_var
    color_var = colorchooser.askcolor()
    text_sample.configure(fg=color_var[1])
    f_color = color_var[1]

font_color_btn.configure(command=change_font_color)

##font style
bold_var =IntVar()
italic_var =IntVar()
underline_var =IntVar()

bold_check = Checkbutton(f2, text="Bold         ", font=("",12,""), variable=bold_var)
bold_check.pack(padx=30)

italic_check = Checkbutton(f2, text="Italic         ", font=("",12,""), variable=italic_var)
italic_check.pack(padx=30)

underline_check = Checkbutton(f2, text="Underline", font=("",12,""), variable=underline_var)
underline_check.pack(padx=30)

## Apply, Ok, Cancle buttons functionality
def apply():
    global current_font_family
    global current_font_size
    global f_color
    global font_style
    current_font_family = font_family.get()
    current_font_size = size_var.get()
    text_area.config(font=(current_font_family,current_font_size,font_style))
    text_area.configure(fg=f_color)
    func()

def cancle():

    global current_font_family
    global current_font_size
    global font_style
    global f_color
    font_box.current(font_tuple.index(a))
    font_size.current(int((b/2) - 4))
    text_sample.config(font=(a,b,c))
    text_sample.configure(fg=d)
    current_font_family = a
    current_font_size = b
    font_style = c
    f_color = d

    def checkbtn_set():
    
        if 'bold' in c:
            if 'italic' in c:
                if 'underline' in c:
                    bold_var.set(1)
                    italic_var.set(1)
                    underline_var.set(1)

                elif 'underline' not in c:
                    bold_var.set(1)
                    italic_var.set(1)
                    underline_var.set(0)

            elif 'italic' not in c:
                if 'underline' in c:
                    bold_var.set(1)
                    italic_var.set(0)
                    underline_var.set(1)

                elif 'underline' not in c:
                    bold_var.set(1)
                    italic_var.set(0)
                    underline_var.set(0)

        elif 'italic' in c:
            if 'bold' in c:
                if 'underline' in c:
                    bold_var.set(1)
                    italic_var.set(1)
                    underline_var.set(1)

                elif 'underline' not in c:
                    bold_var.set(1)
                    italic_var.set(1)
                    underline_var.set(0)

            elif 'bold' not in c:
                if 'underline' in c:
                    bold_var.set(0)
                    italic_var.set(1)
                    underline_var.set(1)

                elif 'underline' not in c:
                    bold_var.set(0)
                    italic_var.set(1)
                    underline_var.set(0)

        elif 'underline' in c:
            if 'bold' in c:
                if 'italic' in c:
                    bold_var.set(1)
                    italic_var.set(1)
                    underline_var.set(1)

                elif 'italic' not in c:
                    bold_var.set(1)
                    italic_var.set(0)
                    underline_var.set(1)

            elif 'bold' not in c:
                if 'italic' in c:
                    bold_var.set(0)
                    italic_var.set(1)
                    underline_var.set(1)

                elif 'italic' not in c:
                    bold_var.set(0)
                    italic_var.set(0)
                    underline_var.set(1)

        elif 'normal' in c:
            bold_var.set(0)
            italic_var.set(0)
            underline_var.set(0)
    checkbtn_set()

    top4.grab_release()
    top4.withdraw()

def ok():

    global current_font_family
    global current_font_size
    global f_color
    global font_style

    current_font_family = font_family.get()
    current_font_size = size_var.get()
    text_area.config(font=(current_font_family,current_font_size,font_style))
    text_area.configure(fg=f_color)

    top4.grab_release()
    top4.withdraw()

## Apply, Ok, Cancle buttons
apply_btn = ttk.Button(f4, text="Apply", takefocus=0)
apply_btn.pack(side=LEFT,padx=50, pady=20)
apply_btn.configure(command=apply)

ok_btn = ttk.Button(f4, text="Ok", takefocus=0)
ok_btn.pack(side=LEFT,padx=22, pady=20)
ok_btn.configure(command=ok)

cancle_btn = ttk.Button(f4, text="Cancle", takefocus=0)
cancle_btn.pack(side=LEFT, pady=20)
cancle_btn.configure(command=cancle)

##  font family and font size functionality
global current_font_family
global current_font_size
global font_style

current_font_family = 'Arial'
current_font_size = 12
font_style = ('normal')

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_sample.config(font=(current_font_family,current_font_size,font_style))

def change_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_sample.config(font=(current_font_family,current_font_size,font_style))

#bold buttton functionality
def change_bold(event):
    global font_style

    a = bold_var.get()
    b = italic_var.get()
    c = underline_var.get()

    if a == 1:
    
        if b == 0:
            if c == 0:
                text_sample.config(font=(current_font_family,current_font_size,'normal'))
                font_style = ('normal')
            elif c == 1:
                text_sample.config(font=(current_font_family,current_font_size,'underline'))
                font_style = ('underline')

        elif b == 1:
            if c == 0:
                text_sample.config(font=(current_font_family,current_font_size,'italic'))
                font_style = ('italic')
            elif c == 1:
                text_sample.config(font=(current_font_family,current_font_size,'italic', 'underline'))
                font_style = ('italic', 'underline')

    elif a == 0 :
    
        if b == 0:
            if c == 0:
                text_sample.config(font=(current_font_family,current_font_size,'bold'))
                font_style = ('bold')
            elif c == 1:
                text_sample.config(font=(current_font_family,current_font_size,'bold', 'underline'))
                font_style = ('bold', 'underline')

        elif b == 1:
        
            if c == 0:
                text_sample.config(font=(current_font_family,current_font_size,'bold','italic'))
                font_style = ('bold','italic')
            elif c == 1:
                text_sample.config(font=(current_font_family,current_font_size,'bold', 'italic', 'underline'))
                font_style = ('bold', 'italic', 'underline')

bold_check.bind("<Button-1>", change_bold)

#Italic button functionality
def change_italic(event):
    global font_style

    a = bold_var.get()
    b = italic_var.get()
    c = underline_var.get()

    if b == 1:
    
        if a == 0:
            if c == 0:
                text_sample.config(font=(current_font_family,current_font_size,'normal'))
                font_style = ('normal')
            elif c == 1:
                text_sample.config(font=(current_font_family,current_font_size,'underline'))
                font_style = ('underline')

        elif a == 1:
            if c == 0:
                text_sample.config(font=(current_font_family,current_font_size,'bold'))
                font_style = ('bold')
            elif c == 1:
                text_sample.config(font=(current_font_family,current_font_size,'bold','underline'))
                font_style = ('bold','underline')

    elif b == 0 :
    
        if a == 0:
            if c == 0:
                text_sample.config(font=(current_font_family,current_font_size,'italic'))
                font_style = ('italic')
            elif c == 1:
                text_sample.config(font=(current_font_family,current_font_size,'italic', 'underline'))
                font_style = ('italic', 'underline')

        elif a == 1:
            if c == 0:
                text_sample.config(font=(current_font_family,current_font_size,'bold', 'italic'))
                font_style = ('bold', 'italic')
            elif c == 1:
                text_sample.config(font=(current_font_family,current_font_size, 'bold', 'italic', 'underline'))
                font_style = ('bold', 'italic', 'underline')

italic_check.bind("<Button-1>", change_italic)

#Underline button functionality
def change_underline(event):
    global font_style

    a = bold_var.get()
    b = italic_var.get()
    c = underline_var.get()

    if c == 1:
        if a == 0:
            if b == 0:
                text_sample.config(font=(current_font_family,current_font_size,'normal'))
                font_style = ('normal')
            elif b == 1:
                text_sample.config(font=(current_font_family,current_font_size,'italic'))
                font_style = ('italic')

        elif a == 1:
            if b == 0:
                text_sample.config(font=(current_font_family,current_font_size,'bold'))
                font_style = ('bold')
            elif b == 1:
                text_sample.config(font=(current_font_family,current_font_size, 'bold', 'italic'))
                font_style = ('bold', 'italic')

    elif c == 0 :
        if a == 0:
            if b == 0:
                text_sample.config(font=(current_font_family,current_font_size,'underline'))
                font_style = ('underline')
            elif b == 1:
                text_sample.config(font=(current_font_family,current_font_size,'italic', 'underline'))
                font_style = ('italic', 'underline')

        elif a == 1:
            if b == 0:
                text_sample.config(font=(current_font_family,current_font_size,'bold', 'underline'))
                font_style = ('bold', 'underline')
            elif b == 1:
                text_sample.config(font=(current_font_family,current_font_size, 'bold', 'italic', 'underline'))
                font_style = ('bold', 'italic', 'underline')

underline_check.bind("<Button-1>", change_underline)

##binding combobox with function
font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)

l = Label(f3, text="         Preview", font=("",11,""))
l.pack(pady=5, anchor=SW)

text_sample = Label(f3, bg="grey10", fg=f_color, font=(current_font_family,current_font_size,""), text="AaBbYyZz", width=50, height=50)
text_sample.pack(padx=40)

top4.mainloop()

##############################################    END    ##################################################
        


root.mainloop()