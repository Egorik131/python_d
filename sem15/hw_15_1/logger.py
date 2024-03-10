import logging

def log_make(info_out: str, logfile):
    FORMAT = '{levelname:<8} - {asctime}. Модуль "{name}", функция "{funcName}" | {msg}'

    logging.basicConfig(filename=logfile, filemode='w',
                        format=FORMAT, style='{',
                        encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(info_out)