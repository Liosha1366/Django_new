from django import template
from books.models import Book
register = template.Library()


@register.simple_tag
def store_title() -> str:
    title = Book.objects.first().publish
    return title
