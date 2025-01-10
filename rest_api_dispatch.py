# Пример запуска workflow через API
# Запускаться будет eighth_workflow.yml
# Можно и через Postman отправлять запрос через API

import requests
import json



#  класс запуска через workflow dispatch по API
class WorkflowDispatchAPI:
    # ссылочка на документацию https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#create-a-workflow-dispatch-event
    API_TOKEN = "API_TOKEN"  # API_TOKEN"  # занести сюда апи токен

    def __init__(self, owner_repo: str, workflow_id: str, inputs: dict, branch: str="main") -> None:
        '''На вход подается OWNER/REPO и WORKFLOW_ID для url шаблона запроса: https://api.github.com/repos/OWNER/REPO/actions/workflows/WORKFLOW_ID/dispatches
        Пример url: https://api.github.com/repos/MkTGts/for_actions/actions/workflows/eighth_workflow.yml/dispatches 
        Также подает API-token GitHub; branch - ветка(по умолчанию бранч, и inputs - параметры инпутсы.)'''

        self.url: str =  f"https://api.github.com/repos/{owner_repo}/actions/workflows/{workflow_id}/dispatches"
        self.branch: str = branch  # ветка
        self.inputs: dict = inputs  # инпутсы
        self.status = None


    def post_to_api_workflow(self):
        # post запрос для запуска экшена
        response = requests.post(
            url=self.url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {__class__.API_TOKEN}",
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



#  класс запуска через workflow dispatch по API
class RepositoryDispatchAPI:
    # ссылочка на документацию https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#create-a-repository-dispatch-event
    API_TOKEN = "API_TOKEN"  # API_TOKEN"  # занести сюда апи токен

    def __init__(self, owner_repo: str, event_type: str, client_payload: dict) -> None:
        '''На вход подается OWNER/REPO для url шаблона запроса: https://api.github.com/repos/OWNER/REPO/dispatches
        Пример url: https://api.github.com/repos/MkTGts/for_actions/dispatches
        Также подает API-token GitHub; эвент тайп (задвался в воркфлоу) и
        client_payload - словарь, ключи и значения задаем здесь. значения будут хранится по пути github.event.client_payload.имя ключа'''

        self.url: str =  f"https://api.github.com/repos/{owner_repo}/dispatches"
        self.event_type = event_type  # эвент тайп задвался в воркфлоу
        self.client_payload = client_payload  # ключи задавались в воркфлоу значения присваиваются в словаре
        self.status = None


    def post_to_api_repository(self):
        # post запрос для запуска экшена
        response = requests.post(
            url=self.url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {__class__.API_TOKEN}",
                "X-GitHub-Api-Version": "2022-11-28"
            },
            json={
                "event_type": self.event_type,
                "client_payload": self.client_payload
            }  
        )

        if response.status_code == 204:
            self.status = "Response Ok"
        else:
            self.status = f"Problem response. Status code = {response.status_code}"



def post_workflow_dispatch() -> str:
    request_api = WorkflowDispatchAPI(
        owner_repo="MkTGts/for_actions",
        workflow_id="eighth_workflow.yml",
        inputs={
            "titleCustom": "Python request via REST API",
            "selectCustom": "val 3"
        }    

    )
    request_api.post_to_api_workflow()
    return request_api.status


def post_repository_dispatch() -> str:
    request_api = RepositoryDispatchAPI(
        owner_repo="MkTGts/for_actions",
        event_type="test_type",
        client_payload={
            "titleTest": "First value",
            "secondTester": "Second value"
        }
    )
    request_api.post_to_api_repository()
    return request_api.status


if __name__ == "__main__":
    print(post_repository_dispatch())    







