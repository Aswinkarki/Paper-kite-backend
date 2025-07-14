import logging
from .repository import FormDataRepository

logger = logging.getLogger(__name__)

class FormDataService:
    def __init__(self):
        self.repository = FormDataRepository()

    def create_form_data(self, data):
        return self.repository.create(data)

    def get_all_form_data(self):
        return self.repository.get_all()

    def get_form_data_by_id(self, form_id):
        return self.repository.get_by_id(form_id)

    def update_form_data(self, form_id, data):
        return self.repository.update(form_id, data)

    def delete_form_data(self, form_id):
        return self.repository.delete(form_id)
