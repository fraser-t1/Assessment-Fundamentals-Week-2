""" this is the solution to task 2 """
from datetime import date


class Assessment:
    """ class for general trainee assessment """
    ValidTypes = {"multiple-choice", "technical", "presentation"}

    def __init__(self, name: str, assessment_type: str, score: float):
        """ initialises Assessment """
        self.name = name
        self.validate_type(assessment_type)
        self.validate_score(score)
        self.type = assessment_type
        self.score = score

    def validate_type(self, assessment_type: str) -> None:
        """ validates assessment type is allowed """
        if assessment_type not in self.ValidTypes:
            raise ValueError("Invalid type of assessment")

    def validate_score(self, score: float) -> None:
        """ validates score is a float in range 0-100 """
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0-100")

    def calculate_score(self) -> float:
        """ returns weighted score to be used by each type of assessment """
        return self.score


class Trainee:
    """ trainee taking part in the assessment process """

    def __init__(self, name: str, email: str, date_of_birth: date, assessments: list = None):
        """ initialises a trainee. Uses None for assessments to avoid mutable default arguments """
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth

        if assessments is None:
            self.assessments = []
        else:
            self.assessments = assessments

    def get_age(self) -> int:
        """ calculates age based on DOB """
        today = date.today()
        age = today.year - self.date_of_birth.year
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """ adds completed assessment to trainee's record """
        if not isinstance(assessment, Assessment):
            raise TypeError("Assessment objects only")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """ finds assessment """
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, assessment_type: str) -> list[Assessment]:
        """ returns assessments of a chosen type """
        if assessment_type not in Assessment.ValidTypes:
            raise ValueError("Invalid assessment type")
        return [assess for assess in self.assessments if assess.type == assessment_type]


class MultipleChoiceAssessment(Assessment):
    """ Assessment subclass with weighting of 70% """

    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self) -> float:
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """ Assessment subclass with weighting of 100% """

    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)

    def calculate_score(self) -> float:
        return self.score * 1.0


class PresentationAssessment(Assessment):
    """ Assessment subclass with weighting of 60% """

    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self) -> float:
        return self.score * 0.6


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
