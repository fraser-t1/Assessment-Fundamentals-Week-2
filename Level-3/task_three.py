from datetime import date


class Assessment:
    ValidTypes = {"multiple-choice", "technical", "presentation"}

    def __init__(self, name: str, assessment_type: str, score: float):
        self.name = name

        if assessment_type not in self.ValidTypes:
            raise ValueError("Invalid type of assessment")
        self.type = assessment_type

        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0-100")
        self.score = score

    def calculate_score(self) -> float:
        return self.score


class Trainee:
    def __init__(self, name: str, email: str, date_of_birth: date, assessments: list = None):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth

        if assessments is None:
            self.assessments = []
        else:
            self.assessments = assessments

    def get_age(self) -> int:
        today = date.today()
        age = today.year - self.date_of_birth.year
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        if not isinstance(assessment, Assessment):
            raise TypeError("Assessment objects only")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, assessment_type: str) -> list[Assessment]:
        if assessment_type not in Assessment.ValidTypes:
            raise ValueError("Invalid assessment type")
        return [assess for assess in self.assessments if assess.type == assessment_type]


class MultipleChoiceAssessment(Assessment):
    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self) -> float:
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)

    def calculate_score(self) -> float:
        return self.score * 1.0


class PresentationAssessment(Assessment):
    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self) -> float:
        return self.score * 0.6


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer

    def is_correct(self) -> bool:
        return self.chosen_answer == self.correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:

        self._quiz = quiz

    def mark(self) -> int:
        if not self._quiz.questions:
            return 0

        count_correct = sum(
            1 for ques in self._quiz.questions if ques.is_correct())
        total_questions = len(self._quiz.questions)

        percentage = (count_correct / total_questions) * 100
        return int(round(percentage, 0))

    def generate_assessment(self) -> Assessment:
        score = float(self.mark())
        name = self._quiz.name

        if self._quiz.type == "multiple-choice":
            return MultipleChoiceAssessment(name, score)
        elif self._quiz.type == "technical":
            return TechnicalAssessment(name, score)
        elif self._quiz.type == "presentation":
            return PresentationAssessment(name, score)
        else:
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

    # Add an implementation for the Marking class below to test your code
