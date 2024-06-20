import pytest
from .student import Student


def test_email():
    obj_anna = Student('ana', 'kowalska', 4.6, None)
    assert obj_anna.email == 'ana.kowalska@university.com'

    obj_anna.name = 'anna'
    assert obj_anna.email == 'anna.kowalska@university.com'


def test_fullname():
    obj_anna = Student('anna', 'kowalska', 4.6, None)
    assert obj_anna.fullname == 'Anna Kowalska'

    obj_anna.last = 'Zamezna'

    assert obj_anna.fullname == 'Anna Zamezna'


def test_grant_scholarship():
    obj_anna = Student('anna', 'kowalska', 4.6, None)
    obj_arek = Student('arkadiusz', 'nowak', 3.8, None)

    obj_anna.grant_scholarship()
    assert obj_anna.scholarship is True

    obj_arek.grant_scholarship()
    assert obj_arek.scholarship is False
