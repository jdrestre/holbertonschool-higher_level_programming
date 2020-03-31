<h1 align="center">0x0F. Python - Object-relational mapping</h1>


## General

Concepts to learn in this project about: 0x0F. Python - Object-relational mapping and modules MySQLdb version 1.3.x and SQLAlchemy version 1.2.x

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Task Project
---
File Name|Task Name|Task Description
---|---|---
[0-select_states.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/0-select_states.py)|0. Get all states|Write a script that lists all states from the database hbtn_0e_0_usa and especific carhateristics
[1-filter_states.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/1-filter_states.py)|1. Filter states|Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
[2-my_filter_states.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/2-my_filter_states.py)|2. Filter states by user input|Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
[3-my_safe_filter_states.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/3-my_safe_filter_states.py)|3. SQL Injection...|it’s an SQL injection to delete all records of a table…
[4-cities_by_state.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/4-cities_by_state.py)|4. Cities by states|Write a script that lists all cities from the database hbtn_0e_4_usa
[5. All cities by state](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/5-filter_cities.py)|5. All cities by state|Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
[model_state.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/model_state.py)|6. First state model|Write a python file that contains the class definition of a State and an instance Base = declarative_base()
[7-model_state_fetch_all.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/7-model_state_fetch_all.py)|7. All states via SQLAlchemy|Write a script that lists all State objects from the database hbtn_0e_6_usa
[8-model_state_fetch_first.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/8-model_state_fetch_first.py)|8. First state|Write a script that prints the first State object from the database hbtn_0e_6_usa
[9-model_state_filter_a.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/9-model_state_filter_a.py)|9. Contains `a`|Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
[10-model_state_my_get.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/10-model_state_my_get.py)|10. Get a state|Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
[11-model_state_insert.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/11-model_state_insert.py)|11. Add a new state|Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
[12-model_state_update_id_2.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/12-model_state_update_id_2.py)|12. Update a state|Write a script that changes the name of a State object from the database hbtn_0e_6_usa
[13-model_state_delete_a.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/13-model_state_delete_a.py)|13. Delete states|Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
[model_city.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/model_city.py), [14-model_city_fetch_by_state.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py)|14. Cities in state|Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City
[relationship_city.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/relationship_city.py), [relationship_state.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/relationship_state.py), [100-relationship_states_cities.py](https://github.com/jdrestre/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/100-relationship_states_cities.py)|15. City relationship|Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py) and Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py




## Author

- Juan David Restrepo Z. [@jdrestre](https://twitter.com/jdrestre)

![N|Solid](https://www.holbertonschool.com/holberton-logo.png) ![N|Solid](https://intranet.hbtn.io/assets/holberton-logo-coral-27055cb2f875eb10bf3b3942e52a24581bc0667695bdc856d4f08b469b678000.png)
