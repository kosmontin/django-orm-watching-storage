from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    serialized_non_closed_visits = []
    for visit in active_visits:
        serialized_non_closed_visits.append({
                    'who_entered': visit.passcard.owner_name,
                    'entered_at': visit.entered_at,
                    'duration': format_duration(visit.get_duration()),
                    'is_strange': visit.is_visit_long()
        })
    context = {
        'non_closed_visits': serialized_non_closed_visits,
    }
    return render(request, 'storage_information.html', context)


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'{int(hours)}ч {int(minutes)}мин'
