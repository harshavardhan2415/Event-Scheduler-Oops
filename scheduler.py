from datetime import datetime
import heapq

class EventScheduler:
    def __init__(self):
        self.events_heap=[]
        self.events_by_date={}
    def add_event(self,event):
        heapq.heappush(self.events_heap,event)
        date_key=event.datetime.date()
        if date_key not in self.events_by_date:
            self.events_by_date[date_key]=[]
        self.events_by_date[date_key].append(event)
    def get_next_event(self):
        return self.events_heap[0] if self.events_heap else None
    def get_events_by_date(self,date_str):
        date_key=datetime.strptime(date_str,"%Y-%m-%d").date()
        return sorted(self.events_by_date.get(date_key,[]))
    def delete_event(self,title):
        for event in self.events_heap:
            if event.title==title:
                self.events_heap.remove(event)
                heapq.heapify(self.events_heap)
                self.events_by_date[event.datetime.date()].remove(event)
                return True
            return False