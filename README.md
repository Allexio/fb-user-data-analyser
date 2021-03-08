<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#Creating-a-Distributable">Creating a Distributable</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This is a tool that analyses data downloadable by a Facebook user and generates a report in a nice, readable format.

Here's why:

* Facebook keeps a lot of data on people and I want to bring their attention to that
* The data you can download from Facebook is in JSON format, which isn't very human readable

This is where my tool comes in. It takes your downloaded Facebook data zip file and then generates a nice report in web dashboard format.

### Built With

This project is built entirely in Python 3. Any version of Python 3 should do.
The dashboard is built on top of a template provided for free by ArchitectUI.

* [Python](https://python.org)
* [ArchitectUI](https://architectui.com/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

There are no prerequisites for this project. It is based purely on Python, with no external libraries.
If you want to build this project into an executable for users who do not have Python, see the section below.

### Creating a Distributable

1. Clone the repo
2. Move to the root directory of the project
3. Install pyinstaller

   ```bat
   pip install pyinstaller
   ```

4. Build the project with pyinstaller

   ```bat
   pyinstaller .\src\main.py --add-data ".\report_template\;.\report_template\"
   ```

<!-- USAGE -->
## Usage

If you have the release version (executable) simply double click the executable.

If you want to launch the python project, you will need python 3.X.

1. Clone the repo
2. Move to the root directory of the project
3. Launch the project with Python

   ```bat
   python ./src/main.py
   ```

<!-- LICENSE -->
## License

The Python code is Distributed under the GPL 3 License. See `LICENSE` for more information.
The HTML/CSS template is distributed under the MIT license.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Cool Readme Template](https://raw.githubusercontent.com/othneildrew/Best-README-Template/)

[product-screenshot]: images/screenshot.png