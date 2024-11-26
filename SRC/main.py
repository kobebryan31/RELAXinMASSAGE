import json
from datetime import datetime, timedelta


class Person:
    def __init__(self, first_name, last_name, email, contact_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact_number = contact_number


class Customer(Person):
    def __init__(self, first_name, last_name, email, contact_number, address):
        super().__init__(first_name, last_name, email, contact_number)
        self.address = address


class Therapist(Person):
    def __init__(self, first_name, last_name, email, contact_number, specialization):
        super().__init__(first_name, last_name, email, contact_number)
        self.specialization = specialization


class Reservation:
    def __init__(self, customer, reserve_time, room_id, service, therapist):
        self.customer = customer
        self.reserve_time = reserve_time
        self.room_id = room_id
        self.service = service
        self.therapist = therapist
        self.duration = timedelta(hours=1, minutes=30)
        self.price = 1500.00

    def to_dict(self):
        return {
            "customer": {
                "first_name": self.customer.first_name,
                "last_name": self.customer.last_name,
                "email": self.customer.email,
                "contact_number": self.customer.contact_number,
                "address": self.customer.address
            },
            "reserve_time": self.reserve_time.strftime("%Y-%m-%d %H:%M"),
            "room_id": self.room_id,
            "service": self.service,
            "therapist": {
                "first_name": self.therapist.first_name,
                "last_name": self.therapist.last_name,
                "specialization": self.therapist.specialization
            },
        }

    @staticmethod
    def from_dict(data):
        customer = Customer(
            data["customer"]["first_name"], data["customer"]["last_name"],
            data["customer"]["email"], data["customer"]["contact_number"],
            data["customer"]["address"]
        )
        therapist = Therapist(
            data["therapist"]["first_name"], data["therapist"]["last_name"],
            "", "", data["therapist"]["specialization"]
        )
        return Reservation(
            customer, datetime.strptime(data["reserve_time"], "%Y-%m-%d %H:%M"),
            data["room_id"], data["service"], therapist
        )

    def get_end_time(self):
        return self.reserve_time + self.duration

    def display_details(self):
        print("\nReservation Details:")
        print(f"Customer: {self.customer.first_name} {self.customer.last_name}")
        print(f"Email: {self.customer.email}")
        print(f"Address: {self.customer.address}")
        print(f"Contact Number: {self.customer.contact_number}")
        print(f"Service: {self.service} in Room {self.room_id}")
        print(f"Therapist: {self.therapist.first_name} {self.therapist.last_name} (Specialization: {self.therapist.specialization})")
        print(f"Reservation Time: {self.reserve_time}")
        print(f"End Time: {self.get_end_time()}")
        print(f"Price: Php {self.price:.2f}\n")


class MassageService:
    SERVICES = {
        1: "Swedish Massage",
        2: "Deep Tissue Massage",
        3: "Sports Massage",
        4: "Hot Stone Massage",
        5: "Aromatherapy Massage",
        6: "Thai Massage",
        7: "Reflexology",
        8: "Prenatal Massage",
        9: "Shiatsu Massage",
        10: "Chair Massage",
    }

    THERAPISTS = {
        1: Therapist("Sarah", "Thompson", "", "", "Swedish Massage"),
        2: Therapist("Michael", "Johnson", "", "", "Deep Tissue Massage"),
        3: Therapist("Emily", "Davis", "", "", "Sports Massage"),
        4: Therapist("James", "Martinez", "", "", "Hot Stone Massage"),
        5: Therapist("Laura", "Green", "", "", "Aromatherapy Massage"),
        6: Therapist("Benjamin", "Lee", "", "", "Thai Massage"),
        7: Therapist("Sophia", "Brown", "", "", "Reflexology"),
        8: Therapist("Olivia", "Wilson", "", "", "Prenatal Massage"),
        9: Therapist("Daniel", "Clark", "", "", "Shiatsu Massage"),
        10: Therapist("Jessica", "Hall", "", "", "Chair Massage"),
    }

    @staticmethod
    def display_services():
        print("\nAvailable Services:")
        for room_id, service in MassageService.SERVICES.items():
            print(f"Room {room_id}: {service}")

    @staticmethod
    def get_service_name(room_id):
        return MassageService.SERVICES.get(room_id)

    @staticmethod
    def get_therapist_details(room_id):
        return MassageService.THERAPISTS.get(room_id)


class ReservationSystem:
    def __init__(self, data_file="reservations.json"):
        self.data_file = data_file
        self.reservations = self.load_reservations()

    def load_reservations(self):
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                return [Reservation.from_dict(res) for res in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_reservations(self):
        with open(self.data_file, "w") as file:
            json.dump([res.to_dict() for res in self.reservations], file, indent=4)

    def add_reservation(self, first_name, last_name, email, address, contact_number, room_id, reserve_time):
        service_name = MassageService.get_service_name(room_id)
        therapist = MassageService.get_therapist_details(room_id)

        if not service_name or not therapist:
            print("Invalid room choice.")
            return

        for reservation in self.reservations:
            if reservation.room_id == room_id and reservation.reserve_time == reserve_time:
                print("This room is already booked for the selected time and date.")
                return

        customer = Customer(first_name, last_name, email, contact_number, address)
        reservation = Reservation(customer, reserve_time, room_id, service_name, therapist)
        self.reservations.append(reservation)
        self.save_reservations()
        print("Reservation confirmed!")
        reservation.display_details()

    def view_reservations(self):
        if not self.reservations:
            print("No reservations found.\n")
            return
        for index, reservation in enumerate(self.reservations, start=1):
            print(f"Reservation {index}:")
            reservation.display_details()

    def delete_reservation(self):
        if not self.reservations:
            print("No reservations found.\n")
            return

        print("Existing Reservations:")
        for index, reservation in enumerate(self.reservations, start=1):
            print(f"{index}. {reservation.customer.first_name} {reservation.customer.last_name} - {reservation.reserve_time}")

        try:
            choice = int(input("Enter the reservation number to delete: "))
            if 1 <= choice <= len(self.reservations):
                removed = self.reservations.pop(choice - 1)
                self.save_reservations()
                print(f"Reservation for {removed.customer.first_name} {removed.customer.last_name} on {removed.reserve_time} has been deleted.")
            else:
                print("Invalid selection. Please choose a valid reservation number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def menu(self):
        while True:
            print("---Massage Reservation---")
            print("1. Make a Reservation")
            print("2. View All Reservations")
            print("3. Delete a Reservation")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                MassageService.display_services()

                try:
                    room_id = int(input("\nChoose a room (1-10) for massage type: "))
                except ValueError:
                    print("Invalid room number. Please enter a number between 1 and 10.")
                    continue

                first_name = input("Enter customer's first name: ")
                last_name = input("Enter customer's last name: ")
                email = input("Enter customer's email address: ")
                address = input("Enter customer's address: ")
                contact_number = input("Enter customer's contact number: ")

                reserve_time_str = input("Enter reservation date and time (YYYY-MM-DD HH:MM): ")
                try:
                    reserve_time = datetime.strptime(reserve_time_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
                    continue

                self.add_reservation(first_name, last_name, email, address, contact_number, room_id, reserve_time)

            elif choice == '2':
                self.view_reservations()
            elif choice == '3':
                self.delete_reservation()
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    reservation_system = ReservationSystem()
    reservation_system.menu()
