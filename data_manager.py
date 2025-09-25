import sqlite3
import re
from typing import List, Optional
from student import Student


class DataManager:
    def __init__(self, db_name="students.db"):
        self.students = []
        self.students_by_id = {}
        self._seq_counter = 0
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                specialization TEXT,
                email TEXT NOT NULL,
                materials TEXT
            )
        """)
        self.conn.commit()

    def generate_id(self) -> str:
        self._seq_counter += 1
        return f"S{self._seq_counter:03d}"

    def add_student(self, name: str, age: int, specialization: str, email: str, materials: Optional[List[str]] = None):
        stu = Student(id_student=self.generate_id(), name=name, age=age, specialization=specialization, email=email, materials=materials)
        self.students.append(stu)
        self.students_by_id[stu.id_student] = stu

        materials_str = ", ".join(stu.materials) if stu.materials else ""
        self.cursor.execute(
            "INSERT INTO students (id, name, age, specialization, email, materials) VALUES (?, ?, ?, ?, ?, ?)",
            (stu.id_student, stu.name, stu.age, stu.specialization, stu.email, materials_str)
        )
        self.conn.commit()
        return stu

    def list_students(self):
        return list(self.students)

    def find_student(self, id_student: str):
        return self.students_by_id.get(id_student)

    def input_one_student(self):
        while True:
            name = input("Enter name: ").strip()
            if name:
                break
            print("Name cannot be empty.")

        specialization = input("Enter specialization: ").strip()

        materials_text = input("Enter materials (if multiple, separate with comma ','): ").strip()
        materials = [m.strip() for m in materials_text.split(",")] if materials_text else []

        while True:
            try:
                age = int(input("Enter age: "))
                if age <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid age. Must be a positive integer.")

        while True:
            email = input("Enter email (example: example@email.com): ").strip()
            if not email or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
                print("Invalid email format! Make sure it looks like: username@domain.com")
            else:
                break

        student = self.add_student(name=name, age=age, specialization=specialization, email=email, materials=materials)
        print(f"Student added with ID: {student.id_student}")
        return student
