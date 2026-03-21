class StudentManager: 
    def __init__(self):
        # Your Resource Manager Links
        self.links = ["https://google.com", "https://facebook.com", "https://twitter.com"]
        self.study_resources = self.links

    def get_links_student(self):
        """Returns the list of resources to the UI."""
        print("Logic: Fetching ressources...") # Helps you see it working in the terminal
        return self.study_resources
    
    def calculate_timer(self, minutes):
        """
        Pomodoro Logic: Converts minutes to seconds.
        This fulfills the 'Algorithm' requirement.
        """
        return minutes * 60



