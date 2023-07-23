#!/usr/bin/env python3
"""Examples of XPath"""
from lxml import etree
from bs4 import BeautifulSoup as bs

with open("BookstoreQ.xml", "r") as fd:
    data = fd.read()

tree = etree.XML(data)
soup = bs(data, "xml")

"""***************************************************************
   SIMPLE PATH EXPRESSION
   All book titles
****************************************************************"""

print(tree.xpath("/Bookstore/Book/Title"))

"""***************************************************************
   ALTERNATIVES (UNION)
   All book or magazine titles
****************************************************************"""

print(tree.xpath("(/Bookstore/Book/Title|/Bookstore/Magazine/Title)"))

"""***************************************************************
   WILDCARD
   All titles
****************************************************************"""

print(tree.xpath("/Bookstore/*/Title"))

"""***************************************************************
   OPERATOR // (ALL DESCENDANTS)
   All titles
****************************************************************"""

print(tree.xpath("//Title"))

"""***************************************************************
   COMBINING // AND WILDCARD
   All elements
****************************************************************"""

print(tree.xpath("//*"))

"""***************************************************************
   SELECTING ATTRIBUTES
   All book ISBNs
   (error, then fix)
****************************************************************"""

print(tree.xpath("/Bookstore/Book/@ISBN"))

"""***************************************************************
   PATH WITH CONDITION
   All books costing less than $90
****************************************************************"""

print(tree.xpath("/Bookstore/Book[@Price < 90]"))

"""***************************************************************
   CONDITION INSIDE PATH
   Titles of books costing less than $90
****************************************************************"""

print(tree.xpath("/Bookstore/Book[@Price < 90]/Title"))

"""***************************************************************
   EXISTENCE CONDITION
   Titles of books containing a remark
****************************************************************"""

print(tree.xpath("/Bookstore/Book[Remark]/Title"))

"""***************************************************************
   COMPLEX CONDITION
   Titles of books costing less than $90 where "Ullman" is
   an author
****************************************************************"""

print(tree.xpath(
    '/Bookstore/Book[@Price < 90 and '
    'Authors/Author/Last_Name = "Ullman"]/Title'
))

"""***************************************************************
   Same query but "Jeffrey Ullman" is an author
   (demonstrate error then fix)
****************************************************************"""

print(tree.xpath(
    '/Bookstore/Book[@Price < 90 and '
    'Authors/Author/Last_Name = "Ullman" and '
    'Authors/Author/First_Name="Jeffrey"]/Title'
))

print(tree.xpath(
    '/Bookstore/Book[@Price < 90 and '
    'Authors/Author/Last_Name = "Widom" and '
    'Authors/Author/First_Name="Jeffrey"]/Title'
))

print(tree.xpath(
    '/Bookstore/Book[@Price < 90 and '
    'Authors/Author[Last_Name = "Ullman" and '
    'First_Name="Jeffrey"]]/Title'
))

"""***************************************************************
   NEGATION
   Titles of books where "Ullman" is an author and "Widom" is
   not an author
   (attempt, can't do)
****************************************************************"""

print(tree.xpath(
    '/Bookstore/Book['
    'Authors/Author/Last_Name = "Ullman" and '
    'Authors/Author/Last_Name != "Widom"]/Title'
))

"""***************************************************************
   Nth ELEMENT
   All second authors, third, tenth authors
****************************************************************"""

print(tree.xpath("//Authors/Author[2]"))
print(tree.xpath("//Authors/Author[3]"))
print(tree.xpath("//Authors/Author[10]"))

"""***************************************************************
   CONTAINS() PREDICATE
   Titles of books with a remark containing "great"
****************************************************************"""

print(tree.xpath('//Book[contains(Remark, "great")]/Title'))

"""***************************************************************
   "SELF-JOIN"
   All magazines where there's a book with the same title
****************************************************************"""

print(tree.xpath("//Magazine[Title = //Book/Title]"))

"""***************************************************************
   PARENT AXIS AND NAME() FUNCTION
   All elements whose parent tag is not "Bookstore" or "Book"
****************************************************************"""

print(tree.xpath(
    '/Bookstore//*[name(parent::*) != "Bookstore" '
    'and name(parent::*) != "Book"]'
))

"""***************************************************************
   SIBLING AXIS
   All books and magazines with non-unique titles
   (not quite right, then fix)
****************************************************************"""

print(tree.xpath(
    '(/Bookstore/Book/Title|/Bookstore/Magazine/Title)[Title = following-sibling::*/Title]'
))

print(tree.xpath(
    '(/Bookstore/Book|/Bookstore/Magazine)[Title = following-sibling::*/Title '
    'or Title = preceding-sibling::*/Title]'
))

"""***************************************************************
   FOR-ALL (KLUDGE)
   Books where every author's first name includes "J"
****************************************************************"""

print(tree.xpath(
    "//Book["
    'count(Authors/Author[contains(First_Name, "J")]) = '
    'count(Authors/Author/First_Name)]'
))

"""***************************************************************
   NEGATION REVISITED
   Titles of books where "Ullman" is an author and "Widom" is
   not an author
****************************************************************"""

print(tree.xpath(
    '/Bookstore/Book[Authors/Author/Last_Name = "Ullman" and '
    'count(Authors/Author[Last_Name = "Widom"]) = 0]/Title'
))
