from linebot.models import MessageTemplateAction,ButtonsTemplate,PostbackTemplateAction,TemplateSendMessage,CarouselTemplate,CarouselColumn
import datetime

def get_fun_msg():
    stateOneTemplate = TemplateSendMessage(
        alt_text='welcome to this chatbot',
        template=ButtonsTemplate(
            title='welcome to this chatbot',
            text='we provide following function',
            thumbnail_image_url='https://i.imgur.com/OsIOOV8.jpg',
            actions=[
                MessageTemplateAction(
                    label='Youtube',
                    text='https://www.youtube.com/'
                ),
                MessageTemplateAction(
                    label='Movie',
                    text='https://movies.yahoo.com.tw/'
                ),
                MessageTemplateAction(
                    label='NBA',
                    text='https://watch.nba.com/'
                ),
                MessageTemplateAction(
                    label='Google',
                    text='https://www.google.com/'
                )

            ]
        )
    )
    return stateOneTemplate
