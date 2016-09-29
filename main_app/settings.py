from oslo_config import cfg


default_group = cfg.OptGroup(name='default')
default_opts = [
    cfg.StrOpt('bind_host', default='127.0.0.1')
]

CONF = cfg.CONF
CONF.register_group(default_group)
CONF.register_opts(default_opts, default_group)


def load_conf_file():
    CONF(default_config_files=['/etc/main-app/app.conf'])
    return CONF


import logging.config


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'main_app': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

logging.config.dictConfig(LOGGING)
