import scrapy
from scrapy.http import Request
from ..items import TransferdataItem
import pandas as pd


class TransferSpiderSpider(scrapy.Spider):
    name = "transfer_spider"
    allowed_domains = ["www.transfermarkt.de"]
    year = 2023
    part_url = f"https://www.transfermarkt.de/bundesliga/transfers/wettbewerb/L1/plus/?saison_id={year}&s_w=&leihe=1&intern=0"
    start_urls = [
        part_url]

    def parse(self, response, year=2023):

        club_list = list()
        name_list = list()
        age_list = list()
        nationality_list = list()
        position_list = list()
        value_list = list()
        club_from_list = list()
        club_to_list = list()
        amount_list = list()
        transfer_year_list = list()

        for i in range(4, 22):
            club_list.append(response.xpath(
                f"/html/body/div[2]/main/div[2]/div[1]/div[{i}]/h2/a[2]/text()").get())

        """for i in range(4, 22):
            for j in (1, 3):
                for tr in response.xpath(f"/html/body/div[2]/main/div[2]/div[1]/div[{i}]/div[{j}]/table/tbody/tr"):

                    name_list.append(tr.xpath(
                        "./td[1]/div[1]/span/a/text()").get())
                    transfer_year_list.append(year)
                    age_list.append(tr.xpath("./td[2]/text()").get())
                    nationality_list.append(
                        tr.xpath("./td[3]/img[1]/@title").get())
                    position_list.append(tr.xpath("./td[5]/text()").get())
                    value_list.append(tr.xpath("./td[6]/text()").get())
                    amount = tr.xpath("./td[9]/a/text()").get()
                    if amount == "Leih-Ende":
                        amount += " " + tr.xpath("./td[9]/a/i/text()").get()
                    amount_list.append(amount)
                    club = tr.xpath("./td[7]/a/img/@title").get()
                    if club == None or club == " " or club == "\xa0":
                        club = tr.xpath(
                            "./td[7]/a/img/@alt").get()
                    if club == None:
                        club = tr.xpath(
                            "./td[7]/img/@title").get()
                    if club == None or club == " " or club == "\xa0":
                        club = tr.xpath(
                            "./td[7]/img/@alt").get()
                    if j == 1:
                        club_to_list.append(club_list[i-4])
                        club_from_list.append(club)
                    elif j == 3:
                        club_from_list.append(club_list[i-4])
                        club_to_list.append(club)

        for i in range(len(name_list)):
            details = TransferdataItem()
            details["player_name"] = name_list[i]
            details["player_age"] = age_list[i]
            details["player_nationality"] = nationality_list[i]
            details["player_position"] = position_list[i]
            details["player_value"] = value_list[i]
            details["club_from"] = club_from_list[i]
            details["club_to"] = club_to_list[i]
            details["transfer_fee"] = amount_list[i]
            details["transfer_date"] = transfer_year_list[i]

            yield details"""

        for i in club_list:
            """create club list for every year"""

            details = TransferdataItem()
            details["club_to"] = i
            details["transfer_date"] = year

            yield details

        if year > 2000:
            year -= 1
            yield Request(
                f"https://www.transfermarkt.de/bundesliga/transfers/wettbewerb/L1/plus/?saison_id={year}&s_w=&leihe=1&intern=0", callback=self.parse, cb_kwargs=dict(year=year))
