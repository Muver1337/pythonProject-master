from .models import SubRubric


def bboard_context_processor(request):
    context = {'rubrics': SubRubric.object.all()}
    return context
