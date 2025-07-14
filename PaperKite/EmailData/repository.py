import logging
from .models import EmailData

logger = logging.getLogger(__name__)

class EmailDataRepository:
    def __init__(self):
        self.queryset = EmailData.objects

    def create(self, email):
        try:
            email_data = self.queryset.create(email=email)
            logger.info(f"EmailData created: {email_data.email}")
            return email_data
        except Exception as e:
            logger.error(f"Error creating EmailData: {e}")
            return None

    def get_all(self):
        return self.queryset.all()

    def get_by_email(self, email):
        try:
            return self.queryset.get(email=email)
        except EmailData.DoesNotExist:
            logger.warning(f"EmailData with email {email} not found")
            return None

    def delete(self, email):
        email_data = self.get_by_email(email)
        if email_data:
            email_data.delete()
            logger.info(f"EmailData {email} deleted")
            return True
        return False
