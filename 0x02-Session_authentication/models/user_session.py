#!/usr/bin/env python3
"""Model for User Session class"""

from models.base import Base
from typing import TypeVar, List, Iterable
import json
import uuid
from os import path



class UserSession(Base):
    """User Session Class"""
    def __init__(self, *args: list, **kwargs: dict):
        """Initializes UserSession"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
