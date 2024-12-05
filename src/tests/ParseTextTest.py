### Import packages ###
import ipytest
import os
from parser import parse_txt

### Configure ipytest ###
ipytest.config(rewrite_asserts=True)
__file__ = "test_parser.py"                          # Module name

# Define test functions
def test_parse_txt():
    """
    Test function for parseing a .txt file.
    """
    FilePath = "/Users/simondn/Documents/CSE583/carmina/TESTFILE.txt"

    # Write a sample .txt file
    with open(TestTxtPath, "w") as f:
        f.write("arma virumque cano troiae qui primus ab oris\n")
        f.write("italiam fato profugus laviniaque venit\n")

    try:
        ExpectedOutput = [
            "arma virumque cano Troiae qui primus ab oris\n",
            "italiam fato profugus Laviniaque venit\n"
        ]
        ActualOutput = parse_txt(FilePath)
        assert ActualOutput == ExpectedOutput
    finally:
        os.remove(TestTxtPath)

# Run the tests
ipytest.run()
