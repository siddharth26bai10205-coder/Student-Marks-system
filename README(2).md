# Student Marks Management System

## About the Project

This is a simple **Student Marks Management System** made using Python.

I created this project to practice basic Python concepts such as: -
Functions - Lists and dictionaries - Loops - If-else conditions - User
input - Error handling - Calculating averages and grades

The program runs in the Python terminal and allows the user to add
students, add their marks, view students, and generate a student report.

## Features

The program has the following options:

1.  **Add Student** -- Adds a new student to the system.
2.  **Show Students** -- Displays the names of all added students.
3.  **Add Marks** -- Adds marks for different subjects.
4.  **Show Report** -- Displays a student's marks, average, and grade.
5.  **Exit** -- Closes the program.

The program also checks that: - The student name is not empty. - The
subject name is not empty. - Marks are entered as numbers. - Marks are
between 0 and 100. - The entered student exists before adding marks or
showing a report.

## Grade System

The program calculates the grade based on the average marks:

  Average Marks   Grade
  --------------- -------
  90 or above     A
  80--89          B
  70--79          C
  60--69          D
  Below 60        F

## How the Program Works

When the program starts, a menu is displayed:

``` text
Student Marks Management System
1: Add student
2: Show students
3: Add marks
4: Show report
5: Exit
```

The user selects an option by entering its number.

### 1. Add Student

The program asks for the student's name and stores the student in a
list.

### 2. Show Students

This option displays all the students currently stored in the program.

### 3. Add Marks

The program asks for: - Student name - Subject - Marks

The marks are checked so that they are between 0 and 100.

### 4. Show Report

The report shows: - Student name - Marks for each subject - Average
marks - Grade

The average is calculated by adding all subject marks and dividing by
the number of subjects.

## Functions Used

The program is divided into different functions to make the code easier
to understand:

-   `add_student()` -- Adds a student.
-   `show_students()` -- Displays the student list.
-   `add_marks()` -- Adds subject marks for a student.
-   `get_average()` -- Calculates the average marks.
-   `get_grade()` -- Finds the grade from the average.
-   `show_report()` -- Displays the complete student report.

## Requirements

You only need:

-   Python 3.x

No external Python libraries are required.

## How to Run

1.  Install Python 3 on your computer.
2.  Download or copy the file:

``` text
students marks system.py
```

3.  Open the file in VS Code, IDLE, PyCharm, or another Python editor.
4.  Run the program.
5.  Use the menu shown in the terminal.

Example:

``` text
python "students marks system.py"
```

## Example

A sample report can look like:

``` text
Student: Rahul
  Maths: 85
  Physics: 78
  Python: 92

Average: 85.0
Grade: B
```

## Limitations

This is a basic student project. The student data is stored only while
the program is running. When the program is closed, the data is lost
because no database or file storage has been added.

## Future Improvements

In the future, the project can be improved by adding:

-   Saving student data to a file
-   Database support
-   Student roll numbers
-   More detailed reports
-   A graphical user interface
-   Editing and deleting students
-   Class-wise student records
-   Exporting reports to PDF or Excel

## Conclusion

This project helped me understand how Python functions, lists,
dictionaries, loops, conditions, and input validation can be combined to
create a small working application.

It is a simple project, but it can be extended with more features as I
learn more Python.
