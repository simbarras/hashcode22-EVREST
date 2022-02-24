from skill import Skill
class Project:

    def __init__(self, name: str, duration: int, score: int, best_before: int):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.skills = []

    def add_skill(self, skill:Skill):
        self.skills.append(skill)

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def get_score(self):
        return self.score

    def get_best_before(self):
        return self.best_before

    def get_skills(self):
        return self.skills
