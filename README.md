# Scierra

Scierra [_see-eh-rah_] is a **S**imulated **C**++ **I**nt**er**preter with **R**ecurrent **A**daptation.

In human words, it's a interactive interpreter for C++, which allows you to run and debug your program immediately as you type. Well, basically. But the implementation is slightly trickier.

To get a quick start, simply launch Scierra on the terminal and type `cout << "Hello, World!";`. Yes. That's a complete program in Scierra.

* [Example](#Example)

* [Installation](#Installation)

    * [Prerequisites](#Prerequisites)

    * [Install with PIP](#Install-with-PIP)

* [Usage](#Usage)

   * [Quick Start](#Quick-Start)
   
   * [Keywords](#Keywords)

## Example

***An sample program running on the Scierra interpreter: ***

```cpp
++> cout << "Hello, World!\n";
Hello, World!

++> #define CYAN "\033[36m"

++> #define GREEN "\033[32m"

++> #define DEFAULT "\033[0m"

++> cout << GREEN << "I am SCIERRA" << DEFAULT << endl;
I am SCIERRA

++>

++> int factorial(int n){

-->     if (n==1 || n==0)

-->         return 1;

-->     else return n * factorial(n-1);

--> }

++> cout << CYAN << "10 factorial is: " << factorial(10) << DEFAULT << endl;
10 factorial is: 3628800

++>

++> <esc>
```

Live demo of the above program running in a terminal with Scierra.

![Basic Scierra Demo](static/basic_demo.png "Scierra Basic Demo")

## Installation

### Prerequisites:

* _Python_ must be **installed** and **added to PATH**.
   
   The key ideas of Scierra and it's CLI have been implemented in Python.

* _GCC_ (GNU Compiler Collection) must be **installed** and **added to PATH**.
   
   This allows Python to access G++ through the command line. If you're a Linux user, there's a good chance that GCC tools are already included in your distro. Users of other operating systems like Windows or MacOS may need to make additional installations. A MinGW installation has been tested to work with Scierra on Windows.

### Install with PIP

Install with PIP using:

    $ pip install scierra

or (for LINUX users):


  
After installation, run Scierra on your terminal using:

    $ scierra

## Usage

### Quick Start

Launch `scierra` in your terminal, and try the following simple program.

It demonstrates Scierra's ability to see whether the line of code you just typed belongs to the `main` function section, global declarations section, or preprocessors section. The `<esc>` command closes the interpreter.

```cpp
++> cout << "Hello, World!\n";
Hello, World!

++> #define CYAN "\033[36m"

++> #define GREEN "\033[32m"

++> #define DEFAULT "\033[0m"

++> cout << GREEN << "I am SCIERRA" << DEFAULT << endl;
I am SCIERRA

++>

++> int factorial(int n){

-->     if (n==1 || n==0)

-->         return 1;

-->     else return n * factorial(n-1);

--> }

++> cout << CYAN << "10 factorial is: " << factorial(10) << DEFAULT << endl;
10 factorial is: 3628800

++>

++> <esc>
```

### Keywords

* `<print>`

* `<restart>`

* `<esc>`

* Code keywords

   * `<`
   
   * `<prep>`
   
   * `<glob>`

## LICENSE
[Apache License 2.0](LICENSE)
