The following commands can be used to run the solution if Docker is installed:

- docker run -d --rm --name solution_container -v "$(pwd)":/usr/src/app python:3.13.2 tail -f /dev/null
- docker exec -it solution_container bash
- pip install pytest
- cd /usr/src/app
- pytest test_solution.py

The commands should be used in a command line prompt after changing directory to the solution folder. It is also possible to use the following commands if Python is installed directly without Docker:

- pip install pytest
- pytest test_solution.py
