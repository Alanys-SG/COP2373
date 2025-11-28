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

DB_NAME = "population_ASG.db"


# Database creation

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    cities = [
        "Miami", "Orlando", "Tampa", "Jacksonville", "Tallahassee",
        "St. Petersburg", "Fort Lauderdale", "Sarasota", "Pensacola", "Gainesville"
    ]
    populations_2023 = [470000, 310000, 390000, 950000, 200000,
                        260000, 180000, 57000, 54000, 140000]

    # Insert baseline year (2023) if not already present
    for city, pop in zip(cities, populations_2023):
        cur.execute("SELECT * FROM population WHERE city=? AND year=2023", (city,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2023, pop))

    conn.commit()
    conn.close()

# Simulation with realistic growth rates
def simulate_population():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Reset simulated years (keep only 2023 baseline)
    cur.execute("DELETE FROM population WHERE year > 2023")

    # Approximate annual growth rates (based on Census/BEBR trends)
    growth_rates = {
        "Miami": 0.018,
        "Orlando": 0.020,
        "Tampa": 0.020,
        "Jacksonville": 0.015,
        "Tallahassee": 0.010,
        "St. Petersburg": 0.012,
        "Fort Lauderdale": 0.015,
        "Sarasota": 0.010,
        "Pensacola": 0.008,
        "Gainesville": 0.010
    }

    # Get cities and base populations
    cur.execute("SELECT city, population FROM population WHERE year=2023")
    data = cur.fetchall()

    for city, base_pop in data:
        population = base_pop
        # default 1% if not listed
        rate = growth_rates.get(city, 0.01)
        for year in range(2024, 2024 + 20):
            population = int(population * (1 + rate))
            cur.execute("INSERT INTO population VALUES (?, ?, ?)", (city, year, population))

    conn.commit()
    conn.close()


# Helper to get cities
def _get_cities():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cur.fetchall()]
    conn.close()
    return cities


# GUI Class
class PopulationGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Florida Population Database")

        # Frame for table
        self.table_frame = tk.Frame(master)
        self.table_frame.pack(pady=10)

        # Treeview widget to display city populations (2023)
        self.tree = ttk.Treeview(self.table_frame, columns=("City", "Population"), show="headings")
        self.tree.heading("City", text="City")
        self.tree.heading("Population", text="Population (2023)")
        self.tree.pack()

        # Load data into table
        self._load_table_data()

        # Frame for dropdown + buttons
        self.control_frame = tk.Frame(master)
        self.control_frame.pack(pady=10)

        # Dropdown for city selection
        tk.Label(self.control_frame, text="Select a city:").pack(side="left")
        self.city_var = tk.StringVar()
        self.city_dropdown = ttk.Combobox(self.control_frame, textvariable=self.city_var)
        self.city_dropdown['values'] = _get_cities()
        self.city_dropdown.pack(side="left")

        # Button to plot city population
        self.plot_button = tk.Button(self.control_frame, text="Show Growth", command=self.plot_city_population)
        self.plot_button.pack(side="left", padx=5)

        # Button to re-simulate growth
        self.resim_button = tk.Button(self.control_frame, text="Re-Simulate Growth", command=self.resimulate)
        self.resim_button.pack(side="left", padx=5)

        # Quit button
        self.quit_button = tk.Button(self.control_frame, text="Quit", command=master.destroy)
        self.quit_button.pack(side="left", padx=5)

    def _load_table_data(self):
        # Clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT city, population FROM population WHERE year=2023")
        rows = cur.fetchall()
        conn.close()

        for row in rows:
            self.tree.insert("", "end", values=row)

    def plot_city_population(self):
        chosen_city = self.city_var.get()
        if not chosen_city:
            return

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT year, population FROM population WHERE city=? ORDER BY year", (chosen_city,))
        data = cur.fetchall()
        conn.close()

        years = [row[0] for row in data]
        populations = [row[1] for row in data]

        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker="o", linestyle="-", color="blue")
        plt.title(f"Population Growth for {chosen_city}")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.grid(True)
        plt.show()

    def resimulate(self):
        simulate_population()
        self._load_table_data()
        # Refresh dropdown values in case cities changed
        self.city_dropdown['values'] = _get_cities()

# -----------------------------
# Main driver
# -----------------------------
def main():
    create_database()
    # initial simulation
    simulate_population()

    root = tk.Tk()
    PopulationGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

