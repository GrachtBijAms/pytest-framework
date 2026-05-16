# pytest Automation Framework

## Overview
A professional test automation framework built with Python and pytest.
Supports UI testing with Playwright, API testing with requests,
data-driven testing, BDD with pytest-bdd, and rich reporting with Allure.

## Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.13 | Core language |
| pytest | 9.0 | Test runner |
| Playwright | 1.44 | Browser automation |
| requests | 2.31 | API testing |
| Allure | 2.41 | Test reporting |
| pytest-html | 4.2 | HTML reporting |
| Faker | 25.0 | Test data generation |


## Project Structure

```
pytest-framework/
├── config/                  # Configuration files
│   ├── config.yaml          # Environment settings
│   └── config_loader.py     # Config loader class
├── core/                    # Core framework utilities
│   ├── base_page.py         # Base page object class
│   └── logger.py            # Logging setup
├── pages/                   # Page object classes
│   ├── login_page.py        # Login page
│   └── home_page.py         # Home page
├── tests/                   # All test files
│   ├── ui/                  # UI tests
│   │   ├── conftest.py      # UI fixtures
│   │   └── test_login.py    # Login tests
│   └── api/                 # API tests
│       ├── conftest.py      # API fixtures
│       └── test_users.py    # User API tests
├── data/                    # Test data
│   ├── excel/               # Excel test data
│   ├── csv/                 # CSV test data
│   └── json/                # JSON test data
├── reports/                 # Generated reports
├── utils/                   # Helper utilities
├── conftest.py              # Root fixtures
├── pytest.ini               # pytest configuration
├── requirements.txt         # Dependencies
└── .env.example             # Environment template
```

## Installation

### Prerequisites
- Python 3.11+
- pip
- Homebrew (Mac only, for Allure)

### Setup

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd pytest-framework
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Install Playwright browsers**
```bash
playwright install
```

**5. Install Allure CLI**
```bash
brew install allure             # Mac
```

**6. Set up environment variables**
```bash
touch .env
# Edit .env with your credentials
```

## Configuration

### Environment Variables (`.env`)
```
ENV=staging                    # Target environment
HEADLESS=false                 # Browser visibility
BROWSER=chromium               # Browser choice
```

### Environments (`config/config.yaml`)
```yaml
environment: staging
environments:
  staging:
    base_url: "https://staging.yourapp.com"
  production:
    base_url: "https://yourapp.com"
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/ui/test_login.py -v
```

### Run by marker
```bash
pytest -m smoke           # smoke tests only
pytest -m regression      # regression tests only
pytest -m ui              # UI tests only
pytest -m api             # API tests only
```

### Run with HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run with Allure report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### Run headless (CI mode)
```bash
HEADLESS=true pytest
```

### Run specific environment
```bash
ENV=staging pytest
ENV=production pytest
```

## Reports

### pytest-html
Generated automatically after every run at `reports/report.html`.
Open in any browser.

### Allure
```bash
# Generate results
pytest --alluredir=reports/allure-results

# Open interactive dashboard
allure serve reports/allure-results
```

Features:
- Test history and trends
- Screenshots on failure
- Step by step execution
- Severity and feature grouping

## Author
Prathamesh Patil
Senior Test Automation Engineer
Amsterdam, Netherlands

## License
MIT
