# Scierra

Scierra [_see-eh-rah_] is a **S**imulated **C**++ **I**nt**er**preter with **R**ecurrent **A**daptation.

In human words, it's a interactive interpreter for C++, which allows you to run and debug your program immediately as you type. Well, basically. But the implementation is slightly trickier.

To get a quick start, simply launch Scierra on the terminal and type `cout << "Hello, World!";`. Yes, that's a complete C++ program in Scierra!

**WARNING**: Scierra is still under development. Even though many vital aspects of C++ (e.g. function definition, templates, classes) are already supported, Scierra does not handle input statements very well. This is unfortunately keeping Scierra in Beta...

## Navigation

* [Example](#Example)

* [Installation](#Installation)

   * [Prerequisites](#Prerequisites)

   * [Install with PIP](#Install-with-PIP)

* [Usage](#Usage)

   * [Quick Start](#Quick-Start)
   
   * [Keywords](#Keywords)

* [Docs](#Docs)

   * [Anatomy of a C++ Program in Scierra](#Anatomy-of-a-C-Program-in-Scierra)

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
   
   This allows Python to access G++ through the command line. If you're a Linux user, there's a good chance that GCC tools are already included in your distro. Users of other operating systems like Windows or MacOS may need to make additional installations. MinGW has been tested to work with Scierra on Windows.

### Install with PIP

Install Scierra with PIP using:

    $ pip install scierra
  
After installation, run Scierra on your terminal using:

    $ scierra

## Usage

### Quick Start

Launch `scierra` in your terminal, and try pasting in the full sample program below.

Note Scierra's ability to automatically categorise whether the block of code you've just typed belongs to the `main` function section, global declarations section, or preprocessors section (refer to the [anatomy of a C++ program in Scierra](#Anatomy-of-a-C-Program-in-Scierra)). The `<esc>` command closes the interpreter.

```cpp
cout << "Hello, World!\n";
#define CYAN "\033[36m"
#define GREEN "\033[32m"
#define DEFAULT "\033[0m"
cout << GREEN << "I am SCIERRA" << DEFAULT << endl;

int factorial(int n){
    if (n==1 || n==0)
        return 1;
    else return n * factorial(n-1);
}
cout << CYAN << "10 factorial is: " << factorial(10) << DEFAULT << endl;

<esc>
```

Demo of the above program running in a terminal with Scierra.

![Basic Scierra Demo](static/basic_demo.png "Scierra Basic Demo")

### Keywords

* `<print>`: Prints out the code you've written so far.

* `<restart>`: Restarts another interpreter session and forgets all local variables.

* `<esc>`: Terminates Scierra.

#### Code keywords

Put the following keywords at the start of each block of your code for special operations.

* `<`: If you put `<` before a single-line statement and don't include any semicolons (e.g. `<10+23` or `<"Hey!"`), Scierra automatically outputs the evaluated value of the statement. It works with all data types, variables and classes that supports `cout` statements.
   
* `<prep>`: Forcefully specifies that the block of code that you type belongs to the 'preprocessor' part of the program. E.g.
   
       ++> <prep>

       --> #include<vector>
      
   Refer to: [Anatomy of a C++ Program in Scierra](#Anatomy-of-a-C-Program-in-Scierra).
   
* `<glob>`: Forcefully specifies that the block of code that you type belongs to the 'globals' part of the program.
      
   Refer to: [Anatomy of a C++ Program in Scierra](#Anatomy-of-a-C-Program-in-Scierra).
   
* `<main>`: Forcefully specifies that the block of code that you type belongs to the 'mains' part of the program.
   
   Refer to: [Anatomy of a C++ Program in Scierra](#Anatomy-of-a-C-Program-in-Scierra).

## Docs

### Anatomy of a C++ Program in Scierra

Scierra divides a C++ program into three distinct sections: the 'preprocessor' section, the 'globals' section, and the 'main' section. 

When you enter a block of code in Scierra, it automatically categorises it into one of these three sections based on syntactical keywords and expressions. You can override this automatic behaviour by using one of the [code keywords](#Code-Keywords).

#### Keywords and Expressions Table

Here is a table showing the different keywords and expressions that Scierra uses to categorise yur block of code.

| Preprocessor Section | Globals Section | Main Section |
| :---: | :---: | :---: |
| `#include` statement | `class` keyword | _Anything Else_ |
| `#define` statement | `struct` keyword |  |
| `typedef` keyword | `return` keyword |  |
| `using` keyword | `void` keyword |  |
|  | `template` keyword |  |
|  | `typename` keyword |  |

## LICENSE
[Apache License 2.0](LICENSE)
