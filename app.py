import parser
import numpy as np
import result

DIR = "input_data/"
# FILES = {"a_an_example", "b_better_start_small", "c_collaboration", "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"}
FILES = {"a_an_example", "b_better_start_small", "c_collaboration",
         "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"}
EXTENSION = ".in.txt"
OUT_FILES = "result.txt"


def run(filename: str):
    print(f"Parse {filename}")
    projects, collaborators = parser.parse(filename)
    results = algo1(projects, collaborators)
    print("Result found")
    parser.generate_output(filename, results)


# nbContributors            nbProjects
# ContributorName           nbSkills
# SkillOfContributorName    level
# ...
# ProjectName               nbDaysToComplete    ScoreAtCompletion   BestBefore  nbContributors
if __name__ == '__main__':
    print("C'est partiii let's gooo")
    run = run(FILES[0])
    run = run(FILES[1])
    run = run(FILES[2])
    run = run(FILES[3])
    run = run(FILES[4])


def algo1(projects, collaborators):
    print("launch algo1")
    results = []

    for project in projects:
        res = result.Result(project.name)
        for p_sk in project.skills:
            for coll in collaborators:
                for

    res.add_collaborator("simon")
    results.append(res)

    return results


def algo2(projects, collaborators):
