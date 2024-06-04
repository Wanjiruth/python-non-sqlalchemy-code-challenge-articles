import pytest
from classes.many_to_many import Author

class TestAuthor:
    """Author in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author = Author("Carry Bradshaw")
        assert author.name == "Carry Bradshaw"

    def test_name_is_string_and_immutable(self):
        """author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        # Check that the name cannot be changed
        with pytest.raises(AttributeError):
            author_1.name = "ActuallyTopher"

    def test_name_is_valid(self):
        """name must be a string longer than 0 characters"""
        # Valid name
        author = Author("Carry Bradshaw")
        assert isinstance(author.name, str)
        assert len(author.name) > 0

        # Uncomment the next two lines if using Exceptions
        # with pytest.raises(ValueError):
        #     Author("")

# Add additional tests as needed for other methods and properties of the Author class
