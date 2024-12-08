#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == "__main__":
    author_1 = Author("Carry Bradshaw")
    author_2 = Author("Nathaniel Hawthorne")
    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture")
    
    Article(author_1, magazine_1, "How to wear a tutu with style")
    Article(author_1, magazine_1, "How to be single and happy")
    Article(author_1, magazine_1, "Dating life in NYC")
    Article(author_1, magazine_2, "Carrara Marble is so 2020")
    Article(author_2, magazine_2, "2023 Eccentric Design Trends")
    
    # list all articles for author_1
    print([article.title for article in author_1.articles()])
    print([magazine.name for magazine in author_1.magazines()])
    print(author_1.topic_areas())
    
    # Debugging - list all articles for magazine_1
    print([article.title for article in magazine_1.articles()])
    print([contributor.name for contributor in magazine_1.contributors()])
    
    # Check the magazine with the most articles
    print(Magazine.top_publisher().name if Magazine.top_publisher() else "No top publisher")

    print("HELLO! :) let's debug :vibing_potato:")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
    