# <div align="center">Massage Reservation Management System</div>

<div align="center">
  <img src="https://github.com/kobebryan31/RELAXinMASSAGE/blob/main/Images/LOGO.jpg" alt="Logo" />
</div>

## Table of Contents

Overview

Concepts Explanation

SDG Integration

Instructions

Acknowledgement

## Overview

-The Massage Reservation System is a user-friendly platform that allows customers to book massages conveniently. It streamlines the reservation process for both customers and business owners, providing features like online booking, service selection, and appointment management.

## Concepts Explanation

<div align="center">
  <img src="https://github.com/kobebryan31/RELAXinMASSAGE/blob/main/Images/OOP%20Principles.png" alt="OOP" />
</div>

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

## SDG Integration

![image](https://github.com/kobebryan31/RELAXinMASSAGE/blob/main/Images/SDG%203%20Good%20Health%20and%20Well-Being.jpg)

Sustainable Development Goal 3 (SDG 3) is part of the United Nations' 2030 Agenda for Sustainable Development. Its main focus is to "ensure healthy lives and promote well-being for all at all ages." This goal emphasizes access to quality healthcare, promotion of mental and physical well-being, and the reduction of illnesses and preventable deaths.

###### Why This Project Integrates SDG 3
This project aligns with SDG 3: Good Health and Well-Being because it creates a structured and accessible system for managing therapeutic services, ensuring that individuals can prioritize their health in a convenient and effective way. Massage therapy is not just about relaxation; it also plays a role in preventive health by improving circulation, reducing muscle tension, and enhancing sleep quality.

## Instructions

### Interact with the System:

##### Follow the menu options displayed on the screen:

1: Make a Reservation - Choose a massage service, input customer details, and confirm the reservation.

2: View All Reservations - View a list of all existing reservations.

3: Exit - Close the program.

#### Persistent Reservations:

All reservations are saved in the reservations.json file in the program's directory.
When you restart the program, it will load the saved reservations automatically.

#### Editing the JSON File (Optional):

You can manually view or edit the reservations.json file using any text editor if needed. Ensure the JSON format remains valid.

##### Example Workflow:

##### Launch the program

###### Choose 1: Make a Reservation.

Select a massage type.

Enter customer details (name, email, address, contact number).

Provide a valid reservation date and time (example: 2024-11-11 7:30).

Review the confirmation message with therapist details.

###### Choose 2: View All Reservations to see all bookings.

###### Choose 3: Exit to quit the program.

## Acknowledgment
I would like to express my heartfelt gratitude to the following individuals and institutions for their invaluable support and guidance throughout the completion of this project:

Batangas State University: For providing me with an excellent education and a platform to develop my skills and knowledge. The university has been instrumental in shaping my growth as a learner and a professional.

Ma'am Fatima Marie P. Agadon: My dedicated instructor, whose unwavering guidance, constructive feedback, and encouragement have been crucial in the successful development of this project. Thank you for your patience, expertise, and inspiration.

My Family: For their unconditional love, support, and understanding. Their encouragement and belief in my abilities have been my driving force to excel and complete this undertaking.

My Girlfriend: For her love, support, understanding, encouragement and belief in my abilities.

The Almighty God: For His infinite wisdom, strength, and blessings. It is through His grace and guidance that I was able to overcome challenges and achieve this success.
