class Article:
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
        
    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
    
    @property
    def title(self):
        return self._title

        

        pass
        
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
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <=16:
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


        

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass