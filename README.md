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

## Modules

| File | Summary |
| ---  | --- |
| setup.sh | A bash script automates the setup process for running a Python application named easy_tags. |
| tags.py | Manages metadata tags on files using a command-line tool. It allows for retrieving all used tags in a user's home directory, getting tags associated with a specific file, executing various tagging commands, adding and removing tags from files. |
| app.kv | The code constructs a user interface for a tag-based file organization application. The interface enables users to navigate through files using a FileChooserListView. It also offers a text input field for creating new tags. A switch container, accommodating two columns, provides a scrollable area for the dynamically added switch elements. Text labels depict the new tag creation field and display the selected file's name. |
| app.py | The code represents an application named EasyTagsApp. It uses Kivy, a Python library for creating multi-touch applications. Functionalities include setting a default path for file choosing, triggering actions on file or tag selection, managing tags related to selected files. |

## Getting Started

Before running Easy Tags, ensure that your system meets the following requirements:

**Package Version:**
- Python 3.10.4
- pip 23.3.2
- Kivy Version: 2.2.1

**Run Application:**
```zsh
./setup
```

## Dependencies

- [Kivy](https://kivy.org/): Open-source Python library for developing multitouch applications.
