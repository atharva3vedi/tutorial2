Simple Presentation Software
Project Contributors
•	Atharva Trivedi 
•	Ashlesha Virulkar
• Priyanshu Kundu 
Project Overview
This project involves the design and development of a simple presentation software that allows users to:
1.	Create, edit, and navigate through slides.
2.	Format and structure slide content with text, images, and simple shapes.
3.	Navigate between slides using Next, Previous, First, and Last options.
4.	Implement optional AI-powered text summarization using ONNX Runtime for efficient execution.
________________________________________


Key Features
1. Slide Editor
•	Users can create and edit slides by adding titles and body text.
•	Users can insert images into slides.
•	Delete functionality allows users to remove unwanted slides.
2. Slide Navigation
•	Navigate between slides using Next and Previous buttons.
•	The first slide is displayed upon application startup.
3. File Handling & Persistence
•	Save presentations in JSON format.
•	Load presentations from saved JSON files.
•	Maintain text and image information when saving and loading presentations.
4. AI-Powered Features
•	AI-driven text summarization using Groq's API for efficient and intelligent slide content generation.
________________________________________

Technical Architecture
1. UI Management
The user interface is developed using tkinter. It provides the following key components:
•	Top Frame: Contains buttons for adding, deleting, saving, and loading slides.
•	Canvas Widget: Displays slide content, including text and images.
•	Navigation Buttons: Provides navigation controls for moving between slides.
2. Slide Manager
•	Stores a list of slides, each containing title, text, and optional image data.
•	Provides functions for adding and deleting slides.
3. Rendering Engine
•	Displays slide content (text and images) on the canvas.
•	Handles dynamic resizing and placement of text and image elements.
4. File Storage
•	JSON format is used to store presentation data.
•	Images are stored as file paths and reloaded upon loading presentations.
5. AI Integration
•	Groq’s API is used to provide AI-driven text summarization.
•	llama-3.3-70b-versatile model generates concise summaries of slide content.
________________________________________

Dependencies
•	tkinter: For the GUI interface
•	Pillow: For image handling
•	json: For file handling
•	Groq: For AI-based summarization
________________________________________

How to Run the Application
1.	Install all required dependencies.
2.	Run the basic_app.py script.
3.	Use the GUI to create and manage slides.
4.	Save presentations using the "Save" button and load them later with the "Load" button.
5.	Generate AI-based text summaries by clicking the "AI Summary" button.
 
Challenges and Key Learnings
Challenges
•	Efficiently rendering text and images on a canvas.
•	Managing file persistence while preserving image references.
•	Integrating AI features seamlessly with the UI.
Key Learnings
•	Improved understanding of tkinter for GUI design.
•	Effective management of multimedia content in Python applications.
•	Practical application of AI-based text summarization.
________________________________________
Future Improvements
1.	Enhanced Multimedia Support: Add video and advanced shape handling.
2.	Collaborative Editing: Support cloud-based editing and storage.
3.	AI Enhancement: Use ONNX Runtime for optimized AI inference.
4.	Advanced Slide Design: Implement templates and themes for slide design.
________________________________________
Conclusion
This project demonstrates a functional, GUI-based presentation software with support for AI-driven features. It serves as a foundation for building more advanced presentation tools in the future.

