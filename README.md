# 💰 Expense Tracker

A simple desktop-based **Expense Tracker** built with Python and Tkinter to help users record, manage, categorize, and analyze their daily expenses.

The application provides a clean interface for tracking spending, setting category-wise budgets, and viewing expense summaries through charts.

## ✨ Features

* ➕ Add and record expenses
* 📝 Manage expense details such as:

  * Date
  * Category
  * Amount
  * Description
* 🗂️ Categorize expenses into:

  * Food
  * Medical
  * Utilities
  * Education
  * Others
* 💰 Set budgets for different expense categories
* 📊 Visualize spending using charts
* 📋 View recorded expenses in a structured table
* 🔎 Easily review and monitor spending patterns
* 🖥️ Simple desktop GUI using Tkinter

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – Graphical User Interface
* **ttkbootstrap** – Modern UI styling
* **Pandas** – Data handling and processing
* **Matplotlib** – Data visualization
* **CSV** – Local expense data storage

## 📂 Project Structure

```text
Expense-Tracker/
│
├── main.py
├── expenses.csv
├── requirements.txt
├── README.md
└── screenshots/
    └── dashboard.png
```

> The exact file structure may vary depending on the final project implementation.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/expense-tracker.git
```

### 2. Navigate to the project directory

```bash
cd expense-tracker
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

## 📊 How It Works

The application follows a simple workflow:

```text
User
  ↓
Enter Expense Details
  ↓
Select Category
  ↓
Save Expense
  ↓
Store Expense Data
  ↓
View / Analyze Expenses
  ↓
Charts & Budget Monitoring
```

## 🗃️ Expense Categories

| Category  | Examples                        |
| --------- | ------------------------------- |
| Food      | Groceries, meals, snacks        |
| Medical   | Medicines, consultations        |
| Utilities | Electricity, internet, bills    |
| Education | Books, courses, stationery      |
| Others    | Travel, shopping, miscellaneous |

## 📈 Data Visualization

The application uses **Matplotlib** to provide visual representations of spending, making it easier to identify which categories contribute most to overall expenses.

## 🧩 Data Flow

```text
          ┌──────────┐
          │   User   │
          └────┬─────┘
               │
               ▼
      ┌─────────────────┐
      │ Expense Tracker │
      │      GUI        │
      └────────┬────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
┌──────────────┐  ┌───────────────┐
│ Expense Data │  │ Budget Data   │
└──────┬───────┘  └───────┬───────┘
       │                  │
       └────────┬─────────┘
                ▼
       ┌─────────────────┐
       │ Analysis &      │
       │ Visualization   │
       └─────────────────┘
```

## 🎯 Project Objectives

* Develop a practical desktop application using Python.
* Provide an easy way to maintain personal expense records.
* Organize expenses into meaningful categories.
* Help users understand their spending patterns.
* Apply Python concepts such as GUI development, file handling, data processing, and visualization.

## 🚀 Future Improvements

* 🔐 User authentication
* ☁️ Cloud-based data storage
* 📱 Mobile version
* 📊 Advanced financial analytics
* 📅 Monthly and yearly reports
* 📄 Export reports to PDF/Excel
* 🔔 Budget-limit notifications
* 🗄️ Migration from CSV to a relational database

## 👩‍💻 Author

**Khushboo Singla**

B.Tech — Computer Science & Engineering

---

⭐ If you found this project useful, consider giving the repository a star!
