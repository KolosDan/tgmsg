class Chat(object):
    def __init__(self, id: int, type: str, **kwargs):
        self.id = id
        self.type = type
        for key in kwargs:
            setattr(self, key, kwargs[key])


class User(object):
    def __init__(self, id: int, **kwargs):
        self.id = id
        for key in kwargs:
            setattr(self, key, kwargs[key])


class IncomingMessage(object):
    def __init__(self, message_id: int, chat, **kwargs):
        self.message_id = message_id
        self.text = ''
        self.chat = Chat(**chat)
        if 'from' in kwargs:
            kwargs['m_from'] = kwargs['from']
        for key in kwargs:
            if key == 'm_from':
                kwargs[key] = User(**kwargs[key])
            setattr(self, key, kwargs[key])


class CallbackQuery(object):
    def __init__(self, id: int, **kwargs):
        self.id = id
        if 'from' in kwargs:
            kwargs['m_from'] = kwargs['from']
            del kwargs['from']
        for key in kwargs:
            if key == 'message':
                kwargs[key] = IncomingMessage(**kwargs[key])
            if key == 'm_from':
                kwargs[key] = User(**kwargs[key])
            setattr(self, key, kwargs[key])


class PollAnswer(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            if key == "user":
                kwargs[key] = User(**kwargs[key])
            setattr(self, key, kwargs[key])


class Update(object):
    def __init__(self, update_id: int, **kwargs):
        self.update_id = update_id
        for key in kwargs:
            if key == 'callback_query':
                kwargs[key] = CallbackQuery(**kwargs[key])
            if key == 'message':
                kwargs[key] = IncomingMessage(**kwargs[key])
            if key == "poll_answer":
                kwargs[key] = PollAnswer(**kwargs[key])
            setattr(self, key, kwargs[key])
