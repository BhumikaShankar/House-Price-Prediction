# House Price Prediction Web App

## Description

This project is a web-based application that predicts house prices using a Random Forest Regressor machine learning algorithm. The model takes user inputs such as the number of bedrooms, bathrooms, living area, house condition, and nearby schools to estimate the house price. This project was developed as a practical application of machine learning and to create a user-friendly tool for basic house price estimation.

## Tech Stack

*   **Machine Learning Algorithm:** Random Forest Regressor (Scikit-learn)
*   **Data Manipulation & Analysis:** Pandas, NumPy
*   **Data Visualization:** Matplotlib
*   **Model Saving & Loading:** Joblib
*   **Web Application Framework:** Streamlit
*   **Programming Language:** Python

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [repository URL]
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd House-Price-Prediction
    ```
3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

```bash
streamlit run app.py
