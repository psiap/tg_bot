from aiogram.dispatcher.filters.state import StatesGroup,State

class R_patrner(StatesGroup):
    RP1 = State()
    RP2 = State()
    RP3 = State()
    RP4 = State()
    RP5 = State()
    RP6 = State()
    RP7 = State()
    RP8 = State()

class send_an_alert_1(StatesGroup):
    SA_1 = State()
    SA_2 = State()
    SA_3 = State()
    SA_4 = State()
    SA_5 = State()
    SA_6 = State()

class deferred_messages_2(StatesGroup):
    DM_1 = State()
    DM_2 = State()
    DM_3 = State()
    DM_4 = State()
    DM_5 = State()

class letter_admin_3(StatesGroup):
    RP3_1 = State()
    RP3_2 = State()
    RP3_3 = State()

class sending_letter_1(StatesGroup):
    SL_1 = State()
    SL_2 = State()
    SL_3 = State()
    SL_4 = State()
    SL_5 = State()

class view_the_rest(StatesGroup):
    VR_1 = State()
    VR_2 = State()
    VR_3 = State()
    VR_4 = State()

class change_addressees(StatesGroup):
    CA_1 = State()
    CA_2_add_1 = State()
    CA_2_add_2 = State()
    CA_2_add_3 = State()
    CA_2_add_4 = State()
    CA_3_del_1 = State()
    CA_3_del_2 = State()
    CA_3_del_3 = State()
    CA_3_del_4 = State()
