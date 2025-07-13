from aiogram.fsm.state import State, StatesGroup


class Register(StatesGroup):
    language = State()
    full_name = State()
    phone_number = State()
    location = State()


class Feedback(StatesGroup):
    feedback = State()
