# Alanys Suazo
# Assignment: Programming Exercise 12

# The purpose of this assignment is to practice using NumPy in a program. The program should be able to read
#   the grades.csv file created during another assignment and analyze and use the data stored. The program
#   should calculate the mean, median, minimum, maximun, and standard deviation for each exam and across all exams,
#   as well as show who passed and failed as well as the passing percentage of the class.


import numpy as np
import csv

# Function to load exam scores from the CSV file into a NumPy array

def load_grades(filename):
    """
    Loads exam scores from the CSV file into a NumPy array.
    Skips the first two columns (First Name, Last Name).
    """
    try:
        data = np.genfromtxt(
            filename,
            delimiter=',',
            skip_header=1,
            usecols=(2, 3, 4),  # Exam 1, Exam 2, Exam 3
            dtype=float
        )
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# Function to print all data including names
def print_full_dataset(filename):
    """
    Prints the entire dataset including student names and exam scores.
    """
    print("\n--- Full Dataset ---")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        print("{:<12}{:<12}{:<8}{:<8}{:<8}".format(*header))
        print("-" * 50)
        for row in reader:
            print("{:<12}{:<12}{:<8}{:<8}{:<8}".format(*row))

# Exam statistics
def exam_statistics(data):
    print("\n--- Exam Statistics ---")
    num_exams = data.shape[1]
    for i in range(num_exams):
        exam = data[:, i]
        print(f"\nExam {i+1}:")
        print(f"  Mean: {float(np.mean(exam)):.2f}")
        print(f"  Median: {float(np.median(exam)):.2f}")
        print(f"  Std Dev: {float(np.std(exam)):.2f}")
        print(f"  Min: {int(np.min(exam))}")
        print(f"  Max: {int(np.max(exam))}")

# Overall statistics
def overall_statistics(data):
    print("\n--- Overall Statistics ---")
    all_grades = data.flatten()
    print(f"Mean: {float(np.mean(all_grades)):.2f}")
    print(f"Median: {float(np.median(all_grades)):.2f}")
    print(f"Std Dev: {float(np.std(all_grades)):.2f}")
    print(f"Min: {int(np.min(all_grades))}")
    print(f"Max: {int(np.max(all_grades))}")

# Pass/fail stats with overall percentage
def pass_fail_stats(data, passing_score=60):
    print("\n--- Pass/Fail per Exam ---")
    num_exams = data.shape[1]
    total_scores = int(data.size)
    passed_scores = int(np.sum(data >= passing_score))

    for i in range(num_exams):
        exam = data[:, i]
        passed = int(np.sum(exam >= passing_score))
        failed = int(np.sum(exam < passing_score))
        print(f"Exam {i+1}: Passed: {passed}, Failed: {failed}")

    percentage = (passed_scores / total_scores) * 100
    print(f"\nOverall Pass Percentage Across All Exams: {percentage:.2f}%")

# Main function
def main():
    filename = "grades.csv"
    grades = load_grades(filename)

    if grades is not None:
        print_full_dataset(filename)
        exam_statistics(grades)
        overall_statistics(grades)
        pass_fail_stats(grades)

if __name__ == "__main__":
    main()

