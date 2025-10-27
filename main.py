from tkinter import *
import ctypes as ct
from tkinter import messagebox
import random

LABEL_WIDTH = 15
BG_COLOR = "#F2EAD3"
ACCENT_COLOR = "#202020"
FONT_NAME = "Arial"
YOUR_EMAIL = "test@mail.com"

# -------------------- PASSWORD GENERATOR ----------------------- #
def generate_password():
    pw_list = get_random_char()
    random.shuffle(pw_list)
    final_password = "".join(pw_list)
    print(final_password)

def get_random_char():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_numbers):
        password_list.append((random.choice(numbers)))

    for char in range(nr_symbols):
        password_list.append((random.choice(symbols)))

    return  password_list
# ----------------------- SAVE PASSWORD -------------------------- #
def save_password():
    website = website_name.get()
    user = user_name.get()
    pw = password.get()

    if website == "" or user == "" or pw == "":
        info_message = messagebox.showinfo(title=website, message="Oops, don´t leave any field empty.")
    else:
        is_ok_message = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {user}\nPassword: {password}\nDo you want to save it?"
        )
        if is_ok_message:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {user} | {pw} \n")
            website_input.delete(0, END)
            password_input.delete(0, END)

# ----------------------- UI SETUP -------------------------- #
#GUI window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)

#Canvas
logo_image = PhotoImage(file="./images/logo.png")
canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)

#Label
label_website = Label(text="Website:", width=LABEL_WIDTH, font=(FONT_NAME, 12, "bold"), fg=ACCENT_COLOR, bg=BG_COLOR, justify="right")
label_user = Label(text="Email/Username:", width=LABEL_WIDTH, font=(FONT_NAME, 12, "bold"), fg=ACCENT_COLOR, bg=BG_COLOR, justify="right")
label_password = Label(text="Password:", width=LABEL_WIDTH, font=(FONT_NAME, 12, "bold"), fg=ACCENT_COLOR, bg=BG_COLOR, justify="right")

#Input
#Text variables for entries
website_name = StringVar()
user_name = StringVar()
password = StringVar()

website_input = Entry(width=53, textvariable=website_name)
website_input.focus()
user_input = Entry(width=53, textvariable=user_name)
user_input.insert(0, YOUR_EMAIL)
password_input = Entry(width=32, textvariable=password)

#Button
generate_password_btn = Button(text="Generate Password", highlightthickness=0, bg=ACCENT_COLOR, fg="white", font=(FONT_NAME, 10), command=generate_password)
save_password_btn = Button(text="Save", width=39, highlightthickness=0, bg=ACCENT_COLOR, fg="white", font=(FONT_NAME, 10), command=save_password)

#Elements position within grid system
canvas.grid(column=1, row=0)

label_website.grid(column=0, row=1)
label_user.grid(column=0, row=2)
label_password.grid(column=0, row=3)

website_input.grid(column=1, row=1, columnspan=2)
user_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)

generate_password_btn.grid(column=2, row=3)
save_password_btn.grid(column=1, row=4, columnspan=2)

#Customize title bar of tk window
def customize_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                         ct.sizeof(value))

customize_title_bar(window)
window.mainloop()