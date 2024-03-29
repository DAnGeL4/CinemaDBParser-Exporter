#--Start imports block
#System imports
import os
import typing as typ
from pydantic import AnyHttpUrl, Protocol, HttpUrl
from datetime import timedelta
from pathlib import Path

#Custom imports
#--Finish imports block

#--Start global constants block

# Flags
#---
DOWNLOAD_PROXY_LISTS: bool = bool(
    False
    #True
)
CHECK_PROXIES: bool = bool(
    False
    #True
)
WRITE_LOG_TO_FILE: bool = bool(
    #False
    True
)
RELOAD_WEB_PAGES: bool = bool(
    False
    #True
)
UPDATE_JSON_DUMPS: bool = bool(
    #False
    True
)
USE_MULTITHREADS: bool = bool(  
    #False
    True
)
ENABLE_PARSING_MODULES: bool = bool(
    #False
    True
)
ENABLE_EXPORTER_MODULES: bool = bool(
    #False
    True
)
RESTART_CELERY_WORKERS: bool = bool(
    #False
    True
)
CELERY_USE_PICKLE_SERIALIZER = bool(
    True
    #False
)
USE_DATABASE = bool(
    #True
    False
)
#---

# Common constants
#---
CELERY_TASKS_MODULE = 'modules.flask.celery_tasks'
FLASK_APPLICATION_NAME: str = "CIE"
FLASK_SESSION_FILE_THRESHOLD = 10
FLASK_TIME_TO_LIVE = int(timedelta(hours=2).total_seconds())
FLASK_SESSION_TIME_TO_LIVE = FLASK_TIME_TO_LIVE
FLASK_CACHE_TIME_TO_LIVE = FLASK_TIME_TO_LIVE
FLASK_SESSION_TYPE = 'filesystem'
FLASK_CACHE_TYPE = 'filesystem'
TITLES_DUMP_KEY_ERRORS = 'errors'
#---

# Web Protocols
#---
PROXY_PROTOCOLS: typ.Dict[str, Protocol] = dict({
    "socks4": "socks4",
    "socks5": "socks5"
})
REQUEST_PROXIES_FORMAT: typ.Dict[Protocol, AnyHttpUrl] = {
    "http": None,  #used socks proxy
    "https": None  #used socks proxy
}
#---

# URLs
#---
CELERY_BROKER_URL: AnyHttpUrl = 'redis://localhost:6379'
CELERY_RESULT_BACKEND: AnyHttpUrl = 'redis://localhost:6379'
#---

# Files and Directories
#---
ROOT_DIRECTORY: Path = os.getcwd()
CONFIG_DIR: Path = os.path.join(ROOT_DIRECTORY, "configs/")
MODULES_DIR: Path = os.path.join(ROOT_DIRECTORY, "modules/")
TEMPLATES_DIR: Path = os.path.join(ROOT_DIRECTORY, "templates/")
VARIABLE_DIR: Path = os.path.join(ROOT_DIRECTORY, 'var/')
GLOBAL_LOG_DIR: Path = os.path.join(VARIABLE_DIR, 'logs/')
PROXY_LISTS_DIR: Path = os.path.join(VARIABLE_DIR, "proxy_lists/")
WEB_PAGES_DIR: Path = os.path.join(VARIABLE_DIR, "web_pages/")
JSON_DUMPS_DIR: Path = os.path.join(VARIABLE_DIR, "json_dumps/")
FLASK_SESSION_FILE_DIR: Path = os.path.join(VARIABLE_DIR, "flask_session/")
FLASK_CACHE_DIR: Path = os.path.join(VARIABLE_DIR, "flask_cache/")
SH_DIR: Path = os.path.join(ROOT_DIRECTORY, "sh_scripts/")

REDIS_SETUP_SH_FILE: Path = os.path.join(SH_DIR, "redis_up.sh")
CELERY_SETUP_SH_FILE: Path = os.path.join(SH_DIR, "celery_worker_up.sh")
CORRECT_PROXIES_FILE: Path = os.path.join(PROXY_LISTS_DIR, "correct_proxies")
GLOBAL_LOG_FILE: Path = os.path.join(GLOBAL_LOG_DIR, 'general_log.log')
COMMON_BASH_LOG_FILE: Path = os.path.join(GLOBAL_LOG_DIR, "bash.log")
LOCAL_PROXY_FILES: typ.Dict[Protocol, str] = dict({
    PROXY_PROTOCOLS["socks4"]: "proxy_socks4",
    PROXY_PROTOCOLS["socks5"]: "proxy_socks5",
})
#---

# Online Files
#---
ONLINE_PROXY_LISTS: typ.Dict[str, HttpUrl] = dict({
    LOCAL_PROXY_FILES[PROXY_PROTOCOLS["socks4"]]:
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    LOCAL_PROXY_FILES[PROXY_PROTOCOLS["socks5"]]:
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
})
#---

#--Finish global constants block
