# Python-Assignment2


To execute this use below command.
Command:  pytest .\Assignment2.py -v -s

Output of this 
PS C:\Users\pblt5065\Documents\API Automation\pythonProject_L> pytest .\Assignment2.py -v -s                         
================================================================================== test session starts ===================================================================================
platform win32 -- Python 3.9.10, pytest-7.4.4, pluggy-1.3.0 -- c:\users\pblt5065\documents\api automation\pythonproject_l\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\pblt5065\Documents\API Automation\pythonProject_L
collected 3 items

Assignment2.py::test_get_user_profile Authentication successful.

User Profile :  {'id': 6077850, 'name': 'Kanishka', 'email': 'niwggwa@example', 'gender': 'female', 'status': 'active'}
Assignment2.py::test_update_user_profile
User profile updated successfully.
User profile after update :  {'name': 'New Display Name', 'id': 6077850, 'email': 'niwggwa@example', 'gender': 'female', 'status': 'active'}
PASSED
Assignment2.py::test_delete_user_profile
User Profile deleted successfully
PASSED

PS C:\Users\pblt5065\Documents\API Automation\pythonProject_L>
