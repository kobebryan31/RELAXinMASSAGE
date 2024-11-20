import json
from datetime import datetime, timedelta

class Reservation:
    def __init__(self, first_name, last_name, email, address, contact_number, reserve_time, room_id, service, therapist_name, therapist_specialization):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.contact_number = contact_number
        self.reserve_time = reserve_time
        self.room_id = room_id
        self.service = service
        self.therapist_name = therapist_name
        self.therapist_specialization = therapist_specialization
        self.duration = timedelta(hours=1, minutes=30)
        self.price = 1500.00

    def to_dict(self):
        """Convert reservation to a dictionary for JSON storage."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address,
            "contact_number": self.contact_number,
            "reserve_time": self.reserve_time.strftime("%Y-%m-%d %H:%M"),
            "room_id": self.room_id,
            "service": self.service,
            "therapist_name": self.therapist_name,
            "therapist_specialization": self.therapist_specialization,
        }

    @staticmethod
    def from_dict(data):
        """Create a Reservation object from a dictionary."""
        return Reservation(
            data["first_name"], data["last_name"], data["email"], data["address"],
            data["contact_number"], datetime.strptime(data["reserve_time"], "%Y-%m-%d %H:%M"),
            data["room_id"], data["service"], data["therapist_name"], data["therapist_specialization"]
        )

    def get_end_time(self):
        return self.reserve_time + self.duration

    def display_details(self):
        print(f"\nReservation Details:")
        print(f"Customer: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Service: {self.service} in Room {self.room_id}")
        print(f"Therapist: {self.therapist_name} (Specialization: {self.therapist_specialization})")
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
        1: {"name": "Sarah Thompson", "specialization": "Swedish Massage"},
        2: {"name": "Michael Johnson", "specialization": "Deep Tissue Massage"},
        3: {"name": "Emily Davis", "specialization": "Sports Massage"},
        4: {"name": "James Martinez", "specialization": "Hot Stone Massage"},
        5: {"name": "Laura Green", "specialization": "Aromatherapy Massage"},
        6: {"name": "Benjamin Lee", "specialization": "Thai Massage"},
        7: {"name": "Sophia Brown", "specialization": "Reflexology"},
        8: {"name": "Olivia Wilson", "specialization": "Prenatal Massage"},
        9: {"name": "Daniel Clark", "specialization": "Shiatsu Massage"},
        10: {"name": "Jessica Hall", "specialization": "Chair Massage"},
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

        reservation = Reservation(
            first_name, last_name, email, address, contact_number, reserve_time, room_id,
            service_name, therapist["name"], therapist["specialization"]
        )
        self.reservations.append(reservation)
        self.save_reservations()
        print("Reservation confirmed!")
        reservation.display_details()

    def view_reservations(self):
        if not self.reservations:
            print("No reservations found.\n")
            return
        for reservation in self.reservations:
            reservation.display_details()

    def menu(self):
        while True:
            print("---Massage Reservation---")
            print("1. Make a Reservation")
            print("2. View All Reservations")
            print("3. Exit")
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
                print("Exiting the system.")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    reservation_system = ReservationSystem()
    reservation_system.menu()
