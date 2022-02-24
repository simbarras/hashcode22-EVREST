from dataclasses import field
from skill import Skill
from contributor import Contributor
from project import Project
from result import Result


def parse(file):
    with open(f"input_data/{file}.in.txt") as f:
        [contributors_count, projects_counts] = f.readline().strip().split()
        contributors = []
        projects = []
        for i in range(int(contributors_count)):
            contributors.append(get_contributor(f))
        for i in range(int(projects_counts)):
            projects.append(get_project(f))
    return [projects, contributors]


def get_skills(number_of_skills, f, data):
    for i in range(number_of_skills):
        [name, level] = f.readline().strip().split()
        data.add_skill(Skill(name=name, level=int(level)))


def get_contributor(f):
    [name, number_of_skills] = f.readline().strip().split()
    contributor = Contributor(name)
    get_skills(int(number_of_skills), f, contributor)
    return contributor


def get_project(f):
    [name, days, score, best_effort,
     number_of_skills] = f.readline().strip().split()
    project = Project(name, int(days), int(score), int(best_effort),
                      int(best_effort) - int(days))
    get_skills(int(number_of_skills), f, project)
    return project


def get_collaborators_as_line(collaborators: [Contributor]):
    line = ""
    for coll in collaborators:
        line += f'{coll.get_name()} '
    return line


def generate_output(res: [Result], filename):
    with open(f'output_data/{filename}.out.txt', 'a') as outfile:
        outfile.write(f'{str(len(res))}\n')
        for result in res:
            outfile.write(f'{result.get_project_name()}\n')
            outfile.write(
                f'{get_collaborators_as_line(result.get_collaborators())}\n')
