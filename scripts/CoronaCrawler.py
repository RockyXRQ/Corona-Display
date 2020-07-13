import requests
import threading
import time
from bs4 import BeautifulSoup


class CronaCrawler:

    def __init__(self, url: str):
        self.__url = url
        self.__page = page = requests.Session().get(url)
        self.__soup = BeautifulSoup(page.content, 'html.parser')

        self.__isUpdated = False
        self.__t1 = threading.Thread(target=self.__country_data_update)
        self.__t2 = threading.Thread(target=self.__area_data_update)

    def __get_json_in_script(self, soup, id: str):
        text = str(soup.find('script', id=id).string)
        return text[text.find('['):text.rfind(']')+1]

    def __save_as_json(self, jsonName: str, value: str):
        with open(jsonName+'.json', 'w', encoding='utf8') as js:
            js.write(value)

    def __country_data_update(self):
        country_info = self.__get_json_in_script(
            self.__soup, 'getListByCountryTypeService2true')
        self.__save_as_json('data/country_data', country_info)

    def __area_data_update(self):
        area_info = self.__get_json_in_script(self.__soup, 'getAreaStat')
        self.__save_as_json('data/area_data', area_info)

    def data_update(self):
        print("数据已更新")
        self.__t1.start()
        self.__t2.start()
        self.__isUpdated = True

    def data_update_by_time(self, secs: int):
        print("爬虫开始，更新时间间隔为 "+str(secs)+" 秒")
        while True:
            self.data_update()
            time.sleep(secs)

    @property
    def isUpdated(self):
        return self.__isUpdated

    @isUpdated.setter
    def isUpdated(self, value: bool):
        self.__isUpdated = value


cronaCrawler = CronaCrawler("https://ncov.dxy.cn/ncovh5/view/pneumonia")

if __name__ == "__main__":

    cronaCrawler.data_update_by_time(3*60)
