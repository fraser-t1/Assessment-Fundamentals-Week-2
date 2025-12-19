# Level 2

Next, let's create classes for each of our assessment types so we do OOP in a better way.

## 1. Types of Assessments

Create a class for

- `MultipleChoiceAssessment`
- `TechnicalAssessment`
- `PresentationAssessment`

Each of these classes should inherit from the `Assessment` class and have a `calculate_score()` method that returns a score for the assessment.Each of the Assessment types have different weightings depending on it's type:

- `MultipleChoiceAssessment` - 70%
- `TechnicalAssessment` - 100%
- `PresentationAssessment` - 60%

For example, if a `TechnicalAssessment` has a score of 80, the `calculate_score()` method should return 80. If a `MultipleChoiceAssessment` has a score of 80, the `calculate_score()` method should return 56.

## 2. Edge Cases and Errors

Ensure you check all of your edge cases and throw errors where appropriate.

Throw a `TypeError` if something is added the `assessments` list in the `Trainee` class that is not a subclass of an `Assessment` class.

## 3. Get Assessment of Type

Add a function to `Trainee` class called `get_assessment_of_type(self, type: str) -> list[Assessment]` that returns a list of all assessments of a given type. The type will be given as a string of either `multiple-choice`, `technical` or `presentation`.

## Note

Due to the way that that default arguments are stored in Python, you should not use mutable default arguments in your function signature. This means that **you should not use `[]` or `{}` as default arguments** in your functions as **this will break the tests.**
