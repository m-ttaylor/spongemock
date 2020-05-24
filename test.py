import pytest
import spongemock

def test_lowercase_i():
    assert(mock3("ryan I do not like this rule") == "rYaN i Do NoT LiKe tHiS RuLe")

# if __name__ == "__main__":
#     unittest.main()