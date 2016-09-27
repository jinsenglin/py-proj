def main():
    from main_app import settings
    CONF = settings.load_conf_file()

    print(CONF.default.bind_host)
