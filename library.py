from typing import List
from models import Book, Member

class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.members: List[Member] = []

    def add_book(self, title: str) -> Book:
        new_id = (max([b.book_id for b in self.books]) + 1) if self.books else 1
        book = Book(book_id=new_id, title=title.strip())
        self.books.append(book)
        return book

    def add_member(self, name: str, voted_brawler_id: int) -> Member:
        new_id = (max([m.member_id for m in self.members]) + 1) if self.members else 1
        member = Member(member_id=new_id, name=name.strip(), voted_brawler_id=voted_brawler_id)
        self.members.append(member)
        return member

    def total_voters(self) -> int:
        return len(set(m.name for m in self.members))

    def total_votes(self) -> int:
        return len(self.members)

    def unique_brawlers_voted(self) -> int:
        return len(set(m.voted_brawler_id for m in self.members))

