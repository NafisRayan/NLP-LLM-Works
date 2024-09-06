# Vau-2 Chatbot

This project demonstrates the use of Microsoft's 2.7 billion parameter [phi-2](https://huggingface.co/microsoft/phi-2) Transformer model to create a chatbot. The chatbot is designed to interact with users, providing responses based on the input it receives.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

Before running the chatbot, ensure you have Python installed on your system. Then, follow these steps:

1. Clone the repository:
git clone https://github.com/nafisrayan/vau-2.git

2. Navigate to the project directory:
cd yourrepository

3. Install the required packages:
pip install -r requirements.txt


## Usage

To start the chatbot, run the following command in your terminal:

python app.py


This will launch the Gradio interface, where you can interact with the chatbot. You can adjust the `max_new_tokens` parameter to control the length of the generated text responses.

## Project Structure

- `requirements.txt`: Lists the Python packages required for the project.
- `app.py`: Contains the main application logic, including the chatbot's text generation pipeline and the Gradio interface setup.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

