# pylint: skip-file

from task_three import Marking, Quiz, Question, MultipleChoiceAssessment, Assessment, TechnicalAssessment
import pytest


def test_marking():
    # Multiple choice questions below
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    marking = Marking(quiz)
    assert marking.mark() == 100.0


def test_generate_assessment():
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    marking = Marking(quiz)
    assessment = marking.generate_assessment()
    assert isinstance(assessment, Assessment)
    assert isinstance(assessment, MultipleChoiceAssessment)
    assert assessment.name == "Maths Quiz"
    assert assessment.calculate_score() == 70


def test_marking_quiz_private():
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    marking = Marking(quiz)
    assert hasattr(marking, "_quiz")
    assert marking._quiz == quiz


def test_marking_quiz_wrong():
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "X", "."),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "X", "."),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    marking = Marking(quiz)
    assert marking.mark() == 60


def test_marking_quiz_none_value():
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", None, "."),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "X", "."),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    marking = Marking(quiz)
    assert marking.mark() == 60


def test_marking_quiz_no_questions():
    questions = []
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    marking = Marking(quiz)
    assert marking.mark() == 0


def test_marking_quiz_one_question():
    questions = [Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A")]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    marking = Marking(quiz)
    assert marking.mark() == 100

    questions = [Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", ".")]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    marking = Marking(quiz)
    assert marking.mark() == 0


def test_marking_assessment_type():
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "X", "."),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "X", "."),
    ]
    quiz = Quiz(questions, "Maths Quiz", "technical")
    marking = Marking(quiz)
    assessment = marking.generate_assessment()
    assert isinstance(assessment, Assessment)
    assert isinstance(assessment, TechnicalAssessment)
