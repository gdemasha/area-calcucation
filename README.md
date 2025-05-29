# Area Calculation Library

A lightweight, extensible Python library for calculating areas of geometric figures. It currently supports **circles** and **triangles**, and is designed for easy expansion to support additional shapes in the future.

## Features

- **Calculate circle area** using radius.
- **Calculate triangle area**:
  - Using three side lengths (Heron’s formula).
  - As a right triangle using legs and hypotenuse.
- **Automatic figure detection** based on parameters provided at compile-time.
- Includes unit tests with `pytest`.
- Built for extensibility — add support for new geometric shapes with ease.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/area_calculation.git
cd area_calculation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```
from area_calculation.library import AreaCalc

area_calc = AreaCalc()

# Calculate area of a circle only
circle_area = area_calc.calculate_area(radius=6, lengths=None)

# Calculate area of a triangle only
triangle_area = area_calc.calculate_area(radius=None, lengths=[3, 4, 5])

# Calculate both at once
both_areas = area_calc.calculate_area(radius=6, lengths=[3, 4, 5])
```
Method: calculate_area(radius, lengths)
- If both parameters are provided, returns a tuple: (circle_area, triangle_area).
- If only one is provided, returns the corresponding area.
- Raises a CalculationException if provided parameters are invalid.

## Extending the Library

To add a new shape:
- Add a new method in AreaCalc.
- Update calculate_area() logic to support the new parameters and call the new method.
- Add unit tests for the new shape in test_calculations.py.
