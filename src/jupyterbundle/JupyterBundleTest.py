import unittest
from pyfonycore.bootstrap import bootstrapped_container
from injecta.testing.services_tester import test_services


class JupyterBundleTest(unittest.TestCase):
    def test_init(self):
        container = bootstrapped_container.init("test")

        test_services(container)


if __name__ == "__main__":
    unittest.main()
