class Article:
    all = []
   
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be of type str and between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, "_name"):
         if((type(title) == str) and (5<= len(title) <=50)):
                self._title = title
         else:
             raise ValueError("Title must be a string with length between 5 and 50 characters")
        else:
            print("Cannot  modify title after it is already set") 

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of type Magazine")
        self._magazine = value



class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be of type str and longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not hasattr(self, "_name"):
         if((type(name) == str) and len(name) > 0):
             self._name = name
         else:
            print("Name must be a string and have at least one character")
        else:
            print("Cannot change name after already set.")

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be of type str and between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be of type str and longer than 0 characters")
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be of type str and between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be of type str and longer than 0 characters")
        self._category = value

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def contributing_authors(self):
        if not self._articles:
            return None
        authors_count = {}
        for article in self._articles:
            author = article.author
            if author not in authors_count:
                authors_count[author] = 0
            authors_count[author] += 1

        contributing_authors = [author for author, count in authors_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        top_magazine = None
        max_articles = 0
        for magazine in cls._all_magazines:
            if len(magazine.articles()) > max_articles:
                max_articles = len(magazine.articles())
                top_magazine = magazine
        return top_magazine










    