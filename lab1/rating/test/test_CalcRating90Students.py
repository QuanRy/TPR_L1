# -*- coding: utf-8 -*-
from lab1.rating.src.Types import DataType
from lab1.rating.src.CaclRating90points import CaclRating90points
import pytest

RatingsType = dict[str, float]


class TestCalcRating90points:
    @pytest.fixture()
    def input_data(self) -> DataType:
        return {
            "Абрамов Петр Сергеевич": [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович": [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97)
            ],
            "Олегов Олег Олегович": [
                ("математика", 96),
                ("русский язык", 91),
                ("программирование", 100)
            ],
            "Борисов Борис Борисович": [
                ("математика", 70),
                ("русский язык", 70),
                ("программирование", 69)
            ]
        }

    def test_student_above_90(self, input_data: DataType) -> None:
        calc_student_above_90 = CaclRating90points(input_data)
        assert calc_student_above_90.find_student_with_two_subjects_above_90() == 1

    def test_print(self, input_data: DataType, capsys) -> None:
        calc_student_above_90 = CaclRating90points(input_data)
        calc_student_above_90.print_result()
        captured = capsys.readouterr()
        assert "Студент, имеющий более 90 баллов за 2 предмета" in captured.out
