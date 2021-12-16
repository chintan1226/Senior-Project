from django.http.response import JsonResponse
from .models import Executive
from .scripts import TwitterAPI, SentimentAnalysis, VisualizeData
from django.shortcuts import render
from datetime import datetime
import json


def search(request):
    return render(request, 'main/search.html')


def error_404(request, exception):
    return render(request, 'main/error_404.html')


def search_name(request):
    name = request.GET.get('name')
    data = []
    if name:
        names_found = Executive.objects.filter(name__icontains=name)

        for name_found in names_found:
            data.append(name_found.name)

    return JsonResponse({'status': 200, 'data': data})


def anaylsis(response, name):
    if name:
        try:
            date = datetime.today().strftime('%Y-%m-%d')
            executive = Executive.objects.get(name=name)

            content = generate_user_data(executive)
            if response.method == "POST":
                if response.POST.get("dateSelected"):
                    date_selected = response.POST.get("dateSelected")
                    date = datetime.strptime(date_selected, '%B %d, %Y')

            print("Date: " + str(date))
            content['stock_graph'] = generate_graph(executive, date)

            return render(response, 'main/analysis.html', content)
        except Exception as e:
            # Add Error Message
            print(e)
            return render(response, 'main/analysis.html')
    # Add Error Message
    return render(response, 'main/analysis.html')


def generate_user_data(executive):

    twitter_data = TwitterAPI.Twitter().generate_twitter_data(executive)
    print("Data Collected")
    anaylsis_df = SentimentAnalysis.Analysis().generate_analysis(twitter_data)
    print("Analysis Collected")
    json_dict = json_records = VisualizeData.Visualize().generate_json_records(anaylsis_df)
    print("Json Generated")
    # stock_table = VisualizeData.Visualize().generate_table(executive.ticker)
    content = {
        'executive': executive,
        'json_records': json.dumps(json_records, indent=4),
        'json_dict': json_dict
    }
    return content


def generate_graph(executive, date):
    stock_data = VisualizeData.Visualize().generate_stock_data(executive.ticker, date)
    print("Stock Data Collected")

    stock_graph = VisualizeData.Visualize().generate_graph(
        executive.ticker, stock_data)
    print("Graph Generated")
    return stock_graph
