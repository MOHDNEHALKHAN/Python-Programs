# Fork and Clone the Repository

1. Go to the GitHub repository you want to fork.
2. Click the "Fork" button in the upper right-hand corner of the repository page.
3. Select your username or organization where you want to fork the repository. This creates a copy of the repository in your GitHub account.
4. Open your terminal (Command Prompt on Windows, Terminal on macOS and Linux).
5. Use this in your terminal
   
```sh
git clone https://github.com/<your-username>/<repository-name>.git
```

# Running Python Programs in Visual Studio Code

This README provides a step-by-step guide on how to execute and run Python programs within Visual Studio Code using the "Python-Program" repository.

## Prerequisites

Before you begin, make sure you have the following installed:

1. **Visual Studio Code**: If you haven't already, download and install Visual Studio Code from the [official website](https://code.visualstudio.com/).

2. **Python Extension**: Install the "Python" extension for Visual Studio Code. Open VS Code, go to the Extensions view by clicking on the square icon in the sidebar or pressing `Ctrl+Shift+X`, and search for "Python". Install the one provided by Microsoft.

3. **Python Interpreter**: You need Python installed on your system. If you haven't installed it yet, download it from the [official Python website](https://www.python.org/downloads/) and follow the installation instructions.

## Getting Started

1. **Clone the Repository**: Start by cloning the "Python-Program" repository to your local machine using either the HTTPS or SSH link provided on the repository page.

```sh
git clone <repository_url>
```

2. **Open the Repository in VS Code**: Open Visual Studio Code, and from the menu, select `File > Open Folder...` Navigate to the directory where you cloned the repository and select the folder.

3. **Create or Open a Python File**: Inside the repository folder, you can either create a new Python file (e.g., `my_script.py`) or open an existing one.

4. **Write Your Python Code**: Write your Python program in the opened file. For example:

```python
print("Hello, World!")
```

## Running the Python Script

1. **Run the Python Program**: Open a terminal in Visual Studio Code by going to `Terminal > New Terminal`. In the terminal, navigate to the directory containing your Python file and use the following command to run it:

```sh
python my_script.py
```