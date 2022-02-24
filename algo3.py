from skill import Skill
from contributor import Contributor
from project import Project
from result import Result


def algo_col_group(project, collaborators, time):
    usable_col = []
    collaborators.sort(key=lambda d: d.next_available())
    for sk in project.skills:
        for col in collaborators:
            for sk_col in col.skills:
                if sk_col.name == sk.name:
                    if sk_col.level >= sk.level:
                        for used_col in usable_col:
                            if used_col.name == col.name:
                                continue
                        usable_col.append(col)
                        col.set_next_available(time + project.get_duration())
                        break
    return usable_col


# DNA
def algo2(projects, collaborators):
    result = []
    print("Sort projects")

    current_time = 0

    projects.sort(key=lambda d: d.get_must_be_started_on())


    for p in projects:
        current_time = p.get_must_be_started_on()
        cols = algo_col_group(p, collaborators, current_time)
        if len(cols) == len(p.skills):
            for i in range(len(cols)):
                current_skill = p.skills[i].name
                j = 0
                for j in range(len(cols[i].skills)):
                    if current_skill == cols[i].skills[j].name:
                        break
                if p.skills[i].level == cols[i].skills[j].level:
                    cols[i].upgrade_skill(current_skill)

            res = Result(p.name)
            res.add_collaborators(cols)
            result.append(res)
    return result
