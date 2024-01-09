import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

def display_tab_content(tab_num):
    selected_value = int(selected_option[tab_num-1].get())
    image_path = image_paths[tab_num-1][selected_value-1]
    
    # Close the last opened image window
    if hasattr(display_tab_content, 'last_image_window') and display_tab_content.last_image_window:
        display_tab_content.last_image_window.destroy()

    # Open a new Toplevel window for image display
    image_window = tk.Toplevel(root)
    image_window.title(f"Image Display - {image_path}")
    display_tab_content.last_image_window = image_window
    
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(image_window, image=photo)
    image_label.image = photo
    image_label.pack()

def show_random_number():
    random_num = random.randint(1, 100)
    random_button.config(text=f"Rand: {random_num} %")

root = tk.Tk()
root.title("Tipton")
root.iconbitmap("mush_small.ico")

# Set the size of the window
root.geometry("250x600")  # Width x Height

# Create a Notebook widget
notebook = ttk.Notebook(root)

# Create tabs
tabs = []
selected_option = []
image_paths = [
    ["7_SB_open_jam.png", "7_SB_limp.png", "7_SB_limp_fold.png", "7_SB_limp_call.png", "7_BB_jam_facing_limp.png", "7_BB_check_facing_limp.png", "7_BB_minraise_facing_limp.png", "7_BB_call_facing_open_jam.png"],
    ["10_SB_limp.png", "10_SB_limp_call.png", "10_SB_limp_fold.png", "10_SB_open_jam.png", "10_BB_jam_facing_limp.png", "10_BB_minraise_facing_limp.png", "10_BB_check_facing_limp.png", "10_BB_call_facing_open_jam.png"],
    ["15_SB_limp.png", "15_SB_minraise.png", "15_SB_open_jam.png", "15_SB_open_fold.png", "15_SB_minraise_call_jam.png", "15_SB_limp_call_all_in.png", "15_BB_minraise_facing_limp.png", "15_BB_jam_facing_minraise.png", "15_BB_jam_facing_limp.png", "15_BB_call_facing_open_jam.png", "15_BB_call_facing_minraise.png", "15_BB_3bet_to_4bb.png"],
    ["20_SB_open_jam.png", "20_SB_open_fold.png", "20_SB_minraise_call_jam.png", "20_SB_minraise.png", "20_SB_limp.png", "20_SB_limp_call_all_in.png", "20_BB_raise_limp_to_2_5bb.png", "20_BB_jam_facing_minraise.png", "20_BB_jam_facing_limp.png", "20_BB_call_facing_open_jam.png", "20_BB_call_facing_minraise.png", "20_BB_3bet_to_4_5bb.png"]
]

image_labels = []

for i in range(1, 5):
    bb = 0
    tab = ttk.Frame(notebook)
    tabs.append(tab)
    if i == 1:
        bb = 7
    elif i == 2:
        bb = 10
    elif i == 3:
        bb = 15
    else:
        bb = 20
    notebook.add(tab, text=f'{bb} BB')

    # Create radio buttons within each tab
    selected_option.append(tk.StringVar(value="0"))

    for j, img_option in enumerate(image_paths[i-1], start=1):
        img_option_no_extension = img_option.rsplit('.', 1)[0]  # Remove the .png extension
        radio_button = tk.Radiobutton(tab, text=img_option_no_extension, variable=selected_option[-1], value=str(j),
                                      command=lambda t=i, v=j: display_tab_content(t))
        radio_button.grid(row=j-1, column=0, pady=5, sticky="w")

# Pack the Notebook widget with fill set to 'both'
notebook.pack(expand=True, fill='both', padx=10, pady=10)

# Random number button at the bottom
random_button = tk.Button(root, text="Rand: 0 %", command=show_random_number)
random_button.pack(side="bottom", pady=10)

root.mainloop()
