"""
Django command to wait for the database to be available
"""

# from typing import Any
from django.core.management.base import BaseCommand



# class Command(BaseCommand):
#     """Django command to wait for the database."""
    
#     def handle(self, *args: Any, **options: Any) -> str | None:
#         pass
#         # return super().handle(*args, **options)
        
class Command(BaseCommand):
    """Django command to wait for the database."""
    
    def handle(self, *args, **options):
        pass
        # return super().handle(*args, **options)