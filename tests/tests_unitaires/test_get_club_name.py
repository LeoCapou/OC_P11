import pytest
import json
from helpers.helper import get_club_by_name
from unittest import TestCase
from pytest import mark


@mark.usefixtures("client")
class TestServer(TestCase):
    def test_get_club_name(self):
        assert get_club_by_name("Simply Lift") == self.clubs[0]