import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage , TemplateSendMessage, LocationSendMessage, StickerSendMessage, ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"

def send_template_message(reply_token, template):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, template)
    return "OK"

def send_location_message(reply_token, location ):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, location)
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
