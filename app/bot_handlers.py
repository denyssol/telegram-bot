from sqlalchemy.orm import Session

from app import deps
from app.bot import bot
from app.db.utils import create_or_get_user, create_or_default_user
from app.state_handler import get_state_and_process


@bot.message_handler(commands=['start'])
def send_welcome(message, session: Session = deps.get_db):
    db = next(session())

    user = create_or_default_user(db, message.chat.id)

    get_state_and_process(db, message, user)


@bot.message_handler(func=lambda message: True)
def handle_message(message, session: Session = deps.get_db):
    db = next(session())

    user = create_or_get_user(db, message.chat.id)

    get_state_and_process(db, message, user)
