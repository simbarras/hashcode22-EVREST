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
                    if sk_col.level == sk.level:
                        col.upgrade_skill(sk_col.name)
                        usable_col.append(col)
                        break
                    elif sk_col.level > sk.level:
                        usable_col.append(col)
                        break
                    col.set_next_available(time + project.get_duration())
                return usable_col
    return usable_col


# DNA
def algo2(projects, collaborators):
    result = []
    print("Sort projects")

    current_time = 0

    projects.sort(key=lambda d: d.get_must_be_started_on())

    """int day = 0
    while true:
        new_project_started = False
        for proj in started_project:
            if proj.started_day + proj.duration == day:
                collaborators.extend(proj.collab)"""
    for p in projects:
        current_time = p.get_must_be_started_on()
        cols = algo_col_group(p, collaborators, current_time)
        if len(cols) == len(p.skills):
            res = Result(p.name)
            res.add_collaborators(cols)
            result.append(res)

    return result
