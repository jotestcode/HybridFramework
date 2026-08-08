## Hybrid Automation Framework (UI + API)  

--------------------------------------------------------------------------------------------------------------------------------

![Python](https://img.shields.io/badge/python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-olive)
![API](https://img.shields.io/badge/API-Requests-blue)
![Framework](https://img.shields.io/badge/Framework-Hybrid%20UI%20%2B%20API-purple)
![POM](https://img.shields.io/badge/Design%20Pattern-Page%20Object%20Model-brightgreen)
![Allure](https://img.shields.io/badge/Allure-Reporting-black)
![HTML Report](https://img.shields.io/badge/Pytest-HTML%20Report-orange)
![Faker](https://img.shields.io/badge/Test%20Data-Faker-brown)
![Browser](https://img.shields.io/badge/Browser-Chrome%20%7C%20Firefox-yellow)

A Hybrid Automation Framework built using **Python, Pytest, Selenium WebDriver**, and **Requests**.  
This framework combines **UI Automation** and **API Automation** into a single project, following the **Page Object Model (POM)** design pattern for UI tests and a reusable API client for REST API testing.  

The framework is designed to be scalable, maintainable, and easy to integrate with CI/CD pipelines.  

## Tech Stack  
- Python  
- Pytest  
- Selenium WebDriver  
- Requests  
- Page Object Model (POM)  
- Faker  
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

# UI Automation

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
- Home Page  
- Login Page  
- Shop Page  
- Miscellaneous UI Page  

-------------------------------------------------------------------------------------------------------------------------------------------

## API Automation  

The API automation is implemented using the Requests library.  

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

---------------------------------------------------------------------------------------------------------------------------------------------

### Logging

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

## Reporting
### Pytest HTML Report

#### Generate HTML report:
```
pytest --html=reports/hybrid_report.html --self-contained-html
```
### Allure Report:

#### Run tests:
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

cd HybridFramework

#### Install dependencies:

pip install -r requirements.txt

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

- Hybrid UI and API automation framework  
- Modular and reusable architecture  
- Page Object Model (POM)  
- Reusable API Client  
- Pytest Fixtures  
- Data-driven test payload generation  
- Faker integration  
- Custom logging  
- HTML and Allure reporting  
- Easy maintenance and scalability  

---------------------------------------------------------------------------------------------------------------------------------------------

### Author

#### Josephine Job

Python | Selenium | API Testing | Pytest | Automation Testing  
