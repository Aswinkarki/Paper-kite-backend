import logging
from .models import FormData

logger = logging.getLogger(__name__)

class FormDataRepository:
    def __init__(self):
        self.queryset = FormData.objects

    def create(self, data):
        try:
            form_data = self.queryset.create(**data)
            logger.info(f"FormData created: {form_data.id}")
            return form_data
        except Exception as e:
            logger.error(f"Error creating FormData: {e}")
            return None

    def get_all(self):
        return self.queryset.all()

    def get_by_id(self, form_id):
        try:
            return self.queryset.get(id=form_id)
        except FormData.DoesNotExist:
            logger.warning(f"FormData with ID {form_id} not found")
            return None

    def update(self, form_id, data):
        form_data = self.get_by_id(form_id)
        if form_data:
            for key, value in data.items():
                setattr(form_data, key, value)
            form_data.save()
            logger.info(f"FormData {form_id} updated")
            return form_data
        return None

    def delete(self, form_id):
        form_data = self.get_by_id(form_id)
        if form_data:
            form_data.delete()
            logger.info(f"FormData {form_id} deleted")
            return True
        return False
