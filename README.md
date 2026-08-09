# Hybrid Automation Framework (UI + API + Jenkins CI)  

--------------------------------------------------------------------------------------------------------------------------------

![Python](https://img.shields.io/badge/python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-olive)
![API](https://img.shields.io/badge/API-Requests-blue)
![Framework](https://img.shields.io/badge/Framework-Hybrid%20UI%20%2B%20API-purple)
![POM](https://img.shields.io/badge/Design%20Pattern-Page%20Object%20Model-brightgreen)
![Allure](https://img.shields.io/badge/Allure-Reporting-black)
![Jenkins](https://img.shields.io/badge/Jenkins-CI-red)
![HTML Report](https://img.shields.io/badge/Pytest-HTML%20Report-orange)
![Faker](https://img.shields.io/badge/Test%20Data-Faker-brown)
![Browser](https://img.shields.io/badge/Browser-Chrome%20%7C%20Firefox-yellow)

A Hybrid Test Automation Framework built using **Python, Pytest, Selenium WebDriver**, and **Requests**.  
The framework combines **UI Automation** and **REST API Automation** in a single project. UI tests follow the **Page Object Model (POM)** design pattern, while API tests use a reusable API client.  

The framework is designed to be modular, scalable, maintainable, reusable and CI-ready.  

----------------------------------------------------------------------------------------------------------------------------

## Project Overview

This framework covers:  

- UI automation using Selenium WebDriver  
- REST API automation using Requests  
- Page Object Model (POM)  
- Pytest fixtures and markers  
- Data-driven test data generation using Faker  
- Custom logging  
- Screenshot capture  
- HTML test reporting  
- Allure reporting support  
- Jenkins CI integration  
- Git/GitHub source control  

### Current Jenkins Execution

The framework is integrated with **Jenkins Freestyle Project** for continuous test execution.

The Jenkins job:

1. Checks out the latest code from GitHub  
2. Creates a Python virtual environment  
3. Installs project dependencies from requirements.txt  
4. Executes the Pytest automation suite  
5. Generates an HTML test report  
6. Publishes the test execution result  

### Latest Jenkins Test Result

### 12 automated tests executed — 12 passed

- UI Tests: 7  
- API Tests: 5  
- Result: 100% Passed  
- Execution Status: SUCCESS  

## Tech Stack  
- Python  
- Pytest  
- Selenium WebDriver  
- Requests  
- Page Object Model (POM)  
- Faker  
- Jenkins  
- Logging  
- Pytest HTML Reports  
- Allure Reports  
- Git & GitHub  

-----------------------------------------------------------------------------------------------------------------------------------------------

## Project Structure


```HybridFramework/  
│  
├── api/   
│   ├── client/  
│   │   └── api_client.py  
│   ├── data/  
│   │   └── user_payload.py  
│   ├── tests/  
│   │   └── test_get_users.py  
│   │   └── test_create_user.py  
│   │   └── test_update_user.py  
│   │   └── test_invalid_user.py  
│   │   └── test_delete_user.py  
│   └── utils/  
│       └── random_data.py  
│  
├── base_pages/  
│   │   └── home_page.py  
│   │   └── login_page.py  
│   │   └── shop_page.py  
│   │   └── miscellaneous_ui_page.py  
│   
├── configurations/  
│   └── config.py   
│  
├── logs/  
│  
├── reports/  
│  
├── screenshots/  
│  
├── test_cases/  
│   │   └── test_home_page.py  
│   │   └── test_login_page.py  
│   │   └── test_shop_page.py  
│   │   └── test_miscellaneous_ui_page.py  
│  
├── utilities/  
│   ├── custom_logger.py  
│   ├── read_properties.py  
│  
├── conftest.py  
├── pytest.ini  
├── requirements.txt  
└── README.md 
``` 

-------------------------------------------------------------------------------------------------------------------------------------------

## UI Automation

The UI automation is developed using Selenium WebDriver with the Page Object Model (POM) design pattern.

### UI Features:
- Page Object Model (POM)  
- Cross-browser support  
- Pytest fixtures  
- Browser management through `conftest.py`  
- Explicit and implicit waits  
- Screenshot capture on failures  
- Custom logging  
- HTML reporting  
- Allure reporting  
- Pytest markers (`ui, sanity, regression`)  

### UI Test Modules:  
### Home Page  

- Page title validation  
- Form submission  
- Input field validation  
- Success message validation  

### Login Page  

- Valid login  
- Invalid login  
- Error message validation  
- New tab/window handling  
- Text extraction and validation  

### Shop Page  

- Product selection  
- Add-to-cart flow  
- Checkout process  
- Country selection  
- Terms and conditions  
- Purchase validation  

### Miscellaneous UI Page  

- Radio buttons  
- Dropdowns  
- Checkboxes  
- Alerts  
- Confirmation popups  
- Browser windows  
- iFrames  
- Mouse hover  
- Web tables  
- Hide/Show elements  
- Scrolling  

-------------------------------------------------------------------------------------------------------------------------------------------

## API Automation  

The API automation is implemented using the **Requests** library with a reusable API client.  

### API Features:
- Reusable API Client  
- GET  
- POST   
- PUT  
- DELETE  
- Authorization using Bearer Token  
- Session management  
- Dynamic payload generation  
- Faker for generating random test data  
- Request and Response logging  
- Response time logging  
- Status code validation  
- Response body validation

### API Test Scenarios 

- Get users  
- Create user  
- Update user  
- Delete user  
- Validate invalid user response  

---------------------------------------------------------------------------------------------------------------------------------------------

## Test Data & Configuration

Environment-specific configuration is managed using **Python-dotenv**.

The framework reads configuration values from a `.env` file, including:  

- Application URLs  
- UI credentials  
- API base URL  
- API token  

Sensitive configuration such as passwords and API tokens **should not be committed to GitHub**.

-----------------------------------------------------------------------------------------------------------------------

## Logging

A centralized custom logger is used throughout the framework.

### UI Logging:
- Test execution  
- Browser actions  
- Navigation  
- Form interactions  
- Validation results  
- Screenshot information  

### API Logging:
- HTTP Method  
- Request Payload  
- Status Code  
- Response Time  
- Response Body  

---------------------------------------------------------------------------------------------------------------------------------------------

## Jenkins CI Integration

The automation framework is integrated with **Jenkins Freestyle Project** for CI-based test execution.  

### Jenkins Workflow
GitHub Repository  
       ↓  
Jenkins Freestyle Job  
       ↓  
Checkout Source Code  
       ↓  
Create Python Virtual Environment  
       ↓  
Install requirements.txt  
       ↓  
Execute Pytest Tests  
       ↓  
Generate HTML Report  
       ↓  
Build Result  

### Jenkins Build Configuration

The Jenkins job performs the following operations:

python3 -m venv venv  
source venv/bin/activate  
python -m pip install --upgrade pip  
python -m pip install -r requirements.txt  
python -m pytest -s -v --html=reports/report.html --browser chrome  

The Jenkins job successfully executes both UI and API automation tests and generates a Pytest HTML report.

#### Latest Successful Build
Test Suite: Hybrid Automation Framework - UI + API  
Total Tests: 12  
Passed: 12  
Failed: 0  
Result: SUCCESS  

--------------------------------------------------------------------------------------------------------------------------- 

## Reporting
### Pytest HTML Report

The framework generates an HTML test execution report using `pytest-html`.
```
pytest --html=reports/report.html --self-contained-html
```
The HTML report provides test execution details, results, environment information and test metedata. 

### Allure Reporting:

#### Run tests with:
```
pytest --alluredir=allure-results
```
Generate and view the report:
```
allure serve allure-results
```
---------------------------------------------------------------------------------------------------------------------------------------------

## Installation

#### Clone the repository:  

git clone: https://github.com/jotestcode/HybridFramework.git

#### Navigate to the project:
```
cd HybridFramework
```
### Create Virtual Environment
```
python3 -m venv venv
```
### Activate Virtual Environment

### macOS / Linux
```
source venv/bin/activate
```
### Windows
```
venv\Scripts\activate
```
#### Install dependencies:
```
pip install -r requirements.txt
```
---------------------------------------------------------------------------------------------------------------------------------------------

### Running Tests

Run all tests:  
```
pytest  
```
Run only UI tests:  
```
pytest -m ui 
```
Run only API tests:  
```
pytest -m api         
```
Run regression suite:
```
pytest -m regression  
```
Run sanity suite:
```
pytest -m sanity
```

Run UI + API together with HTML report:  
```
pytest -m "ui or api" --html=reports/hybrid_report.html --self-contained-html  
```

Run UI + API together with HTML and Allure reports:  
```
pytest -m "ui or api" --html=reports/hybrid_report.html --self-contained-html --alluredir=allure-results   
```
------------------------------------------------------------------------------------------------------------------------------------------- 

## Framework Highlights

- Hybrid UI and API automation  
- Selenium WebDriver automation  
- REST API automation using Requests  
- Page Object Model (POM) architecture  
- Reusable API Client  
- Pytest fixtures  
- Pytest markers  
- Dynamic test data generation  
- Faker integration  
- Environment-based configuration  
- Custom logging  
- Screenshot capture  
- HTML test reporting  
- Allure reporting support  
- Jenkins CI integration  
- Git/GitHub source control  
- Modular and maintainable architecture   

---------------------------------------------------------------------------------------------------------------------------------------------

### Author

#### Josephine Job

Python | Selenium | API Testing | Pytest | Automation Testing  | Jenkins
