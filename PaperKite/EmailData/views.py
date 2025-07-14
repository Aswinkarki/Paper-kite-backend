from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import EmailDataService
from .serializers import EmailDataSerializer

class EmailDataView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = EmailDataService()

    def post(self, request):
        serializer = EmailDataSerializer(data=request.data)
        if serializer.is_valid():
            email_data = self.service.create_email_data(serializer.validated_data['email'])
            if email_data:
                return Response(EmailDataSerializer(email_data).data, status=status.HTTP_201_CREATED)
            return Response({"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        email_data = self.service.get_all_email_data()
        serializer = EmailDataSerializer(email_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EmailDataDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = EmailDataService()

    def get(self, request, email):
        email_data = self.service.get_email_data_by_email(email)
        if email_data:
            return Response(EmailDataSerializer(email_data).data, status=status.HTTP_200_OK)
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, email):
        if self.service.delete_email_data(email):
            return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Delete failed"}, status=status.HTTP_400_BAD_REQUEST)
