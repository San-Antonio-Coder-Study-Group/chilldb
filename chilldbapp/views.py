from django.shortcuts import render

def db_visualizer(request):
    # Placeholder data for now (we'll replace this with real DB data later)
    context = {
        'databases': [
            {'name': 'range-partition-db', 'type': 'Range Partition', 'status': 'Active'},
            {'name': 'hash-partition-db', 'type': 'Hash Partition', 'status': 'Active'},
            {'name': 'local-index-db', 'type': 'Local Index', 'status': 'Active'},
        ]
    }
    return render(request, 'chilldbapp/db_visualizer.html', context)