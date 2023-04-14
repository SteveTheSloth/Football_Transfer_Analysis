
import scrapy


class TransferdataItem(scrapy.Item):
    player_name = scrapy.Field()
    player_age = scrapy.Field()
    player_nationality = scrapy.Field()
    player_position = scrapy.Field()
    player_value = scrapy.Field()
    club_from = scrapy.Field()
    club_to = scrapy.Field()
    transfer_type = scrapy.Field()
    transfer_fee = scrapy.Field()
    transfer_date = scrapy.Field()
