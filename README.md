# lab-python

Run unit test on project

- Linux\Mac
```
pytest
```
- Windows
```
python -m pytest
```

### Coverage code
To generate coverage report, using the package 'pytest-cov' with the command:
```
pytest --cov-report html:report/coverage --cov=lab tests
```
Where

**--cov=[PROJECT]** - Coverage project

**--cov-report** - Ouput format, where:
- **HTML** - Generate HTML report *--cov-report html*
- **XML** - Generate XML report *--cov-report xml*

### Common Commands

Unit test
```
pytest -s --html=report\unit_test.html
```

Coverage
```
pytest --cov-report html:report/coverage --cov=lab tests/
```
