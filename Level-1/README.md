# Level 1

In this challenge, you're building out our assessment platform to allow us to assess candidates for our data science roles. We have a number of different assessments that we use to assess candidates and we need to be able to run these assessments and store the results.

We will be using OOP in this challenge.

## 1. Trainee

You should have a `Trainee` class that has the following attributes:

- `name` - str
- `email` - str
- `date_of_birth` - `date` object
- `assessments` - list[Assessment]

It has methods to:

- `get_age() -> int` - returns the age of the trainee in years
- `add_assessment(assessment: Assessment) -> None` - adds an `Assessment` to the trainee's list of assessments
- `get_assessment(name: str) -> Assessment | None` - returns the `Assessment` object that has the name given
  - Return `None` if not found

## 2. Assessment

You should have an `Assessment` class that has the following attributes:

- `name` - str
- `type` - str
  - Can only be `multiple-choice`, `technical` or `presentation`. Throw a ValueError if not.
- score - float (0-100). Throw a ValueError if outside of this range.

## Note

Due to the way that that default arguments are stored in Python, you should not use mutable default arguments in your function signature. This means that **you should not use `[]` or `{}` as default arguments** in your functions as **this will break the tests.**
