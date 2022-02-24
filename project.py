from skill import Skill
class Project:

    def __init__(self, name: str, duration: int, score: int, best_before: int, must_be_started_on:int):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.skills = []
        self.must_be_started_on = must_be_started_on

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

    def get_must_be_started_on(self):
        return self.must_be_started_on
