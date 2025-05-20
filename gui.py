import tkinter as tk
from tkinter import ttk

from client import Client
from employee import Employee
from event import Event
from guest import Guest
from supplier import Supplier
from venue import Venue


# noinspection PyTypeChecker
class EventOrganizerApp:
    def __init__(self, root):
        self.main_menu_frame = None
        self.root = root
        self.root.title("Event Organizer App")
        self.root.geometry("800x600")
        self.root.configure(bg="black")
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use a different theme for ttk widgets

        self.employees, self.events, self.clients, self.guests, self.suppliers, self.venues = DataHandler.load_data()  # Load existing data or create new data
        self.create_main_menu()

    def create_main_menu(self):
        self.main_menu_frame = tk.Frame(self.root)
        self.main_menu_frame = tk.Frame(self.root, bg="black")
        self.main_menu_frame.pack(pady=20)

        buttons = [
            ("Add Employee", self.add_employee),
            ("Add Event", self.add_event),
            ("Add Client", self.add_client),
            ("Add Guest", self.add_guest),
            ("Add Supplier", self.add_supplier),
            ("Add Venue", self.add_venue),
            ("Display Employees", lambda: self.display_data("Employees")),
            ("Display Events", lambda: self.display_data("Events")),
            ("Display Clients", lambda: self.display_data("Clients")),
            ("Display Guests", lambda: self.display_data("Guests")),
            ("Display Suppliers", lambda: self.display_data("Suppliers")),
            ("Display Venues", lambda: self.display_data("Venues"))
        ]

        for text, command in buttons:
            tk.Button(self.main_menu_frame, text=text, command=command, width=20, height=2, bg="#4CAF50",
                      fg="white").pack(fill=tk.X, padx=10, pady=5)

    def save_data(self):
        DataHandler.save_data(self.employees, self.events, self.clients, self.guests, self.suppliers, self.venues)

    def display_data(self, data_type):
        display_window = tk.Toplevel(self.root)
        display_window.title(f"Display {data_type}")

        data_list = getattr(self, data_type.lower())  # Get the list of data based on data_type

        columns = self.get_columns(data_type)
        tree = ttk.Treeview(display_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        for data_item in data_list:
            data_info = self.get_data_info(data_item, data_type)
            tree.insert('', 'end', values=data_info)

        tree.pack(expand=True, fill="both")

    def get_columns(self, data_type):
        if data_type == "Employees":
            return ["Name", "ID", "Department", "Job Title", "Basic Salary", "Manager ID"]
        elif data_type == "Events":
            return ["ID", "Type", "Theme", "Date", "Time", "Duration", "Venue Address", "Client ID", "Guest List",
                    "Catering Company", "Cleaning Company", "Decorations Company", "Entertainment Company",
                    "Furniture Supply Company", "Invoice"]
        elif data_type == "Clients":
            return ["ID", "Name", "Address", "Contact Details", "Budget"]
        elif data_type == "Guests":
            return ["ID", "Name", "Address", "Contact Details"]
        elif data_type == "Suppliers":
            return ["ID", "Name", "Address", "Contact Details", "Services Offered"]
        elif data_type == "Venues":
            return ["ID", "Name", "Address", "Contact", "Min Guests", "Max Guests"]

    def get_data_info(self, data_item, data_type):
        if data_type == "Employees":
            return data_item.name, data_item.employee_id, data_item.department, data_item.job_title, data_item.basic_salary, data_item.manager_id
        elif data_type == "Events":
            return (data_item.event_id, data_item.event_type, data_item.theme, data_item.date, data_item.time,
                    data_item.duration, data_item.venue_address, data_item.client_id, data_item.guest_list,
                    data_item.catering_company, data_item.cleaning_company, data_item.decorations_company,
                    data_item.entertainment_company, data_item.furniture_supply_company, data_item.invoice)
        elif data_type == "Clients":
            return (data_item.client_id, data_item.name, data_item.address, data_item.contact_details, data_item.budget)
        elif data_type == "Guests":
            return (data_item.guest_id, data_item.name, data_item.address, data_item.contact_details)
        elif data_type == "Suppliers":
            return (data_item.supplier_id, data_item.name, data_item.address, data_item.contact_details,
                    data_item.services_offered)
        elif data_type == "Venues":
            return (data_item.venue_id, data_item.name, data_item.address, data_item.contact, data_item.min_guests,
                    data_item.max_guests)

    def add_employee(self):
        add_employee_window = tk.Toplevel(self.root)
        add_employee_window.title("Add Employee")
        add_employee_window.geometry("400x300")

        # Set background color to black
        add_employee_window.configure(bg="black")

        # Create a frame with black background for content
        content_frame = tk.Frame(add_employee_window, bg="black")
        content_frame.pack(expand=True, fill="both")

        tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
        self.name_entry = tk.Entry(content_frame)
        self.name_entry.pack()

        tk.Label(content_frame, text="Employee ID:", fg="green", bg="black").pack()
        self.employee_id_entry = tk.Entry(content_frame)
        self.employee_id_entry.pack()

        tk.Label(content_frame, text="Department:", fg="green", bg="black").pack()
        self.department_entry = tk.Entry(content_frame)
        self.department_entry.pack()

        tk.Label(content_frame, text="Job Title:", fg="green", bg="black").pack()
        self.job_title_entry = tk.Entry(content_frame)
        self.job_title_entry.pack()

        tk.Label(content_frame, text="Basic Salary:", fg="green", bg="black").pack()
        self.basic_salary_entry = tk.Entry(content_frame)
        self.basic_salary_entry.pack()

        tk.Label(content_frame, text="Manager ID:", fg="green", bg="black").pack()
        self.manager_id_entry = tk.Entry(content_frame)
        self.manager_id_entry.pack()

        tk.Button(content_frame, text="Save", command=self.save_employee, fg="green", bg="black").pack()

    def save_employee(self):
        name = self.name_entry.get()
        employee_id = self.employee_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        manager_id = self.manager_id_entry.get()

        if name and employee_id and department and job_title and basic_salary and manager_id:
            employee = Employee(name, employee_id, department, job_title, basic_salary, manager_id)
            self.employees.append(employee)
            self.save_data()

        self.name_entry.delete(0, tk.END)
        self.employee_id_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.job_title_entry.delete(0, tk.END)
        self.basic_salary_entry.delete(0, tk.END)
        self.manager_id_entry.delete(0, tk.END)

    def add_event(self):
        add_event_window = tk.Toplevel(self.root)
        add_event_window.title("Add Event")
        add_event_window.geometry("400x700")

        # Set background color to black
        add_event_window.configure(bg="black")

        # Create a frame with black background for content
        content_frame = tk.Frame(add_event_window, bg="black")
        content_frame.pack(expand=True, fill="both")

        tk.Label(content_frame, text="Event ID:", fg="green", bg="black").pack()
        self.event_id_entry = tk.Entry(content_frame)
        self.event_id_entry.pack()

        tk.Label(content_frame, text="Event Type:", fg="green", bg="black").pack()
        self.event_type_entry = tk.Entry(content_frame)
        self.event_type_entry.pack()

        tk.Label(content_frame, text="Theme:", fg="green", bg="black").pack()
        self.theme_entry = tk.Entry(content_frame)
        self.theme_entry.pack()

        tk.Label(content_frame, text="Date:", fg="green", bg="black").pack()
        self.date_entry = tk.Entry(content_frame)
        self.date_entry.pack()

        tk.Label(content_frame, text="Time:", fg="green", bg="black").pack()
        self.time_entry = tk.Entry(content_frame)
        self.time_entry.pack()

        tk.Label(content_frame, text="Duration:", fg="green", bg="black").pack()
        self.duration_entry = tk.Entry(content_frame)
        self.duration_entry.pack()

        tk.Label(content_frame, text="Venue Address:", fg="green", bg="black").pack()
        self.venue_address_entry = tk.Entry(content_frame)
        self.venue_address_entry.pack()

        tk.Label(content_frame, text="Client ID:", fg="green", bg="black").pack()
        self.client_id_entry = tk.Entry(content_frame)
        self.client_id_entry.pack()

        tk.Label(content_frame, text="Guest List:", fg="green", bg="black").pack()
        self.guest_list_entry = tk.Entry(content_frame)
        self.guest_list_entry.pack()

        tk.Label(content_frame, text="Catering Company:", fg="green", bg="black").pack()
        self.catering_company_entry = tk.Entry(content_frame)
        self.catering_company_entry.pack()

        tk.Label(content_frame, text="Cleaning Company:", fg="green", bg="black").pack()
        self.cleaning_company_entry = tk.Entry(content_frame)
        self.cleaning_company_entry.pack()

        tk.Label(content_frame, text="Decorations Company:", fg="green", bg="black").pack()
        self.decorations_company_entry = tk.Entry(content_frame)
        self.decorations_company_entry.pack()

        tk.Label(content_frame, text="Entertainment Company:", fg="green", bg="black").pack()
        self.entertainment_company_entry = tk.Entry(content_frame)
        self.entertainment_company_entry.pack()

        tk.Label(content_frame, text="Furniture Supply Company:", fg="green", bg="black").pack()
        self.furniture_supply_company_entry = tk.Entry(content_frame)
        self.furniture_supply_company_entry.pack()

        tk.Label(content_frame, text="Invoice:", fg="green", bg="black").pack()
        self.invoice_entry = tk.Entry(content_frame)
        self.invoice_entry.pack()

        save_button = tk.Button(content_frame, text="Save", fg="green", bg="black")
        save_button.config(command=lambda: self.save_event(add_event_window))  # Pass add_event_window as an argument
        save_button.pack()

    def save_event(self, add_event_window):  # Add add_event_window as an argument
        event_id = self.event_id_entry.get()
        event_type = self.event_type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_address = self.venue_address_entry.get()
        client_id = self.client_id_entry.get()
        guest_list = self.guest_list_entry.get()
        catering_company = self.catering_company_entry.get()
        cleaning_company = self.cleaning_company_entry.get()
        decorations_company = self.decorations_company_entry.get()
        entertainment_company = self.entertainment_company_entry.get()
        furniture_supply_company = self.furniture_supply_company_entry.get()
        invoice = self.invoice_entry.get()

        if all([event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                catering_company, cleaning_company, decorations_company, entertainment_company,
                furniture_supply_company, invoice]):
            event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                          catering_company, cleaning_company, decorations_company, entertainment_company,
                          furniture_supply_company, invoice)
            self.events.append(event)
            self.save_data()
            # You can add any additional actions here after saving the event
            add_event_window.destroy()

        # Clear entry fields after saving
        self.event_id_entry.delete(0, tk.END)
        self.event_type_entry.delete(0, tk.END)
        self.theme_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.venue_address_entry.delete(0, tk.END)
        self.client_id_entry.delete(0, tk.END)
        self.guest_list_entry.delete(0, tk.END)
        self.catering_company_entry.delete(0, tk.END)
        self.cleaning_company_entry.delete(0, tk.END)
        self.decorations_company_entry.delete(0, tk.END)
        self.entertainment_company_entry.delete(0, tk.END)
        self.furniture_supply_company_entry.delete(0, tk.END)
        self.invoice_entry.delete(0, tk.END)

    def add_client(self):
        add_client_window = tk.Toplevel(self.root)
        add_client_window.title("Add Client")
        add_client_window.geometry("400x300")

        # Set background color to black
        add_client_window.configure(bg="black")

        # Create a frame with black background for content
        content_frame = tk.Frame(add_client_window, bg="black")
        content_frame.pack(expand=True, fill="both")

        tk.Label(content_frame, text="Client ID:", fg="green", bg="black").pack()
        self.client_id_entry = tk.Entry(content_frame)
        self.client_id_entry.pack()

        tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
        self.client_name_entry = tk.Entry(content_frame)
        self.client_name_entry.pack()

        tk.Label(content_frame, text="Address:", fg="green", bg="black").pack()
        self.client_address_entry = tk.Entry(content_frame)
        self.client_address_entry.pack()

        tk.Label(content_frame, text="Contact Details:", fg="green", bg="black").pack()
        self.client_contact_entry = tk.Entry(content_frame)
        self.client_contact_entry.pack()

        tk.Label(content_frame, text="Budget:", fg="green", bg="black").pack()
        self.client_budget_entry = tk.Entry(content_frame)
        self.client_budget_entry.pack()

        tk.Button(content_frame, text="Save", fg="green", bg="black",
                  command=lambda: self.save_client(add_client_window)).pack()

    def save_client(self, add_client_window):
        client_id = self.client_id_entry.get()
        name = self.client_name_entry.get()
        address = self.client_address_entry.get()
        contact_details = self.client_contact_entry.get()
        budget = self.client_budget_entry.get()

        if all([client_id, name, address, contact_details, budget]):
            client = Client(client_id, name, address, contact_details, budget)
            self.clients.append(client)
            self.save_data()

            # Clear entry fields after saving
            self.client_id_entry.delete(0, tk.END)
            self.client_name_entry.delete(0, tk.END)
            self.client_address_entry.delete(0, tk.END)
            self.client_contact_entry.delete(0, tk.END)
            self.client_budget_entry.delete(0, tk.END)

            add_client_window.destroy()  # Destroy the window after all operations are completed

    def add_guest(self):
        add_guest_window = tk.Toplevel(self.root)
        add_guest_window.title("Add Guest")
        add_guest_window.geometry("400x300")

        # Set background color to black
        add_guest_window.configure(bg="black")

        # Create a frame with black background for content
        content_frame = tk.Frame(add_guest_window, bg="black")
        content_frame.pack(expand=True, fill="both")

        tk.Label(content_frame, text="Guest ID:", fg="green", bg="black").pack()
        self.guest_id_entry = tk.Entry(content_frame)
        self.guest_id_entry.pack()

        tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
        self.guest_name_entry = tk.Entry(content_frame)
        self.guest_name_entry.pack()

        tk.Label(content_frame, text="Address:", fg="green", bg="black").pack()
        self.guest_address_entry = tk.Entry(content_frame)
        self.guest_address_entry.pack()

        tk.Label(content_frame, text="Contact Details:", fg="green", bg="black").pack()
        self.guest_contact_entry = tk.Entry(content_frame)
        self.guest_contact_entry.pack()

        # Pass add_guest_window argument to self.save_guest() using a lambda function
        tk.config(command=lambda: self.save_guest(add_guest_window))  # Pass add_event_window as an argument
        tk.pack()

    def save_guest(self, add_guest_window):
        guest_id = self.guest_id_entry.get()
        name = self.guest_name_entry.get()
        address = self.guest_address_entry.get()
        contact_details = self.guest_contact_entry.get()

        if all([guest_id, name, address, contact_details]):
            guest = Guest(guest_id, name, address, contact_details)
            self.guests.append(guest)
            self.save_data()

            # Clear entry fields after saving
            self.guest_id_entry.delete(0, tk.END)
            self.guest_name_entry.delete(0, tk.END)
            self.guest_address_entry.delete(0, tk.END)
            self.guest_contact_entry.delete(0, tk.END)

            add_guest_window.destroy()  # Destroy the window after all operations are completed
    def add_supplier(self):
        add_supplier_window = tk.Toplevel(self.root)
        add_supplier_window.title("Add Supplier")
        add_supplier_window.geometry("400x300")

        # Set background color to black
        add_supplier_window.configure(bg="black")

        # Create a frame with black background for content
        content_frame = tk.Frame(add_supplier_window, bg="black")
        content_frame.pack(expand=True, fill="both")

        tk.Label(content_frame, text="Supplier ID:", fg="green", bg="black").pack()
        self.supplier_id_entry = tk.Entry(content_frame)
        self.supplier_id_entry.pack()

        tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
        self.supplier_name_entry = tk.Entry(content_frame)
        self.supplier_name_entry.pack()

        tk.Label(content_frame, text="Address:", fg="green", bg="black").pack()
        self.supplier_address_entry = tk.Entry(content_frame)
        self.supplier_address_entry.pack()

        tk.Label(content_frame, text="Contact Details:", fg="green", bg="black").pack()
        self.supplier_contact_entry = tk.Entry(content_frame)
        self.supplier_contact_entry.pack()

        tk.Label(content_frame, text="Services Offered:", fg="green", bg="black").pack()
        self.supplier_services_entry = tk.Entry(content_frame)
        self.supplier_services_entry.pack()

        tk.Button(content_frame, text="Save", fg="green", bg="black",
                  command=lambda: self.save_supplier(add_supplier_window)).pack()


    def save_supplier(self, add_supplier_window):
        supplier_id = self.supplier_id_entry.get()
        name = self.supplier_name_entry.get()
        address = self.supplier_address_entry.get()
        contact_details = self.supplier_contact_entry.get()
        services_offered = self.supplier_services_entry.get()

        if all([supplier_id, name, address, contact_details, services_offered]):
            supplier = Supplier(supplier_id, name, address, contact_details, services_offered)
            self.suppliers.append(supplier)
            self.save_data()

            # Clear entry fields after saving
            self.supplier_id_entry.delete(0, tk.END)
            self.supplier_name_entry.delete(0, tk.END)
            self.supplier_address_entry.delete(0, tk.END)
            self.supplier_contact_entry.delete(0, tk.END)

            add_supplier_window.destroy()
    def add_venue(self):
        add_venue_window = tk.Toplevel(self.root)
        add_venue_window.title("Add Venue")
        add_venue_window.geometry("400x300")

        # Set background color to black
        add_venue_window.configure(bg="black")

        # Create a frame with black background for content
        content_frame = tk.Frame(add_venue_window, bg="black")
        content_frame.pack(expand=True, fill="both")

        tk.Label(content_frame, text="Venue ID:", fg="green", bg="black").pack()
        self.venue_id_entry = tk.Entry(content_frame)
        self.venue_id_entry.pack()

        tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
        self.venue_name_entry = tk.Entry(content_frame)
        self.venue_name_entry.pack()

        tk.Label(content_frame, text="Address:", fg="green", bg="black").pack()
        self.venue_address_entry = tk.Entry(content_frame)
        self.venue_address_entry.pack()

        tk.Label(content_frame, text="Contact:", fg="green", bg="black").pack()
        self.venue_contact_entry = tk.Entry(content_frame)
        self.venue_contact_entry.pack()

        tk.Label(content_frame, text="Minimum Guests:", fg="green", bg="black").pack()
        self.min_guests_entry = tk.Entry(content_frame)
        self.min_guests_entry.pack()

        tk.Label(content_frame, text="Maximum Guests:", fg="green", bg="black").pack()
        self.max_guests_entry = tk.Entry(content_frame)
        self.max_guests_entry.pack()

        tk.Button(content_frame, text="Save", fg="green", bg="black", command=self.save_venue).pack()

    def save_venue(self, add_venue_window):
        venue_id = self.venue_id_entry.get()
        name = self.venue_name_entry.get()
        address = self.venue_address_entry.get()
        contact = self.venue_contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        if all([venue_id, name, address, contact, min_guests, max_guests]):
            venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
            self.venues.append(venue)
            self.save_data()
            # Additional actions after saving can be added here
            add_venue_window.destroy()

        # Clear entry fields after saving
        self.venue_id_entry.delete(0, tk.END)
        self.venue_name_entry.delete(0, tk.END)
        self.venue_address_entry.delete(0, tk.END)
        self.venue_contact_entry.delete(0, tk.END)
        self.min_guests_entry.delete(0, tk.END)
        self.max_guests_entry.delete(0, tk.END)


from data_handler import DataHandler

class Event_Organizer_App:
    def __init__(self, root):
        self.main_menu_frame = None
        self.root = root
        self.root.title("Event Organizer App")
        self.root.geometry("800x600")
        self.root.configure(bg="black")
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use a different theme for ttk widgets

        self.employees, self.events, self.clients, self.guests, self.suppliers, self.venues = DataHandler.load_data()  # Load existing data or create new data
        self.create_main_menu()

    def create_main_menu(self):
        self.main_menu_frame = tk.Frame(self.root)
        self.main_menu_frame = tk.Frame(self.root, bg="black")
        self.main_menu_frame.pack(pady=20)

        buttons = [
            ("Add Employee", self.add_employee),
            ("Add Event", self.add_event),
            ("Add Client", self.add_client),
            ("Add Guest", self.add_guest),
            ("Add Supplier", self.add_supplier),
            ("Add Venue", self.add_venue),
            ("Display Employees", lambda: self.display_data("Employees")),
            ("Display Events", lambda: self.display_data("Events")),
            ("Display Clients", lambda: self.display_data("Clients")),
            ("Display Guests", lambda: self.display_data("Guests")),
            ("Display Suppliers", lambda: self.display_data("Suppliers")),
            ("Display Venues", lambda: self.display_data("Venues"))
        ]

        for text, command in buttons:
            tk.Button(self.main_menu_frame, text=text, command=command, width=20, height=2, bg="#4CAF50", fg="white").pack(fill=tk.X, padx=10, pady=5)


    def save_data(self):
        DataHandler.save_data(self.employees, self.events, self.clients, self.guests, self.suppliers, self.venues)

    
    def display_data(self, data_type):
        display_window = tk.Toplevel(self.root)
        display_window.title(f"Display {data_type}")

        data_list = getattr(self, data_type.lower())  # Get the list of data based on data_type
        
        columns = self.get_columns(data_type)
        tree = ttk.Treeview(display_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
        
        for data_item in data_list:
            data_info = self.get_data_info(data_item, data_type)
            tree.insert('', 'end', values=data_info)

        tree.pack(expand=True, fill="both")
            
    def get_columns(self, data_type):
        if data_type == "Employees":
            return ["Name", "ID", "Department", "Job Title", "Basic Salary", "Manager ID"]
        elif data_type == "Events":
            return ["ID", "Type", "Theme", "Date", "Time", "Duration", "Venue Address", "Client ID", "Guest List", "Catering Company", "Cleaning Company", "Decorations Company", "Entertainment Company", "Furniture Supply Company", "Invoice"]
        elif data_type == "Clients":
            return ["ID", "Name", "Address", "Contact Details", "Budget"]
        elif data_type == "Guests":
            return ["ID", "Name", "Address", "Contact Details"]
        elif data_type == "Suppliers":
            return ["ID", "Name", "Address", "Contact Details", "Services Offered"]
        elif data_type == "Venues":
            return ["ID", "Name", "Address", "Contact", "Min Guests", "Max Guests"]
            
    def get_data_info(self, data_item, data_type):
        if data_type == "Employees":
            return data_item.name, data_item.employee_id, data_item.department, data_item.job_title, data_item.basic_salary, data_item.manager_id
        elif data_type == "Events":
            return (data_item.event_id, data_item.event_type, data_item.theme, data_item.date, data_item.time, data_item.duration, data_item.venue_address, data_item.client_id, data_item.guest_list, data_item.catering_company, data_item.cleaning_company, data_item.decorations_company, data_item.entertainment_company, data_item.furniture_supply_company, data_item.invoice)
        elif data_type == "Clients":
            return (data_item.client_id, data_item.name, data_item.address, data_item.contact_details, data_item.budget)
        elif data_type == "Guests":
            return (data_item.guest_id, data_item.name, data_item.address, data_item.contact_details)
        elif data_type == "Suppliers":
            return (data_item.supplier_id, data_item.name, data_item.address, data_item.contact_details, data_item.services_offered)
        elif data_type == "Venues":
            return (data_item.venue_id, data_item.name, data_item.address, data_item.contact, data_item.min_guests, data_item.max_guests)

    def add_employee(self):
     add_employee_window = tk.Toplevel(self.root)
     add_employee_window.title("Add Employee")
     add_employee_window.geometry("400x300")
    
    # Set background color to black
     add_employee_window.configure(bg="black")
    
    # Create a frame with black background for content
     content_frame = tk.Frame(add_employee_window, bg="black")
     content_frame.pack(expand=True, fill="both")
    
     tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
     self.name_entry = tk.Entry(content_frame)
     self.name_entry.pack()
    
     tk.Label(content_frame, text="Employee ID:", fg="green", bg="black").pack()
     self.employee_id_entry = tk.Entry(content_frame)
     self.employee_id_entry.pack()
    
     tk.Label(content_frame, text="Department:", fg="green", bg="black").pack()
     self.department_entry = tk.Entry(content_frame)
     self.department_entry.pack()
    
     tk.Label(content_frame, text="Job Title:", fg="green", bg="black").pack()
     self.job_title_entry = tk.Entry(content_frame)
     self.job_title_entry.pack()
    
     tk.Label(content_frame, text="Basic Salary:", fg="green", bg="black").pack()
     self.basic_salary_entry = tk.Entry(content_frame)
     self.basic_salary_entry.pack()
    
     tk.Label(content_frame, text="Manager ID:", fg="green", bg="black").pack()
     self.manager_id_entry = tk.Entry(content_frame)
     self.manager_id_entry.pack()
    
     tk.Button(content_frame, text="Save", command=self.save_employee, fg="green", bg="black").pack()

    def save_employee(self):
     name = self.name_entry.get()
     employee_id = self.employee_id_entry.get()
     department = self.department_entry.get()
     job_title = self.job_title_entry.get()
     basic_salary = self.basic_salary_entry.get()
     manager_id = self.manager_id_entry.get()

     if name and employee_id and department and job_title and basic_salary and manager_id:
        employee = Employee(name, employee_id, department, job_title, basic_salary, manager_id)
        self.employees.append(employee)
        self.save_data()

     self.name_entry.delete(0, tk.END)
     self.employee_id_entry.delete(0, tk.END)
     self.department_entry.delete(0, tk.END)
     self.job_title_entry.delete(0, tk.END)
     self.basic_salary_entry.delete(0, tk.END)
     self.manager_id_entry.delete(0, tk.END) 
     
    def add_event(self):
     add_event_window = tk.Toplevel(self.root)
     add_event_window.title("Add Event")
     add_event_window.geometry("400x700")
    
    # Set background color to black
     add_event_window.configure(bg="black")
    
    # Create a frame with black background for content
     content_frame = tk.Frame(add_event_window, bg="black")
     content_frame.pack(expand=True, fill="both")
    
     tk.Label(content_frame, text="Event ID:", fg="green", bg="black").pack()
     self.event_id_entry = tk.Entry(content_frame)
     self.event_id_entry.pack()

     tk.Label(content_frame, text="Event Type:", fg="green", bg="black").pack()
     self.event_type_entry = tk.Entry(content_frame)
     self.event_type_entry.pack()

     tk.Label(content_frame, text="Theme:", fg="green", bg="black").pack()
     self.theme_entry = tk.Entry(content_frame)
     self.theme_entry.pack()

     tk.Label(content_frame, text="Date:", fg="green", bg="black").pack()
     self.date_entry = tk.Entry(content_frame)
     self.date_entry.pack()

     tk.Label(content_frame, text="Time:", fg="green", bg="black").pack()
     self.time_entry = tk.Entry(content_frame)
     self.time_entry.pack()

     tk.Label(content_frame, text="Duration:", fg="green", bg="black").pack()
     self.duration_entry = tk.Entry(content_frame)
     self.duration_entry.pack()

     tk.Label(content_frame, text="Venue Address:", fg="green", bg="black").pack()
     self.venue_address_entry = tk.Entry(content_frame)
     self.venue_address_entry.pack()

     tk.Label(content_frame, text="Client ID:", fg="green", bg="black").pack()
     self.client_id_entry = tk.Entry(content_frame)
     self.client_id_entry.pack()

     tk.Label(content_frame, text="Guest List:", fg="green", bg="black").pack()
     self.guest_list_entry = tk.Entry(content_frame)
     self.guest_list_entry.pack()

     tk.Label(content_frame, text="Catering Company:", fg="green", bg="black").pack()
     self.catering_company_entry = tk.Entry(content_frame)
     self.catering_company_entry.pack()

     tk.Label(content_frame, text="Cleaning Company:", fg="green", bg="black").pack()
     self.cleaning_company_entry = tk.Entry(content_frame)
     self.cleaning_company_entry.pack()

     tk.Label(content_frame, text="Decorations Company:", fg="green", bg="black").pack()
     self.decorations_company_entry = tk.Entry(content_frame)
     self.decorations_company_entry.pack()

     tk.Label(content_frame, text="Entertainment Company:", fg="green", bg="black").pack()
     self.entertainment_company_entry = tk.Entry(content_frame)
     self.entertainment_company_entry.pack()

     tk.Label(content_frame, text="Furniture Supply Company:", fg="green", bg="black").pack()
     self.furniture_supply_company_entry = tk.Entry(content_frame)
     self.furniture_supply_company_entry.pack()

     tk.Label(content_frame, text="Invoice:", fg="green", bg="black").pack()
     self.invoice_entry = tk.Entry(content_frame)
     self.invoice_entry.pack()

     save_button = tk.Button(content_frame, text="Save", fg="green", bg="black")
     save_button.config(command=lambda: self.save_event(add_event_window))  # Pass add_event_window as an argument
     save_button.pack()

     
    def save_event(self, add_event_window):  # Add add_event_window as an argument
     event_id = self.event_id_entry.get()
     event_type = self.event_type_entry.get()
     theme = self.theme_entry.get()
     date = self.date_entry.get()
     time = self.time_entry.get()
     duration = self.duration_entry.get()
     venue_address = self.venue_address_entry.get()
     client_id = self.client_id_entry.get()
     guest_list = self.guest_list_entry.get()
     catering_company = self.catering_company_entry.get()
     cleaning_company = self.cleaning_company_entry.get()
     decorations_company = self.decorations_company_entry.get()
     entertainment_company = self.entertainment_company_entry.get()
     furniture_supply_company = self.furniture_supply_company_entry.get()
     invoice = self.invoice_entry.get()

     if all([event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_supply_company, invoice]):
        event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_supply_company, invoice)
        self.events.append(event)
        self.save_data()
        # You can add any additional actions here after saving the event
        add_event_window.destroy()

    # Clear entry fields after saving
     self.event_id_entry.delete(0, tk.END)
     self.event_type_entry.delete(0, tk.END)
     self.theme_entry.delete(0, tk.END)
     self.date_entry.delete(0, tk.END)
     self.time_entry.delete(0, tk.END)
     self.duration_entry.delete(0, tk.END)
     self.venue_address_entry.delete(0, tk.END)
     self.client_id_entry.delete(0, tk.END)
     self.guest_list_entry.delete(0, tk.END)
     self.catering_company_entry.delete(0, tk.END)
     self.cleaning_company_entry.delete(0, tk.END)
     self.decorations_company_entry.delete(0, tk.END)
     self.entertainment_company_entry.delete(0, tk.END)
     self.furniture_supply_company_entry.delete(0, tk.END)
     self.invoice_entry.delete(0, tk.END)

    
    def add_client(self):
     add_client_window = tk.Toplevel(self.root)
     add_client_window.title("Add Client")
     add_client_window.geometry("400x300")
    
    # Set background color to black
     add_client_window.configure(bg="black")
    
    # Create a frame with black background for content
     content_frame = tk.Frame(add_client_window, bg="black")
     content_frame.pack(expand=True, fill="both")
    
     tk.Label(content_frame, text="Client ID:", fg="green", bg="black").pack()
     self.client_id_entry = tk.Entry(content_frame)
     self.client_id_entry.pack()

     tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
     self.client_name_entry = tk.Entry(content_frame)
     self.client_name_entry.pack()

     tk.Label(content_frame, text="Address:", fg="green", bg="black").pack()
     self.client_address_entry = tk.Entry(content_frame)
     self.client_address_entry.pack()

     tk.Label(content_frame, text="Contact Details:", fg="green", bg="black").pack()
     self.client_contact_entry = tk.Entry(content_frame)
     self.client_contact_entry.pack()

     tk.Label(content_frame, text="Budget:", fg="green", bg="black").pack()
     self.client_budget_entry = tk.Entry(content_frame)
     self.client_budget_entry.pack()

     tk.Button(content_frame, text="Save", fg="green", bg="black", command=lambda: self.save_client(add_client_window)).pack()
    def save_client(self, add_client_window):
     client_id = self.client_id_entry.get()
     name: str = self.client_name_entry.get()
     address = self.client_address_entry.get()
     contact_details = self.client_contact_entry.get()
     budget = self.client_budget_entry.get()

     if all([client_id, name, address, contact_details, budget]):
         client = Client(client_id, name, address, contact_details, budget)
         self.clients.append(client)
         self.save_data()
         add_client_window.destroy()

    # Clear entry fields after saving
     self.client_id_entry.delete(0, tk.END)
     self.client_name_entry.delete(0, tk.END)
     self.client_address_entry.delete(0, tk.END)
     self.client_contact_entry.delete(0, tk.END)
     self.client_budget_entry.delete(0, tk.END)
    
    def add_guest(self):
     add_guest_window = tk.Toplevel(self.root)
     add_guest_window.title("Add Guest")
     add_guest_window.geometry("400x300")
    
    # Set background color to black
     add_guest_window.configure(bg="black")
    
    # Create a frame with black background for content
     content_frame = tk.Frame(add_guest_window, bg="black")
     content_frame.pack(expand=True, fill="both")
    
     tk.Label(content_frame, text="Guest ID:", fg="green", bg="black").pack()
     self.guest_id_entry = tk.Entry(content_frame)
     self.guest_id_entry.pack()

     tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
     self.guest_name_entry = tk.Entry(content_frame)
     self.guest_name_entry.pack()

     tk.Label(content_frame, text="Address:", fg="green", bg="black").pack()
     self.guest_address_entry = tk.Entry(content_frame)
     self.guest_address_entry.pack()

     tk.Label(content_frame, text="Contact Details:", fg="green", bg="black").pack()
     self.guest_contact_entry = tk.Entry(content_frame)
     self.guest_contact_entry.pack()

     save_button = tk.Button(content_frame, text="Save", fg="green", bg="black")
     save_button.config(command=lambda: self.save_guest(add_guest_window))  # Pass add_event_window as an argument
     save_button.pack()

    def save_guest(self, add_guest_window):
        guest_id = self.guest_id_entry.get()
        name = self.guest_name_entry.get()
        address = self.guest_address_entry.get()
        contact_details = self.guest_contact_entry.get()

        if all([guest_id, name, address, contact_details]):
            guest = Guest(guest_id, name, address, contact_details)
            self.guests.append(guest)
            self.save_data()
            add_guest_window.destroy()  # Destroy the window
            # Clear entry fields after saving
            self.guest_id_entry.delete(0, tk.END)
            self.guest_name_entry.delete(0, tk.END)
            self.guest_address_entry.delete(0, tk.END)
            self.guest_contact_entry.delete(0, tk.END)

    # noinspection PyTypeChecker
    def add_supplier(self):
     add_supplier_window = tk.Toplevel(self.root)
     add_supplier_window.title("Add Supplier")
     add_supplier_window.geometry("400x300")
    
    # Set background color to black
     add_supplier_window.configure(bg="black")
    
    # Create a frame with black background for content
     content_frame = tk.Frame(add_supplier_window, bg="black")
     content_frame.pack(expand=True, fill="both")
    
     tk.Label(content_frame, text="Supplier ID:", fg="green", bg="black").pack()
     self.supplier_id_entry = tk.Entry(content_frame)
     self.supplier_id_entry.pack()

     tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
     self.supplier_name_entry = tk.Entry(content_frame)
     self.supplier_name_entry.pack()

     tk.Label(content_frame, text="Address:", fg="green", bg="black").pack()
     self.supplier_address_entry = tk.Entry(content_frame)
     self.supplier_address_entry.pack()

     tk.Label(content_frame, text="Contact Details:", fg="green", bg="black").pack()
     self.supplier_contact_entry = tk.Entry(content_frame)
     self.supplier_contact_entry.pack()

     tk.Label(content_frame, text="Services Offered:", fg="green", bg="black").pack()
     self.supplier_services_entry = tk.Entry(content_frame)
     self.supplier_services_entry.pack()

     saves_button = tk.Button(content_frame, text="Save", fg="green", bg="black")
     saves_button.config(command=lambda: self.save_supplier(add_supplier_window))  # Pass add_event_window as an argument
     saves_button.pack()

    def save_supplier(self,add_supplier_window):
     supplier_id = self.supplier_id_entry.get()
     name = self.supplier_name_entry.get()
     address = self.supplier_address_entry.get()
     contact_details = self.supplier_contact_entry.get()
     services_offered = self.supplier_services_entry.get()

     if all([supplier_id, name, address, contact_details, services_offered]):
        supplier = Supplier(supplier_id, name, address, contact_details, services_offered)
        self.suppliers.append(supplier)
        self.save_data()
        # Additional actions after saving can be added here
        add_supplier_window.destroy()

    # Clear entry fields after saving
     self.supplier_id_entry.delete(0, tk.END)
     self.supplier_name_entry.delete(0, tk.END)
     self.supplier_address_entry.delete(0, tk.END)
     self.supplier_contact_entry.delete(0, tk.END)
     self.supplier_services_entry.delete(0, tk.END)
    
    def add_venue(self):
     add_venue_window = tk.Toplevel(self.root)
     add_venue_window.title("Add Venue")
     add_venue_window.geometry("400x300")
    
    # Set background color to black
     add_venue_window.configure(bg="black")
    
    # Create a frame with black background for content
     content_frame = tk.Frame(add_venue_window, bg="black")
     content_frame.pack(expand=True, fill="both")
    
     tk.Label(content_frame, text="Venue ID:", fg="green", bg="black").pack()
     self.venue_id_entry = tk.Entry(content_frame)
     self.venue_id_entry.pack()

     tk.Label(content_frame, text="Name:", fg="green", bg="black").pack()
     self.venue_name_entry = tk.Entry(content_frame)
     self.venue_name_entry.pack()

     tk.Label(content_frame, text="Address:", fg="green", bg="black").pack()
     self.venue_address_entry = tk.Entry(content_frame)
     self.venue_address_entry.pack()

     tk.Label(content_frame, text="Contact:", fg="green", bg="black").pack()
     self.venue_contact_entry = tk.Entry(content_frame)
     self.venue_contact_entry.pack()

     tk.Label(content_frame, text="Minimum Guests:", fg="green", bg="black").pack()
     self.min_guests_entry = tk.Entry(content_frame)
     self.min_guests_entry.pack()

     tk.Label(content_frame, text="Maximum Guests:", fg="green", bg="black").pack()
     self.max_guests_entry = tk.Entry(content_frame)
     self.max_guests_entry.pack()

     savees_button = tk.Button(content_frame, text="Save", fg="green", bg="black")
     savees_button.config(
         command=lambda: self.save_venue(add_venue_window))  # Pass add_event_window as an argument
     savees_button.pack()

    def save_venue(self,add_venue_window):
     venue_id = self.venue_id_entry.get()
     name = self.venue_name_entry.get()
     address = self.venue_address_entry.get()
     contact = self.venue_contact_entry.get()
     min_guests = self.min_guests_entry.get()
     max_guests = self.max_guests_entry.get()

     if all([venue_id, name, address, contact, min_guests, max_guests]):
        venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
        self.venues.append(venue)
        self.save_data()
        # Additional actions after saving can be added here
        add_venue_window.destroy()

    # Clear entry fields after saving
     self.venue_id_entry.delete(0, tk.END)
     self.venue_name_entry.delete(0, tk.END)
     self.venue_address_entry.delete(0, tk.END)
     self.venue_contact_entry.delete(0, tk.END)
     self.min_guests_entry.delete(0, tk.END)
     self.max_guests_entry.delete(0, tk.END)
              