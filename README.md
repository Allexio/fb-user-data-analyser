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
        <li><a href="#creating-your-own-distributable">Creating a Distributable</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <ul>
        <li><a href="#with-the-executable">With Executable</a></li>
        <li><a href="#with-python">With Python</a></li>
      </ul>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![Facebook Data Analyser Screenshot][product-screenshot]

This is a tool that analyses data downloadable by a Facebook user and generates a report in a nice, readable format.

Here's why:

* Facebook keeps a lot of data on people and I want to bring their attention to that
* Facebook gives you a way to download the data in HTML format, but the HTML variant is very plain (the data is basically in list form, making any kind of information gleaning *extremely* hard to do).

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

To use this tool, you need to [download your facebook data from Facebook](https://www.facebook.com/dyi/). This data needs to be downloaded in JSON format and needs to contain everything (quick reminder that my tool runs locally and of course does not upload your data at any time).


### Creating your own Distributable

_This is entirely optional, and is meant for developers, not users_

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

### With the executable

(**Windows only**)

See the prerequisites section if you haven't already.

0. Download the latest release from github (the release section is located in the tab on the right)
1. Extract the contents of the release zip file wherever you want.
2. Go in the resulting folder
3. Double click on fb_data_analyser.exe
4. If Windows shows you a warning about the fact that you downloaded this from the internet, click show more and then run anyway.

### With Python

If you want to launch the python project, you will need python 3.7+

The Python version of this project also requires the NudeNet pypi library.

```sh
pip install NudeNet
```

1. Clone the rep
2. Move to the root directory of the project
3. Launch the project with Python

   ```bat
   python ./src/fb_data_analyser.py
   ```

! **WARNING FOR MAC USERS** !

The tool expects a zip file where the contents are directly at the top level of the zip file.

If the facebook data file you download was automatically unzipped, you will have to manually zip the file, by selecting all the contents of the folder.

To clarify, the tree should look like this:

```
my-facebook-data.zip
-> about_you
-> accounts_center
-> ads_and_businesses
```

and not like this:

```
my-facebook-data.zip
-> my-facebook-data
  -> about_you
  -> accounts_center
  -> ads_and_businesses
```

<!-- LICENSE -->
## License

The Python code is Distributed under the GPL 3 License. See `LICENSE` for more information.
The HTML/CSS template, ChartJS and Bootstrap are all distributed under the MIT license.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Cool Readme Template](https://raw.githubusercontent.com/othneildrew/Best-README-Template/)

[product-screenshot]: report_template/assets/images/screenshot.jpg
