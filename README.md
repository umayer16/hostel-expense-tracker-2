# Hostel Expense Tracker
#### Video Demo:  :https://youtu.be/L37-Tu5f_9c?si=veHxtTKSITVpEYcz
#### Description:

The Hostel Expense Tracker is a Python-based application designed to help students and residents of hostels manage their daily expenses efficiently. Many students living away from home struggle to track their spending on meals, transportation, books, and other essentials. This project provides a simple, intuitive, and visual way to record expenses, summarize them by category, and visualize spending patterns over time.

The core of the project is implemented in `project.py`, which contains the `main()` function along with several supporting functions that handle the main functionalities. The three primary functions, besides `main()`, are `add_expense`, `summarize_expenses`, and `expenses_over_time`.

- **add_expense(category, amount, date)**: This function allows users to add a new expense by specifying its category, amount, and date. Expenses are stored in a JSON file (`expenses.json`) to ensure persistent storage between sessions.
- **summarize_expenses()**: This function calculates the total spending per category and returns a summary as a dictionary. It allows users to quickly see which categories consume the most resources.
- **expenses_over_time()**: This function calculates total spending for each date, enabling users to understand how their expenses change over time.
- **visualize_expenses()**: This additional function generates bar, pie, and line charts using matplotlib to provide a visual representation of the user's spending habits. Visualizations are saved as PNG files and also displayed interactively.

The `test_project.py` file contains unit tests for the main functions, ensuring correctness and reliability. Using the pytest framework, each function is thoroughly tested. For example, `test_add_expense()` checks whether expenses are added correctly, `test_summarize_expenses()` ensures category totals are accurate, and `test_expenses_over_time()` verifies that daily totals are calculated properly. Additionally, `test_visualize_expenses_runs()` confirms that the visualization functions run without errors, even if no data is present. These tests provide confidence that the application behaves as intended under different scenarios.

The project also includes a `requirements.txt` file that lists all necessary external libraries. These include `matplotlib` for data visualization, `tabulate` for nicely formatted tables in the console, and `pytest` for running unit tests. By using a requirements file, any user can quickly install all dependencies and run the project seamlessly.

When designing the application, several choices were made to balance usability, simplicity, and functionality. JSON was chosen as the storage format for its readability and ease of use, making it easy to debug or manually edit expense records. The command-line interface provides a straightforward menu system that is accessible even to users without prior programming experience. For visualization, matplotlib was used because it offers comprehensive plotting capabilities and allows exporting graphs for future reference. Each function was kept at the top level, avoiding nested functions to maintain clarity and meet CS50 requirements.

Overall, the Hostel Expense Tracker is a robust yet simple tool for managing personal finances in a hostel setting. It demonstrates key programming concepts learned throughout the CS50 course, including file I/O, data structures, functions, testing, and third-party library usage. Users can extend the project by adding features such as recurring expenses, budget alerts, or exporting summaries to CSV, making it a solid foundation for further development.
