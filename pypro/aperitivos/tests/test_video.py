import pytest
from django.urls import reverse

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def video(db):
    v = Video(slug='motivacao', tilulo='Video Aperitivo: Motivacao', vimeo_id='682069825')
    v.save()
    return v


@pytest.fixture
def resp(client, db):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, 'Video Aperitivo: Motivacao')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/682069825"')


