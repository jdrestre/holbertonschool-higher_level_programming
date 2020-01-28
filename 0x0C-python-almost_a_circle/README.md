# 0x0C. Python - Almost a circle

![N|Solid](https://www.holbertonschool.com/holberton-logo.png) ![N|Solid](https://intranet.hbtn.io/assets/holberton-logo-coral-27055cb2f875eb10bf3b3942e52a24581bc0667695bdc856d4f08b469b678000.png)
---

## Description
Repository to study the following Python topics: Almost a circle. This project will help you be ready for it.

In this project, you will review everything about Python:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

You will also learn about:

- args and kwargs
- Serialization/Deserialization
- JSON

### General Learning Objectives

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Task Project
---
File Name|Task Name|Task Description
---|---|---
tests/|0. If it's not tested it doesn't work|Folder containing all test files. Note: All files, classes and methods must be unit tested and be PEP 8 validated.
models/base.py, models/__init__.py|1. Base class|Write the first class Base, Create a folder named models with an empty file __init__.py, Create a file named models/base.py
models/rectangle.py|2. First Rectangle|Write the class Rectangle that inherits from Base and add getter/setter each attribute
models/rectangle.py|3. Validate attributes|Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded): TypeError and ValueError into getter/setter
models/rectangle.py|4. Area first|Update the class Rectangle by adding the public method def area(self)
models/rectangle.py|5. Display #0|Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character #
models/rectangle.py|6. __str__|Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
models/rectangle.py|7. Display #1|Update the class Rectangle by improving the public method def display(self) # taking care of x and y
models/rectangle.py|8. Update #0|Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute id, width, height, x, y
models/rectangle.py|9. Update #1|Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes
models/square.py|10. And now, the Square!|Write the class Square that inherits from Rectangle
models/square.py|11. Square size|Update the class Square by adding the public getter and setter size
models/square.py|12. Square update|Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes
models/rectangle.py|13. Rectangle instance to dictionary representation|Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
models/square.py|14. Square instance to dictionary representation|Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
models/base.py|15. Dictionary to JSON string|Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries


---
## Author

Juan David Restrepo Z. [@jdrestre](https://twitter.com/jdrestre)