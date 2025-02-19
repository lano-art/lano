class LessonsManager:
    def __init__(self):
        self.lessons = []

    def add_lesson(self, title, content):
        lesson = {'title': title, 'content': content}
        self.lessons.append(lesson)

    def get_lessons(self):
        return self.lessons
