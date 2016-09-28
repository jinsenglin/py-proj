def main():
    from main_app import settings
    CONF = settings.load_conf_file()

    from main_app.i18n import _
    print('%s %s' % (_('listening'), CONF.default.bind_host))
