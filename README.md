**0x00. AirBnB clone - The console**


**Background Context**

**Welcome to the AirBnB clone project!**
Before starting, please read the AirBnB concept page.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

**What’s a command interpreter?**
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

**Resources**
*Read or watch:*
cmd module
cmd module in depth
packages concept page
uuid module
datetime
unittest module
args/kwargs
Python test cheatsheet
cmd module wiki page
python unittest
**Learning Objectives**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function
- Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

**Requirements**
*Python Scripts*
. Allowed editors: vi, vim, emacs
. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
. All your files should end with a new line
. The first line of all your files should be exactly #!/usr/bin/python3
. A README.md file, at the root of the folder of the project, is mandatory
. Your code should use the pycodestyle (version 2.8.*)
. All your files must be executable
.The length of your files will be tested using wc
. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

**Tasks**
0. README, AUTHORS
Write a README.md:
description of the project
description of the command interpreter:
how to start it
how to use it
examples
You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
You should use branches and pull requests on GitHub - it will help you as team to organize your work
1. Be pycodestyle compliant!
Write beautiful code that passes the pycodestyle checks.
2. Unittests
3. BaseModel
4. Create BaseModel from dictionary
5. Store first object
6. Console 0.0.1
7. console 0.1
8. First User
9. More classes!
10. Console 1.0
11. All instance by class name
12. Count instnaces
13. Show
14. Destroy
15. Update
16. Update from dictionary
17. Unittest for the Console!
