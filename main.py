import json
import os
import matplotlib.pyplot as plt
from tabulate import tabulate

DATA_FILE = "expenses.json"

# ---------------- Core Functions ---------------- #

def load_expenses():
    """Load expenses from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(category, amount, date):
    """Add a new expense (category, amount, date)."""
    expenses = load_expenses()
    expenses.append({"category": category, "amount": float(amount), "date": date})
    save_expenses(expenses)
    return expenses

def summarize_expenses():
    """Return a dict with categories as keys and total amounts as values."""
    expenses = load_expenses()
    summary = {}
    for expense in expenses:
        summary[expense["category"]] = summary.get(expense["category"], 0) + float(expense["amount"])
    return summary

def expenses_over_time():
    """Return a dict with dates as keys and total expenses per date as values."""
    expenses = load_expenses()
    daily_totals = {}
    for expense in expenses:
        date = expense["date"]
        amount = float(expense["amount"])
        daily_totals[date] = daily_totals.get(date, 0) + amount
    return dict(sorted(daily_totals.items(), key=lambda x: x[0]))

# ---------------- Visualization ---------------- #

def visualize_expenses():
    """Create bar, pie, and line charts for expenses."""
    summary = summarize_expenses()
    if not summary:
        print("No data to visualize.")
        return

    categories = list(summary.keys())
    amounts = list(summary.values())

    # --- Bar Chart ---
    plt.figure(figsize=(6, 4))
    plt.bar(categories, amounts, color="skyblue")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("expenses_bar.png")
    plt.show()

    # --- Pie Chart ---
    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Expense Distribution")
    plt.tight_layout()
    plt.savefig("expenses_pie.png")
    plt.show()

    # --- Line Chart ---
    daily_totals = expenses_over_time()
    if daily_totals:
        dates = list(daily_totals.keys())
        totals = list(daily_totals.values())
        plt.figure(figsize=(7, 4))
        plt.plot(dates, totals, marker="o", linestyle="-", color="green")
        plt.title("Expenses Over Time")
        plt.xlabel("Date")
        plt.ylabel("Total Amount")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.savefig("expenses_line.png")
        plt.show()

# ---------------- CLI ---------------- #

def main():
    while True:
        print("\n=== Hostel Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Visualize Expenses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Category: ")
            amount = input("Amount: ")
            date = input("Date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
            print("✅ Expense added!")

        elif choice == "2":
            expenses = load_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                table = [[e["date"], e["category"], e["amount"]] for e in expenses]
                headers = ["Date", "Category", "Amount"]
                print(tabulate(table, headers, tablefmt="grid"))

        elif choice == "3":
            summary = summarize_expenses()
            if not summary:
                print("No expenses recorded yet.")
            else:
                print("\nExpense Summary by Category:")
                for cat, amt in summary.items():
                    print(f"- {cat}: {amt:.2f}")

        elif choice == "4":
            visualize_expenses()

        elif choice == "5":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please select 1–5.")


if __name__ == "__main__":
    main()
