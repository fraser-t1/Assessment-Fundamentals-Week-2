""" this is the solution to task 1 """
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


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
