def main():
    from main_app import settings
    CONF = settings.load_conf_file()

    import gettext
    locale_path = '/home/pi/py-proj/main_app/locale/'
    zh_trans = gettext.translation('main-app', locale_path, languages=['zh_TW'])
    en_trans = gettext.translation('main-app', locale_path, languages=['en_US'])
    en_trans.install()
    print('%s %s' % (_('listening'), CONF.default.bind_host))
