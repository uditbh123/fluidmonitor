# 🧪 Fluid Monitor Dashboard

A full-stack web application for logging, tracking, and visualizing industrial fluid sensor readings — built with Django, Bootstrap 5, and Chart.js.

---

## 💡 Why I Built This

This project was built to simulate a real-world use case: monitoring industrial fluids like coolants and lubricants used in manufacturing machines. These fluids need to be constantly checked — if pH levels drift or temperatures spike, machines get damaged.

This dashboard replaces a manual clipboard process with a proper web interface where operators can log readings, spot trends over time, and filter by sensor.

The project was intentionally designed to mirror the core product idea at Spesnes — a startup building comprehensive analysis and maintenance solutions for industrial fluids.

---

## 🚀 Features

- **Log sensor readings** — record pH, temperature, concentration, and percentage values from any sensor
- **Live dashboard** — view all readings in a clean, responsive Bootstrap 5 table
- **Add readings from the frontend** — a form page lets any user log a new reading without needing admin access
- **Data visualization** — interactive line chart showing sensor values over time using Chart.js
- **Filter by sensor** — narrow down readings to a specific sensor with a dropdown filter
- **Statistics** — automatic calculation of average, minimum, and maximum values
- **Django Admin** — full admin panel for managing data directly
- **JSON API endpoint** — `/chart-data/` returns sensor data as JSON, consumed by the frontend chart

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Backend | Python 3, Django 6 | Server logic, routing, ORM |
| Database | SQLite | Storing sensor readings |
| Frontend | HTML5, Bootstrap 5 | Responsive UI and layout |
| Charts | Chart.js | Data visualization |
| JavaScript | Vanilla JS, Fetch API | Dynamic chart loading |
| Version Control | Git, GitHub | Source control |

---

## 🏗️ How It Works

The project follows Django's **MTV architecture** (Model, Template, View):

```
Browser Request
      ↓
urls.py → routes the request to the right view
      ↓
views.py → fetches data from the database
      ↓
models.py → defines the shape of the data in the database
      ↓
template (HTML) → renders the page with data
      ↓
Browser displays the result
```

### The Database Layer
Sensor readings are stored in a SQLite database using Django's ORM. Instead of writing raw SQL, models are defined as Python classes and Django handles the translation automatically:

```python
class Reading(models.Model):
    sensor_name = models.CharField(max_length=100)        # Text field
    value       = models.DecimalField(...)                # Precise decimal number
    unit        = models.CharField(choices=...)           # Restricted to pH, C, mg/L, %
    recorded_at = models.DateTimeField(auto_now_add=True) # Auto timestamp
    notes       = models.TextField(blank=True)            # Optional notes
```

### The Form Layer
New readings are submitted through a Django ModelForm. Django handles:
- Rendering the form fields as HTML automatically
- Validating input before saving (is value a number? is unit a valid choice?)
- CSRF protection — a hidden security token that prevents malicious form submissions
- Saving valid data to the database and redirecting back to the dashboard

### The Mini API
The chart is powered by a JSON endpoint built in Django:
- `/chart-data/` returns sensor readings as JSON
- JavaScript uses `fetch()` to call this endpoint
- Chart.js renders the data as an interactive line graph

This is a simplified version of how real data pipelines work — the backend serves data, the frontend consumes it.

---

## 📁 Project Structure

```
fluidmonitor/
├── core/                        # Project configuration
│   ├── settings.py              # App settings, installed apps, database config
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # Web server entry point
├── readings/                    # Main Django app
│   ├── migrations/              # Database migration history
│   │   └── 0001_initial.py      # First migration — creates readings table
│   ├── templates/
│   │   └── readings/
│   │       ├── home.html        # Dashboard page with stats and table
│   │       └── add_reading.html # Add new reading form page
│   ├── models.py                # Reading data model (database table)
│   ├── views.py                 # Business logic and page rendering
│   ├── urls.py                  # App-level URL routing
│   ├── forms.py                 # Django ModelForm for adding readings
│   └── admin.py                 # Admin panel configuration
├── db.sqlite3                   # SQLite database (auto-created)
├── manage.py                    # Django management commands
├── .gitignore                   # Files excluded from version control
└── README.md                    # This file
```

---

## 🗄️ Database Model

The core data model is a `Reading` object stored in the `readings_reading` table:

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Auto-generated primary key |
| `sensor_name` | CharField | Name of the sensor e.g. "Tank A" |
| `value` | DecimalField | The numeric reading e.g. 7.24 |
| `unit` | CharField | Unit of measurement (pH, C, mg/L, %) |
| `recorded_at` | DateTimeField | Timestamp — set automatically on save |
| `notes` | TextField | Optional notes about the reading |

### How Migrations Work
Django uses a two-step process to keep Python code and the database in sync:

- **`makemigrations`** — reads models.py and creates a blueprint file describing the table structure
- **`migrate`** — executes that blueprint and creates/updates the actual database table

This two-step approach allows migration files to be shared across teams so every developer's database stays in sync.

---

## ⚙️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/uditbh123/fluidmonitor.git
cd fluidmonitor

# Install Django
pip install django

# Run database migrations
python manage.py migrate

# Create an admin account
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Then open **http://127.0.0.1:8000** in your browser.

Admin panel available at **http://127.0.0.1:8000/admin**

---

## 📸 Pages

| Page | URL | Description |
|------|-----|-------------|
| Dashboard | `/` | All readings, stats cards, and chart |
| Add Reading | `/add/` | Form to log a new sensor reading from the frontend |
| Admin | `/admin/` | Django admin panel for superusers |
| Chart Data | `/chart-data/` | JSON API endpoint for the chart |

---

## 🧠 Key Concepts Learned

**Day 1 — Django foundations**
- MTV architecture — how Models, Templates, and Views work together
- URL routing — how web requests are directed to the right function
- Template rendering — how Django fills HTML with dynamic data
- App registration — why every app must be in INSTALLED_APPS

**Day 2 — Database & ORM**
- Django ORM — querying and writing to a database using Python instead of raw SQL
- Model fields — CharField, DecimalField, DateTimeField, TextField and when to use each
- Migrations — the two-step process of makemigrations and migrate
- auto_now_add — automatic timestamps on record creation
- Django Admin — registering models and configuring list views
- Decorators — what @admin.register does and why the @ symbol matters

**Day 3 — Bootstrap 5 Dashboard**
- Bootstrap grid system — how col-md-4 creates responsive side-by-side layouts
- Bootstrap components — cards, tables, navbars, buttons using only class names
- Django template syntax — loops, filters, and passing context from views to templates
- Django ORM aggregation — calculating avg, min, max across all database rows
- QuerySet ordering — order_by('-recorded_at') to sort newest first

**Day 4 — Django Forms**
- ModelForm — generating a form automatically from a database model
- GET vs POST — GET loads the empty form, POST submits and saves the data
- Form validation — Django checks data before saving to the database
- CSRF protection — the hidden security token that prevents malicious submissions
- HttpResponse requirement — every Django view must return a response or Django raises an error
- Python indentation — how incorrect indentation causes logic bugs like returning None

---

## 🗓️ Build Progress

- [x] Day 1 — Django setup, URL routing, first template
- [x] Day 2 — Database model, migrations, Django Admin
- [x] Day 3 — Bootstrap 5 dashboard, stats cards, readings table
- [x] Day 4 — Django forms, add reading page, form validation, CSRF
- [ ] Day 5 — Chart.js visualization, JSON API endpoint
- [ ] Day 6 — Filter by sensor, polish and responsive design

---

## 👨‍💻 Author

**Udit Bhandari**
- GitHub: [@uditbh123](https://github.com/uditbh123)

---

*Built as a learning project to explore Django backend development, data visualization, and full-stack web architecture.*