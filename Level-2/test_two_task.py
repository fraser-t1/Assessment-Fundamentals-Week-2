# pylint: skip-file

from task_two import MultipleChoiceAssessment, TechnicalAssessment, PresentationAssessment, Assessment, Trainee
import pytest
from datetime import date


@pytest.fixture(autouse=True)
def run_before_and_after_tests(tmpdir):
    # Setup: fill with any logic you want
    yield  # this is where the testing happens
    # Teardown : fill with any logic you want


def test_assessment_multiple_choice():
    assessment = MultipleChoiceAssessment("Python Basics", 21)
    assert assessment.name == "Python Basics"
    assert assessment.calculate_score() == 14.7


def test_assessment_technical():
    assessment = TechnicalAssessment("Python Basics", 20)
    assert assessment.name == "Python Basics"
    assert assessment.calculate_score() == 20.0


def test_assessment_presentation():
    assessment = PresentationAssessment("Python Basics", 20)
    assert assessment.name == "Python Basics"
    assert assessment.calculate_score() == 12.0


def test_is_assessment():
    assessment = MultipleChoiceAssessment("Python Basics", 20)
    assert isinstance(assessment, Assessment) == True
    assert isinstance(assessment, MultipleChoiceAssessment) == True
    assert isinstance(assessment, TechnicalAssessment) == False
    assert isinstance(assessment, PresentationAssessment) == False


def test_is_assessment_2():
    assessment1 = MultipleChoiceAssessment("Python Basics", 20)
    assessment2 = PresentationAssessment("Python Basics", 20)
    assessment3 = TechnicalAssessment("Python Basics", 20)

    assert isinstance(assessment1, Assessment) == True
    assert isinstance(assessment2, Assessment) == True
    assert isinstance(assessment3, Assessment) == True


def test_add_assessment_value_error():
    trainee = Trainee("Sigma", "test", date.today())
    with pytest.raises(TypeError):
        trainee.add_assessment({})


def test_get_assessment_of_type():
    trainee = Trainee("Sigma", "test", date.today())
    assessment1 = MultipleChoiceAssessment("Python Basics", 20)
    assessment2 = PresentationAssessment("Python Basics", 20)
    assessment3 = MultipleChoiceAssessment("Python Basics", 20)
    trainee.add_assessment(assessment1)
    trainee.add_assessment(assessment2)
    trainee.add_assessment(assessment3)

    assert len(trainee.get_assessment_of_type("multiple-choice")) == 2
    assert len(trainee.get_assessment_of_type("technical")) == 0
    assert len(trainee.get_assessment_of_type("presentation")) == 1
