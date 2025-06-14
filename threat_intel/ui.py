import tkinter as tk
from threading import Thread
from .platform import ThreatIntelPlatform

class ThreatIntelUI(tk.Tk):
    """Simple Tkinter UI for ThreatIntelPlatform."""
    def __init__(self):
        super().__init__()
        self.title("Threat Intel Platform")
        self.platform = ThreatIntelPlatform()
        self.label = tk.Label(self, text="Click Refresh to fetch data.")
        self.label.pack(padx=20, pady=10)
        refresh_btn = tk.Button(self, text="Refresh", command=self.refresh)
        refresh_btn.pack(pady=(0, 10))

    def refresh(self):
        self.label.config(text="Fetching...")
        def fetch():
            try:
                result = self.platform.daily_attacked()
            except Exception as e:
                result = f"Error: {e}"
            self.label.after(0, lambda: self.label.config(text=result))
        Thread(target=fetch, daemon=True).start()

if __name__ == "__main__":
    app = ThreatIntelUI()
    app.mainloop()
