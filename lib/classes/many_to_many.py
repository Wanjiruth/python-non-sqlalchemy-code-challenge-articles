# article.py

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._validate_author(author)
        self._validate_magazine(magazine)
        self._validate_title(title)

        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)

    @staticmethod
    def _validate_author(author):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")

    @staticmethod
    def _validate_magazine(magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")

    @staticmethod
    def _validate_title(title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be changed after initialization")

    @author.setter
    def author(self, value):
        self._validate_author(value)
        self._author = value

    @magazine.setter
    def magazine(self, value):
        self._validate_magazine(value)
        self._magazine = value


# author.py

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))


# magazine.py

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")

        self._name = name
        self._category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        if not self.articles():
            return None
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()))
