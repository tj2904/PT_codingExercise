# PT Remote Coding Exercise

## Overview

* Written in Python using version 3.9
* No external dependancies
* Naming chosen to match the task, in production something more descriptive would be prefered, e.g. ```StudentProgressCalculation```

## Usage

The ```Student``` class takes in the 6 test values as parameters to construct an object:

* Mock Maths score (```int```)
* Actual Maths score  (```int```)
* Mock English score  (```int```)
* Actual English score  (```int```)
* Mock Sciene score  (```int```)
* Actual Sciene score  (```int```)

There are 2 methods within the class:

* ```.averageActual()``` which returns the average of the 3 subjects actual scores
* ```.progress()``` which returns the progress score

## Tests

Tests are provided using unittest. These assert the responses of both methods using a randomly chosen selection of 4 students from the provided data. Run ```test_pt_studentRanking.py``` from Python's shell.

## Design decisions

* I could have initiated the object with empty values for the averages and progress values to be added to in the function.
This was not done as the spec asked for a return when supplied with values for the tests.
* I considered returning JSON, but again this is outside the scope.
* I decided not to round values before returning, prefering instead to allow this to be done downstream to avoid introducing hard-to-find rounding errors in any further/future calculations
