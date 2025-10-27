# Alanys Suazo
# Assignment: Programming Exercise CSV

# The purpose of this assignment is to practice using the CSV package and collecting data to import and export
#   from this single program. The program should be able to create a csv file and append it with student
#   first name, last name, and their 3 test scores. After the file has been created and appended, the program
#   should be able to read the csv file and display the information in table format.

# imports the Comma Separated Values package.
import csv

# This function writes the user input into the csv file.
def writer_program(loop_interval):

    #creates and opens a csv file and overwrites every time the program runs.
    with open("grades.csv", 'w', newline='') as file:
        writer = csv.writer(file)

        #writing the header for the table/dictionary
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # creating a loop for the number of students entered.
        for i in  range(loop_interval):

            print(f'Enter data for student {i+1}:')
            # for both the first and last names, the program will check if they are valid by accepting letters only
            while True:
                first = input("First Name: ")
                if first.strip().isalpha():
                    break
                else:
                    print("Invalid input. Please enter letters only.")

            while True:
                last = input("Last Name: ")
                if last.strip().isalpha():
                    break
                else:
                    print("Invalid input. Please enter letters only.")

            # for each of the exam scores, the program will check that they are numerical and in the acceptable range
            while True:
                try:
                    exam1 = float(input("Exam 1 score: "))
                    if 0 <= exam1 <= 100:
                        break
                    else:
                        print('Score much be between 0 and 100.')
                except ValueError:
                    print("Invalid input. Please enter a number.")

            while True:
                try:
                    exam2 = float(input("Exam 2 score: "))
                    if 0 <= exam2 <= 100:
                        break
                    else:
                        print('Score much be between 0 and 100.')
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            while True:
                try:
                    exam3 = float(input("Exam 3 score: "))
                    if 0 <= exam3 <= 100:
                        break
                    else:
                        print('Score much be between 0 and 100.')
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            #writes the data into the dictionary
            writer.writerow([first, last, exam1, exam2, exam3])

#This program was created to read the csv file created and display its contents to the user in a table format
def reader_program():
    #introdicing the program
    print('Welcome to the Grade Organizer!')
    print("This program can help you organize your student's scores into one place!")

    #collecting the classroom size data
    loop_interval = int(input('Please enter the number of students you have to put on file:  '))

    #sending the data to the folowing program so the loop can be initiated accurately
    writer_program(loop_interval)

    print('\n Here is the organised scores:\n')

    # opend the file in read mode so that it can print without any errors
    with open("grades.csv", 'r') as file:
        csvreader = csv.reader(file)

        #Formating and printing the header
        print("\n{:<12}{:<12}{:<8}{:<8}{:<8}".format("First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"))
        print("-" * 48)
        #skiping to the next line so that it doesn't reprint the header for each new row/student
        next(csvreader)

        # printing the student rows
        for row in csvreader:
            print("{:<12}{:<12}{:<8}{:<8}{:<8}".format(*row))


#calling the function
if __name__ == "__main__":
    reader_program()