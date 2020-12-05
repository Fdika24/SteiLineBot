from linebot import LineBotApi, WebhookHandler

import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

line_bot_api = LineBotApi('6zD7qNcZHoTJKL//r0odUpgEQCZghzMEtrxLyDliXevFF0K7bcf2HYzplYH1jmre7wqWYu/kaCgQ8QGQ7Da/FLmvPHSbiDefh0DUCF8WZCNxxuuWBrzG4WCLazxIbok+oZf0GuUNQxGEpNPnwl2J6QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f35b52879515aa305b5f87011a00518d')
