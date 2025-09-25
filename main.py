from data_manager import DataManager
import os


if __name__ == "__main__":
    # إعادة تعيين قاعدة البيانات عند كل تشغيل
    if os.path.exists("students.db"):
        os.remove("students.db")

    mgr = DataManager()
    while True:
        student = mgr.input_one_student()
        cont = input("Add another? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

    print("\nAll students:")
    for s in mgr.list_students():
        s.display()
