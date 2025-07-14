from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import FormDataService
from .serializers import FormDataSerializer

class FormDataView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = FormDataService()


    def post(self, request):
        serializer = FormDataSerializer(data=request.data)
        if serializer.is_valid():
            form_data = self.service.create_form_data(serializer.validated_data)
            return Response(FormDataSerializer(form_data).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        form_data = self.service.get_all_form_data()
        serializer = FormDataSerializer(form_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FormDataDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = FormDataService()

    def get(self, request, form_id):
        form_data = self.service.get_form_data_by_id(form_id)
        if form_data:
            return Response(FormDataSerializer(form_data).data, status=status.HTTP_200_OK)
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, form_id):
        serializer = FormDataSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            updated_form_data = self.service.update_form_data(form_id, serializer.validated_data)
            if updated_form_data:
                return Response(FormDataSerializer(updated_form_data).data, status=status.HTTP_200_OK)
        return Response({"message": "Update failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, form_id):
        if self.service.delete_form_data(form_id):
            return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Delete failed"}, status=status.HTTP_400_BAD_REQUEST)
