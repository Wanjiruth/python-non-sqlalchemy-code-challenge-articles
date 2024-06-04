import pytest
from classes.many_to_many import Magazine

class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_has_name_and_category(self):
        """Magazine is initialized with a name and category"""
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.name == "Vogue"
        assert magazine.category == "Fashion"

    def test_name_is_mutable_string(self):
        """magazine name is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.name, str)
        assert isinstance(magazine_2.name, str)

        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        # Check that setting an invalid name raises a ValueError
        with pytest.raises(ValueError):
            magazine_2.name = 2

        with pytest.raises(ValueError):
            magazine_2.name = "A"

        with pytest.raises(ValueError):
            magazine_2.name = "This name is too long for a magazine"

    def test_category_is_mutable_string(self):
        """magazine category is of type str and can change"""
        magazine = Magazine("Vogue", "Fashion")

        assert isinstance(magazine.category, str)

        magazine.category = "Lifestyle"
        assert magazine.category == "Lifestyle"

        # Check that setting an invalid category raises a ValueError
        with pytest.raises(ValueError):
            magazine.category = 10

        with pytest.raises(ValueError):
            magazine.category = ""

# Add additional tests as needed for other methods and properties of the Magazine class
