def main():
    from main_app import settings
    CONF = settings.load_conf_file()

    from main_app.i18n import _
    import logging
    logger = logging.getLogger(__name__)
    logger.info('%s %s' % (_('listening'), CONF.default.bind_host))
