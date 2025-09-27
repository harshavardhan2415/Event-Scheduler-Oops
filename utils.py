def print_events(events):
    if not events:
        print("No events found.")
    else:
        for idx, event in enumerate(events, 1):
            print(f"{idx}. {event}")