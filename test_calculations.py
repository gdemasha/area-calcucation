from typing import Optional
import pytest
from contextlib import nullcontext as does_not_raise

from area_calculation.library import AreaCalc
from area_calculation.exceptions import LibException


area_calc = AreaCalc()


class TestCalculation():
    """Class for testing AreaCalc methods."""
    @pytest.mark.parametrize(
        'radius, expectation',
        [
            (6, does_not_raise()),
            ('6', pytest.raises(LibException)),
            (234.097, does_not_raise()),
        ]
    )
    def test_calc_circle_area(self, radius: float, expectation):
        """Test circle area calculation."""
        with expectation:
            assert area_calc.calc_circle_area(radius)
            assert type(area_calc.calc_circle_area(radius)) == float
            if radius == 6:
                area = area_calc.calc_circle_area(6)
                assert round(area, 2) == 113.10

    @pytest.mark.parametrize(
        'lengths, expectation',
        [
            ([2, 18.6, 9], does_not_raise()),
            ('6', pytest.raises(LibException)),
            ([3, '29', '13'], pytest.raises(LibException)),
        ]
    )
    def test_sort_lengths(self, lengths: list[float | int], expectation):
        """Test sorting and type check."""
        with expectation:
            assert area_calc.sort_lengths(lengths)
            assert type(area_calc.sort_lengths(lengths)) == list
            assert area_calc.sort_lengths(lengths) == sorted(lengths)

    @pytest.mark.parametrize(
        'leg_a, leg_b, hypotenuse, expectation',
        [
            (3, 4, 5, does_not_raise()),
            (1, 19, 3, pytest.raises(AssertionError)),
            ('3', '29', '13', pytest.raises(LibException)),
        ]
    )
    def test_check_triangle_angle(
        self,
        leg_a: float | int,
        leg_b: float | int,
        hypotenuse: float | int,
        expectation
    ):
        """Test checking that the triangle is right."""
        with expectation:
            assert area_calc.check_triangle_angle(
                leg_a, leg_b, hypotenuse
            ) is True

    @pytest.mark.parametrize(
        'lengths, expectation',
        [
            ([3, 4, 5], does_not_raise()),
            ([6, 7, 5], does_not_raise()),
            ([2, 18, 9], pytest.raises(LibException)),
            (None, pytest.raises(LibException)),
            ([3, '29', '13'], pytest.raises(LibException)),
            ([3, 16, 4, 2], pytest.raises(LibException))
        ]
    )
    def test_calc_triangle_area(self, lengths: list[float | int], expectation):
        """Test calculating triangle's area."""
        with expectation:
            assert area_calc.calc_triangle_area(lengths)
            assert type(area_calc.calc_triangle_area(lengths)) == float
            assert not (
                lengths[0] + lengths[1] <= lengths[2]
                or lengths[0] + lengths[2] <= lengths[1]
                or lengths[1] + lengths[2] <= lengths[0]
            )

    @pytest.mark.parametrize(
        'radius, lengths, expectation',
        [
            (6, None, does_not_raise()),
            (6, [3, 4, 5], does_not_raise()),
            (None, [3, 4, 5], does_not_raise()),
            (None, [6, 7, 5], does_not_raise()),
            (None, [2, 18, 9], pytest.raises(LibException)),
            ('3', [3, '29', '13'], pytest.raises(LibException)),
            (None, [3, 16, 4, 2], pytest.raises(LibException)),
            (None, None, pytest.raises(LibException))
        ]
    )
    def test_calculate_area(
        self, radius: Optional[float],
        lengths: Optional[list[float | int]],
        expectation
    ):
        """Test defining figure in compile-time and calculating its area."""
        with expectation:
            assert area_calc.calculate_area(radius, lengths)
            if radius is not None and lengths is not None:
                assert type(
                    area_calc.calculate_area(radius, lengths)
                ) == tuple
            elif radius is not None:
                area = area_calc.calc_circle_area(radius)
                assert area_calc.calculate_area(radius, lengths) == area
            elif lengths is not None:
                area = area_calc.calc_triangle_area(lengths)
                assert area_calc.calculate_area(radius, lengths) == area
