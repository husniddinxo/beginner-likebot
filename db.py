import json


class DB:
    def __init__(self) -> None:
        with open('db.json') as f:
            data = f.read()
            if data:
                self.data = json.loads(data)
            else:
                self.data = {}
    
    def save(self) -> None:
        '''save file'''
        with open('db.json', 'w') as f:
            data = json.dumps(self.data, indent=4)
            f.write(data)

    def add(self, chat_id: str) -> bool:
        '''add new user'''
        self.data[chat_id] = {
            "like": 0,
            "dislike": 0,
        }
        self.save()
        return True
    
    def increase_like(self, chat_id: str) -> dict:
        self.data[chat_id]['like'] += 1
        self.save()
        return self.data[chat_id]
    
    def increase_dislike(self, chat_id: str) -> dict:
        self.data[chat_id]['dislike'] += 1
        self.save()
        return self.data[chat_id]
