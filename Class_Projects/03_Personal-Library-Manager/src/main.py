import flet as ft
from typing import List, Dict
import json
import os
from datetime import datetime

class Book:
    def __init__(self, title: str, author: str, year: int, genre: str, read: bool = False, date_added: str = None):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read = read
        self.date_added = date_added or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "read": self.read,
            "date_added": self.date_added
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        return cls(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            genre=data["genre"],
            read=data.get("read", False),
            date_added=data.get("date_added", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )

class LibraryManager:
    def __init__(self):
        self.books: List[Book] = []
        self.load_books()

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        self.save_books()

    def search_books(self, query: str) -> List[Book]:
        if not query:
            return self.books
        query = query.lower()
        return [
            book for book in self.books
            if query in book.title.lower() or
               query in book.author.lower() or
               query in book.genre.lower()
        ]

    def get_statistics(self) -> Dict:
        total = len(self.books)
        read = sum(1 for book in self.books if book.read)
        return {
            "total": total,
            "read": read,
            "percentage": (read / total * 100) if total > 0 else 0
        }

    def save_books(self):
        os.makedirs("storage", exist_ok=True)
        with open("storage/books.json", "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def load_books(self):
        try:
            with open("storage/books.json", "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(book_data) for book_data in data]
        except FileNotFoundError:
            self.books = []

    def toggle_read_status(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.read = not book.read
                break
        self.save_books()

def main(page: ft.Page):
    page.title = "Personal Library Manager"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.spacing = 20
    page.scroll = ft.ScrollMode.AUTO
    page.window_width = 800
    page.window_height = 900
    page.window_resizable = True

    library = LibraryManager()

    # UI Components
    title_input = ft.TextField(label="Title", width=300, border_radius=10)
    author_input = ft.TextField(label="Author", width=300, border_radius=10)
    year_input = ft.TextField(label="Publication Year", width=300, border_radius=10)
    genre_input = ft.TextField(label="Genre", width=300, border_radius=10)
    read_checkbox = ft.Checkbox(label="Read", value=False)

    search_input = ft.TextField(
        label="Search by title, author, or genre",
        width=300,
        border_radius=10,
        prefix_icon=ft.Icons.SEARCH,
        on_change=lambda e: search_books_clicked(e)
    )
    books_grid = ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=350,
        spacing=10,
        run_spacing=10,
        padding=20,
        height=400,
    )
    status_text = ft.Text("", color=ft.Colors.GREEN, size=16, weight=ft.FontWeight.BOLD)

    def show_status(message: str, color: str = ft.Colors.GREEN):
        status_text.value = message
        status_text.color = color
        status_text.update()

    def add_book_clicked(e):
        if not all([title_input.value, author_input.value, year_input.value, genre_input.value]):
            show_status("Please fill in all fields!", ft.Colors.RED)
            return

        try:
            year = int(year_input.value)
            if year < 1800 or year > datetime.now().year:
                raise ValueError("Invalid year")

            book = Book(
                title=title_input.value,
                author=author_input.value,
                year=year,
                genre=genre_input.value,
                read=read_checkbox.value
            )
            library.add_book(book)
            clear_inputs()
            update_books_list()
            show_status("Book added successfully!")
        except ValueError as ve:
            show_status(str(ve) if str(ve) != "Invalid year" else "Please enter a valid year!", ft.Colors.RED)

    def clear_inputs():
        title_input.value = ""
        author_input.value = ""
        year_input.value = ""
        genre_input.value = ""
        read_checkbox.value = False
        title_input.update()
        author_input.update()
        year_input.update()
        genre_input.update()
        read_checkbox.update()

    def remove_book_clicked(book_title: str):
        library.remove_book(book_title)
        update_books_list()
        show_status("Book removed successfully!")

    def toggle_read_status_clicked(book_title: str):
        library.toggle_read_status(book_title)
        update_books_list()
        show_status("Book status updated successfully!")

    def search_books_clicked(e):
        query = search_input.value
        results = library.search_books(query)
        books_grid.controls.clear()

        if not results:
            books_grid.controls.append(
                ft.Container(
                    content=ft.Text(
                        "No books found",
                        size=16,
                        color=ft.Colors.GREY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.alignment.center,
                )
            )
        else:
            for book in results:
                books_grid.controls.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Row(
                                [
                                    ft.Icon(
                                        ft.Icons.BOOK if not book.read else ft.Icons.BOOKMARK,
                                        color=ft.Colors.GREEN if book.read else ft.Colors.GREY,
                                        size=24,
                                    ),
                                    ft.Text(
                                        book.title,
                                        weight=ft.FontWeight.BOLD,
                                        size=16,
                                        expand=True,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            ft.Divider(height=1, color=ft.Colors.BLUE_GREY_100),
                            ft.Column([
                                ft.Text(f"Author: {book.author}", size=14),
                                ft.Text(f"Year: {book.year}", size=14),
                                ft.Text(f"Genre: {book.genre}", size=14),
                                ft.Text(
                                    f"Added: {book.date_added}",
                                    size=12,
                                    color=ft.Colors.GREY,
                                ),
                            ], spacing=4),
                            ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.Icons.CHECK_CIRCLE if not book.read else ft.Icons.CHECK_CIRCLE_OUTLINE,
                                        icon_color=ft.Colors.GREEN,
                                        tooltip="Toggle Read Status",
                                        on_click=lambda b, title=book.title: toggle_read_status_clicked(title),
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,
                                        icon_color=ft.Colors.RED,
                                        tooltip="Delete Book",
                                        on_click=lambda b, title=book.title: remove_book_clicked(title),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ], spacing=10),
                        width=300,
                        height=200,
                        border=ft.border.all(1, ft.Colors.BLUE_GREY_100),
                        border_radius=10,
                        padding=15,
                        bgcolor=ft.Colors.WHITE,
                    )
                )
        books_grid.update()

    def update_books_list():
        books_grid.controls.clear()
        search_books_clicked(None)
        books_grid.update()

    def show_statistics(e):
        stats = library.get_statistics()
        show_status(
            f"Total Books: {stats['total']}\n"
            f"Books Read: {stats['read']}\n"
            f"Read Percentage: {stats['percentage']:.1f}%"
        )

    def clear_all_books(e):
        if len(library.books) == 0:
            show_status("Library is already empty!", ft.Colors.ORANGE)
            return
        library.books.clear()
        library.save_books()
        books_grid.controls.clear()
        update_books_list()
        show_status("All books have been removed!")

    # Layout
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Personal Library Manager",
                       size=32,
                       weight=ft.FontWeight.BOLD,
                       color=ft.Colors.BLUE,
                       text_align=ft.TextAlign.CENTER),
                status_text,
            ]),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLUE_GREY_100,
                offset=ft.Offset(0, 3),
            ),
        ),

        ft.Container(
            content=ft.Column([
                ft.Text("Add New Book",
                       size=24,
                       weight=ft.FontWeight.BOLD,
                       color=ft.Colors.BLUE),
                title_input,
                author_input,
                year_input,
                genre_input,
                read_checkbox,
                ft.ElevatedButton(
                    "Add Book",
                    on_click=add_book_clicked,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.BLUE,
                        padding=10,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                ),
            ]),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.BLUE_GREY_100),
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLUE_GREY_100,
                offset=ft.Offset(0, 3),
            ),
        ),

        ft.Container(
            content=ft.Column([
                ft.Text("Search Books",
                       size=24,
                       weight=ft.FontWeight.BOLD,
                       color=ft.Colors.BLUE),
                search_input,
            ]),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.BLUE_GREY_100),
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLUE_GREY_100,
                offset=ft.Offset(0, 3),
            ),
        ),

        ft.Container(
            content=ft.Column([
                ft.Row(
                    [
                        ft.Icon(ft.Icons.LIBRARY_BOOKS, color=ft.Colors.BLUE, size=30),
                        ft.Text(
                            "Library Contents",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(height=2, color=ft.Colors.BLUE_GREY_100),
                ft.Container(
                    content=books_grid,
                    border=ft.border.all(1, ft.Colors.BLUE_GREY_100),
                    border_radius=10,
                    padding=10,
                    bgcolor=ft.Colors.WHITE,
                    height=450,
                ),
            ]),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.BLUE_GREY_100),
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLUE_GREY_100,
                offset=ft.Offset(0, 3),
            ),
            margin=ft.margin.only(bottom=20),
        ),

        ft.Container(
            content=ft.Row(
                [
                    ft.ElevatedButton(
                        "Show Statistics",
                        on_click=show_statistics,
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE,
                            padding=10,
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                    ),
                    ft.ElevatedButton(
                        "Refresh List",
                        on_click=lambda e: update_books_list(),
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE,
                            padding=10,
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                    ),
                    ft.ElevatedButton(
                        "Clear All Books",
                        on_click=clear_all_books,
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.RED,
                            padding=10,
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLUE_GREY_100,
                offset=ft.Offset(0, 3),
            ),
        ),
    )

    update_books_list()

ft.app(target=main)
