import customtkinter as ctk
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Sign Up Page",
    user="postgres",
    password="123456"
)

cursor = conn.cursor()

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sign Up")
app.geometry("450x650")
app.resizable(False, False)

# Title
title = ctk.CTkLabel(
    app,
    text="Create Account",
    font=ctk.CTkFont(size=24, weight="bold")
)
title.pack(pady=(30, 20))

# Frame
frame = ctk.CTkFrame(app)
frame.pack(padx=40, pady=10, expand=True, fill="both")

# Name
name_label = ctk.CTkLabel(frame, text="Full Name", font=ctk.CTkFont(size=13))
name_label.pack(anchor="w", padx=20, pady=(15, 0))

name_entry = ctk.CTkEntry(frame, placeholder_text="Enter your name", width=350)
name_entry.pack(padx=20, pady=(5, 0))

# Email
email_label = ctk.CTkLabel(frame, text="Email", font=ctk.CTkFont(size=13))
email_label.pack(anchor="w", padx=20, pady=(15, 0))

email_entry = ctk.CTkEntry(frame, placeholder_text="Enter your mail", width=350)
email_entry.pack(padx=20, pady=(5, 0))

# Gender
gender_label = ctk.CTkLabel(frame, text="Gender", font=ctk.CTkFont(size=13))
gender_label.pack(anchor="w", padx=20, pady=(15, 0))

gender_var = ctk.StringVar(value="Female")

gender_frame = ctk.CTkFrame(frame, fg_color="transparent")
gender_frame.pack(anchor="w", padx=20)

ctk.CTkRadioButton(
    gender_frame,
    text="Male",
    variable=gender_var,
    value="Male"
).pack(side="left", padx=(0, 15))

ctk.CTkRadioButton(
    gender_frame,
    text="Female",
    variable=gender_var,
    value="Female"
).pack(side="left", padx=(0, 15))

ctk.CTkRadioButton(
    gender_frame,
    text="Others",
    variable=gender_var,
    value="Others"
).pack(side="left")

# City
city_label = ctk.CTkLabel(frame, text="City", font=ctk.CTkFont(size=13))
city_label.pack(anchor="w", padx=20, pady=(15, 0))

city_entry = ctk.CTkEntry(frame, placeholder_text="Enter your City", width=350)
city_entry.pack(padx=20, pady=(5, 0))

# Pincode
pincode_label = ctk.CTkLabel(frame, text="Pincode", font=ctk.CTkFont(size=13))
pincode_label.pack(anchor="w", padx=20, pady=(15, 0))

pincode_entry = ctk.CTkEntry(frame, placeholder_text="Enter your Pincode", width=350)
pincode_entry.pack(padx=20, pady=(5, 0))


# Submit function
def submit():
    name = name_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    city = city_entry.get()
    pincode = pincode_entry.get()

    if not all([name, email, city, pincode]):
        result_label.configure(
            text="⚠️ Please fill all fields!",
            text_color="red"
        )
        return

    try:
        cursor.execute(
            """
            INSERT INTO users
            (full_name, email, gender, city, pincode)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (name, email, gender, city, pincode)
        )

        conn.commit()

        result_label.configure(
            text=f"✅ Registered: {name} | {email} | {gender} | {city} | {pincode}",
            text_color="green"
        )

    except Exception as e:
        result_label.configure(
            text=f"Error: {e}",
            text_color="red"
        )


# Submit Button
ctk.CTkButton(
    frame,
    text="Sign Up",
    width=350,
    height=40,
    font=ctk.CTkFont(size=14, weight="bold"),
    command=submit
).pack(padx=20, pady=(25, 10))

# Result label
result_label = ctk.CTkLabel(
    frame,
    text="",
    font=ctk.CTkFont(size=11),
    wraplength=340
)
result_label.pack(pady=(0, 15))

app.mainloop()