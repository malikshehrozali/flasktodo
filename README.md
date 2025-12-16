# Flask Todo App

A sleek and functional todo application built with Flask, designed to help you manage your daily tasks efficiently with a clean, modern interface.

![Flask Todo App](https://img.shields.io/badge/Flask-2.0%2B-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## ✨ Features

- ✅ **Add, Edit, Delete Tasks** - Full CRUD functionality
- 🎯 **Mark Tasks as Complete** - Visual indicators for completed tasks
- 📱 **Responsive Design** - Works on desktop and mobile devices
- 🎨 **Clean UI** - Modern, minimalist interface
- ⚡ **Fast & Lightweight** - Built with Flask for optimal performance
- 💾 **Persistent Storage** - Data persists across sessions
- 🔍 **Task Filtering** - View all, active, or completed tasks

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flasktodo.git
   cd flask-todo-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser and navigate to**
   ```
   http://127.0.0.1:5000
   ```

## 📁 Project Structure

```
flask-todo-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/               # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── main.js       # JavaScript functionality
├── templates/            # HTML templates
│   ├── layout.html         # Base template
│   ├── home.html        # Main todo interface
│   ├── register.html        # Main todo interface 
│   └── login.html          # Error page
└── README.md             # This file
```

## 🛠️ Technologies Used

- **Backend**: Flask 2.0+
- **Frontend**: HTML5, Bootstrap
- **Data Storage**: Mysql
- **Styling**: Booststrap

## 🎮 How to Use

1. **Adding a Task**
   - Type your task in the input field
   - Press Enter or click the "Add" button

2. **Managing Tasks**
   - ✅ Click the checkbox to mark as complete
   - ✏️ Click the edit icon to modify a task
   - 🗑️ Click the delete icon to remove a task

3. **Filtering Tasks**
   - **All**: View all tasks
   - **Active**: View only pending tasks
   - **Completed**: View only finished tasks


## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Kill the process on port 5000
   sudo lsof -t -i tcp:5000 | xargs kill -9
   ```

2. **Module not found error**
   ```bash
   # Ensure virtual environment is activated
   pip install -r requirements.txt
   ```

3. **JSON file permission error**
   ```bash
   # Change permissions on data directory
   chmod 755 data/
   ```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt
---
```

⭐ **Star this repo** if you found it useful!

**Happy Coding!** 🎉