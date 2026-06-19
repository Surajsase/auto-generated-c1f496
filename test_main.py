import unittest
import sys
import io
import main

class TestDesignSystemComponents(unittest.TestCase):
    def test_design_system_components(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        main.design_system_components()
        sys.stdout = sys.__stdout__
        self.assertIn('UI', capturedOutput.getvalue())
        self.assertIn('Network', capturedOutput.getvalue())
        self.assertIn('Database', capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()