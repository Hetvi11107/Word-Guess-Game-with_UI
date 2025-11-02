# Word-Guess-Game-with_UI

## 🧩 Word Guess Game (Flask)

A fun web-based "Guess the Country Name" game built with Python Flask.
The player has to guess letters to reveal a hidden country name before running out of chances!

## 🚀 Features

🎮 Interactive country name guessing game
💡 10 chances to guess the correct word
🏁 Win/Lose message at the end of each round
🔁 Option to replay the game instantly
💻 Simple Flask backend with session-based state
🎨 Responsive UI with HTML & CSS

## 🧠 How the Game Works

The game randomly selects a country name from the list.
You have 10 guesses to find all the letters.
Each correct letter fills its position in the word.
Each wrong guess decreases your remaining chances.
The game ends when:
    ✅ You guess all letters → You Win!
    ❌ You run out of guesses → You Lose!

## 🧾 Project Structure
word-guess-game/<br>
│<br>
├── app.py                    # Main Flask application<br>
├── templates/<br>
│   ├── gamehomepage.html      # Start screen<br>
│   └── gameplay.html          # Game <br>
│<br>
├── static/<br>
│   └── game.css               # Styling for both pages<br>
│<br>
├── requirements.txt           # Python dependencies<br>
└── README.md                  # Project documentation<br>

## ⚙️ Installation and Setup
## 1️⃣ Clone this repository
git clone https://github.com/yourusername/word-guess-game.git
cd word-guess-game

## 2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate     # for Windows
# OR
source venv/bin/activate  # for macOS/Linux

## 3️⃣ Install dependencies
pip install -r requirements.txt

## 4️⃣ Run the Flask app
python app.py

## 5️⃣ Open in browser

Visit → http://127.0.0.1:5000

## 🧩 Requirements

Create a file named requirements.txt and include:
Flask==3.0.3

## 🖼️ Screens

Home Page:
➡️ Click “Start” to begin the game

Game Page:
Enter a letter
See remaining guesses
Get instant win/lose feedback

## 🛠️ Technologies Used

Python (Flask) — Backend web framework
HTML5, CSS3 — Frontend design
Jinja2 — Template rendering

## 📦 Future Enhancements

✅ Add scoring system
🎨 Improve animations
🌍 Add difficulty levels
📱 Make fully mobile responsive

## 💡 Author
🎓 Diploma in IT | 💡 Tech & Cyber Security 🌐 GitHub Profile https://github.com/Hetvi11107