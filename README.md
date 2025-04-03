# AI Wardrobe Organizer 🧥👖✨

A web application designed to help you manage your wardrobe digitally, offering AI-powered outfit suggestions and clothing categorization using Google Gemini.

## 🚀 Introduction

Tired of staring into your closet and not knowing what to wear? The AI Wardrobe Organizer helps you inventory your clothing items and leverages the power of AI to:

*   Suggest outfits suitable for different occasions based *only* on what you own.
*   Automatically categorize your items by type, style, and season.

This provides a smart and efficient way to manage your clothes and get daily style inspiration!

## ✨ Features

*   **Digital Wardrobe Inventory:** Add and view text descriptions of your clothing items.
*   **AI Outfit Suggestions:** Get personalized outfit recommendations based on your wardrobe contents and a specified occasion (e.g., casual, formal).
*   **AI Clothing Categorization:** Automatically analyze and tag items with their category (Top, Bottom, etc.), style (Casual, Formal, etc.), and suitable seasons.
*   **Web-Based Interface:** Accessible via any modern web browser.
*   **Responsive Design:** Adapts to various screen sizes (desktop, tablet, mobile).
*   **Sleek UI:** Features a modern, dark theme with subtle 3D effects and an AI/Tech-inspired background.

## 🛠️ Tech Stack

*   **Backend:** Python, Flask
*   **AI Integration:** Google Gemini API (`google-generativeai`)
*   **Frontend:** HTML, CSS, Vanilla JavaScript
*   **Environment Management:** `python-dotenv` (for API keys)

## ⚙️ Installation & Setup (Local Development)

Follow these steps to run the application on your local machine:

1.  **Prerequisites:**
    *   Python 3.x installed ([python.org](https://www.python.org/))
    *   `pip` (Python package installer)

2.  **Clone the Repository (Optional):**
    ```bash
    git clone <your-repository-url>
    cd ai-wardrobe-organizer
    ```
    (If you don't have a repository, just navigate to the project directory containing `app.py`)

3.  **Create and Activate Virtual Environment:**
    *   Create:
        ```bash
        python -m venv venv
        ```
    *   Activate:
        *   Windows: `.\venv\Scripts\activate`
        *   macOS/Linux: `source venv/bin/activate`

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure API Key:**
    *   Obtain a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/).
    *   Create a file named `.env` in the root directory of the project (alongside `app.py`).
    *   Add your API key to this file:
        ```env
        GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE
        ```
    *   **Important:** Replace `YOUR_ACTUAL_API_KEY_HERE` with your real key. **Do not commit this file to version control if your repository is public.**

6.  **Run the Application:**
    ```bash
    flask run
    ```
    Or alternatively:
    ```bash
    python app.py
    ```
    The application will typically be available at `http://127.0.0.1:5000/` or `http://localhost:5001/`. Check the terminal output for the exact address.

## ▶️ Usage

1.  **Open the App:** Navigate to the local URL (e.g., `http://127.0.0.1:5000/`) in your web browser.
2.  **Add Items:** Use the "Add New Item" form to input descriptions of your clothes (e.g., "Navy Blue Blazer", "White Linen Shirt").
3.  **View Wardrobe:** See your added items listed under "My Wardrobe".
4.  **Categorize Items:** Click the "Categorize" button next to any item in the list. The AI will analyze it, and the category details will appear below the item.
5.  **Get Suggestions:** Enter an occasion (optional, defaults to "casual") in the "Get Outfit Suggestion" section and click "Suggest Outfit". The AI will propose an outfit using items from your wardrobe list.

## ☁️ Deployment (Vercel Example)

This Flask application can be easily deployed to platforms like Vercel:

1.  **Ensure `vercel.json` is configured:** (Check the example provided in previous steps or Vercel documentation). It should specify how to build and run the Python application.
2.  **Ensure `requirements.txt` is up-to-date.**
3.  **Push your code to a Git provider** (GitHub, GitLab, Bitbucket).
4.  **Connect your Git repository to Vercel.**
5.  **Configure Environment Variables:** In your Vercel project settings, add your `GEMINI_API_KEY` as an environment variable. **Do not store the key directly in your code or `vercel.json`.**
6.  **Deploy!** Vercel should automatically build and deploy your application based on the configuration.

## 📄 License

(Optional: Add license information here, e.g., MIT License)
