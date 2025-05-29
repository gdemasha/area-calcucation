"""Library calculating circle's and triangle's areas.
It checks if radius, lengths or both are provided and calculates figures' areas
according to the given parameters.
"""
import math
import structlog
from typing import Optional

from area_calculation.exceptions import LibException


logger = structlog.get_logger()


class AreaCalc():
    """Class for calculating geometric figures' areas"""
    def calc_circle_area(self, radius: float | int) -> float:
        """Function for calculating circle's area."""
        try:
            return math.pi * (radius ** 2)
        except Exception as e:
            logger.error(e)
            raise LibException(f'calc_circle_area: error {e}')

    def sort_lengths(self, lengths: list[float | int]) -> list:
        """Function to sort lengths in ascending order."""
        try:
            if all(isinstance(num, (int, float)) for num in lengths):
                return sorted(lengths)
            else:
                raise LibException(
                    'All elements in lengths must be int or float'
                )
        except Exception as e:
            logger.error(e)
            raise LibException(f'sort_lengths: error {e}')

    def check_triangle_angle(
        self,
        leg_a: float | int,
        leg_b: float | int,
        hypotenuse: float | int
    ) -> bool:
        """Check if the triangle is right."""
        try:
            return (hypotenuse ** 2 == leg_b ** 2 + leg_a ** 2)
        except Exception as e:
            logger.error(e)
            raise LibException(f'check_triangle_angle: error {e}')

    def calc_triangle_area(self, lengths: list[float | int]) -> float:
        """Calculate triangle's area."""
        try:
            if len(lengths) == 3:
                a, b, c = self.sort_lengths(lengths)
            else:
                raise LibException('Wrong number of sides')

            if a + b <= c or a + c <= b or b + c <= a:
                raise ValueError(
                   'Invalid triangle: side lengths do not '
                   'satisfy triangle inequality'
                )

            if self.check_triangle_angle(a, b, c):
                return (a * b) / 2
            else:
                perimeter = (sum(lengths)) / 2
                return math.sqrt(
                    perimeter
                    * (perimeter - b)
                    * (perimeter - a)
                    * (perimeter - c)
                )
        except Exception as e:
            logger.error(e)
            raise LibException(f'calc_triangle_area: error {e}')

    def calculate_area(
        self,
        radius: Optional[float],
        lengths: Optional[list[float | int]]
    ) -> float | tuple[float, float]:
        """Calculate an area of a given figure"""
        try:
            if radius is not None and lengths is not None:
                return (
                    self.calc_circle_area(radius),
                    self.calc_triangle_area(lengths)
                )
            elif lengths is not None:
                return self.calc_triangle_area(lengths)
            elif radius is not None:
                return self.calc_circle_area(radius)
            else:
                raise LibException(
                    'No appropriate data was received to calculate an area'
                )
        except Exception as e:
            logger.error(e)
            raise LibException(f'calculate_area: error {e}')
