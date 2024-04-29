import customtkinter as ct
import os

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")
root = ct.CTk()
root.geometry("500x500")
frame = ct.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ct.CTkLabel(master=frame, text="Minecraft Server", font=("Roboto", 24))
label.pack(pady=12, padx=10)




inputmb = ct.CTkEntry(master=frame, placeholder_text="MB Ram")
inputmb.pack(pady=12, padx=10)
button = ct.CTkButton(
    master=frame,
    text="Start Server",
    command=lambda: os.system(f"java -Xmx{inputmb.get()}M -Xms{inputmb.get()}M -jar server.jar"),
)
button.pack(pady=12, padx=10)

label_ter = ct.CTkLabel(master=frame, text=f'')
root.mainloop()
