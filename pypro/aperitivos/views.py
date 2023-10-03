from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video


videos = [
    Video(slug='dublin', titulo='Dublin Tour', vimeo_id='682069825'),
    Video(slug='limerick', titulo='Limerick Tour', vimeo_id='251497668'),

]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video_request(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})

