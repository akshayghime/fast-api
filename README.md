[![Fast API Deployment](https://github.com/akshayghime/fast-api/actions/workflows/devops.yml/badge.svg)](https://github.com/akshayghime/fast-api/actions/workflows/devops.yml)


# fast-api
Continuous Delivery of FastAPI Data Engineering API on AWS Platform

#Scaffold

![image](https://github.com/user-attachments/assets/289c1a70-2b29-448d-9b98-f38ee1b58184)

1. Create a python virtual environment and activate it
    python3 -m venv ~/.fast-api-venv
    Source virtual environment in bash config file
    nano ~/.bashrc
    and paste the following line at the bottom
    source ~/.fast-api-venv/bin/activate
2. Create all scaffold empty files:-
    touch requirements.txt,
    touch Makefile,
    touch Dockerfile,
    mkdir mylib,
    touch mylib/__init__.py,
    touch mylib/logic.py
3. Populate Makefile and requirements.txt
---- Use make install command
---- To check the versions installed on your venv, use pip freeze
---- add those versions in requirements file and use make install command again

4. Setup github actions workflow, which means to setup continuous integration

5. Setup format, lint, test steps in both Makefile and .github/workflows devops.yml file

6. Create command line tool to interact with project and test the logic using python fire or click, In this case I used fire. Dont forget to shebang line at the start of your cli tool python file which tells the interpreter to run as a script. Also you need to run chmod +x cli-fire.py (Name of your cli tool file) in the command line first. Then you can simply pass on the file name (./cli-fire.py --help, ./cli-fire.py --length 5,./cli-fire.py) to run it as a script. Check file cli-fire.py for reference code. You can also play around with the file and check/test your functions by installing ipython. Try with wikipedia search.
   Sample code-

   ![image](https://github.com/user-attachments/assets/d8c45a6b-dead-4312-8074-ae50f412966a)

7. Pro tip you can also convert the whole module into a cli by adding the file name into FIRE function.
   ![image](https://github.com/user-attachments/assets/1641d269-c2b9-4d15-bdd0-4cfb180561a0)

8. We are going to create a function that takes in the input from wiki result and displays out phrases. For this we used textblob, do the required installation. Create test_main.py file and test output of phrase function which was created in logic.py file. Dont forget to update your main.py file and tweak a little bit so that fast api can listen to the call for this newly created function.