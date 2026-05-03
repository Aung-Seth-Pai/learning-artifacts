from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        pass

class EmailNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"Email: {message}"

class SlackNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"Slack: {message}"
        
class AlertSystem(ABC):
    @abstractmethod
    def create_notifier(self) -> Notifier:
        pass

    def trigger_alert(self, message: str) -> str:
        notifier = self.create_notifier()
        return notifier.send(message)

class DailyAlertSender(AlertSystem):
     def create_notifier(self) -> Notifier:
        return EmailNotifier()
    
class CritialAlertSender(AlertSystem):
    def create_notifier(self) -> Notifier:
        return SlackNotifier()

# --- Client Code ---
def process_incident(system: AlertSystem, incident: str):
    """The client doesn't know or care how the alert is delivered."""
    result = system.trigger_alert(incident)
    print(result)

if __name__ == "__main__":
    print("--- Routine Data Sync ---")
    routine_system = DailyAlertSender()
    process_incident(routine_system, "Daily solar irradiance data loaded successfully.")

    print("\n--- Pipeline Crash ---")
    crash_system = CritialAlertSender()
    process_incident(crash_system, "CRITICAL: Database connection timeout!")