# Restaurant Menu API

<p>restaurant menu api. api that has user registration and login functionality</p>
<p>logged user can prform crud operations on restaurants, menus and dishes.</p>

### there are next links on our site

1. **localhost/api displays available links.**
2. **localhost/users displays registered users.**
3. **localhost/restaurants displays created restaurants.**
4. **localhost/menus displays created menucategory.**
5. **localhost/submenus displays created submenucategories.**
6. **localhost/submenus/2/ displays submenucategory and dishes associated with submenu.**
7. **localhost/dishes displays created dishes.**

<p>unauthorized users cant add or modifie objects.</p>
<p>Site has superuser (user:admin, pass:admin).</p>

### Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)

### Prerequisites

- <img src="readme/assets/python.png" width="25" style="position: relative; top: 8px" /> _Python @3.X and up_
- <img src="readme/assets/django.png" width="25" style="position: relative; top: 8px" /> _Django @5.X and up_

#

### Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/NikaKhiz/restaurant-menu-api.git
   cd django-store
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

   or

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install django and necessary libraries**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Run scripts**:

- Simply run the `python3 manage.py runserver` command :

```bash
python manage.py runserver
```

or

```bash
python3 manage.py runserver
```

### the code above will start development server and you should be good to go. you can visit site on [localhost](http://127.0.0.1:8000/)!!!
