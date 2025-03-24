from typing import List
import model
import db

TITLE_LIMIT = 30
TEXT_LIMIT = 200

class LogicException(Exception):
    pass

class CalendarLogic:
    def __init__(self):
        self._calendar_db = db.CalendarDB()

    @staticmethod
    def _validate_event(event: model.CalendarEvent):
        if event is None:
            raise LogicException("event is None")
        if event.date is None or not isinstance(event.date, str) or len(event.date) != 10:
            raise LogicException("invalid date format, expected YYYY-MM-DD")
        if event.title is None or len(event.title) > TITLE_LIMIT:
            raise LogicException(f"title length > MAX: {TITLE_LIMIT}")
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text length > MAX: {TEXT_LIMIT}")

    def create(self, event: model.CalendarEvent) -> str:
        self._validate_event(event)
        try:
            return self._calendar_db.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.CalendarEvent]:
        try:
            return self._calendar_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.CalendarEvent:
        try:
            return self._calendar_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: model.CalendarEvent):
        self._validate_event(event)
        try:
            return self._calendar_db.update(_id, event)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._calendar_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")