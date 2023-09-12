from django.shortcuts import render


def video(request, slug):
    videos = {
     'motivacao': {'titulo': 'Video Aperitivo: Motivacao', 'vimeo_id': 682069825},
     'Instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 251497668},
    }
    video = videos[slug]
    return render(request, 'Aperitivos/video.html', context={'video': video})