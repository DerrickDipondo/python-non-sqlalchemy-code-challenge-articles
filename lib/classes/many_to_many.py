class Article:

    all = []

    def __init__(self, author, magazine, title):
        # The logic for validating author instance
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be an Author instance")
        
        # The logic for validating magazine instance
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("Magazine must be a Magazine instance")
        
        # The logic for validating title
        if isinstance(title, str):
            if 5 <= len(title) <= 50:
                self._title = title
            else:
                raise Exception("Title does not fall within the specified limit")
        else:
            raise Exception("Title must be a string")
        
        # Add to tracking lists
        self._author._articles.append(self)
        self._magazine._articles.append(self)
        Article.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            # Update relationship
            if self._author is not new_author:
                self._author._articles.remove(self)
                new_author._articles.append(self)
            self._author = new_author
        else:
            raise Exception("New_author must be an Author instance")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            # Update relationship
            if self._magazine is not new_magazine:
                self._magazine._articles.remove(self)
                new_magazine._articles.append(self)
            self._magazine = new_magazine
        else:
            raise Exception("New Magazine must be a Magazine instance")
    
    @property
    def title(self):
        return self._title

class Author:
    def __init__(self, name):
        # Checking if the name is a string and the len > 0
        if isinstance(name, str):
            if len(name) > 0:
                self._name = name
            else: 
                raise Exception("Name must be longer than 0 characters")
        else:
            raise Exception("Name must be a string")
        self._articles = []
    
    @property
    def name(self):
        return self._name
    
    # Returns a list of all articles the author has written
    def articles(self):
        return self._articles[:]  # Changed to instance-based
    
    # Returns a unique list of magazines the author has contributed to
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    # Creates and returns a new Article instance associated with this author
    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine):
            if isinstance(title, str):
                if 5 <= len(title) <= 50:
                    new_article = Article(self, magazine, title)  
                    return new_article  
                else:
                    raise Exception("Title must be between 5 and 50 characters")
            else:
                raise Exception("Title must be a string")
        else:
            raise Exception("Magazine must be an instance of the Magazine class")

    # Returns a unique list of magazine categories or None if no articles
    def topic_areas(self):
        articles = self.articles()
        if len(articles) > 0:
            return list(set(article.magazine.category for article in articles))
        else:
            return None

class Magazine:
    _all_magazines = []  

    def __init__(self, name, category):
        # The logic for validating name
        if isinstance(name, str):
            if 2 <= len(name) <= 16:
                self._name = name
            else:
                raise Exception("Name does not fall within the specified limit")
        else:
            raise Exception("Name must be a string")
        
        # The logic for validating category
        if isinstance(category, str):
            if len(category) > 0:
                self._category = category
            else:
                raise Exception("Category must be greater than 0")
        else:
            raise Exception("Category must be a string")
        
        self._articles = []  
        Magazine._all_magazines.append(self) 
        
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else:
                raise Exception("Name does not fall within the specified limit")
        else: 
            raise Exception("Name must be a string")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category) > 0:
                self._category = new_category
            else:
                raise Exception("Category must be greater than 0")
        else:
            raise Exception("Category must be a string")
        
    # Return list of articles
    def articles(self):
        return self._articles[:]
    
    # Returns a list of title strings of all articles or None if no articles
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    
    # Returns a list of authors with >2 articles or None if none qualify
    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        top_authors = [author for author, count in author_count.items() if count > 2]
        return top_authors if top_authors else None
    
    def contributors(self):
        return list(set(article.author for article in self._articles)) if self._articles else []
    
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines or all(not mag._articles for mag in cls._all_magazines):
            return None
        return max(cls._all_magazines, key=lambda mag: len(mag._articles))