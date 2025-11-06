*Library management System
Just a Simple School Library management System that works on two main parts the Student and the Library manager who lends the books to Students

*The IDEA
The idea is basically a student goes to the library to borrow a book, gives out details of the book that they want to borrow we check if copies are available through the system, after that he / she will be required to give out the student ID the system will search to see if student is valid before granting the borrow.

*Components of the application
*Library Manager
A simple UI interface created using a GUI module “ customTkinter “ in python 
Displaying some basic information like updates for any books which have overstayed in the hands of the students being able to push notifications to the students that will be visible to them via the library portals.

Request schedules from Students who want to borrow books from the library no need for the students to go to the library and find out that the book is not available

Etc…etc…

*Student
Since this is a small app it will have list of books borrowed
Alerts to return books after due date passes
Update on request made by the student etc… etc…

*Database design
Using mySQl database engine to store information that the system needs.
Tables / Entities
-Students
  - Id, name, Department
  - Borrowed books 
-Books
 - Name, Author
 - Copies Available
-BooksBorrowed
 - Student information
 - Book(s) borrowed

NOTE:
THIS APPLICATION AS A WHOLE WILL LIVE WITHIN THE SAME MACHINE SO NO NEED FOR NETWORKING TO A SERVER TO TALK TO THE DATABASE ENGINE, THIS IS TO JUST ILLUSTRATE A SIMPLE LIBRARY MANAGEMENT SYSTEM ( LMS ).
WE WILL HAVE TWO PARTS THE LIBRARY MANAGER UI AND STUDENT UI BOTH HAVING DIRECT ACCESS TO THE DATABASE “LIBRARYSTORE”.

