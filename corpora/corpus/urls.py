from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url, include
from corpus.views import views
from corpus.views.views import SentenceListView, StatsView, ListenView
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(_(r'^record/'), views.record, name='record'),
    url(_(r'^listen/'), ListenView.as_view(), name='listen'),

    url(r'^submit_recording/',
        views.submit_recording,
        name='submit_recording'),
    url(r'^failed_submit/', views.failed_submit, name='failed_submit'),
    url(_(r'^sentences/'), SentenceListView.as_view(), name='sentence-list'),

    url(_(r'^stats/'), cache_page(60*60*1)(StatsView.as_view()), name='stats'),

    url(r'^recording-file/(?P<pk>[\d]+)/$',
        views.RecordingFileView.as_view(),
        name='recording_file'),
]
