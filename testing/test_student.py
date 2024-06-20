# test_student.py
import pytest
from .student import Student



@pytest.fixture(scope='module')
def student():
    print("---> Creating a new Student object")
    return Student('anna', 'kowalska', 4.6, None)

def test_email(student):
    print("Running test_email")
    assert student.email == 'anna.kowalska@university.com'

def test_fullname(student):
    print("Running test_fullname")
    assert student.fullname == 'Anna Kowalska'

