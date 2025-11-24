 🏥 Small Clinic Management system :

Introducing the Clinic manager system , a simple Command-Line application built with Python for managing patient records in a small clinic setting.

✨ Features : This clinic manager provides a full suite of functionalities necessary for day-to-day patient record keeping:
1.Add Patient: Input details of a new patient with like ID, Name, Age, and Gender.
2.View Patient by ID: Searching of a specific patient's complete record that has been inputted.
3.Search All Patients: Shows all registered patients.
4.Search by Name: Find patients by their names irrespective of the case insensitive.
5.Add Appointment: Recording appointments for patients.
6.Add History Note:Add medical history to a patient's record for doctor's reference.
7.Edit Patient Details: Updating a patient's Name, Age, or Gender i entered incorrectly.
8.Delete Record: Removing of a patient's record from the database if the patient has been logged out.
9.Clear All Records: Deletion of the entire inputted data.
10.Show Statistics: statistics of the patient population including total, male, and female counts.

 🛠️ How It Works : The system stores all patient data in a file named `patients.txt`. Each patient record is displayed in a single line, with the different types of data separated by (|).

| Field Index | Data Stored | Example Data |
| [0] | Patient ID | 11 |
| [1] | Name | Nehal Sonal |
| [2] | Age | 21 |
| [3] | Gender | Female |
| [4] | History Notes | Typhoid in 2006 |
| [5] | Appointments | 15/12/2025 |

The Python functions handle opening, reading, writing, and closing the file to perform all the required tasks.

🚀 Getting into the program -

*Required condition : You only need Python 3 installed on your system.

*Running the Application :
1.  Save the Code: Save the Python code as a file named smalclinicmanager.py .
2.  Run from Command Line Interface: Open your terminal or command prompt, navigate to the directory where you saved the file, and run: smalclinicmanager.py
3.  Use the Menu: The program will start and present a menu.Simply enter the corresponding choice to the action you want to perform (e.g., `1` to add a patient).

📝 Patient Record Structure Example :
When you add a patient, a record is created in `patients.txt`. It will look something like this (all on a single line): 
11|Nehal Sonal|21|Female|None|None
After adding a history note and an appointment, the same record will look like :
11|Nehal Sonal|21|Female|Typhoid in 2006| 15/12/2025 |

💡 Improvements & Future Plans :
1) Check for valid input data- The program should check if the Age is actually a number and make sure every new patient gets a unique ID.
2) User friendly screen- Typing in black and white screens is boring so we need to make interesting user interface using Tkinter or PyQt.
3) Store dates systematically - Right now the data stored for appointments is plain text and not arranged in a correct manner so for that we need to work more.


