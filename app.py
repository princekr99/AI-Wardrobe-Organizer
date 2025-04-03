# app.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)

# --- Gemini AI Integration ---
# Configure the Gemini API key (Store this securely, e.g., in environment variables)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("⚠️ Gemini API Key not found. Please set the GEMINI_API_KEY environment variable.")
    # Handle the missing key case appropriately - maybe disable AI features
else:
    genai.configure(api_key=GEMINI_API_KEY)

# Function to get suggestions from Gemini
def get_ai_suggestion(prompt_text):
    if not GEMINI_API_KEY:
        return "AI features disabled: API key missing."
    try:
        model = genai.GenerativeModel('gemini-1.5-pro') # Or other suitable Gemini model
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return f"Sorry, couldn't get an AI suggestion at this time. Error: {e}"

def get_ai_categorization(item_description):
    if not GEMINI_API_KEY:
        return "AI features disabled: API key missing."
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        # More specific prompt for categorization
        prompt = f"""Analyze the following clothing item: '{item_description}'.
        Provide its primary category (e.g., Top, Bottom, Dress, Outerwear, Footwear, Accessory),
        suggested style(s) (e.g., Casual, Formal, Sporty, Business Casual),
        and suitable season(s) (e.g., Summer, Winter, All-Season, Spring/Fall).
        Format the output clearly, perhaps like:
        Category: [Primary Category] | Style: [Style(s)] | Season: [Season(s)]
        Keep the response concise."""
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API for categorization: {e}")
        return f"Sorry, couldn't get AI categorization. Error: {e}"



# --- Wardrobe Data (Example - Replace with Database/Storage) ---
# In a real app, you'd use a database (like PostgreSQL, MongoDB, or SQLite)
# or cloud storage to store user wardrobes.
user_wardrobe = {
    "user1": ["blue jeans", "white t-shirt", "black sneakers", "red dress", "leather jacket"]
}

# --- Routes ---
@app.route('/')
def home():
    # Pass wardrobe items to the template
    items = user_wardrobe.get("user1", [])
    return render_template('index.html', wardrobe_items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    item_description = request.form.get('item_description')
    if item_description:
        # Add item to user's wardrobe (using placeholder user "user1")
        if "user1" not in user_wardrobe:
            user_wardrobe["user1"] = []
        user_wardrobe["user1"].append(item_description)
        # Optionally, use Gemini to categorize the item here
        # categorization_prompt = f"Categorize this clothing item: {item_description}"
        # category = get_ai_suggestion(categorization_prompt)
        # Store category along with item...
        print(f"Added item: {item_description}") # Server log
    # In a real app, you'd redirect or update the page dynamically
    return "Item added (Placeholder Response - Refresh to see changes)"

@app.route('/suggest_outfit', methods=['GET'])
def suggest_outfit():
    user_items = user_wardrobe.get("user1", [])
    if not user_items:
        return jsonify({"suggestion": "Your wardrobe is empty! Add some items first."})

    occasion = request.args.get('occasion', 'casual')
    # Improved prompt using item list
    prompt = f"My wardrobe contains: {', '.join(user_items)}. Suggest a {occasion} outfit combination using *only* items from this list. If items don't match the occasion well, suggest the best possible option or state that."

    suggestion = get_ai_suggestion(prompt)
    return jsonify({"suggestion": suggestion})

# NEW Route for categorization
@app.route('/categorize_item', methods=['POST'])
def categorize_item_route():
    item_description = request.form.get('item_description')
    if not item_description:
        return jsonify({"error": "No item description provided."}), 400

    print(f"Received request to categorize: {item_description}") # Server log
    category_info = get_ai_categorization(item_description)
    print(f"Gemini categorization result: {category_info}") # Server log

    return jsonify({"item": item_description, "category_info": category_info})


# --- Vercel Specific ---
# Vercel runs the app using a WSGI server like Gunicorn.
# The 'app' variable is the entry point.

if __name__ == '__main__':
    # This is for local development
    app.run(debug=True, port=5001) # Use a port other than Vercel's default if needed
