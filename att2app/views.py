from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date, parse_time
from django.views.decorators.http import require_http_methods
import json
from .models import Temperatures

@csrf_exempt  # Allows testing without CSRF token
@require_http_methods(["POST"])  # Restrict to POST requests
def add_temperature(request):
    """
    A view to add new temperature data into the database.
    """
    try:
        # Parse the JSON body of the request
        data = json.loads(request.body)

        # Extract and validate fields from the request body
        date = parse_date(data.get("date"))
        time = parse_time(data.get("time", "00:00:00"))
        temperature1 = data.get("temperature1", 0)
        humidity1 = data.get("humidity1", 0)
        temperature2 = data.get("temperature2", 0)
        humidity2 = data.get("humidity2", 0)
        temperature3 = data.get("temperature3", 0)
        humidity3 = data.get("humidity3", 0)
        temperature4 = data.get("temperature4", 0)
        humidity4 = data.get("humidity4", 0)
        temperature5 = data.get("temperature5", 0)
        humidity5 = data.get("humidity5", 0)

        # Create and save the Temperatures object
        temperature_entry = Temperatures.objects.create(
            date=date,
            time=time,
            temperature1=temperature1,
            humidity1=humidity1,
            temperature2=temperature2,
            humidity2=humidity2,
            temperature3=temperature3,
            humidity3=humidity3,
            temperature4=temperature4,
            humidity4=humidity4,
            temperature5=temperature5,
            humidity5=humidity5,
        )

        # Return a success response with the created record
        return JsonResponse({"success": True, "id": temperature_entry.id}, status=201)

    except Exception as e:
        # Handle errors and return failure response
        return JsonResponse({"success": False, "error": str(e)}, status=400)
