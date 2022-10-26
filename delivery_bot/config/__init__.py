import os
from .settings import BotSettings, BotSettingsEnv

if os.getenv('TOKEN'):
    settings = BotSettingsEnv()
else:
    settings = BotSettings()