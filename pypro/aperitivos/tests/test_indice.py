from model_bakery import baker
import pytest
from django.urls import reverse

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))

@pytest.fixture
def videos(db):
    return baker.make(Video, 3)


def test_status_code(resp):
    assert resp.status_code == 200



def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


@pytest.mark.parametrize(
    'slug',
    [
        'motivacao',
        'instalacao-windows'
   ]
)
def test_link_video(resp, slug):
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')




