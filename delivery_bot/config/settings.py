from datetime import datetime, time
from pydantic import BaseSettings, HttpUrl

class BotSettings(BaseSettings):
    api_url: HttpUrl
    api_user: str
    api_password: str
    token: str
    time_start: time
    time_end: time
    
    class Config:
        env_file = './config/.settings'
        
class BotSettingsEnv(BaseSettings):
    api_url: str
    api_user: str
    api_password: str
    token: str
    time_start: time
    time_end: time
