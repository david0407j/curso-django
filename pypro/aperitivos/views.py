from django.shortcuts import render

videos = [
      {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivacao', 'vimeo_id': 682069825},
      {'slug': 'instalacao-windows', 'titulo': 'Instalacao Windows', 'vimeo_id': 251497668},
]


def indice(request):
    return render(request, 'aperitivos/indice.html')


videos_dct = {dct['slug']: dct for dct in videos}


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})