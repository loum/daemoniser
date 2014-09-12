# pylint: disable=R0904,C0103
""":class:`daemoniser.Service` tests.

"""
import unittest2

import daemoniser


class TestService(unittest2.TestCase):
    """:class:`daemoniser.Service` test cases.
    """
    @classmethod
    def setUp(cls):
        cls._service = daemoniser.Service()

    def test_init(self):
        """Initialise a daemoniser.Service object.
        """
        msg = 'Object is not a daemoniser.Service'
        self.assertIsInstance(self._service, daemoniser.Service, msg)

    @classmethod
    def tearDown(cls):
        cls._service = None
        del cls._service
