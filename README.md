# Massage Reservation Management System

![image](https://github.com/kobebryan31/RELAXinMASSAGE/blob/main/Images/LOGO.jpg)

## Table of Contents

Overview

Concepts Explanation

SDG Integration

Instructions

## Overview

-The Massage Reservation System is a user-friendly platform that allows customers to book massages conveniently. It streamlines the reservation process for both customers and business owners, providing features like online booking, service selection, and appointment management.

## Concepts Explanation

![image](https://github.com/kobebryan31/RELAXinMASSAGE/blob/main/Images/OOP%20Principles.png)

### 1. Encapsulation
Encapsulation involves bundling data and methods that operate on that data within a single unit (class). It also restricts direct access to some components, providing controlled interfaces for interaction.

In the Code:

Data encapsulation is evident in the Reservation class, where attributes like first_name, last_name, reserve_time, are encapsulated within the class. Methods like display_details() and to_dict() provide controlled access to these attributes.
The ReservationSystem class encapsulates all reservations in the self.reservations attribute and provides methods (add_reservation, view_reservations) to manage them.

### 2. Abstraction
Abstraction simplifies complex systems by modeling classes appropriate to the real world while hiding unnecessary implementation details.

In the Code:

The MassageService class abstracts the complexity of managing services and therapists. Instead of exposing raw data structures, it provides methods like display_services() and get_therapist_details() to interact with services and therapist data.
The ReservationSystem class abstracts the entire reservation management process, so the user interacts only with high-level options like "Make a Reservation" and "View All Reservations," without needing to know how the reservations are stored or processed.

### 3. Inheritance
Inheritance allows a class to inherit attributes and methods from another class, enabling code reuse and the creation of hierarchical relationships.

In the Code:

Although direct inheritance isn’t explicitly used here, the design could easily be extended. For example:
A VIPReservation class could inherit from the Reservation class, adding features like priority booking.
Similarly, a ServiceManager class could extend MassageService for additional functionalities, like dynamically adding services

### 4. Polymorphism
Polymorphism allows methods in different classes to have the same name but behave differently depending on the context.

In the Code:

Polymorphism is partially demonstrated through method overloading in a broader sense:
The Reservation class has methods like to_dict() for JSON serialization and display_details() for user-friendly display. Both methods handle the same object (Reservation) but serve different purposes.
Similarly, methods like add_reservation in ReservationSystem work differently depending on the room and reservation details.

## SDG Integrtion

![image]()
