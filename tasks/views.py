from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializers import CustomUserSerializer
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        else:
            return Task.objects.filter(assignee=user)


def update(self, request, *args, **kwargs):
    instance = self.get_object()
    assignee_id = request.data.get('assignee')
    if assignee_id:
        try:
            assignee = CustomUserSerializer.objects.get(id=assignee_id)
            instance.assignee = assignee
            instance.save()
            return Response({'status': 'Task assigned successfully.'})
        except CustomUserSerializer.DoesNotExist:
            return Response({'error': 'Invalid assignee ID.'}, status=status.HTTP_400_BAD_REQUEST)

    status = request.data.get('status')
    if status:
        instance.status = status
        instance.save()
        return Response({'status': 'Task status updated successfully.'})

    return Response({'error': 'Status field is required.'}, status=status.HTTP_400_BAD_REQUEST)
