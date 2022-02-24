import parser
import numpy as np
import result
import random as rnd
import pygad

from project import Project
from skill import Skill
from result import Result
from contributor import Contributor
import algo3

# FILES = {"a_an_example", "b_better_start_small", "c_collaboration", "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"}
FILES = ["a_an_example", "b_better_start_small", "c_collaboration",
         "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"]


def run(filename: str):
    projects, collaborators = parser.parse(filename)
   # results = algo2(projects, collaborators)
    res2 = algo3.algo2(projects, collaborators)
    #parser.generate_output(results, filename)
    parser.generate_output(res2, filename)


def algo_col_group(project, collaborators):
    usable_col = []
    for sk in project.skills:
        for col in collaborators:
            for sk_col in col.skills:
                if sk_col.name == sk.name:
                    if sk_col.level >= sk.level:
                        for used_col in usable_col:
                            if used_col.name == col.name:
                                continue
                        usable_col.append(col)
                        break
    return usable_col


def fitness(project):
    return project.score * 2 + \
           project.duration * -1 + \
           project.best_before * 0 + \
           len(project.skills) * 0 + \
           project.must_be_started_on * 0


# DNA
def algo2(projects, collaborators):
    result = []
    print("Sort projects")
    projects.sort(key=fitness)

    """int day = 0
    while true:
        new_project_started = False
        for proj in started_project:
            if proj.started_day + proj.duration == day:
                collaborators.extend(proj.collab)"""
    for p in projects:
        cols = algo_col_group(p, collaborators)
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


# nbContributors            nbProjects
# ContributorName           nbSkills
# SkillOfContributorName    level
# ...
# ProjectName               nbDaysToComplete    ScoreAtCompletion   BestBefore  nbContributors
if __name__ == "__main__":
    print("C'est partiii let's gooo")
    run(FILES[0])
    run(FILES[1])
    run(FILES[2])
    run(FILES[3])
    run(FILES[4])
