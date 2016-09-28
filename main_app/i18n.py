import oslo_i18n


DOMAIN = 'main-app'

_translators = oslo_i18n.TranslatorFactory(domain=DOMAIN)
_ = _translators.primary
_C = _translators.contextual_form
_P = _translators.plural_form
_LI = _translators.log_info
_LW = _translators.log_warning
_LE = _translators.log_error
_LC = _translators.log_critical


def get_available_languages():
    return oslo_i18n.get_available_languages(DOMAIN)
