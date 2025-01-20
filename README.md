---
title: "Bulletproof Django API for a TMS project"
published: true
tags: django, python, tutorial, drf
series: "Django Project Series"
cover_image: "https://ucarecdn.com/456732bc-6c7d-4774-875b-3cb178dd59df/-/resize/1050/"
---

# 🛡️ Bulletproof Django API for a TMS project 🎓

## Introduction
In this tutorial, we will build a robust web application using Django and Django REST Framework (DRF), designed to serve as a solid foundation for production-ready projects. This is my first tutorial, and it will guide you through the creation of a bulletproof project skeleton with a well-organized structure that adheres to best practices.

We will manage a collection of books, allowing users to perform CRUD (Create, Read, Update, Delete) operations through a REST API, but with a lot more features, including:

- Good Project Structure: Organizing the project into Django apps, separating concerns, and following a clean directory structure.
- Role-Based Access Control (RBAC): Ensuring secure access by assigning different roles and permissions to users (e.g., admin, author, reader).
- Logging: Setting up logging for better monitoring and debugging in production environments.
- Email Integration: Sending emails for user registration, password reset, and notifications.
- File Upload: Allowing users to upload book images or other media.
- Input Validation: Using serializers to validate data inputs to ensure they conform to expected formats and business rules.
- Swagger for API Documentation: Automatically generating interactive API documentation to make testing and using the API easier.
This tutorial will help you set up a powerful, maintainable, and secure Django application suitable for real-world projects. By the end, you’ll have a well-structured Django project with industry-standard features and practices.

---

## Prerequisites

- Python installed (version 3.8 or higher recommended).
- Basic understanding of Python and Django.
- pip (Python package installer).
- Virtual environment setup knowledge (e.g., venv).

---

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

3. Create `.flake8` file: This file is used to configure Flake8 settings (linter for Python code style). Example .flake8 content:

    ```ini
    [flake8]
    max-line-length = 100
    extend-ignore = E203, W503
    ```
4. Install Flake8: `(.venv) django@ubuntuguest:~/tms$ pip install flake8`

5. Configure VS Code Settings for Your Django Project:
    - Create a .vscode folder in the root directory of your project.
    - Inside the .vscode folder, create a settings.json file.
    - Add the following content to settings.json:
    ```json
    {
        "flake8.args": [
            "--max-line-length=100",
            "--ignore=E203,W503,F401,F403"
        ],
        "black-formatter.args": [
            "--line-length=100"
        ],
        "editor.formatOnSave": true,
        "[html]": {
            "editor.formatOnSave": false
        }
    }
    ```

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

5. Create a `LICENSE` file: This file specifies the terms under which your project can be used, modified, and distributed. It is essential for defining the legal rights and obligations of others who want to use your code. Choose a license that suits your project, such as MIT, Apache 2.0, or GPL, and include the corresponding text in this file..
6. Create the `.gitignore` file: This file specifies intentionally untracked files or directories that Git should ignore. It helps prevent sensitive information, temporary files, or unnecessary system-generated files (e.g., .env, *.pyc, __pycache__/, .vscode/) from being included in your repository. Customize it based on your project's needs to keep your repository clean and secure.
7. Set Up SSH Key for GitHub:
    ```
    (.venv) django@ubuntuguest:~/tms$ ls ~/.ssh
    (.venv) django@ubuntuguest:~/tms$ ssh-keygen -t ed25519 -C "your_email@example.com"`
    (.venv) django@ubuntuguest:~/tms$ cat ~/.ssh/id_ed25519.pub` and Copy the output.
    ```
    Add the SSH key to GitHub. Go to Settings > SSH and GPG keys > New SSH key. Paste the key and give it a title.
8. Change Directory: `(.venv) django@ubuntuguest:~/tms$ cd /path/to/your/project`
9. Initialize Git Repository: `(.venv) django@ubuntuguest:~/tms$ git init`
10. Add Remote Repository: `(.venv) django@ubuntuguest:~/tms$ git remote add origin git@github.com:username/repository.git`
11. Stage Files: `(.venv) django@ubuntuguest:~/tms$ git add .`
12. Create Initial Commit: `(.venv) django@ubuntuguest:~/tms$ git commit -m "Initial commit"`
13. Push to Remote Repository:`(.venv) django@ubuntuguest:~/tms$ git push -u origin main`


### Snapshot the VM

Once the VM is configured and the initial setup is complete, take a snapshot to preserve this state: 
- Go to VMware > Snapshot > Take Snapshot.
- Name it something like InitialSetup

---

## Step 2: Creating the Accounts App

### Restructure Django Apps
Organizing your Django apps into a dedicated folder (e.g., apps or djangoapps) is a good practice. It improves project structure, enhances maintainability, and keeps your root directory clean. This approach makes it easier to locate apps, especially in large projects, and separates them logically from configuration files and other resources.
- Create a core folder: `(.venv) django@ubuntuguest:~/tms$ mkdir djangoapps`
1. Create a new app inside it: `(.venv) django@ubuntuguest:~/tms/djangoapps$ django-admin startapp accounts`

2. Register the app in settings.py:

    ```python
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # internal apps
        "accounts",
        # external apps
        "rest_framework",
    ]
    ```

3. When running the server `(.venv) django@ubuntuguest:~/tms$ python manage.py runserver 0.0.0.0:8000`, you may see the following error : `ModuleNotFoundError: No module named 'accounts'`. This error occurs because Django cannot find the accounts app in your project. You need to change the app name inside `tms/djangoapps/accounts/apps.py` from `accounts` to `djangoapps.accounts` and update it inside settings `INSTALLED_APPS`.
    ```python
        INSTALLED_APPS = [
            ...
            "djangoapps.accounts",
            ...
        ]
    ```

4. Create the User model in accounts/models.py:
    ```python
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    from django.core.validators import EmailValidator
    from django.utils.translation import gettext_lazy as _


    class UserModel(AbstractUser):
        # Override the email field to make it unique and mandatory
        email = models.EmailField(
            unique=True,
            blank=False,
            null=False,
            validators=[EmailValidator],
            error_messages={
                "unique": _("A user with this email already exists."),
            },
        )
        # extra fields
        phone_number = models.CharField(max_length=15, unique=True, blank=False, null=True)

        USERNAME_FIELD = "email" # Change the username field to email
        REQUIRED_FIELDS = ["username"] # make the username origianl field required

        class Meta:
            verbose_name = _("User")
            verbose_name_plural = _("Users")
            db_table = "user"
            ordering = ["-id"]
    ```

5. Add the line `AUTH_USER_MODEL = "accounts.UserModel"` in the settings.py file tells Django to use a custom user model (UserModel) defined in the accounts app instead of the default User model provided by Django. 
6. Apply migrations:

    ```bash
    (.venv) django@ubuntuguest:~/tms$ python manage.py makemigrations
    Migrations for 'accounts':
        djangoapps/accounts/migrations/0001_initial.py
            + Create model UserModel
    (.venv) django@ubuntuguest:~/tms$ python manage.py migrate
    Operations to perform:
        Apply all migrations: accounts, admin, auth, contenttypes, sessions
    Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0001_initial... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying auth.0010_alter_group_name_max_length... OK
        Applying auth.0011_update_proxy_permissions... OK
        Applying auth.0012_alter_user_first_name_max_length... OK
        Applying accounts.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying sessions.0001_initial... OK
    ```
7. Register the model in `admin.py`:
    - Create Custom User Forms: In the forms.py file within your accounts app, define two custom forms: one for creating a user (CustomUserCreationForm) and another for updating user data (CustomUserChangeForm).
        ```python
        from django.contrib.auth.forms import UserCreationForm, UserChangeForm
        from .models import UserModel

        class CustomUserCreationForm(UserCreationForm):
            """
            Custom form for creating new users. Includes all required fields
            and a repeated password field.
            """

            class Meta:
                model = UserModel
                fields = ("username", "email", "phone_number")  # Include the fields you want to expose


        class CustomUserChangeForm(UserChangeForm):
            """
            Custom form for updating existing users.
            """

            class Meta:
                model = UserModel
                fields = (
                    "username",
                    "email",
                    "phone_number",
                )  # Include fields you want to allow updates on
        ```
    - Create the Custom Admin Class: In admin.py, define a custom admin class (CustomUserAdmin) that inherits from UserAdmin. This class will allow you to customize how the user model appears in the Django admin interface.
        ```python
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from django.utils.translation import gettext_lazy as _
        from django.urls import reverse
        from django.utils.html import format_html

        from .models import UserModel
        from .forms import CustomUserCreationForm, CustomUserChangeForm


        class CustomUserAdmin(UserAdmin):
            """
            Custom admin for the CustomUser model.
            """

            add_form = CustomUserCreationForm
            form = CustomUserChangeForm
            model = UserModel

            # Fields to display in the admin list view
            list_display = ("username", "email", "phone_number", "is_staff", "is_active")
            list_filter = ("is_staff", "is_active", "groups")
            readonly_fields = ("last_login", "date_joined")

            # Fields to display in the admin detail/edit view
            fieldsets = (
                (None, {"fields": ("username", "password")}),
                ("Personal Info", {"fields": ("email", "phone_number", "profile_picture")}),
                (
                    "Permissions",
                    {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
                ),
                ("Important dates", {"fields": ("last_login", "date_joined")}),
            )

            # Fields to display in the admin add view
            add_fieldsets = (
                (
                    None,
                    {
                        "classes": ("wide",),
                        "fields": (
                            "username",
                            "email",
                            "phone_number",
                            "profile_picture",
                            "password1",
                            "password2",
                            "is_staff",
                            "is_active",
                        ),
                    },
                ),
            )

            # Fields to search in the admin list view
            search_fields = ("username", "email", "phone_number")
            ordering = ("username",)


        # Register the CustomUser with the customized admin
        admin.site.register(UserModel, CustomUserAdmin)
        ```
8. Create a Superuser in Django:
    - Run the following command to create a superuser: `(.venv) django@ubuntuguest:~/tms$ python manage.py createsuperuser`
    - Provide the required information for the superuser: Username, Email, Password (you'll be asked to enter it twice).
9. Access the Admin Interface: After registering and migrating, start the development server: `(.venv) django@ubuntuguest:~/tms$ python manage.py runserver 0.0.0.0:8000`.
10. Access the Django Admin Interface: Open a browser and go to **http://ip_address:8000/admin/**. Log in with the superuser credentials you just created, and you should be able to access the admin panel with your custom user model.
![alt text](media/image-1.png)
*User Management - List of Users.*
![alt text](media/image-2.png)
*User Management - Edit User.*
![alt text](media/image-3.png)
*User Management - Add New User.*

11. Commit and Push Changes to GitHub: 
- To follow the Conventional Commits standard, here's an example commit message for adding the accounts app:
    ```git
    git commit -m "feat(accounts): add custom user model, forms, and admin configurations"
    ```
- Push the changes to your remote repository:
    ```git
    git push origin development
    ```