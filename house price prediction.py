import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ===== Load and prepare the dataset =====
data = pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\PythonProject\train.csv")
features = ["GrLivArea", "BedroomAbvGr", "FullBath"]
target = "SalePrice"

X = data[features]
y = data[target]

model = LinearRegression()
model.fit(X, y)

def predict_price():
    try:
        sqft = int(entry_sqft.get())
        bedrooms = int(entry_bedrooms.get())
        bathrooms = int(entry_bathrooms.get())

        input_data = [[sqft, bedrooms, bathrooms]]
        predicted_price = model.predict(input_data)[0]
        price_2025 = predicted_price * 8.5

        result_label.config(
            text=f"No of square feet: {sqft}\n"
                 f"No of bedrooms: {bedrooms}\n"
                 f"No of bathrooms: {bathrooms}\n"
                 f"Predicted Price (2025): ₹ {int(price_2025):,}"
        )
    except Exception:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# ===== Colors & Fonts =====
LABEL_FG = "#333333"
ENTRY_BG = "#FFFFFF"
ENTRY_FG = "#000000"
BUTTON_BG = "#1976D2"
BUTTON_FG = "#FFFFFF"
RESULT_FG = "#D32F2F"

label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# ===== Tkinter Window =====
root = tk.Tk()
root.title("House Price Predictor 2025")
root.geometry("900x500")

# ===== Load and set background image =====
bg_image_path = r"C:\Users\Lenovo\PycharmProjects\PythonProject\apartment.jpg"
bg_image = Image.open(bg_image_path).resize((900, 500), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ===== Center Frame (light colored) =====
center_frame = tk.Frame(root, bg="#FAFAFA", bd=2, relief="ridge")
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# ===== Widgets =====
tk.Label(center_frame, text="Enter Square Feet:", bg="#FAFAFA", fg=LABEL_FG, font=label_font).pack(pady=3)
entry_sqft = tk.Entry(center_frame, font=entry_font, bg=ENTRY_BG, fg=ENTRY_FG)
entry_sqft.pack()

tk.Label(center_frame, text="Enter Number of Bedrooms:", bg="#FAFAFA", fg=LABEL_FG, font=label_font).pack(pady=3)
entry_bedrooms = tk.Entry(center_frame, font=entry_font, bg=ENTRY_BG, fg=ENTRY_FG)
entry_bedrooms.pack()

tk.Label(center_frame, text="Enter Number of Bathrooms:", bg="#FAFAFA", fg=LABEL_FG, font=label_font).pack(pady=3)
entry_bathrooms = tk.Entry(center_frame, font=entry_font, bg=ENTRY_BG, fg=ENTRY_FG)
entry_bathrooms.pack()

tk.Button(
    center_frame,
    text="Predict Price",
    command=predict_price,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground="#2196F3",
    activeforeground="#FFFFFF",
    font=button_font
).pack(pady=8)

# ===== Result Label =====
result_label = tk.Label(center_frame, text="", bg="#FAFAFA", fg=RESULT_FG, font=label_font, justify="left")
result_label.pack()

root.mainloop()

