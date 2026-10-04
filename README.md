# 🐍 Day 16 — Object-Oriented Programming (OOP)

A beginner-level Python practice project focused on understanding the fundamentals of **Object-Oriented Programming (OOP)**, including objects, attributes, methods, and modifying object properties.

## 📌 About

This project was created as part of **Day 16 of my Python learning journey**.

The goal was to understand how Python uses **objects** and how we can interact with them using attributes and methods.

The practice includes examples using the **Turtle** module and the **PrettyTable** library.

## 🧠 What I Practiced

### 🐢 1. Working with Objects

Used the Python `turtle` module to create a Turtle object:

```python
from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
```

This demonstrates how an object can be created and then controlled using its methods.

### ⚙️ 2. Object Attributes and Methods

Practiced the difference between:

* **Attributes** — information or properties belonging to an object.
* **Methods** — functions that belong to an object and perform an action.

Example:

```python
my_screen = Screen()

print(my_screen.canvheight)
my_screen.exitonclick()
```

Here, `canvheight` is accessed as an attribute, while `exitonclick()` is called as a method.

### 📊 3. Using PrettyTable

Practiced working with an external Python library called **PrettyTable** to create formatted tables.

```python
from prettytable import PrettyTable

table = PrettyTable()

table.add_column(
    "Pokemon Name",
    ["Pikachu", "Squirtle", "Charmander", "Haxorus",
     "Krookodile", "Staraptor", "Gengar"]
)

table.add_column(
    "Type",
    ["Electer", "Water", "Fire", "Dragon",
     "Ground", "Flying", "Ghost"]
)

table.align = "l"

print(table)
```

This exercise helped me practice creating an object, modifying its attributes, and calling its methods.

## 🛠️ Concepts Covered

* Object-Oriented Programming
* Objects
* Classes
* Object attributes
* Object methods
* Creating objects
* Calling methods
* Modifying object attributes
* Python Turtle
* External Python libraries
* PrettyTable

## 📦 Libraries Used

### Turtle

Python's built-in `turtle` module was used for experimenting with objects and methods.

### PrettyTable

The `prettytable` library was used to create formatted tables.

Install it using:

```bash
pip install prettytable
```

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python version:

```bash
python --version
```

### 2. Install PrettyTable

```bash
pip install prettytable
```

### 3. Run the Python file

```bash
python main.py
```

## 📂 Project Structure

```text
python-oop-day-16/
│
├── main.py
└── README.md
```

## 🎯 Learning Objective

The main objective of this exercise was to understand that Python programs can be built around **objects**, which contain their own data and behavior.

This was an introductory step toward learning more advanced OOP concepts such as:

* Classes
* Constructors
* Inheritance
* Encapsulation
* Polymorphism

## 🚀 Future Improvements

* Create custom Python classes
* Learn constructors using `__init__`
* Create object attributes
* Create custom methods
* Practice inheritance
* Build a small OOP-based project

## 👤 Author

**Your Name**

GitHub: `https://github.com/your-username`

---

📚 **Part of my Python learning journey — Day 16**
