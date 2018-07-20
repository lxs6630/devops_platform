import logging.handlers
import logging
import time
from jenkins_ops import config
log = logging.getLogger('log')
time_cut = logging.handlers.TimedRotatingFileHandler(filename=config.log_file, when='D', interval=1, backupCount=config.backup_count)
formatter = logging.Formatter("[%(asctime)s %(filename)s %(levelname)s] %(message)s", datefmt='%a, %m-%d-%Y %H:%M:%S')
time_cut.setFormatter(formatter)
log.setLevel(config.log_level)
time_cut.suffix = "%Y-%m-%d"  # 如果设定是天，就必须写成"%Y-%m-%d"其他格式不生效
log.addHandler(time_cut)