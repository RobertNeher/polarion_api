import requests
import json

from configuration import Configuration

class WorkItem():
    def __init__(self, projectID: str) -> None:
        self.config = Configuration()
        self.workItems = []

        self.url = f'http://{self.config.polarionHost}/{self.config.polarionAPIPrefix}/projects/{projectID}/workitems'
        self.response = requests.get(url=self.url,
                params=self.config.dataFilter,
                headers={
                    "accept": "application/json",
                    "content-type": "application/json",
                    "authorization": f"Bearer {self.config.apiToken}"
                }
        )

        if self.response.status_code != 200:
            print(f"Request '{self.url}' failed: {self.response.status_code}")
            exit
    
        workItems = json.loads(self.response.text)["data"]

        for workItem in workItems:
            self.workItems.append(workItem)


    def getWorkItemDetails(self, workItemID: str) -> map:
        for workItem in self.workItems:
            id = workItem["id"].split("/")[1]
            if id == workItemID:
                return workItem["attributes"]


if __name__ == "__main__":
    workItems = WorkItem("elibrary")
    print(workItems.getWorkItemDetails("EL-40"))