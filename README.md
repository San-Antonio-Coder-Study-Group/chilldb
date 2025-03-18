## ChillDB
> A team-built project with an altruistic twist, designed for learning and growth. <br>
> We’re diving into databases, sharpening our Python skills, and exploring Django together. <br>

---

### What’s This All About?
ChillDB is a Django-powered playground where we can get hands-on with databases, data ingestion, and visualization. We’re building an app that imports data, displays it nicely on the front end, and lets users mess with database partitions—like setting up leaders, followers, and assigning records. Along the way, we’re learning Django’s MVC flow, brushing up on object-oriented programming, and keeping the vibes relaxed yet productive.

---

### Goals
- Craft a Django app that ingests a hefty amount of data with ease.
- Create a clean front-end interface for visualizing database goodies.
- Enable database tinkering: partitioning, record assignment, and maybe even leader/follower setups.
- Master Django and its MVC paradigm as a team.
- Level up our object-oriented programming skills through real-world practice.
- Build something useful for others while having fun and learning together.

---

### Project Structure
Here’s how our project is laid out—pretty standard Django stuff with a sprinkle of extras:

```bash
.
├── README.md
├── init.py
├── asgi.py
├── chilldbapp
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── init.py
│   ├── models.py
│   ├── templates
│   │   └── chilldbapp
│   │       └── db_visualizer.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── settings.py
├── urls.py
└── wsgi.py



```



---

### Running the Project
Let’s get this thing up and running! Here’s how:

#### Prerequisites
- Python 3.8+ (we’re using Django 4.2.20)
- Docker && Docker Compose (for spinning up the MySQL databases)
- docker-compose up -d 
- Check the docker-compose.yml for connection credentials

#### Steps
1. **Clone the Repo**
   ```bash
   git clone git@github.com:San-Antonio-Coder-Study-Group/chilldb.git
   cd chilldb
   ```
2. **Setup the virtual environment**
```bash
python -m venv venv
source venv/bin/activate 
```

3. **Install Dependencies**
- `pip3 -r requirements.txt`

4. **Run Migrations (for the default SQLite DB for now)**
`python manage.py migrate`

5. `python manage.py runserver`


## TODO

---
> Here’s what’s on our plate—feel free to grab a task and run with it!

- Hook up the MySQL databases from `docker-compose.yml` to Django (update `settings.py`).
- Replace placeholder data in `db_visualizer` with real database queries.
- Add data ingestion logic—import some chunky datasets to play with.
- Build out partitioning features: range, hash, and local index support.
- Set up static assets (CSS/JS) for a polished front-end:
   - Move inline styles from `db_visualizer.html` to a `static/chilldbapp/css/` folder.
   - Add JS for dynamic interactions in `static/chilldbapp/js/`.
- Create models in `chilldbapp/models.py` for database records and partitions.
- Add user controls for modifying partitions (e.g., forms or API endpoints).
- Implement leader/follower logic for distributed database vibes.