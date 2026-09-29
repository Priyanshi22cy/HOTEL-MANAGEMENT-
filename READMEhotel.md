# Hotel Management System

## 1\. Objective

The objective of this project is to provide a simple command-line hotel
management system that stores and manages hotel data in a MySQL
database.

The application is designed to help hotel staff:

* Create and maintain a list of hotel rooms.
* Register guests and assign available rooms.
* Search for guest details.
* Update guest information.
* Process guest check-out and calculate the room bill.
* Add and maintain employee records.
* Display and delete employee information.
* Persist application data using MySQL.

The program automatically creates the `hotel\_management\_` database and
its required tables when it starts.

\---

## 2\. Key Features

### Guest Management

* Guest check-in.
* Display currently available rooms during check-in.
* Assign a room to a guest.
* Store guest contact information.
* Search guest details using guest ID.
* Update selected guest information.
* Check out a guest.
* Calculate the bill using room tariff × number of days stayed.
* Store the check-out date.

### Room Management

* Add rooms to the hotel database.
* Store:

  * Room number
  * Room type
  * Tariff
  * Availability status
* Display available rooms during guest check-in.
* Change room status during guest operations.

### Employee Management

* Add employee records.
* Update employee information.
* Update employee salary by a percentage.
* Delete an employee record.
* Search/display employee information.

### Database Management

The application uses MySQL for persistent storage and creates the
following tables:

* `guests`
* `rooms`
* `employees`

\---

## 3\. Technology Stack

Component              Technology

\---

Programming Language   Python
Database               MySQL
Database Driver        `mysql.connector`
User Interface         Command-line / terminal
Data Storage           MySQL relational database

\---

## 4\. System Architecture

The project follows a simple layered architecture:

1. **User Layer**

   * Hotel staff interact with the application through terminal
input.
2. **Menu / Application Layer**

   * The main menu routes the user to guest or employee management.
   * Functions implement individual operations.
3. **Database Access Layer**

   * `mysql.connector` establishes the connection to MySQL.
   * SQL commands are executed through the cursor object.
4. **Database Layer**

   * MySQL stores rooms, guests, and employee information.

## 5\. Program Flow

When the program starts, it connects to MySQL and calls the database
setup function. The database and required tables are created if they do
not already exist.

The application then asks whether rooms should be added and enters the
main menu.

The main menu provides:

* Guest Management
* Employee Management
* Exit

Guest Management provides check-in, guest search, guest update,
check-out, and exit operations.

Employee Management provides employee creation, update, deletion,
display, and exit operations.

## 6\. Database Design

### 6.1 `guests` Table

Column           Type            Description

\---

`guest\_id`       `INT`           Primary key identifying a guest
`first\_name`     `VARCHAR(20)`   Guest first name
`last\_name`      `VARCHAR(20)`   Guest last name
`c\_in`           `DATE`          Check-in date
`c\_out`          `DATE`          Check-out date
`room\_number`    `INT`           Assigned room number
`email`          `VARCHAR(50)`   Guest email
`phone\_number`   `VARCHAR(15)`   Guest phone number

### 6.2 `rooms` Table

Column          Type              Description

\---

`room\_number`   `INT`             Primary key identifying a room
`room\_type`     `VARCHAR(20)`     Type/category of room
`tariff`        `DECIMAL(10,2)`   Room price/tariff
`status`        `VARCHAR(10)`     Room availability status

The default room status is `Available`.

### 6.3 `employees` Table

Column           Type            Description

\---

`employee\_id`    `INT`           Primary key identifying an employee
`first\_name`     `VARCHAR(20)`   Employee first name
`last\_name`      `VARCHAR(20)`   Employee last name
`position`       `VARCHAR(20)`   Employee position
`department`     `VARCHAR(20)`   Employee department
`hire\_date`      `DATE`          Date of hiring
`salary`         `INT`           Employee salary
`email`          `VARCHAR(50)`   Employee email
`phone\_number`   `VARCHAR(15)`   Employee phone number

### Database Relationship Overview

The supplied code does not define explicit SQL foreign-key constraints
between the tables. The guest's `room\_number` corresponds logically to a
room in the `rooms` table.

\---

## 7\. Main Modules / Functions

### Database Setup

#### `data\_setup()`

Creates the database and the three required tables if they do not
already exist.

### Room Management

#### `add\_room()`

Accepts room details from the user and attempts to insert them into the
`rooms` table.

### Guest Management

#### `guest\_check\_in()`

* Collects guest information.
* Queries rooms whose status is `available`.
* Displays available rooms.
* Assigns the selected room to the guest.
* Inserts the guest record.
* Marks the room as `occupied`.

#### `find\_guest\_details()`

Searches for a guest using `guest\_id` and displays their stored
information.

#### `upg\_guest\_info()`

Provides a menu for updating selected guest fields.

#### `guest\_check\_out()`

* Takes a room number.
* Finds the guest occupying that room.
* Retrieves the room tariff.
* Calculates the bill based on the entered number of days.
* Asks whether payment was received.
* Stores a check-out date when payment is confirmed.

### Employee Management

#### `add\_employee\_info()`

Adds a new employee to the `employees` table.

#### `upg\_employee\_info()`

Allows modification of employee:

* First name
* Last name
* Position
* Department
* Salary
* Email
* Phone number

The salary option supports percentage-based increment or decrement.

#### `delete\_employee\_info()`

Deletes an employee using their employee ID.

#### `display\_employee\_info()`

Retrieves and displays employee details using employee ID.

\---

## 8\. Application Menu

The top-level application provides three choices:

``` text
1. Guest Management
2. Employee Management
3. Exit
```

### Guest Menu

``` text
1. Guest Check In
2. Find a Guest's Details
3. Update a Guest's Info
4. Check Out
5. Exit
```

### Employee Menu

``` text
1. Add Employee Information
2. Upgrade/Update Employee Information
3. Delete Employee Information
4. Display Employee Information
5. Exit
```

\---

## 9\. Check-In Workflow

``` mermaid
sequenceDiagram
    participant User
    participant Python as Python Application
    participant MySQL

    User->>Python: Enter guest details
    Python->>MySQL: Query available rooms
    MySQL-->>Python: Return available rooms
    Python-->>User: Display available rooms
    User->>Python: Select room
    Python->>MySQL: Insert guest record
    Python->>MySQL: Set room status = occupied
    MySQL-->>Python: Commit changes
    Python-->>User: Guest checked in
```

\---

## 10\. Check-Out and Billing

The check-out function retrieves the room tariff and calculates:

``` text
Total Bill = Room Tariff × Number of Days Stayed
```

For example, if:

``` text
Room tariff = Rs. 2500/night
Days stayed = 3
```

then:

``` text
Total Bill = Rs. 2500 × 3
           = Rs. 7500
```

The program then displays an invoice containing the guest name, room
number, duration, and total amount.

\---

## 11\. Installation and Setup

### Prerequisites

Install:

* Python 3.x
* MySQL Server
* MySQL client/tools
* Python MySQL connector

Install the connector with:

``` bash
pip install mysql-connector-python
```

### MySQL Configuration

The current source connects using:

``` python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="localhost"
)
```

Therefore, the local MySQL installation must have credentials matching
the configuration in the Python source, or the connection settings must
be changed.

### Run the Application

Save the source file and run:

``` bash
python "HOTEL MANAGEMENT PROJECT.py"
```

The application then attempts to:

1. Connect to MySQL.
2. Create `hotel\_management\_` if it does not exist.
3. Create the required tables.
4. Start the hotel management menu.

\---

## 12\. Typical Usage

### First Run

1. Start MySQL.
2. Run the Python program.
3. Allow the application to create the database/tables.
4. Add rooms.
5. Open Guest Management to check guests in.
6. Use Employee Management to maintain employee records.

### Example Room Data

``` text
Room Number: 101
Room Type: Deluxe single bedded
Tariff: 203
Status: Available
```

### Example Guest Data

``` text
Guest ID: 101
First Name: Michael
Last Name: Ross
Check-in Date: 2026-09-29
Room: 304
Email: mike@gmail.com
Phone: 9876543210
```

\---

### 13.4 SQL safety

Several queries are built using string formatting, for example:

``` python
"select \* from guests where guest\_id={}".format(gid)
```

and:

``` python
"update guests set first\_name='{}' where guest\_id={}".format(f1, gid)
```

This approach can create SQL injection and quoting problems.
Parameterized queries using `%s` placeholders should be used
consistently.

### 13.5 Input validation

The program directly converts many user inputs using `int()` and accepts
dates as strings. Invalid input can therefore terminate the program or
create invalid data.

A stronger implementation should validate:

* IDs
* Room numbers
* Tariffs
* Salary
* Phone numbers
* Email addresses
* Dates
* Room status
* Menu choices

\---

## 14\. Current Limitations

The supplied implementation is a small educational console application
rather than a production hotel management platform.

Current limitations include:

* No graphical/web interface.
* No authentication or user roles.
* No reservation system for future bookings.
* No automated date/duration calculation during billing.
* No dedicated payment table or payment history.
* No invoice storage.

\---

## 15\. Possible Future Enhancements

The project can be extended with:

### User Interface

* Tkinter desktop GUI.
* Flask/Django web interface.
* Responsive hotel management dashboard.

### Guest Features

* Guest registration and profiles.
* Reservation management.
* Search by name, phone, or room.
* Booking history.
* Automated check-in/check-out dates.

### Room Features

* Room categories.
* Room availability calendar.
* Maintenance status.
* Room cleaning status.
* Dynamic pricing.

### Billing

* Automatic stay-duration calculation.
* Taxes and discounts.
* Payment methods.
* Payment history.
* Printable/downloadable invoices.

### Employee Features

* Employee login.
* Role-based permissions.
* Attendance management.
* Payroll management.

### Database Improvements

* Foreign-key constraints.
* Indexes for frequently searched fields.
* Transactions for multi-step operations.
* Parameterized queries throughout.
* Proper database error handling.
* Environment-based configuration.

### Reporting

* Occupancy reports.
* Revenue reports.
* Guest history.
* Employee reports.
* Room utilization statistics.

\---

## 16.Architecture

hotel-management/
│
├── main.py
├── config.py
│
├── database/
│   ├── connection.py
│   └── schema.sql
│
├── models/
│   ├── guest.py
│   ├── room.py
│   └── employee.py
│
├── services/
│   ├── guest\_service.py
│   ├── room\_service.py
│   ├── employee\_service.py
│   └── billing\_service.py
│
├── repositories/
│   ├── guest\_repository.py
│   ├── room\_repository.py
│   └── employee\_repository.py
│
└── README.md
```

This separation would make the project easier to test, maintain, and
extend.



## 18\. Project Summary

The **Hotel Management System** is a Python console application
connected to MySQL. It demonstrates fundamental concepts of:

* Python functions
* Menu-driven programming
* MySQL database connectivity
* SQL table creation
* CRUD operations
* Guest and room management
* Employee management
* Basic billing

The project provides a useful foundation for learning how a Python
application can interact with a relational database to manage real-world
business data.

\---

# Author

## PRIYANSHI

**Project:** Hotel Management System
**Technology:** Python 3 , and sql
**Type: Menu driven hotel management system** 

**Purpose:** Learning and Educational Project



