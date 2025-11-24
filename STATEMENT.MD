# PROBLEM STATEMENT :MANAGEMENT SYSTEM DESIGNED FOR SMALL SCALE CLINICS .
This is a digital system created to handle patient records,their appointments, histories for reference ,and etc.

# SCOPE OF THE PROJECT :
The system helps reduce minor error,avoiding appointment clashes,maintaining statistics,deleting or adding patient id,viewing patient details,etc.
To keep patient records, including personal, medical, and visitation history, accurate and well-organized. 
To enable smooth appointment scheduling without conflicts with physician availability.
To make it possible for physicians to document diagnosis, prescription, and treatment information. 
To offer a simple system for generating invoices or billing. 
To guarantee that doctors and staff have simple access to previous records. 
To lessen the amount of paperwork, mistakes, and administrative work.
The system will include :
*patient registration and their detail management
*appointment booking
*record of history of patient 
*viewing patient by their ids or name.
*total statistics of the clinic.
*addition/deletion of patient details.
*editing the incorrect patient details.
*deletion of complete clinic records.
*complete view of all the patients registered in the clinic.

#TARGET USERS :
*Clinic receptionists
-handling of patient registration 
-booking/rescheduling their appointments
*front desk staff
-manage patient files and contact details.
*doctors
-for reference
-who do not want to hire extra employee
-update diagnostics
*nurses 
-to assist the doctors
-track the treatment
*pharmacists
-manage medicine inventory
*clinic owners
-oversee the entire clinic workflow
-check revenue
*patients 
-to view their details
*billing staff/accountant 
-generating bills for the consultation or appointment
-maintaining of financial records 


# HIGH-LEVEL FEATURES :
*Managing Files :
-Reading, writing, updating, and opening a text document (patients.txt).
-used to permanently store all patient records.

*Functions
-Numerous small functions, such as addpat(), viewpatient(), namesearch(), etc., make up the code.
-Every function carries out a single, distinct task.

 #Lists
-Readal() is used to store file lines inside lists.After that, lists are updated and returned to the file.

#Operations on Strings
-Using.split ("|") to split patient records
-Using "|" to join updated data. join (row)
-lowercasing names in search results.

 #Loops
-loops to review every patient record.
-The menu will run in an endless while True loop until it is terminated.

#Checking Conditions (if-else)
- used everywhere to check valid choices, match IDs, and confirm gender, among other things.

 #User Input Handling
-The user provides input to the program for patient information, editing, searching, scheduling appointments, confirming deletions, etc.

#Program Driven by the Menu
-makes use of a printed menu that keeps running until the user selects Exit.
-Simple Data Formatting

#Records are kept with separators.
-When more than one note is added, "||" is used to store appointments and history.

#Basic Data Processing
-counting the number of male and female patients.

#Verifying the existence of the ID.
-updating particular fields.
