from loguru import logger
from notifiers.logging import NotificationHandler
from config import bot_token, chat_ids

paramsFilipp = {
    'token': bot_token,
    'chat_id': chat_ids['fil']
}
paramsBomb = {
    'token': '6614528317:AAH1gbupuyL3XgLaVyrw1tDRVZLlKhSROdo',
    'chat_id': chat_ids['bomb']
}
tg_handlerFilipp = NotificationHandler("telegram", defaults=paramsFilipp)
tg_handlerBomb = NotificationHandler("telegram", defaults=paramsBomb)

# добавляем в logger правило, что все логи уровня info и выше отсылаются в телегу
logger.add(tg_handlerFilipp, level="SUCCESS",format="{message}")
logger.add(tg_handlerBomb, level="SUCCESS",format="{message}")


logger.success('ккк')