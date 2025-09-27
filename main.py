from event import Event
from scheduler import EventScheduler
from utils import print_events
from sample_data import load_sample_events

def menu():
    print("\n📅 Event Scheduler Menu")
    print("1. Add Event")
    print("2. View Events by Date")
    print("3. View Next Event")
    print("4. Delete Event")
    print("5. Exit")

def main():
    scheduler = EventScheduler()

    # Load some sample events
    for e in load_sample_events():
        scheduler.add_event(e)

    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Enter title: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            location = input("Enter location: ")
            priority = int(input("Enter priority (0-5): "))
            event = Event(title, date, time, location, priority)
            scheduler.add_event(event)
            print("✅ Event added successfully!")

        elif choice == "2":
            date_str = input("Enter date (YYYY-MM-DD): ")
            events = scheduler.get_events_by_date(date_str)
            print_events(events)

        elif choice == "3":
            event = scheduler.get_next_event()
            print("Next Event:", event if event else "None")

        elif choice == "4":
            title = input("Enter title of event to delete: ")
            success = scheduler.delete_event(title)
            print("🗑️ Deleted successfully!" if success else "⚠️ Event not found.")

        elif choice == "5":
            print("👋 Exiting Event Scheduler. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
