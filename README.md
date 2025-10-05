# Personal Expense Tracker (CLI)

A simple command-line application for tracking personal expenses, built for the Evaao internship assignment.

## Features
- Add a new expense (amount, date, note) from the command line.
- View a list of all expenses.
- Data is saved to a `expenses.json` file.

## Tech Stack
- Python

## How to Run
1. Clone this repository.
2. Open your terminal in the project folder.
3. **To add an expense:**
   ```bash
   python tracker.py add <amount> <date YYYY-MM-DD> "<note>"
   # Example: python tracker.py add 500 2025-10-05 "Dinner"# evaao-assignment