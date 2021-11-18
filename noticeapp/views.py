from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from noticeapp.models import Notice
from noticeapp.forms import NoticeCreationForm
from django.urls import reverse_lazy


class NoticeCreateView(CreateView):
    model = Notice
    form_class = NoticeCreationForm
    template_name = "noticeapp/create.html"
    success_url = reverse_lazy('noticeapp:list')


class NoticeListView(ListView):
    model = Notice
    context_object_name = "notice_list"
    template_name = "noticeapp/list.html"
    paginate_by = 30

    def get_queryset(self):

        search = self.request.GET.get("search")

        if search == None or search == "전체":
            print("None and All Check")

            model = Notice.objects.all()

            return model

        else:
            model = Notice.objects.filter(type=search)
            return model

    def get_context_data(self, *args, **kwargs):
        context = super(NoticeListView, self).get_context_data(**kwargs)
        notice_list = Notice.objects.all().order_by("type")

        type_list = []

        for notice in notice_list:
            type_list.append(notice.type)

        type_list = list(set(type_list))
        context["type_list"] = type_list

        print(type_list)

        return context

    def get(self, *args, **kwargs):

        return super(NoticeListView, self).get(args, kwargs)


class NoticeDetailView(DetailView):
    model = Notice
    context_object_name = "target_notice"
    template_name = "noticeapp/detail.html"


class NoticeUpdateView(UpdateView):
    model = Notice
    context_object_name = "target_notice"
    form_class = NoticeCreationForm
    template_name = "noticeapp/update.html"
    success_url = reverse_lazy('noticeapp:list')


class NoticeDeleteView(DeleteView):
    model = Notice
    context_object_name = "target_notice"
    template_name = "noticeapp/delete.html"
    success_url = reverse_lazy('noticeapp:list')
