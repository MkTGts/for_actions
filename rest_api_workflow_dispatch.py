# Пример запуска workflow через API
# Запускаться будет eighth_workflow.yml
# Можно и через Postman отправлять запрос через API

import requests
import json



class Workflow_API:
    API_TOKEN = "API_TOKEN"  # API_TOKEN"  # занести сюда апи токен

    def __init__(self, owner_repo: str, workflow_id: str, inputs: dict, branch: str="main") -> None:
        '''На вход подается OWNER/REPO и WORKFLOW_ID для url шаблона запроса: https://api.github.com/repos/OWNER/REPO/actions/workflows/WORKFLOW_ID/dispatches
        Пример url: https://api.github.com/repos/MkTGts/for_actions/actions/workflows/eighth_workflow.yml/dispatches 
        Также подает API-token GitHub; branch - ветка(по умолчанию бранч, и inputs - параметры инпутсы.)'''

        self.url: str =  f"https://api.github.com/repos/{owner_repo}/actions/workflows/{workflow_id}/dispatches"
        self.api_token: str = __class__.API_TOKEN
        self.branch: str = branch
        self.inputs: dict = inputs
        self.status = None


    def post_to_api_workflow(self):
        # post запрос для запуска экшена
        response = requests.post(
            url=self.url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.api_token}",
                "X-GitHub-Api-Version": "2022-11-28"
            },
            json={
                "ref": self.branch,
                "inputs": self.inputs
            }
            
        )

        if response.status_code == 204:
            self.status = "Response Ok"
        else:
            self.status = f"Problem response. Status code = {response.status_code}"



def post_api() -> str:
    request_api = Workflow_API(
        owner_repo="MkTGts/for_actions",
        workflow_id="eighth_workflow.yml",
        inputs={
            "titleCustom": "Python request via REST API",
            "selectCustom": "val 3"
        }    

    )
    request_api.post_to_api_workflow()
    return request_api.status


if __name__ == "__main__":
    print(post_api())







