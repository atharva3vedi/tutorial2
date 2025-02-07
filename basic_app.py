import sys
import tkinter as tk

class PresentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Presentation Software")
        
        self.slides = ["Welcome Slide", "AI in PowerPoint", "Conclusion"]
        self.current_slide = 0
        
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack()
        
        self.add_button = tk.Button(root, text="Add Slide", command=self.add_slide)
        self.add_button.pack()
        
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_slide)
        self.prev_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_slide)
        self.next_button.pack(side=tk.RIGHT, padx=20, pady=10)
        
        self.display_slide()
        
    def display_slide(self):
        self.canvas.delete("all")
        slide_text = self.slides[self.current_slide]
        self.canvas.create_text(300, 200, text=slide_text, font=("Arial", 20), fill="black")
    
    def next_slide(self):
        if self.current_slide < len(self.slides) - 1:
            self.current_slide += 1
            self.display_slide()
    
    def prev_slide(self):
        if self.current_slide > 0:
            self.current_slide -= 1
            self.display_slide()
    
    def add_slide(self):
        new_slide_text = self.entry.get()
        if new_slide_text:
            self.slides.append(new_slide_text)
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = PresentationApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
