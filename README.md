# 🛡️ Bulletproof Django API for a TMS project 🎓

## Introduction
In this tutorial, we will build a simple web application using Django and Django REST Framework (DRF). Our project will manage a collection of books, allowing users to perform CRUD (Create, Read, Update, Delete) operations through a REST API.

## Prerequisites

- Python installed (version 3.8 or higher recommended).
- Basic understanding of Python and Django.
- pip (Python package installer).
- Virtual environment setup knowledge (e.g., venv).

## Step 1: Setting Up the Environment

### Recommended VM Configuration for Your Host:
- Memory (RAM): Allocate 8 GB to the VM to ensure smooth performance while leaving sufficient resources for the host.
- Processors: Assign 4 cores (8 threads) to the VM.
- Storage: Allocate 100 GB as planned for the VM's hard disk.
- Network: Use Bridged Networking if the VM needs a unique IP on the local network or NAT for internet access via the host.

### Setting Up a VM

1. Download the Ubuntu Cloud Image: Ensure you have downloaded the **ubuntu-22.04-server-cloudimg-amd64.ova** file from a trusted source (e.g., Ubuntu official site).
2. Open VMware: Launch **VMware Workstation**, VMware Fusion, or VMware ESXi, depending on your setup.
3. Import the OVA file:
    - Click File > Open or Import an OVA.
    - Select the ubuntu-22.04-server-cloudimg-amd64.ova file.
    - Follow the prompts to import the image.
4. Name the VM: Provide a descriptive name, e.g., **TMS_VM**.
5. Configure the VM (Adjust Memory, Set Processors, Configure Hard Disk, Network Configuration)

### Start and Configure Ubuntu 22.04 Server

1. Start the VM
2. Login and Update System:

    `ubuntu@ubuntuguest:~$ sudo apt update && sudo apt upgrade -y`

3. Install Essential Tools:

    `ubuntu@ubuntuguest:~$ sudo apt install git python3 python3.10-venv python3-pip python3-venv git build-essential -y`

4. Set Up a User:

    ```
    ubuntu@ubuntuguest:~$ sudo groupadd bulletproof
    ubuntu@ubuntuguest:~$ sudo adduser django
    ubuntu@ubuntuguest:~$ sudo usermod -aG bulletproof django
    ```

5. Create a directory for your project
    
    `ubuntu@ubuntuguest:~$ mkdir /home/django/projects`

6. Change the group ownership to bulletproof:

    `ubuntu@ubuntuguest:~$ sudo chown :bulletproof /home/django/projects`

7. Set permissions so that only group members can write to the directory:

    `ubuntu@ubuntuguest:~$ sudo chmod 775 /home/django/projects`

8. Set the new user's default directory and permissions:

    ```
    ubuntu@ubuntuguest:~$ sudo usermod -d /home/django/projects django
    ubuntu@ubuntuguest:~$ sudo chown django:bulletproof /home/django/projects
    ubuntu@ubuntuguest:~$ su - django
    django@ubuntuguest:~$ 
    ```

### Vscode setup
To set up VS Code for your Django project via Remote-SSH, install the Python and Pylance extensions for Python support. Add Flake8 for linting and Black for code formatting. Install the Django extension for specific project features. Ensure that Flake8 and Black are also installed on the remote VM via pip. Configure the Python interpreter to use the virtual environment, and enable linting and formatting through VS Code settings for a seamless development experience.

1. Create pyproject.toml: This is an optional file for managing project metadata and build configuration. Create it manually or use a template. Example:

    ```toml
    [tool.black]
    line-length = 100
    ```
2. Install black: `(.venv) django@ubuntuguest:~/tms$ pip install black`

2. Create `.flake8` file: This file is used to configure Flake8 settings (linter for Python code style). Example .flake8 content:

    ```ini
    [flake8]
    max-line-length = 100
    extend-ignore = E203, W503
    ```
2. Install Flake8: `(.venv) django@ubuntuguest:~/tms$ pip install flake8`


### Python setup

1. Create a virtual environment:
    ```python
    django@ubuntuguest:~$ mkdir tms && cd tms
    django@ubuntuguest:~$ python3 -m venv .venv
    django@ubuntuguest:~$ source .venv/bin/activate  # On Windows: env\Scripts\activate
    ```
2. Install Django and DRF:

    `(.venv) django@ubuntuguest:~/tms$ pip install django djangorestframework`

3. Create a Django project:

    `(.venv) django@ubuntuguest:~/tms$ django-admin startproject tms .`

4. Run the development server:

    `(.venv) django@ubuntuguest:~/tms$ python manage.py runserver 0.0.0.0:8000`

 If you encounter the error: `django.core.exceptions.DisallowedHost: Invalid HTTP_HOST header: 'ip_address:8000'. You may need to add 'ip_address' to ALLOWED_HOSTS.`. Add your server’s IP address (e.g., 10.0.0.10) to the ALLOWED_HOSTS in settings.py: `ALLOWED_HOSTS = ['10.0.0.10', 'localhost', '127.0.0.1']`

Visit http://ip_address:8000 to see the default Django homepage.

### Setting up the Git Repository
1. Create a `README.md` file: This file provides basic information about your project, such as purpose, installation instructions, and usage.

    ```bash
    (.venv) django@ubuntuguest:~/tms$ touch README.md
    ```

    Add your project description to the file. Example:

    ```markdown
    # Training Management System (TMS)
    This is a Django-based project for managing training courses, students, and instructors.
    ```

2. Create `requirements.txt`: This file lists all the dependencies for your project. To generate requirements.txt based on the virtual environment:

    ```bash
    (.venv) django@ubuntuguest:~/tms$ pip freeze > requirements.txt
    ```

5. Create a `LICENSE` file.
6. Create the `.gitignore` file.

### Snapshot the VM

Once the VM is configured and the initial setup is complete, take a snapshot to preserve this state: 
- Go to VMware > Snapshot > Take Snapshot.
- Name it something like InitialSetup