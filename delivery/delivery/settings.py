DEBUG = True


if DEBUG:
    from delivery.settings_dev import *
else:
    from delivery.settings_prod import *