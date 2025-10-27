from tkinter import *
import ctypes as ct

LABEL_WIDTH = 15
BG_COLOR = "#F2EAD3"
ACCENT_COLOR = "#202020"
FONT_NAME = "Arial"

# -------------------- PASSWORD GENERATOR ----------------------- #


# ----------------------- SAVE PASSWORD -------------------------- #


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
website_input = Entry(width=53)
user_input = Entry(width=53)
password_input = Entry(width=32)
#Button
generate_password_btn = Button(text="Generate Password", highlightthickness=0, bg=ACCENT_COLOR, fg="white", font=(FONT_NAME, 10))
save_password_btn = Button(text="Save", width=39, highlightthickness=0, bg=ACCENT_COLOR, fg="white", font=(FONT_NAME, 10))

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