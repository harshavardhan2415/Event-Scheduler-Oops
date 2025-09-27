from event import Event
def load_sample_events():
    return[
           Event("Doctor Appointment", "2025-10-02", "14:30", "Clinic", 2),
        Event("Team Meeting", "2025-10-01", "10:00", "Office", 1),
        Event("Birthday Party", "2025-10-05", "18:00", "Home", 0),
    ]