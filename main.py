import streamlit as st
import os
import google.generativeai as genai

# --- Function to call Gemini API ---
def generate_itinerary(destination, duration, interests):
    """
    Calls the Gemini API to generate a travel itinerary.
    """
    try:
        # Configure the API key from Streamlit secrets (for deployment)
        # or from a local secrets.toml file (for local testing)
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        
        # Crafting a detailed prompt
        prompt = f"""
        You are an expert travel agent. Create a detailed, day-by-day travel itinerary for a trip to {destination} for {duration} days.
        
        The traveler's interests are: {interests}.
        
        For each day, please provide a plan for the morning, afternoon, and evening.
        Include specific suggestions for activities, sights, and restaurants (with a brief description).
        
        Structure the output clearly using Markdown. Use a main heading for each day (e.g., "## Day 1: Arrival and Exploration").
        Make the itinerary engaging and practical.
        """
        
        # Initialize and call the Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        return response.text
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.error("Please make sure your Google API key is set up correctly in your secrets.")
        return None

# --- Page Setup ---
st.set_page_config(
    page_title="Personalized Trip Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Personalized Trip Planner")
st.write("Tell me your travel preferences, and I'll craft the perfect itinerary for you!")

# --- User Inputs ---
st.header("Your Travel Details")

col1, col2 = st.columns(2)

with col1:
    destination = st.text_input("📍 Where do you want to go?")
    duration = st.number_input("⏳ How many days will your trip be?", min_value=1, max_value=30, value=5)

with col2:
    interests = st.text_area("📝 What are your interests? (e.g., history, food, hiking, art, nightlife)")

# --- Generate Button ---
if st.button("Generate Itinerary", type="primary"):
    if destination and duration and interests:
        with st.spinner("Crafting your personalized itinerary... This may take a moment."):
            itinerary = generate_itinerary(destination, duration, interests)
            if itinerary:
                st.header("Your Personalized Itinerary")
                st.markdown(itinerary) # Using st.markdown to render the formatted text
    else:
        st.warning("Please fill in all the details above.")