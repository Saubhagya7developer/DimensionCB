# Web Chatbot Project

This project implements a web-based chatbot using Python for the backend and HTML, CSS, and JavaScript for the frontend. The chatbot utilizes the Open router API to provide responses to user queries.

## Project Structure

```
web-chatbot-project
├── backend
│   ├── app.py                # Entry point for the backend application
│   ├── chatbot
│   │   └── jpy_v_02_01.py    # Chatbot implementation
│   └── requirements.txt       # List of dependencies
├── frontend
│   ├── index.html            # Hello_world HTML document
│   ├── styles
│   │   └── style.css         # Styles for the frontend
│   └── scripts
│       └── app.js            # JavaScript code for user interactions
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd web-chatbot-project
   ```

2. **Install backend dependencies:**
   Navigate to the `backend` directory and install the required packages:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the backend server:**
   Execute the following command to start the backend application:
   ```
   python app.py
   ```

4. **Open the frontend:**
   Open `frontend/index.html` in your web browser to access the chatbot interface.

## User 
- Type your questions in the input field and press enter to interact with the chatbot.
- The chatbot will respond with answers based on the queries you provide.

## Additional Information

- Ensure you have an active OpenAI API key and configure it in the `jpy_v_02_01.py` file.
- Modify the styles in `style.css` to customize the appearance of the chatbot interface.
- Update `app.js` to enhance user interactions or add new features.

## A very Special thanks to Deepseek and Chatgpt to help me build the Project 