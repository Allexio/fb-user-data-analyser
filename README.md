<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="">
    <img src="report_template/assets/images/logo.png" alt="Logo" width="280" height="80">
  </a>

  <h3 align="center">Facebook Data Analyser</h3>

  <p align="center">
    A tool to analyse your Facebook data, because no one wants to do it manually!
    <br />
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

[![Facebook Data Analyser Screenshot][product-screenshot]](https://example.com)

This is a tool that analyses data downloadable by a Facebook user and generates a report in a nice, readable format.

Here's why:

* Facebook keeps a lot of data on people and I want to bring their attention to that
* The data you can download from Facebook is in JSON format, which isn't very human readable

This is where my tool comes in. It takes your downloaded Facebook data zip file and then generates a nice report in web dashboard format.

### Built With

This project is built entirely in Python 3. Any version of Python 3 should do.
The dashboard is built on top of a template provided for free by ArchitectUI.

* [Python](https://python.org) - Language I used
* [NudeNet](https://pypi.org/project/NudeNet/) - Nudity detection algorithms
* [Bootstrap](https://getbootstrap.com/) - UI elements
* [ChartJS](https://www.chartjs.org/) - Cool graphs
* [ArchitectUI](https://architectui.com/) - Inspired the initial design

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This project requires the NudeNet pypi library.

```sh
pip install NudeNet
```

To use this tool, you also need to download your facebook data from [Facebook](https://facebook.com/your_information). This data needs to be downloaded in JSON format and needs to contain everything (quick reminder that my tool runs locally and of course does not upload your data at any time).

If you want to build this project into an executable for users who do not have Python installed, see the section below.

### Creating your own Distributable (optional)

1. Clone the repo
2. Move to the root directory of the project
3. Install pyinstaller

   ```sh
   pip install pyinstaller
   ```

4. Build the project with pyinstaller

   ```bat
   pyinstaller .\src\main.py --add-data ".\report_template\;.\report_template\"
   ```

<!-- USAGE -->
## Usage

See the prerequisites section if you haven't already.

If you have the release version (executable) simply unzip the folder and then double click the executable (the .exe file. There should be only one).

If you want to launch the python project, you will need python 3.7+

1. Clone the repo
2. Move to the root directory of the project
3. Launch the project with Python

   ```bat
   python ./src/fb_data_analyser.py
   ```

<!-- LICENSE -->
## License

The Python code is Distributed under the GPL 3 License. See `LICENSE` for more information.
The HTML/CSS template is distributed under the MIT license, as well as ChartJS and Bootstrap.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Cool Readme Template](https://raw.githubusercontent.com/othneildrew/Best-README-Template/)

[product-screenshot]: images/screenshot.png