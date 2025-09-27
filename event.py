from datetime import datetime
class Event:
    def __init__(self,title,date,time,location,priority=0):
        self.title=title
        self.datetime=datetime.strptime(f"{date} {time}","%Y-%m-%d %H:%M")
        self.location=location
        self.priority=priority
    def __lt__(self,other):
        return self.datetime < other.datetime
    def __repr__(self):
        return f"{self.title} at {self.location} on {self.datetime.strftime('%Y-%m-%d %H:%M')}"
    
    