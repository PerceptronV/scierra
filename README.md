# Scierra

Scierra [_see-eh-rah_] is a **S**imulated **C**++ **I**nt**er**preter with **R**ecurrent **A**daptation.

In human words, it's a interactive interpreter for C++, which allows you to run and debug your program immediately as you type. Well, basically. But the implementation is slightly trickier.

To get a quick start, simply launch Scierra on the terminal and type `cout << "Hello, World!";`. Yes. That's a complete C++ program in Scierra.

* [Example](#Example)

* [Installation](#Installation)

    * [Prerequisites](#Prerequisites)

    * [Install with PIP](#Install-with-PIP)

* [Usage](#Usage)

   * [Quick Start](#Quick-Start)
   
   * [Keywords](#Keywords)

* [Docs](#Docs)

   * [Anatomy of a C++ Program in Scierra](#Anatomy-of-a-C++-Program-in-Scierra)

* [LICENSE](#LICENSE)

## Example

***An sample program running on the Scierra interpreter:***

```cpp
++> cout << "Hello, World!";
Hello, World!
++> int factorial(int n){

-->     if (n==1 || n==0)

-->         return 1;

-->     else return n * factorial(n-1);

--> }

++> cout << "10 factorial is: " << factorial(10);
10 factorial is: 3628800
```

## Installation

### Prerequisites:

* _Python_ must be **installed** and **added to PATH**.
   
   The key ideas of Scierra and it's CLI have been implemented in Python.

* _GCC_ (GNU Compiler Collection) must be **installed** and **added to PATH**.
   
   This allows Python to access G++ through the command line. If you're a Linux user, there's a good chance that GCC tools are already included in your distro. Users of other operating systems like Windows or MacOS may need to make additional installations. A MinGW installation has been tested to work with Scierra on Windows.

### Install with PIP

Install with PIP using:

    $ pip install scierra
  
After installation, run Scierra on your terminal using:

    $ scierra

## Usage

### Quick Start

Launch `scierra` in your terminal, and try the full sample program below.

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

Demo of the above program running in a terminal with Scierra.

![Basic Scierra Demo](static/basic_demo.png "Scierra Basic Demo")

### Keywords

* `<print>`

   Prints out the code you've written so far.

* `<restart>`

   Restarts another interpreter session and forgets all local variables.

* `<esc>`

   Terminates Scierra.

* Code keywords

   Put the following keywords at the start of each block of your code for special operations.

   * `<`
   
      If you put `<` before a single-line statement and don't include any semicolons (e.g. `<10+23` or `<"Hey!"`), Scierra automatically outputs the evaluated value of the statement. Works with all data types, variables and classes that supports `cout` statements. Also supports printing the return value of functions.
   
   * `<prep>`
   
   Forcefully specify that the block of code that you've just typed belongs to 
   
   * `<glob>`
   
   * `<main>`

## Docs

### Anatomy of a C++ Program in Scierra

## LICENSE
[Apache License 2.0](LICENSE)
