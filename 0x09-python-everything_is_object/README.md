# 0x09. Python - Everything is object

![N|Solid](https://www.holbertonschool.com/holberton-logo.png) ![N|Solid](https://intranet.hbtn.io/assets/holberton-logo-coral-27055cb2f875eb10bf3b3942e52a24581bc0667695bdc856d4f08b469b678000.png)
---

## Description
Repository to study the following Python topics: Now that we understand that everything is an object and have a little bit of knowledge, lets pause and look a little bit closer at how Python works with different types of objects.

- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Task Project
---
File Name|Task Name|Task Description
---|---|---
[0-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/0-answer.txt)|0. Who am I?|What function would you use to print the type of an object?
[1-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/1-answer.txt)|1. Where are you?|How do you get the variable identifier (which is the memory address in the CPython implementation)?
[2-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/2-answer.txt)|2. Right count |point to the same object
[3-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/3-answer.txt)|3. Right count =|yes point to the same object
[4-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/4-answer.txt)|4. Right count =|Yes point to the same object
[5-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/5-answer.txt)|5. Right count =+|No point
[6-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/6-answer.txt)|6. Is equal|Print True ==
[7-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/7-answer.txt)|7. Is the same|Print True 'is'
[8-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/8-answer.txt)|8. Is really equal|Print True ==
[9-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/9-answer.txt)|9. Is really the same|Print True 'is'
[10-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/10-answer.txt)|10. And with a list, is it equal|== True list [] focus in content of list
[11-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/11-answer.txt)|11-answer.txt|is False in list. Focus in point of list
[12-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/12-answer.txt)|12. And with a list, is it really equal|True == alias in Python
[13-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/13-answer.txt)|13-answer.txt|True with is because used alias in list l2 = l1 
[14-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/14-answer.txt)|14. List append|used .append and alias with lists
[15-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/15-answer.txt)|15. List add|add value into the list is different 
[16-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/16-answer.txt)|16. Integer incrementation|increments work 
[17-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/17-answer.txt)|17. List incrementation|change content of list with .append
[18-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/18-answer.txt)|18. List assignation|assing values after def 
[19-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/19-answer.txt)|19. Copy a list object|returns a copy of a list.
[20-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/20-answer.txt)|20. Tuple or not?|yes tuple
[21-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/21-answer.txt)|21. Tuple or not?|yes tuple
[22-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/22-answer.txt)|22. Tuple or not?|no tuple
[23-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/23-answer.txt)|23. Tuple or not?|yes tuple
[24-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/24-answer.txt)|24. Richard Sim's special #0|True integers a = (1)
[25-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/25-answer.txt)|25. Richard Sim's special #1|False diffents tuples with 'is'
[26-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/26-answer.txt)|26. Richard Sim's special #2|True tuples emptys
[27-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/27-answer.txt)|27. Richard Sim's special #3|No, change
[28-answer.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/28-answer.txt)|28. Richard Sim's special #4|Yes, don't change
[106-line1.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line1.txt), [106-line2.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line2.txt), [106-line3.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line3.txt), [106-line4.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line4.txt), [106-line5.txt](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line5.txt)|30 o 35. Clear strings|objects and more objects


---
## Author

Juan David Restrepo Z. [@jdrestre](https://twitter.com/jdrestre)