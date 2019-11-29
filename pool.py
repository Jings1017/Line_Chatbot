from linebot.models import MessageTemplateAction,ButtonsTemplate,PostbackTemplateAction,TemplateSendMessage,CarouselTemplate,CarouselColumn
import datetime

def get_center_msg():
    stateOneTemplate = TemplateSendMessage(
        alt_text='welcome to this chatbot',
        template=ButtonsTemplate(
            title='welcome to this chatbot',
            text='we provide following function',
            thumbnail_image_url='https://i.imgur.com/ZjBmY3N.jpg',
            actions=[
                MessageTemplateAction(
                    label='Youtube',
                    text='https://www.youtube.com/'
                ),
                MessageTemplateAction(
                    label='movie',
                    text='https://movies.yahoo.com.tw/'
                )
            ]
        )
    )
    return stateOneTemplate