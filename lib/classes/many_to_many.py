class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
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
    @property
    def name(self):
        return self._name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str):
            if len(name) => 2 and <= 16:
                self.name = name
            else:
                raise Exception("Name does not fall within the specified limit")
        else:
            raise Exception("Name must be a string")
        
    @property
    def name(self):
        return self.name
    
    @name.setter


    def category(self):
        if isinstance(categories, str):
            if len(categories) > 0:
                self.categories = categories
            else:
                raise Exception("Name must be longer than 0 characters")
        else:
            raise Exception("Name must be a string")
        
    @property
    def categories(self);
        return self.categories

        

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass