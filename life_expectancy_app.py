import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# ── Load Data ──────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "nsp_life_expectancy_work.xlsx")

age_ranges = [
    (0,   0,   63.28),
    (1,   4,   65.26),
    (5,   9,   62.14),
    (10,  14,  57.61),
    (15,  19,  52.92),
    (20,  24,  48.50),
    (25,  29,  44.29),
    (30,  34,  40.02),
    (35,  39,  35.72),
    (40,  44,  31.32),
    (45,  49,  27.13),
    (50,  54,  23.07),
    (55,  59,  19.31),
    (60,  64,  15.71),
    (65,  69,  12.54),
    (70,  74,   9.88),
    (75,  79,   7.92),
    (80, 120,   7.40),
]

def get_life_expectancy(age):
    for lower, upper, expectancy in age_ranges:
        if lower <= age <= upper:
            return expectancy
    return None

# ── App Logic ──────────────────────────────────────────────────────
def check_expectancy():
    user_input = age_entry.get().strip()

    if not user_input.isdigit():
        result_label.config(text="⚠ Please enter a valid whole number.", fg="#e74c3c")
        return

    age = int(user_input)

    if age < 0 or age > 120:
        result_label.config(text="⚠ Please enter an age between 0 and 120.", fg="#e74c3c")
        return

    result = get_life_expectancy(age)

    if result is not None:
        result_label.config(
            text=f"✅ At age {age}, you have a life\nexpectancy of {result} more years.",
            fg="#27ae60"
        )
    else:
        result_label.config(text="⚠ Could not find data for that age.", fg="#e74c3c")

def clear_input():
    age_entry.delete(0, tk.END)
    result_label.config(text="", fg="#50492c")
    age_entry.focus()

# ── Build GUI ──────────────────────────────────────────────────────
root = tk.Tk()
root.title("Life Expectancy App")
root.geometry("480x520")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# ── Header ─────────────────────────────────────────────────────────
header_frame = tk.Frame(root, bg="#1a3c5e", pady=20)
header_frame.pack(fill="x")

tk.Label(
    header_frame,
    text="🏥 Life Expectancy",
    font=("Georgia", 22, "bold"),
    bg="#1a3c5e",
    fg="white"
).pack()

tk.Label(
    header_frame,
    text="National · Males · 2021 PHC Model Life Table",
    font=("Georgia", 10),
    bg="#1a3c5e",
    fg="#a8c8e8"
).pack(pady=(4, 0))

# ── Main Card ──────────────────────────────────────────────────────
card = tk.Frame(root, bg="white", bd=0, relief="flat", padx=30, pady=30)
card.pack(padx=30, pady=30, fill="both", expand=True)

tk.Label(
    card,
    text="Enter Your Age",
    font=("Georgia", 13, "bold"),
    bg="white",
    fg="#1a3c5e"
).pack(anchor="w")

tk.Label(
    card,
    text="Enter a whole number between 0 and 120",
    font=("Georgia", 9),
    bg="white",
    fg="#7f8c8d"
).pack(anchor="w", pady=(2, 10))

# Age input box
age_entry = tk.Entry(
    card,
    font=("Georgia", 18),
    width=10,
    bd=2,
    relief="groove",
    justify="center",
    fg="#1a3c5e"
)
age_entry.pack(pady=(0, 20))
age_entry.focus()

# Bind Enter key
root.bind("<Return>", lambda event: check_expectancy())

# Buttons
btn_frame = tk.Frame(card, bg="white")
btn_frame.pack()

check_btn = tk.Button(
    btn_frame,
    text="Check",
    font=("Georgia", 12, "bold"),
    bg="#1a3c5e",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white",
    width=10,
    bd=0,
    pady=8,
    cursor="hand2",
    command=check_expectancy
)
check_btn.grid(row=0, column=0, padx=(0, 10))

clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    font=("Georgia", 12),
    bg="#ecf0f1",
    fg="#2c3e50",
    activebackground="#bdc3c7",
    width=10,
    bd=0,
    pady=8,
    cursor="hand2",
    command=clear_input
)
clear_btn.grid(row=0, column=1)

# Divider
tk.Frame(card, bg="#ecf0f1", height=2).pack(fill="x", pady=20)

# Result label
result_label = tk.Label(
    card,
    text="",
    font=("Georgia", 13, "bold"),
    bg="white",
    fg="#27ae60",
    wraplength=360,
    justify="center"
)
result_label.pack()

# ── Footer ─────────────────────────────────────────────────────────
tk.Label(
    root,
    text="Source: Ghana Statistical Service · 2021 Population & Housing Census",
    font=("Georgia", 8),
    bg="#f0f4f8",
    fg="#95a5a6"
).pack(pady=(0, 10))

root.mainloop()
