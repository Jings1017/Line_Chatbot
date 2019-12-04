from linebot.models import MessageTemplateAction,ButtonsTemplate,PostbackTemplateAction,TemplateSendMessage,CarouselTemplate,CarouselColumn
import datetime

def get_lobby_msg():
    stateOneTemplate = TemplateSendMessage(
        alt_text='welcome to this chatbot',
        template=ButtonsTemplate(
            title='welcome to this chatbot',
            text='we provide following function',
            thumbnail_image_url='https://i.imgur.com/OsIOOV8.jpg',
            actions=[
                MessageTemplateAction(
                    label='food',
                    text='food'
                ),
                MessageTemplateAction(
                    label='drink',
                    text='drink'
                ),
                MessageTemplateAction(
                    label='sticker',
                    text='sticker'
                ),
                MessageTemplateAction(
                    label='location',
                    text='location'
                )

            ]
        )
    )
    return stateOneTemplate

def get_food_msg():
    stateOneTemplate = TemplateSendMessage(
        alt_text='I will service you',
        template=ButtonsTemplate(
            title='welcome to this chatbot',
            text='we provide following function',
            thumbnail_image_url='https://i.imgur.com/OsIOOV8.jpg',
            actions=[
                MessageTemplateAction(
                    label='breakfast',
                    text='breakfast'
                ),
                MessageTemplateAction(
                    label='lunch',
                    text='lunch'
                ),
                MessageTemplateAction(
                    label='dinner',
                    text='dinner'
                )
            ]
        )
    )
    return stateOneTemplate

def get_drink_msg():
    stateOneTemplate = TemplateSendMessage(
        alt_text='I will service you',
        template=ButtonsTemplate(
            title='welcome to this chatbot',
            text='we provide following function',
            thumbnail_image_url='https://i.imgur.com/OsIOOV8.jpg',
            actions=[
                MessageTemplateAction(
                    label='coffee',
                    text='coffee'
                ),
                MessageTemplateAction(
                    label='tea',
                    text='tea'
                )
            ]
        )
    )
    return stateOneTemplate

def get_location_msg():
    stateOneTemplate = TemplateSendMessage(
        alt_text='I will service you',
        template=ButtonsTemplate(
            title='welcome to this chatbot',
            text='we provide following function',
            thumbnail_image_url='https://i.imgur.com/OsIOOV8.jpg',
            actions=[
                MessageTemplateAction(
                    label='NCKU CSIE',
                    text='NCKU CSIE'
                ),
                MessageTemplateAction(
                    label='Tainan Main Station',
                    text='Tainan Main Station'
                ),
                MessageTemplateAction(
                    label='THSR Tainan Station',
                    text='THSR Tainan Station'
                )
            ]
        )
    )
    return stateOneTemplate