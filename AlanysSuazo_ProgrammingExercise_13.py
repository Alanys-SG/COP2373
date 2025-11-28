# Alanys Suazo
# Assignment: Programming Exercise 13

# The purpose of this assignment is to practice the advance usage of Numpy and other packages used for data collection
#   and display, such as matplotlib. The program should create a database of the populations of 10 Florida cities for
#   the year 2023, after which it should be able to simulation the population fluctuations for the next 20 years.
#   User interaction shoudl allow the user to pick and chose the plot of data for the city of their chose and the
#   program should display the data visually using matplotlib

import sqlite3
import random
import matplotlib.pyplot as plt


def create_database(db_name="poulation_ASG.edb"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
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

    # Only insert if not already present
    for city, pop in zip(cities, populations_2023):
        cursor.execute("SELECT * FROM population WHERE city=? AND year=2023", (city,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2023, pop))

    conn.commit()
    conn.close()


# 2. Function to simulate growth/decline for 20 years
def simulate_population(db_name="population_ASG.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Get cities and base populations
    cursor.execute("SELECT city, population FROM population WHERE year=2023")
    data = cursor.fetchall()

    for city, base_pop in data:
        population = base_pop
        for year in range(2024, 2024 + 20):
            # Random growth/decline rate between -2% and +3%
            rate = random.uniform(-0.02, 0.03)
            population = int(population * (1 + rate))
            cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, year, population))

    conn.commit()
    conn.close()


# 3. Function to plot population growth for a chosen city
def plot_city_population(db_name="population_ASG.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Get list of cities
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    print("\nAvailable cities:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    choice = int(input("\nChoose a city by number: "))
    chosen_city = cities[choice - 1]

    # Get population data for chosen city
    cursor.execute("SELECT year, population FROM population WHERE city=? ORDER BY year", (chosen_city,))
    data = cursor.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(years, populations, marker="o", linestyle="-", color="blue")
    plt.title(f"Population Growth for {chosen_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()


# Main driver
def main():
    db_name = "population_ASG.db"
    create_database(db_name)
    simulate_population(db_name)
    plot_city_population(db_name)


if __name__ == "__main__":
    main()



