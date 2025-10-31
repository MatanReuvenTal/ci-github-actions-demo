import unittest
from main import devops_course

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(devops_course("Matan","GitHub Actions"), "This is Matan's assignment in GitHub Actions")
        self.assertEqual(devops_course("Matan", "ArgoCD"), "This is Matan's assignment in ArgoCD")
        self.assertEqual(devops_course("Matan", "AWS"), "This is Matan's assignment in AWS")

if __name__ == '__main__':
    unittest.main()
