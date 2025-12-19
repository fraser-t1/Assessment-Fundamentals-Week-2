# Level 3

Finally, let's create a `Marking` class that will help us to mark assessments.

## 1. Marking

In `task_three.py` you'll find the beginnings of a `Marking` class. Update it to have the following:

- `__init__(self, quiz: Quiz)`
  - This method should take a `Quiz` object and store it in a private variable called `_quiz`.
- `mark(self) -> int`
  - This method should return the total score for the assessment as a percentage, rounded to zero decimal places (i.e. an `int`).
  - Each correct answer is worth a single point
  - This function must **not** throw any errors
- `generate_assessment(self) -> Assessment`
  - This should return an instance of an `Assessment` of the correct subclass with the correct name and score.
    - e.g. If the quiz is a `multiple-choice` then this should return a `MultipleChoiceAssessment`. If it is a `technical` quiz then this should return a `TechnicalAssessment` etc

A quiz can contain any number of questions from 0 to 100.

## Note

Due to the way that that default arguments are stored in Python, you should not use mutable default arguments in your function signature. This means that **you should not use `[]` or `{}` as default arguments** in your functions as **this will break the tests.**
