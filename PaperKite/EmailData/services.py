import logging

from EmailData.task import send_subscription_email
from .repository import EmailDataRepository

logger = logging.getLogger(__name__)

class EmailDataService:
    def __init__(self):
        self.repository = EmailDataRepository()

    def create_email_data(self, email):
        email_data = self.repository.create(email)
        if email_data:
            send_subscription_email.delay(email)  # Trigger Celery task
        return email_data

    def get_all_email_data(self):
        return self.repository.get_all()

    def get_email_data_by_email(self, email):
        return self.repository.get_by_email(email)

    def delete_email_data(self, email):
        return self.repository.delete(email)
