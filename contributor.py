import skill


class Contributor:
    name: str
    skills: list

    def __init__(self, name: str):
        self.name = name
        self.skills = []
        self.work_days = 0

    def add_skill(self, sk: skill):
        self.skills.append(sk)

    def upgrade_skill(self, sk_name: str):
        for s in self.skills:
            if s.name == sk_name:
                s.level += 1
                return

    def get_skills(self):
        return self.skills

    def get_name(self):
        return self.name

    def set_next_available(self, time):
        self.work_days = time

    def next_available(self):
        return self.work_days

    def is_free_on(self, time):
        return time > self.work_days
