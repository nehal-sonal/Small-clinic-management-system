# 🏥 Small Clinic Manager (Python CLI)

Welcome to the **Small Clinic Manager**, a simple Command-Line Interface (CLI) application built with **Python** for managing patient records in a small clinic setting.

This project is a straightforward example of file-based data management, utilizing a plain text file (`patients.txt`) to store and retrieve patient information. It's a great demonstration of basic CRUD (Create, Read, Update, Delete) operations using Python's fundamental file I/O capabilities.

---

## ✨ Features

This clinic manager provides a full suite of functionalities necessary for day-to-day patient record keeping:

* **Add Patient:** Easily enroll a new patient with details like ID, Name, Age, and Gender.
* **View Patient by ID:** Look up a specific patient's complete record, including their history and appointments.
* **Search All Patients:** Display a quick list of all registered patients.
* **Search by Name:** Find patients whose names contain a specific search term (case-insensitive).
* **Add Appointment:** Record new appointments for existing patients.
* **Add History Note:** Append new medical history notes to a patient's record.
* **Edit Patient Details:** Update a patient's Name, Age, or Gender.
* **Delete Record:** Permanently remove a patient's record from the system.
* **Clear All Records:** **(Use with Caution!)** Delete the entire database.
* **Show Statistics:** Get a basic overview of the patient population (total, male, and female counts).

---

## 🛠️ How It Works

The system stores all patient data in a file named `patients.txt`. Each patient record occupies a single line, with the data fields separated by a pipe character (`|`).

| Field Index | Data Stored | Example Data |
| :---: | :---: | :--- |
| `[0]` | Patient ID | `101` |
| `[1]` | Name | `Alice Smith` |
| `[2]` | Age | `35` |
| `[3]` | Gender | `Female` |
| `[4]` | History Notes | `Flu shot 2023 || Check-up: healthy` |
| `[5]` | Appointments | `15/12/2025-Routine Checkup` |

The Python functions handle opening, reading, writing, and closing the file to perform all the management tasks.

---

## 🚀 Getting Started

### Prerequisites

You only need **Python 3** installed on your system.

### Running the Application

1.  **Save the Code:** Save the provided Python code as a file named `clinic_manager.py` (or any name you like).
2.  **Run from CLI:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

    ```bash
    python clinic_manager.py
    ```

3.  **Use the Menu:** The program will start and present a menu. Simply enter the corresponding choice to the action you want to perform (e.g., `1` to add a patient).

---

## 📝 Patient Record Structure Example

When you add a patient, a record is created in `patients.txt`. It will look something like this (all on a single line):
