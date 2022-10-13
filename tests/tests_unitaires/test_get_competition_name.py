import pytest
import json
from helpers.helper import get_competition_by_name
from unittest import TestCase
from pytest import mark


@mark.usefixtures("client")
class TestServer(TestCase):
    def test_get_competition_by_name(self):
        assert get_competition_by_name("TEST Spring Festival") == self.competitions[0]