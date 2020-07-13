from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwner
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the user's task.

    list:
    Return a list of all the existing tasks.

    create:
    Create a new task instance.

    update:
    Update existing task.
    """
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        """
        This queryset should return a list of all the todolists
        for the currently authenticated user.
        """
        return self.request.user.tasks.all()
