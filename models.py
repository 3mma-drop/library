from dataclasses import dataclass

@dataclass
class Book:  # Usamos Book como Brawler
    book_id: int
    title: str  # nombre del brawler

@dataclass
class Member:  # Usamos Member como votante
    member_id: int
    name: str
    voted_brawler_id: int  # ID del brawler votado


    