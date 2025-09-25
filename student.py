import re
from typing import List, Optional


class Student:
    def __init__(self, id_student: str, name: str, age: int, specialization: str, email: str, materials: Optional[List[str]] = None):
        self.id_student = id_student
        self.name = name
        self.specialization = specialization
        self.materials = materials or []
        self.attendance_records = []

        self.set_age(age)
        self.set_email(email)

    def set_age(self, age: int):
        if not isinstance(age, int) or age <= 0:
            raise ValueError(f"Invalid age: {age}. Must be a positive integer.")
        self.age = age

    def set_email(self, email: str):
        email = (email or "").strip()
        if not email or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            raise ValueError(f"Invalid or missing email: '{email}'")
        self.email = email

    def add_material(self, m: str) -> bool:
        m = (m or "").strip()
        if not m or m in self.materials:
            return False
        self.materials.append(m)
        return True

    def remove_material(self, m: str) -> bool:
        m = (m or "").strip()
        if m in self.materials:
            self.materials.remove(m)
            return True
        return False

    def __str__(self):
        return (f"ID:{self.id_student} | Name:{self.name} | Age:{self.age} | "
                f"Spec:{self.specialization} | Email:{self.email} | Materials:{self.materials}")

    def display(self):
        print(self.__str__())
