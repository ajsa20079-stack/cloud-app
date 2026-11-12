import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app


def test_addition():
    assert 2 + 2 == 4


def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200


def test_cars_api():
    r = app.test_client().get("/api/cars")
    assert r.status_code == 200
    assert len(r.get_json()) > 0
