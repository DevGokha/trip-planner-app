# ✈️ Personalized Trip Planner

This web application leverages the power of the Google Gemini API to generate custom travel itineraries based on user preferences. Simply provide a destination, trip duration, and your interests, and the AI will craft a detailed, day-by-day plan for your perfect getaway.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)[https://devgokha-trip-planner-app.streamlit.app/]])



## ✨ Key Features

-   **Dynamic Itinerary Generation:** Get a unique travel plan tailored to your specific inputs.
-   **Interest-Based Recommendations:** Whether you love history, food, hiking, or art, the suggestions will match your passions.
-   **Detailed Daily Plans:** Each day's itinerary is broken down into morning, afternoon, and evening activities, including specific sight and restaurant recommendations.
-   **Interactive & User-Friendly Interface:** Built with Streamlit for a clean, simple, and responsive user experience.

## 🛠️ Technology Stack

-   **Frontend:** Streamlit
-   **Language:** Python
-   **Core AI Model:** Google Gemini API (`gemini-1.5-flash`)
-   **Deployment:** Streamlit Community Cloud

## 🚀 Live Application

You can access and use the live application here: **[(https://devgokha-trip-planner-app.streamlit.app/)])**

## ⚙️ How to Run Locally

To set up and run this project on your own machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/DevGokha/trip-planner-app.git](https://github.com/DevGokha/trip-planner-app.git)
    cd trip-planner-app
    ```

2.  **Set Up a Virtual Environment:**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate the environment
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    Make sure you have a `requirements.txt` file with the following content:
    ```
    streamlit
    google-generativeai
    ```
    Then, run the installation command:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key:**
    -   In the root of your project folder, create a new directory named `.streamlit`.
    -   Inside the `.streamlit` directory, create a new file named `secrets.toml`.
    -   Add your Google Gemini API key to this file as shown below:
        ```toml
        GOOGLE_API_KEY = "AIzaSyBZUaNaMC5GOT5h6AqaHX3-Q_SRZy*****"
        ```

5.  **Run the Streamlit App:**
    ```bash
    streamlit run main.py
    ```

