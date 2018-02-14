from rest_framework import generics
from guardian.shortcuts import get_objects_for_user

from .models import Answer
from .serializers import AnswerSerializer


class AnswerList(generics.ListCreateAPIView):
    """
    Answer list.
    """
    model = Answer
    serializer_class = AnswerSerializer

    def get_queryset(self):
        print(self.request.user)
        answers_qs = get_objects_for_user(self.request.user, Answer.CAN_VIEW, Answer)
        return answers_qs


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Answer detail.
    """
    model = Answer
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return get_objects_for_user(self.request.user,
                                    [Answer.CAN_VIEW,
                                     Answer.CAN_DELETE,
                                     Answer.CAN_UPDATE],
                                    Answer)


answer_list = AnswerList.as_view()
answer_detail = AnswerDetail.as_view()
