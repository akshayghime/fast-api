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