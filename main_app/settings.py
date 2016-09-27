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
