import pytest
from samochod import Samochod


samochod = Samochod()


def test_przyspieszanie():
    assert samochod.predkosc == 0

    samochod.przyspieszanie()
    samochod.przyspieszanie()
    samochod.przyspieszanie()

    assert samochod.predkosc == 15


def test_hamowanie():
    assert samochod.predkosc == 15

    samochod.hamowanie()
    samochod.hamowanie()
    samochod.hamowanie()
    samochod.hamowanie()

    assert samochod.predkosc == 0


def test_zmiany_predkości():
    assert samochod.predkosc == 0

    samochod.przyspieszanie()
    samochod.przyspieszanie()
    samochod.przyspieszanie()
    samochod.przyspieszanie()
    samochod.przyspieszanie()
    samochod.przyspieszanie()
    samochod.hamowanie()
    samochod.hamowanie()

    assert samochod.predkosc == 20
