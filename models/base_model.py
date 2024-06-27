from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        model_dict = self.__dict__
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        model_dict['updates_at'] = self.updated_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        return model_dict

    def __str__(self) -> str:
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
