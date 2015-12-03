from django.apps import AppConfig


class BlancBasicAssetsConfig(AppConfig):
    name = 'blanc_basic_assets'
    label = 'assets'

    def ready(self):
        super(BlancBasicAssetsConfig, self).ready()
        from . import listeners  # noqa
