from django.apps import AppConfig


class OnlineAuctionAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'online_auction_app'

    def ready(self):
        import online_auction_app.signals.signals

