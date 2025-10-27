from tkinter import *

# -------------------- PASSWORD GENERATOR ----------------------- #


# ----------------------- SAVE PASSWORD -------------------------- #


# ----------------------- UI SETUP -------------------------- #
#GUI window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Canvas
logo_image = PhotoImage(file="./images/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)

#Label
label_website = Label(text="Website:")
label_user = Label(text="Email/Username:")
label_password = Label(text="Password:")

#Input
website_input = Entry()
user_input = Entry()
password_input = Entry()
#Button
generate_password_btn = Button(text="Generate Password")
save_password_btn = Button(text="Save")

#Elements position within grid system
canvas.grid(column=1, row=0)
label_website.grid(column=0, row=1)
label_user.grid(column=0, row=2)
label_password.grid(column=0, row=3)
website_input.grid(column=1, row=1, columnspan=2)
user_input.grid(column=1, row=2)
password_input.grid(column=1, row=3)
generate_password_btn.grid(column=2, row=3)
save_password_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()