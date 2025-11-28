# Alanys Suazo
# Assignment: Programming Exercise 13

# The purpose of this assignment is to practice the advance usage of Numpy and other packages used for data collection
#   and display, such as matplotlib. The program should create a database of the populations of 10 Florida cities for
#   the year 2023, after which it should be able to simulation the population fluctuations for the next 20 years.
#   User interaction shoudl allow the user to pick and chose the plot of data for the city of their chose and the
#   program should display the data visually using matplotlib

import sqlite3
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

DB_NAME = "population_ASG.db"


# -----------------------------
# Database creation with baseline 2023–2025 data
# -----------------------------
def create_database():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()

        # Composite primary key ensures UPSERT works
        cur.execute("""
            CREATE TABLE IF NOT EXISTS population (
                city TEXT,
                year INTEGER,
                population INTEGER,
                PRIMARY KEY (city, year)
            )
        """)

        baseline_data = {
            "Miami": {2023: 470000, 2024: 478000, 2025: 485000},
            "Orlando": {2023: 310000, 2024: 316000, 2025: 322000},
            "Tampa": {2023: 390000, 2024: 398000, 2025: 406000},
            "Jacksonville": {2023: 950000, 2024: 964000, 2025: 978000},
            "Tallahassee": {2023: 200000, 2024: 202000, 2025: 204000},
            "St. Petersburg": {2023: 260000, 2024: 263000, 2025: 266000},
            "Fort Lauderdale": {2023: 180000, 2024: 183000, 2025: 186000},
            "Sarasota": {2023: 57000, 2024: 58000, 2025: 59000},
            "Pensacola": {2023: 54000, 2024: 54500, 2025: 55000},
            "Gainesville": {2023: 140000, 2024: 142000, 2025: 144000}
        }

        # UPSERT baseline values
        for city, years in baseline_data.items():
            for year, pop in years.items():
                cur.execute("""
                    INSERT INTO population (city, year, population)
                    VALUES (?, ?, ?)
                    ON CONFLICT(city, year) DO UPDATE SET population=excluded.population
                """, (city, year, pop))

        conn.commit()


# -----------------------------
# Simulation from 2023 onward using NumPy
# -----------------------------
def simulate_population():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()

        # Remove any previously simulated years beyond 2025
        cur.execute("DELETE FROM population WHERE year > 2025")

        # Get baseline populations
        cur.execute("SELECT city, population FROM population WHERE year=2023")
        data_2023 = dict(cur.fetchall())
        cur.execute("SELECT city, population FROM population WHERE year=2025")
        data_2025 = dict(cur.fetchall())

        for city in data_2023:
            pop_2023 = data_2023[city]
            pop_2025 = data_2025.get(city, pop_2023)

            # Average annual growth rate between 2023 and 2025
            if pop_2023 > 0 and pop_2025 > 0:
                rate = np.power(pop_2025 / pop_2023, 0.5) - 1
            else:
                rate = 0.01

            years = np.arange(2026, 2026 + 20, dtype=int)
            populations = (pop_2025 * np.power(1 + rate, np.arange(1, 21))).astype(int)

            for year, pop in zip(years, populations):
                cur.execute("""
                    INSERT INTO population (city, year, population)
                    VALUES (?, ?, ?)
                    ON CONFLICT(city, year) DO UPDATE SET population=excluded.population
                """, (city, int(year), int(pop)))

        conn.commit()


# -----------------------------
# Helper to get cities
# -----------------------------
def get_cities():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT city FROM population ORDER BY city")
        return [row[0] for row in cur.fetchall()]


# -----------------------------
# GUI Class
# -----------------------------
class PopulationGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Florida Population Database")

        # Table
        self.tree = ttk.Treeview(master, columns=("City", "Population"), show="headings")
        self.tree.heading("City", text="City")
        self.tree.heading("Population", text="Population (2025)")
        self.tree.pack(pady=10)

        self._load_table_data()

        # Controls
        self.control_frame = tk.Frame(master)
        self.control_frame.pack(pady=10)

        tk.Label(self.control_frame, text="Select a city:").pack(side="left")
        self.city_var = tk.StringVar()
        self.city_dropdown = ttk.Combobox(self.control_frame, textvariable=self.city_var, state="readonly")
        self.city_dropdown['values'] = get_cities()
        self.city_dropdown.pack(side="left")

        tk.Button(self.control_frame, text="Show Growth", command=self.plot_city_population).pack(side="left", padx=5)
        tk.Button(self.control_frame, text="Re-Simulate Growth", command=self.resimulate).pack(side="left", padx=5)
        tk.Button(self.control_frame, text="Quit", command=master.destroy).pack(side="left", padx=5)

    def _load_table_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            cur.execute("SELECT city, population FROM population WHERE year=2025 ORDER BY city")
            for city, pop in cur.fetchall():
                self.tree.insert("", "end", values=(city, pop))

    def plot_city_population(self):
        chosen_city = self.city_var.get()
        if not chosen_city:
            return
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            cur.execute("SELECT year, population FROM population WHERE city=? ORDER BY year", (chosen_city,))
            data = cur.fetchall()

        years = np.array([int(r[0]) for r in data], dtype=int)
        populations = np.array([int(r[1]) for r in data], dtype=int)

        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker="o", linestyle="-", color="blue")
        plt.xticks(years, rotation=45)
        plt.title(f"Population Growth for {chosen_city}")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def resimulate(self):
        simulate_population()
        self._load_table_data()
        self.city_dropdown['values'] = get_cities()


# -----------------------------
# Main driver
# -----------------------------
def main():
    create_database()
    simulate_population()
    root = tk.Tk()
    PopulationGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()