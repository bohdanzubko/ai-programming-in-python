# Programming classes in Python

## Tasks
* First task

    Write a program for selling tickets for master classes.
Each ticket has a unique number and price.
There are four types of tickets: regular, advance (purchased 90 or more days before the event), late (purchased 
less than 7 days before the event) and student.

  * Ticket prices:
    * advance ticket - N-30% discount from the regular ticket price;
    * student ticket - N-50% discount from the regular ticket price;
    * late ticket - additional N+20% to the regular ticket price.

  * All tickets must have the following properties:
    * the possibility of searching for a ticket by number;
    * an opportunity to find out the ticket price;
    * the possibility of printing a ticket.


* Second task
    
    Create classes Student, Student-budgeter, Group, Discipline, Teacher with the following functionality.

    * Basic class Student with the following content:
      * text fields (surname, first name, patronymic),
      * numeric fields (year of birth, year of admission to university).

    * Create the Student-Budget class as an heir of the Student class and declare in it:
      * an additional monetary field is a scholarship.

    * Create a Group class with the following content:
      * Text field - group number.
      * An array of type Student (a constructor that receives an array of students of type Student of arbitrary length).

    * Create a Discipline class with the following content:
      * The text field is the name.
      * Numeric fields – number of credits, semester of teaching.

    * Create a class Teacher with the following content:
      * text fields (surname, first name, patronymic),
      * numeric fields (year of birth, teaching experience).
      * An array of the Discipline type (a constructor that receives an array of educational disciplines of the 
      Discipline type of arbitrary length).
      * The TotalSubject method, which returns the total number of all academic subjects including the total number 
      of credits.

## Results
Console screenshots in the folders
