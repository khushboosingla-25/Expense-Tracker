import tkinter as tk
from tkinter import ttk, StringVar, DoubleVar
import ttkbootstrap as tb
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
from tkinter import filedialog, messagebox

# WINDOW 
app = tb.Window(themename="cyborg")   # changed theme
app.title("Expense Tracker")
app.geometry("1000x650")

# FRAMES 
frame_add = tb.Frame(app, bootstyle="info")
frame_add.place(relx=0.02, rely=0.02, relwidth=0.46, relheight=0.40)

frame_table = tb.Frame(app, bootstyle="success")
frame_table.place(relx=0.50, rely=0.02, relwidth=0.48, relheight=0.40)

frame_pie = tb.Frame(app, bootstyle="secondary")
frame_pie.place(relx=0.02, rely=0.44, relwidth=0.46, relheight=0.40)

frame_summary = tb.Frame(app, bootstyle="dark")
frame_summary.place(relx=0.50, rely=0.44, relwidth=0.48, relheight=0.52)

# All VARIABLES
categories = [
    "Food🍕", "Transport🚗", "Medical😷", "Bills💸",
    "Education📖", "Utilities🛒", "Others💲"
]


date_var = StringVar(value=datetime.now().strftime("%Y-%m-%d"))
cat_var = StringVar()
amt_var = StringVar()
desc_var = StringVar()

monthly_budget = 5000.0
budget_var = StringVar(value=str(int(monthly_budget)))

total_expense_var = StringVar(value="₹0.00")
remaining_budget_var = StringVar(value=f"₹{monthly_budget:.2f}")
usage_percent_var = DoubleVar(value=0.0)

# Add expense frame
ttk.Label(
    frame_add, text="Add Expense",
    font=("Segoe UI", 16, "bold"), bootstyle="inverse-info"
).grid(row=0, column=0, columnspan=2, pady=(8, 10), padx=10, sticky="w")

ttk.Label(frame_add, text="Date").grid(row=1, column=0, padx=12, pady=5, sticky="e")
ttk.Entry(frame_add, textvariable=date_var, width=18).grid(
    row=1, column=1, padx=12, pady=5, sticky="w"
)

ttk.Label(frame_add, text="Category").grid(row=2, column=0, padx=12, pady=5, sticky="e")
ttk.Combobox(
    frame_add, textvariable=cat_var, values=categories,
    state="readonly", width=16
).grid(row=2, column=1, padx=12, pady=5, sticky="w")

ttk.Label(frame_add, text="Amount").grid(row=3, column=0, padx=12, pady=5, sticky="e")
ttk.Entry(frame_add, textvariable=amt_var, width=18).grid(
    row=3, column=1, padx=12, pady=5, sticky="w"
)

ttk.Label(frame_add, text="Description").grid(row=4, column=0, padx=12, pady=5, sticky="e")
ttk.Entry(frame_add, textvariable=desc_var, width=18).grid(
    row=4, column=1, padx=12, pady=5, sticky="w"
)

# Tabel frame
ttk.Label(
    frame_table, text="Expenses",
    font=("Segoe UI", 14, "bold"), bootstyle="inverse-success"
).grid(row=0, column=0, padx=8, pady=(8, 4), sticky="w")

columns = ["date", "category", "amount", "description"]
tree = ttk.Treeview(
    frame_table, columns=columns, show="headings",
    height=10, bootstyle="success"
)
for col, txt, w in [
    ("date", "Date", 100),
    ("category", "Category", 120),
    ("amount", "Amount", 80),
    ("description", "Description", 140),
]:
    tree.heading(col, text=txt)
    tree.column(col, width=w)

tree.grid(row=1, column=0, sticky="nsew", padx=8, pady=(0, 4))
frame_table.grid_rowconfigure(1, weight=1)
frame_table.grid_columnconfigure(0, weight=1)

ttk.Button(
    frame_table, text="Delete Selected",
    bootstyle="danger", command=lambda: delete_selected()
).grid(row=2, column=0, sticky="ew", padx=8, pady=(4, 8))

# functions
def get_category_totals():
    totals = {}
    for row_id in tree.get_children():
        vals = tree.item(row_id)["values"]
        if len(vals) < 3:
            continue
        cat = vals[1]
        try:
            amt = float(vals[2])
        except ValueError:
            amt = 0.0
        totals[cat] = totals.get(cat, 0.0) + amt
    return totals

# pie chart
ttk.Label(
    frame_pie, text="Spending Breakdown",
    font=("Segoe UI", 14, "bold"), bootstyle="inverse-warning"
).pack(anchor="nw", padx=10, pady=(8, 0))

def update_pie_chart():
    totals = get_category_totals()
    fig, ax = plt.subplots(figsize=(3.4, 2.8), dpi=80)
    ax.clear()
    if totals:
        labels = list(totals.keys())
        sizes = list(totals.values())
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    else:
        ax.text(0.5, 0.5, "No data", ha="center", va="center")
    if hasattr(update_pie_chart, "canvas"):
        update_pie_chart.canvas.get_tk_widget().destroy()
    update_pie_chart.canvas = FigureCanvasTkAgg(fig, master=frame_pie)
    update_pie_chart.canvas.get_tk_widget().pack(expand=True, padx=10, pady=6)
    plt.close(fig)

# summary frame
ttk.Label(
    frame_summary, text="Budget Summary",
    font=("Segoe UI", 16, "bold"), bootstyle="inverse-danger"
).grid(row=0, column=0, columnspan=3, sticky="w", padx=12, pady=(8, 10))

ttk.Label(frame_summary, text="Monthly Budget:").grid(
    row=1, column=0, sticky="w", padx=12, pady=4
)
ttk.Entry(frame_summary, textvariable=budget_var, width=10).grid(
    row=1, column=1, sticky="w", padx=4, pady=4
)

def apply_global_budget():
    global monthly_budget
    try:
        monthly_budget = float(budget_var.get())
    except ValueError:
        monthly_budget = 0.0
        budget_var.set("0")
    update_stats()

ttk.Button(
    frame_summary, text="Set Budget",
    bootstyle="info", command=apply_global_budget
).grid(row=1, column=2, padx=4, pady=4, sticky="w")

ttk.Label(frame_summary, text="Total Expense:").grid(
    row=2, column=0, sticky="w", padx=12, pady=4
)
ttk.Label(frame_summary, textvariable=total_expense_var).grid(
    row=2, column=1, sticky="w", padx=4, pady=4
)

ttk.Label(frame_summary, text="Remaining Budget:").grid(
    row=3, column=0, sticky="w", padx=12, pady=4
)
ttk.Label(frame_summary, textvariable=remaining_budget_var).grid(
    row=3, column=1, sticky="w", padx=4, pady=4
)

ttk.Label(frame_summary, text="Budget Usage (%):").grid(
    row=4, column=0, sticky="w", padx=12, pady=4
)
ttk.Label(frame_summary, textvariable=usage_percent_var).grid(
    row=4, column=1, sticky="w", padx=4, pady=4
)

progress = ttk.Progressbar(
    frame_summary, orient="horizontal", length=260,
    mode="determinate", maximum=100,
    variable=usage_percent_var, style="success.Horizontal.TProgressbar"
)
progress.grid(row=5, column=0, columnspan=3, padx=12, pady=8, sticky="w")

#STATS 
def update_stats():
    total = 0.0
    for row_id in tree.get_children():
        vals = tree.item(row_id)["values"]
        if len(vals) < 3:
            continue
        try:
            amt = float(vals[2])
        except ValueError:
            amt = 0.0
        total += amt

    total_expense_var.set(f"₹{total:.2f}")
    if monthly_budget > 0:
        remaining = max(0.0, monthly_budget - total)
        percent = (total / monthly_budget) * 100
    else:
        remaining = 0.0
        percent = 0.0

    remaining_budget_var.set(f"₹{remaining:.2f}")
    usage_percent_var.set(round(percent, 1))

    if percent > 100:
        progress.configure(style="danger.Horizontal.TProgressbar")
    else:
        progress.configure(style="success.Horizontal.TProgressbar")

# CSV
def save_to_csv():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save as"
    )
    if not file_path:
        return
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for row_id in tree.get_children():
            writer.writerow(tree.item(row_id)["values"])
    messagebox.showinfo("Saved", f"Expenses saved to {file_path}")

def load_from_csv():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Open"
    )
    if not file_path:
        return
    for row_id in tree.get_children():
        tree.delete(row_id)
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tree.insert(
                "", "end",
                values=(row["Date"], row["Category"], row["Amount"], row["Description"])
            )
    update_pie_chart()
    update_stats()

# Add and delete
def add_expense():
    if not amt_var.get().strip():
        messagebox.showerror("Error", "Amount is required.")
        return
    try:
        float(amt_var.get())
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    tree.insert(
        "", "end",
        values=(date_var.get(), cat_var.get(), amt_var.get(), desc_var.get())
    )
    update_pie_chart()
    update_stats()

def delete_selected():
    for item in tree.selection():
        tree.delete(item)
    update_pie_chart()
    update_stats()

# buttons
ttk.Button(
    frame_add, text="Add Expense",
    bootstyle="success", command=add_expense
).grid(row=5, column=0, columnspan=2, padx=12, pady=(8, 4), sticky="ew")

ttk.Button(
    frame_add, text="Save CSV",
    bootstyle="info", command=save_to_csv
).grid(row=6, column=0, padx=12, pady=(4, 6), sticky="ew")

ttk.Button(
    frame_add, text="Load CSV",
    bootstyle="primary", command=load_from_csv
).grid(row=6, column=1, padx=12, pady=(4, 6), sticky="ew")


update_pie_chart()
update_stats()

app.mainloop()