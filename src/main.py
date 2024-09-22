import customtkinter as ctk


# window config
root = ctk.CTk()
root.geometry("400x400")
root.title("todolist")
# root.iconbitmap("")




# textbox frame
textbox_frame = ctk.CTkFrame(root,width=400)
textbox_frame.pack(pady=10)


textbox = ctk.CTkTextbox(textbox_frame,width=300)
textbox.pack()

tasks = ["walk the dog","buy groceries","pay for coffee"]

for item in tasks:
  textbox.insert(ctk.END,item)

#scrollbar = ctk.CTkScrollbar(textbox)
#scrollbar.pack(side=ctk.RIGHT)



# entry frame
entry_frame = ctk.CTkFrame(root,
                           height=40,width=300)
entry_frame.pack(pady=10)

# entry field
entry = ctk.CTkEntry(entry_frame,
                     placeholder_text="type your task here",
                     height=40,width=300)
entry.pack()


button_frame = ctk.CTkFrame(root,
                            width=300,height=40)
button_frame.pack()

# buttons
add_button = ctk.CTkButton(button_frame,
                           text="Add task",
                           fg_color="#495057",
                           hover_color="#343a40")

add_button.pack(side=ctk.LEFT,padx=5)


delete_button = ctk.CTkButton(button_frame,
                              text="Delete task",
                              fg_color="#495057",
                              hover_color="#343a40")

delete_button.pack(side=ctk.LEFT,padx=5)

# functions
def add_task():
    pass
   


def delete_task():
    pass

# window loop
if __name__ == "__main__":
    root.mainloop()

