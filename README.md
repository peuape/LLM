These are the codes I wrote to practise using langchain. Below is the README for animal_dictionary.

# Imaginary Animal Query Assistant

The **Animal Query Assistant** is a Streamlit application that provides detailed information about five mythical animals. Users can interact with the app by asking questions related to these animals. The app is built using Python, Streamlit, and the OpenAI API.

---

## Features

- **Ask Questions:** Users can input queries about the animals, and the app responds with relevant details.
- **OpenAI Integration:** Uses the OpenAI API for natural language processing.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd animal_dictionary
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to the URL displayed in the terminal.

3. Enter your OpenAI API key in the app and start asking questions about the animals.


---

## Animal Information

The app supports the following animals:
- **Glitterfang**
- **Lunarkeeper**
- **Frostmane**
- **Thundertusk**
- **Flarehawk**

Photos for each animal are named as `<animal_name>.jpg` and should be placed in the same directory as `app.py`.

---

## Requirements

- Python 3.8 or higher
- OpenAI API key

---

