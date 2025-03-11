import qrcode
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox


def generate_qr():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer un lien valide")
        return
    
    fill_color = fill_color_var.get()
    back_color = back_color_var.get()
    
    qr = qrcode.QRCode(
        version=3,
        box_size=10,
        border=5
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Succès", f"QR Code enregistré sous {save_path}")


def choose_fill_color():
    color = colorchooser.askcolor(title="Choisir la couleur du QR code")[1]
    if color:
        fill_color_var.set(color)


def choose_back_color():
    color = colorchooser.askcolor(title="Choisir la couleur de fond")[1]
    if color:
        back_color_var.set(color)


# Interface Graphique
root = tk.Tk()
root.title("Générateur de QR Code")
root.geometry("400x300")

welcome_label = tk.Label(root, text="Bienvenue ! Entrez un lien pour générer un QR Code", font=("Arial", 12))
welcome_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

fill_color_var = tk.StringVar(value="black")
back_color_var = tk.StringVar(value="white")

tk.Button(root, text="Choisir couleur QR", command=choose_fill_color).pack(pady=5)
tk.Button(root, text="Choisir couleur fond", command=choose_back_color).pack(pady=5)
tk.Button(root, text="Générer QR Code", command=generate_qr).pack(pady=10)

root.mainloop()