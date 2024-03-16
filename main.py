from highrise import *
from highrise.models import *
from highrise import (
    BaseBot,
    __main__
)
from highrise.models import (
    Position,
    SessionMetadata,
    User
)
from asyncio import run as arun
from highrise import BaseBot, Position
from highrise import SessionMetadata, User
from highrise import __main__
from asyncio import run as arun
from highrise import *
from highrise.models import*
from highrise import*
from flask import Flask
from threading import Thread
from highrise.__main__ import *
import time
from highrise.models import (
    SessionMetadata,
    User)

class Bot(BaseBot):
    def __init__(self):
        super().__init__()


    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("hi im alive?")
        self.highrise.tg.create_task(self.highrise.teleport(
            session_metadata.user_id, Position(17.00, 0.00,13.5, "FrontRight")))

      
    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            print(f"Caught Teleport Error: {e}")

  
    async def run(self, room_id, token) -> None:
        await __main__.main(self, room_id, token)
class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Alive"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()
    
class RunBot():
    room_ids = ["63c125b111edc5478ba262e1", "63c125b111edc5478ba262e1", "63c125b111edc5478ba262e1",
                "63c125b111edc5478ba262e1", "63c125b111edc5478ba262e1",
               "63c125b111edc5478ba262e1",
               "63c125b111edc5478ba262e1",
               "63c125b111edc5478ba262e1"]
    
    bot_tokens = [
        "59a62549806513248bbd6b65178d455e0c44363e20f015118bd9f6439245ce6f",
        "cb6bb5baf8c9a94eec55f589d9904db836ab422223583b5bd337d1710432665d",
        "bc3850812af38a0b5eaa910d6d1730ceca22d88038494a414361061c7b40350f",
        "323126dc40a691e34716f266482d4122e5f6a5518b3e727ba5bdc8f076fe5065",
        "8632c85b82a8ddcbfa5a6528db226dbbc9644cc2567e07801870c32cbaf0623c",
"a5941d7d5fbc6959109357a5b53ec48bf320a81852de6e132d6f4b3b651fa217",
"57d16b98791f6066adbbd31e3b6a664915610cc6019ac7ce18c6a311a5dcab13",
"8b59e86292696c94bb392e8f1d3fb8c635944feff0a5ecb81f27d72b2e9f786d"]
    
    bot_file = "main"
    bot_class = "Bot"

    def __init__(self) -> None:
        self.definitions = []
        for room_id, bot_token in zip(self.room_ids, self.bot_tokens):
            self.definitions.append(
                BotDefinition(
                    getattr(import_module(self.bot_file), self.bot_class)(),
                    room_id, bot_token)
            )

    def run_loop(self) -> None:
        while True:
            try:
                arun(main(self.definitions))
            except Exception as e:
                import traceback
                print("Caught an exception:")
                traceback.print_exc()
                time.sleep(1)
                continue


if __name__ == "__main__":
    WebServer().keep_alive()
    RunBot().run_loop()