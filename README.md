# currency_convertor
📌 Introduction

The Currency Converter is a Python-based application that allows users to convert one currency into another using real-time or predefined exchange rates. This project helps in understanding API integration, user input handling, and basic financial calculations.

🎯 Objective

The main objective of this project is to:

Convert currencies accurately between different countries
Learn how to work with APIs (for live exchange rates)
Practice Python programming concepts
Build a useful real-world application
⚙️ Features
Convert one currency to another (e.g., USD to INR)
Supports multiple international currencies
Real-time exchange rates (if API is used)
User-friendly interface (CLI / GUI)
Error handling for invalid inputs
🛠️ Technologies Used
Python 3
Requests library (for API calls)
JSON handling
(Optional) Tkinter for GUI
🧠 Working Principle
The user enters:
Base currency (e.g., USD)
Target currency (e.g., INR)
Amount to convert
The program fetches exchange rates using an API or predefined data.
The conversion is calculated using the formula:
Converted Amount = Amount × Exchange Rate
The result is displayed to the user.
📂 Project Structure
currency-converter/
│── converter.py        # Main program
│── config.py           # API key (if used)
│── requirements.txt    # Dependencies
│── README.md           # Documentation
▶️ How to Run
Clone the repository
git clone https://github.com/Manshi-Chauhan/currency_convertor
Navigate to the project folder
cd currency-converter
Install dependencies
pip install -r requirements.txt
Run the program
python converter.py
📊 Example Output
Enter base currency: USD  
Enter target currency: INR  
Enter amount: 10  

Converted Amount: 830 INR
⚠️ Error Handling
Handles invalid currency codes
Prevents negative or non-numeric inputs
Manages API/network errors gracefully
🔮 Future Enhancements
Add graphical user interface (GUI)
Support cryptocurrency conversion
Store conversion history
Add currency trends and charts
👨‍💻 Conclusion

This project demonstrates how Python can be used to build practical applications involving real-time data and user interaction. It is a great beginner-to-intermediate level project.

👤 Author

Your Name
Manshi Chauhan
