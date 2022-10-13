import pytest
import json
from helpers.helper import get_club_by_email
from unittest import TestCase
from pytest import mark


@mark.usefixtures("client")
class TestServer(TestCase):
    def test_get_club_email(self):
        assert get_club_by_email("john@simplylift.co") == self.clubs[0]