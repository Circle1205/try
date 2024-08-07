import logging
import datetime

# 設置logger跟輸出形式
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s  %(levelname)-8s %(module)s:%(lineno)d] %(message)s',
                              datefmt='%Y%m%d %H:%M:%S')

# 將log輸出到console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)  # 將ch handler添加到logger中，日誌消息輸出到console

# 將log輸出到檔
log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)

# 情境
if __name__ == "__main__":
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')
