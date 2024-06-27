# ATS System with Streamlit and Google Generative AI

This project is a web application built using Streamlit that evaluates a candidate's resume against a given job description. The app uses Google's Generative AI model (Gemini-Pro) to identify missing keywords in the resume that are present in the job description and calculates the percentage score of the resume based on keyword matching.

## Project Structure

- `.env`: Contains the API key for accessing Google's Generative AI.
- `venv`: Virtual environment for managing dependencies.
- `requirements.txt`: Lists the Python packages required for the project.
- `app.py`: The main application file.

## Prerequisites

- Python 3.7 or higher
- Git
- A GitHub account

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/my-python-project.git
    cd my-python-project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your API key**:
    - Create a `.env` file in the project root directory.
    - Add your Gemini API key to the `.env` file:
      ```
      GEMINI_API_KEY=your_api_key_here
      ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open your web browser** and go to `http://localhost:8501`.

3. **Use the app**:
    - Input your job description in the provided text box.
    - Upload your resume PDF file.
    - Click the "Submit" button to get the analysis.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
