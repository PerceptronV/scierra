# Scierra
A ***S***imulated ***C***++ ***I***nt***er***preter with ***R***ecurrent ***A***daptation

Scierra is a Python package that makes use of the GCC CLI to simulate an interpreted C++ environment.

* [Example](#Example)

* [Installation](#Installation)

    * [Prerequisites](#Prerequisites)

    * [Install with PIP](#Install-with-PIP)

## Example
![Basic Scierra Demo](static/basic_demo.png "Scierra Basic Demo")

## Installation
### Prerequisites:
* GCC (GNU Compiler Collection) must be **installed** and **added to PATH**.
    This is to allow Python to access G++ through the command line. MinGW has been tested to work on Windows, so Cygwin should, too. However, this hasn't been tested.

### Install with PIP
Install with pip using:

    $ pip install scierra
  
After installation, run on command-line using:

    $ scierra
