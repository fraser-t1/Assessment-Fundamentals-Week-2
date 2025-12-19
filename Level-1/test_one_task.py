# pylint: skip-file

from task_one import Trainee, Assessment
import pytest
from dateutil.relativedelta import relativedelta
from datetime import date, datetime

def test_trainee():
    years_ago = date.today() - relativedelta(years=20)

    trainee = Trainee("Sigma", "test", years_ago)
    assert trainee.name == "Sigma"
    assert trainee.email == "test"
    assert trainee.assessments == []

    assert trainee.date_of_birth == years_ago
    assert trainee.get_age() == 20.0


def test_assessment():
    assessment = Assessment("Python Basics", "multiple-choice", 90.1)
    assert assessment.name == "Python Basics"
    assert assessment.type == "multiple-choice"
    assert assessment.score == 90.1


def test_valid_assessments_types():
    Assessment("Python Basics", "technical", 50.0)
    Assessment("Python Basics", "multiple-choice", 50.0)
    Assessment("Python Basics", "technical", 50.0)


def test_invalid_assessments_score():
    with pytest.raises(ValueError):
        Assessment("Python Basics", "multiple-choice", -1)
    with pytest.raises(ValueError):
        Assessment("Python Basics", "multiple-choice", 101)


def test_invalid_assessment_type():
    with pytest.raises(ValueError):
        Assessment("Python Basics", "invalid-type", 90.1)


def test_assessments_in_trainee():
    t = Trainee("John Doe", "johndoe@example.com", date(1990, 5, 1))
    a = Assessment("Python Basics", "multiple-choice", 90.1)
    t.add_assessment(a)
    assert len(t.assessments) == 1


def test_assessments_in_trainee_retrieve():
    t = Trainee("John Doe", "johndoe@example.com", date(1990, 5, 1))
    a = Assessment("Python Basics", "multiple-choice", 90.1)
    t.add_assessment(a)
    assert len(t.assessments) == 1
    assert t.get_assessment("Python Basics") == a
    assert t.get_assessment("Nonexistent Assessment") is None


def test_get_assessment_from_empty_list():
    t = Trainee("John Doe", "johndoe@example.com", date(1990, 5, 1))
    assert t.get_assessment("Python Basics") is None


def test_multiple_assessments_with_same_name():
    t = Trainee("John Doe", "johndoe@example.com", date(1990, 5, 1))
    a1 = Assessment("Python Basics", "multiple-choice", 90.1)
    a2 = Assessment("Python Basics", "technical", 90.1)
    t.add_assessment(a1)
    t.add_assessment(a2)
    # The first added assessment
    assert t.get_assessment("Python Basics") == a1
