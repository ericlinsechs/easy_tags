# Easy Tags
<img src="./img/easy_tags_demo.png">

Easy Tags is a graphical user interface (GUI) application designed to simplify the management of Finder tags on macOS. With Easy Tags, users can effortlessly add, remove, and create new tags for files, enhancing the organization and accessibility of their data.

This project was developed as my final project for [Harvard's CS50 course](https://cs50.harvard.edu/x/2023/project/).

## Features

- **User-Friendly Interface:** Easy Tags provides an intuitive GUI with a file explorer on the left, a tag input box on the top-right, and a tag list with status switches on the right.

- **Tag Management:** Easily add or remove tags from selected files using the convenient interface.

- **Tag Creation:** Users can create new tags on-the-fly by entering tag names in the input box.

- **Visual Feedback:** The status switches visually indicate the presence of tags on selected files, making it easy to identify tagged items.

- **Language Support:** English and Chinese

## Getting Started

Before running Easy Tags, ensure that your system meets the following requirements:

1. **Package Version:**
    - Python 3.10.4
    - Kivy Version: 2.2.1

2. **Install `tag` Command-Line Tool:**
    ```bash
    brew install tag
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create Virtual Environment:**
    ```bash
    python -m virtualenv kivy_venv
    ```

5. **Activate Virtual Environment:**
    ```bash
    source kivy_venv/bin/activate
    ```

6. **Install Kivy:**

    ```bash
    python -m pip install "kivy[base]" kivy_examples
    ```

7. **Running the Application:**
    ```bash
    python app.py
    ```

## Dependencies

- [Kivy](https://kivy.org/): Open-source Python library for developing multitouch applications.
