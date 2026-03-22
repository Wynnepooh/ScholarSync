import tkinter as tk
import time 
import threading
from abc import ABC, abstractmethod

# 1. The Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, seconds) :
         pass 
    
# 2. The Subject (Logic
class TimerSubject:
    def __init__(self):
        self.observers = []
        self._time = 1500 # 25 Minutes
        
    def attach(self, observer):
        
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._time)
    
    def start(self):
        while self._time > 0:
            time.sleep(1) 
            self._time -= 1
            self.notify()

            # 3. The Concrete Observer (GUI) 
class TimerGUI(tk.Tk, Observer):
    def __init__(self, root):
        self.label = tk.Label(root, text="25:00", font=("Arial", 50))
        self.label.pack(pady=50) 
        
    def update(self, seconds):
        mins, secs = divmod(seconds, 60)
      
        self.label.config(text=f"{mins:02d}:{secs:02d}")

        # Execution
if __name__ == "__main__":
    root = tk.Tk()  
    root.title("ScholarSync Timer")
   
    timer_subject = TimerSubject()
    timer_gui = TimerGUI(root)
    timer_subject.attach(timer_gui)

    # Run the timer in a separate thread to keep the GUI doesn't freeze

    threading.Thread(target=timer_subject.start, daemon=True).start()

    root.mainloop()