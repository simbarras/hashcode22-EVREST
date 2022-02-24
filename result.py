class Result:
    project: str
    collaborator: list

    def __init__(self, project: str):
        self.project = project
        self.collaborator = []

    def add_collaborator(self, collaborator: str):
        self.collaborator.append(collaborator)

    def add_collaborators(self, collaborators: list):
        self.collaborator.extend(collaborators)

    def get_project_name(self):
        return self.project

    def get_collaborators(self):
        return self.collaborator