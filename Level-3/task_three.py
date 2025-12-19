""" this is the solution to task 3 """
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


class Question:
    """ represents one question in a quiz """

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer

    def is_correct(self) -> bool:
        """ checks is user's answer is correct """
        return self.chosen_answer == self.correct_answer

    def update_answer(self, new_answer: str) -> None:
        """ updates user's answer for this question """
        self.chosen_answer = new_answer


class Quiz:
    """ collection of questions in an assessment type """

    def __init__(self, questions_for_quiz: list, name: str, quiz_type: str):
        self.questions = questions_for_quiz
        self.name = name
        self.type = quiz_type

    def validate_length(self) -> None:
        """ ensures quiz does not exceed 100 questions """
        if not 0 <= len(self.questions) <= 100:
            raise ValueError("quiz must have 0-100")

    def add_question(self, question_for_quiz: Question) -> None:
        """ adds a Question and re-validates length """
        self.questions.append(question_for_quiz)
        self.validate_length()


class Marking:
    """ scoring logic for a quiz and coverts it into an Assessment """

    def __init__(self, quiz_for_marking: Quiz) -> None:

        self._quiz = quiz_for_marking

    def mark(self) -> int:
        """ calculates percentage of correct answers rounded to 0 dp """
        if not self._quiz.questions:
            return 0

        count_correct = sum(
            1 for ques in self._quiz.questions if ques.is_correct())
        total_questions = len(self._quiz.questions)

        percentage = (count_correct / total_questions) * 100
        return int(round(percentage, 0))

    def generate_assessment(self) -> Assessment:
        """ returns specific Assessment subclass """

        score = float(self.mark())
        name = self._quiz.name

        if self._quiz.type == "multiple-choice":
            return MultipleChoiceAssessment(name, score)
        if self._quiz.type == "technical":
            return TechnicalAssessment(name, score)
        if self._quiz.type == "presentation":
            return PresentationAssessment(name, score)

        return Assessment(name, self._quiz.type, score)


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    marker = Marking(quiz)

    print(f"Percentage: {marker.mark()}%")

    final_assessment = marker.generate_assessment()
    print(f"Generated type: {type(final_assessment).__name__}")
    print(f"Weighted score: {final_assessment.calculate_score()}")

    trainee = Trainee("Fraser", "f@sigma", date(2025, 12, 1))
    trainee.add_assessment(final_assessment)
    print(f"Trainee assessments: {trainee.assessments}")
