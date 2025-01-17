from requests import get
import json




class ApiWB:
    def __init__(self, id_card):
        self.id_card = id_card


    @staticmethod   
    def gett(url: str):
        return get(
            url=url
        ).json()


    def get_api_wb(self) -> dict:
        self.id_card = self.id_card
        url = f"https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1586360&spp=30&hide_dtype=10&ab_testing=false&nm={self.id_card}"
        #response = get(
        #    url=url
        #).json()
        response = __class__.gett(url=url)
        self.price = response["data"]["products"][0]["sizes"][0]["price"]["total"]  # полная цена товара
        self.name = response["data"]["products"][0]["name"]  # наименование товара
        self.rating = response["data"]["products"][0]['reviewRating']   # райтинг товара
        self.feedbacks = response["data"]["products"][0]["feedbacks"]  # количество отзываов


    def get_api_wb_description(self) -> dict:
        url = f'https://basket-12.wbbasket.ru/vol1696/part169684/{self.id_card}/info/ru/card.json'
        response = __class__.gett(url=url)
        self.description = response['description']


s = ApiWB(id_card="229598924")
s.get_api_wb()
s.get_api_wb_description()
print(s.description)

'''if __name__ == "__main__":
    response = get_api_wb(id_card="229598924")
    #print(response)
    #print(json.dumps(response, indent=4, ensure_ascii=False))
    price = response["data"]["products"][0]["sizes"][0]["price"]["total"]  # полная цена товара
    name = response["data"]["products"][0]["name"]  # наименование товара
    rating = response["data"]["products"][0]['reviewRating']   # райтинг товара
    feedbacks = response["data"]["products"][0]["feedbacks"]  # количество отзываов
    # описание товара и изображение хз пока '''


