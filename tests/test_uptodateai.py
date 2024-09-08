import unittest
from src.uptodateai.utils import urljoin

class TestUpToDateAI(unittest.TestCase):
    def test_urljoin(self):
        self.assertEqual(urljoin('http://example.com', 'path', 'to', 'page'),
                         'http://example.com/path/to/page')
        self.assertEqual(urljoin('http://example.com/', '/path/', '/to/', '/page/'),
                         'http://example.com/path/to/page')

if __name__ == '__main__':
    unittest.main()