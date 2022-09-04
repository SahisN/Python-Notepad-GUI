from tkinter import *
from datetime import datetime
from tkinter import filedialog, messagebox


# Functions
def font_selector():
    def apply_font():
        font = font_entry.get()
        style = style_entry.get()
        size = size_entry.get()

        if style == 'Default':
            style = ''

        else:
            style.lower()

        # text_field.config(width=600, height=600, font=('Arial', 10))
        text_field.config(font=(font, int(size), style.lower()))
        font_screen.destroy()

    def append_font_entry(event):

        font_entry.config(state='normal')
        font_entry.delete(0, END)
        selection = font_list.curselection()
        text = font_list.get(selection)
        font_entry.insert(0, text)
        font_entry.config(state='readonly')

    def append_style_entry(event):

        style_entry.config(state='normal')
        style_entry.delete(0, END)
        selection = style_list.curselection()
        text = style_list.get(selection)
        style_entry.insert(0, text)
        style_entry.config(state='readonly')

    def append_size_entry(event):

        size_entry.config(state='normal')
        size_entry.delete(0, END)
        selection = size_list.curselection()
        text = size_list.get(selection)
        size_entry.insert(0, text)
        size_entry.config(state='readonly')

    def set_default_text():
        font_entry.insert(0, 'Arial')
        style_entry.insert(0, 'Default')
        size_entry.insert(0, 14)

        font_entry.config(state='readonly')
        style_entry.config(state='readonly')
        size_entry.config(state='readonly')

    def generate_fontlist():

        list_of_fonts = ['Times New Roman', 'Verdana', 'Arial', 'Candara', 'Courier New CE', 'Impact', 'Ink Free',
                         'Chiller', 'Tw Cen MT Condensed', 'Tw Cen MT Condensed', 'Wingdings 2', 'Wingdings 3']

        index = 0
        for fonts in list_of_fonts:
            font_list.insert(index, fonts)
            index += 1

    def generate_sizelist():

        index = 0
        for sizes in range(2, 101, 2):
            size_list.insert(index, sizes)
            index += 1

    # Screen settings
    font_screen = Toplevel()
    font_screen.title('Font')
    geometry = font_screen.geometry('470x200')
    font_screen.resizable(False, False)
    # root.geometry(+x+y) will position window
    font_screen.geometry('+800+120')

    # Screen content

    # Screen frame
    frame = Frame(font_screen)
    frame.pack()

    # Labels
    font_label = Label(frame, text='Font')
    style_label = Label(frame, text='Style')
    size_label = Label(frame, text='Size')

    # Empty Labels - column
    empty_column = Label(frame, text=' ')
    empty_column_2 = Label(frame, text=' ')

    # Empty Labels - row
    empty_row = Label(frame)
    empty_row_2 = Label(frame)

    # Entry box
    font_entry = Entry(frame)
    style_entry = Entry(frame)
    size_entry = Entry(frame)
    set_default_text()

    # Listbox Scrollbars
    font_scrollbar = Scrollbar(frame)
    style_scrollbar = Scrollbar(frame)
    size_scrollbar = Scrollbar(frame)

    # List box
    font_list = Listbox(frame, selectmode=SINGLE, height=4, yscrollcommand=font_scrollbar.set)
    generate_fontlist()

    # Configure font list scrollbar
    font_scrollbar.config(command=font_list.yview)

    style_list = Listbox(frame, selectmode=SINGLE, height=4, yscrollcommand=style_scrollbar.set)
    style_list.insert(0, 'Default')
    style_list.insert(1, 'Bold')
    style_list.insert(2, 'Italic')
    style_list.insert(3, 'Bold Italic')

    # Configure style list scrollbar
    style_scrollbar.config(command=style_list.yview)

    size_list = Listbox(frame, selectmode=SINGLE, height=4, yscrollcommand=size_scrollbar.set)
    generate_sizelist()

    # Configure size list scrollbar
    size_scrollbar.config(command=size_list.yview)

    # Key binds
    font_list.bind('<ButtonRelease-1>', append_font_entry)
    style_list.bind('<ButtonRelease-1>', append_style_entry)
    size_list.bind('<ButtonRelease-1>', append_size_entry)

    # Buttons
    ok_button = Button(frame, text='Ok', highlightthickness=5, width=5, command=apply_font)
    cancel_button = Button(frame, text='Cancel', highlightthickness=5, width=5, command=font_screen.destroy)

    # Grid layout

    # Adding font labels
    font_label.grid(row=0, column=0)
    style_label.grid(row=0, column=2)
    size_label.grid(row=0, column=4)

    # Adding Empty columns
    empty_column.grid(row=0, column=1, padx=10)
    empty_column_2.grid(row=0, column=3, padx=10)

    # Adding Empty rows
    empty_row.grid(row=3, column=2)
    empty_row_2.grid(row=4, column=4)

    # Adding font entry
    font_entry.grid(row=1, column=0)
    style_entry.grid(row=1, column=2)
    size_entry.grid(row=1, column=4)

    # Adding list box
    font_list.grid(row=2, column=0)
    style_list.grid(row=2, column=2)
    size_list.grid(row=2, column=4)

    # Scrollbars
    font_scrollbar.grid(row=1, column=1, rowspan=2, sticky=N + S + W)
    style_scrollbar.grid(row=1, column=3, rowspan=2, sticky=N + S + W)
    size_scrollbar.grid(row=1, column=5, rowspan=2, sticky=N + S + W)

    # Adding Buttons
    ok_button.grid(row=5, column=2, sticky='e')
    cancel_button.grid(row=5, column=4, sticky='w')


def lock_edit():
    is_editable = edit_only.get()

    if is_editable:
        text_field.config(state=DISABLED)

    else:
        text_field.config(state=NORMAL)

    # text_field.config(state='readonly')


def date_time():
    fetch_time = datetime.now()
    current_time = fetch_time.strftime("%H:%M:%S")
    current_date = fetch_time.strftime('%x')

    text_field.insert('1.0', current_time + ' ' + current_date)


def wordwrap():
    wrap = word_wrap.get()

    if wrap:
        text_field.config(wrap=WORD)

    else:
        text_field.config(wrap=NONE)

    # text_field.config(wrap=TRUE)


def open_file(event=None):
    # Ask users to choose txt files from their directory
    file_extension = [('Text Documents', '*.txt'), ('Python File', '*.py')]
    open_file = filedialog.askopenfilename(title='Open', filetypes=file_extension, defaultextension=file_extension)

    # Confirms if user wants to open files
    if open_file != '':

        # open and read the files the user chose
        text_file = open(open_file, 'r')
        read_file = text_file.read()

        # Delete old contents and add new contents to the notepad
        text_field.delete('1.0', END)
        text_field.insert('1.0', read_file)

        # Close the file to prevent any data leaks or corruption
        text_file.close()

    else:
        pass


def new_file(event=None):
    user_input = messagebox.askyesnocancel('Notepad', 'Do you want to save?')

    if user_input:
        file_saved = save_file()

        if file_saved:
            clear_text()


    elif user_input is None:
        pass

    elif not user_input:
        text_field.delete('1.0', END)


def save_file(event=None):
    # Ask user to chose the save directory
    file_extension = [('Text Documents', '*.txt'), ('Python File', '*.py')]
    select_file = filedialog.asksaveasfilename(title="Save", filetypes=file_extension, defaultextension=file_extension)

    # Confirms if user wants to save
    if select_file != '':

        # Creates a file with all of content in the notepad where user chose
        save_file = open(select_file, 'w')
        save_file.write(text_field.get('1.0', END))

        # Close file to prevent data leaks
        save_file.close()

        return True

    else:
        pass


def clear_text():
    text_field.delete('1.0', END)


def exit():
    user_input = messagebox.askquestion('Notepad', 'Do you want to exit?')

    if user_input == 'yes':
        screen.destroy()

    else:
        pass


def copy():
    screen.clipboard_clear()
    screen.clipboard_append(text_field.get('1.0', END))


def paste():
    try:
        text_field.insert('1.0', screen.clipboard_get())

    except:
        pass


# Screen settings - title, size, icon, location
screen = Tk()
screen.title("NotePad")
screen.geometry('550x450+210+85')


# -- Screen Content --

# Frame 
frame = Frame(screen)
frame.pack()

# Specials Variables for menubars
edit_only = BooleanVar()
edit_only.set(False)

word_wrap = BooleanVar()
word_wrap.set(False)

# Menubar 
menu_bar = Menu(screen)
screen.config(menu=menu_bar)

# Creating menu files
file_menu = Menu(menu_bar, tearoff=False)
edit_menu = Menu(menu_bar, tearoff=False)
format = Menu(menu_bar, tearoff=False)

# File Menu Content - New, Open, Save, Exit
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit)

# Edit 
edit_menu.add_command(label='Copy Text', command=copy)
edit_menu.add_command(label='Paste Text', command=paste)
edit_menu.add_checkbutton(label='Read Only', onvalue=1, offvalue=0, variable=edit_only, command=lock_edit)
edit_menu.add_command(label='Date/Time', command=date_time)
edit_menu.add_command(label='Clear', command=clear_text)

# Format - Wordwrap, font selector
format.add_checkbutton(label='Wordwrap', onvalue=1, offvalue=0, variable=word_wrap, command=wordwrap)
format.add_command(label='Font', command=font_selector)

# Add File menus to the menu
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_cascade(label='Format', menu=format)

# Scrollbars - x
xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)

# Scrollbars - y
yscrollbar = Scrollbar(frame)
yscrollbar.pack(side=RIGHT, fill=Y)

# Text Field
text_field = Text(frame, borderwidth=3, relief=FLAT, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set,
                  wrap=NONE)

# Config textfield width=600, height=600, font=('Arial','10)
text_field.config(width=600, height=600, font=('Arial', 14))
text_field.pack()

# Scrollbar x and y configure
xscrollbar.config(command=text_field.xview)
yscrollbar.config(command=text_field.yview)

# Key binds
screen.bind_all('<Control-s>', save_file)
screen.bind_all('<Control-o>', open_file)
screen.bind_all('<Control-n>', new_file)

# Protocol for closing a window
screen.protocol("WM_DELETE_WINDOW", exit)


# Main loop
screen.mainloop()
