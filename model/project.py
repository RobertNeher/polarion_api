import json

from utilities.configuration import Configuration
from utilities.utils import polarionRequest

class Project():
    def __init__(self) -> None:
        config = Configuration()
        self.projects = []

        response = polarionRequest("/projects")

        if response is None:
            print(f"Request at end point '/projects' failed: {response.status_code}")
            return

        _projects = json.loads(response.text)["data"]

        for _project in _projects:
            self.projects.append(_project)


    def getDetails(self, projectID: str) -> map:
        for _project in self.projects:
            if _project["id"] == projectID:
                return _project["attributes"]


if __name__ == "__main__":
    projects = Project()

    for project in projects.projects:
        print(f"{project['id']}: {project['attributes']['name']}")