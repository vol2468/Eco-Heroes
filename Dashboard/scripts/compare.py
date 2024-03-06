from flask import Flask, render_template, request
import requests
import json

compare = Flask(__name__) 
@compare.route('/') 

def compare(): #(latitude, longitude)
    # if request.method == 'POST':
    currlatitude=37.419734 #database
    currlongitude=-122.0827784 #database
    mapdata=request.form
    latitude=float(mapdata.get('lat'))
    longitude=float(mapdata.get('long'))
    url = 'https://airquality.googleapis.com/v1/currentConditions:lookup'
    KEY = ''
    header = {"X-goog-api-key": KEY, "Content-Type": "application/json"}
    data = {
        "universalAqi": True,
        "location": {
            "latitude": currlatitude, #latitude var
            "longitude": currlongitude #longitude var
        },
        "extraComputations": [
            "HEALTH_RECOMMENDATIONS",
            "DOMINANT_POLLUTANT_CONCENTRATION",
            "POLLUTANT_CONCENTRATION",
            "LOCAL_AQI",
            "POLLUTANT_ADDITIONAL_INFO"
        ],
        "languageCode": "en"
    }
    response = requests.post(url, json=data, headers=header)
    my_api_response = response.json()
    index=my_api_response.get('indexes')
    indexFirst=index[0]
    my_quality=indexFirst.get('aqi')
    my_categ=indexFirst.get('category')
    my_dominant=indexFirst.get('dominantPollutant')
    pollutant=my_api_response.get('pollutants')
    my_effects=''
    for i in range(1,len(pollutant)):
        code=pollutant[i].get('code')
        if(code==my_dominant):
                additional=pollutant[i].get('additionalInfo')
                my_effects=additional.get('effects')
    my_recommendation=my_api_response.get('healthRecommendations')
    my_children=my_recommendation.get('children')    
    # json_data = json.dumps(api_response, indent=2)

    data = {
    "universalAqi": True,
    "location": {
        # "latitude": 37.419734, #latitude var
        # "longitude": -122.0827784 #longitude var
        "latitude": latitude, #latitude var
        "longitude": longitude #longitude var
    },
    "extraComputations": [
        "HEALTH_RECOMMENDATIONS",
        "DOMINANT_POLLUTANT_CONCENTRATION",
        "POLLUTANT_CONCENTRATION",
        "LOCAL_AQI",
        "POLLUTANT_ADDITIONAL_INFO"
    ],
    "languageCode": "en"}

    response = requests.post(url, json=data, headers=header)
    api_response = response.json()
    index=api_response.get('indexes')
    if index:
        indexFirst=index[0]
        quality=indexFirst.get('aqi')
        categ=indexFirst.get('category')
        dominant=indexFirst.get('dominantPollutant')
        pollutant=api_response.get('pollutants')
        effects=''
        for i in range(1,len(pollutant)):
            code=pollutant[i].get('code')
            if(code==dominant):
                    additional=pollutant[i].get('additionalInfo')
                    effects=additional.get('effects')
        recommendation=api_response.get('healthRecommendations')
        children=recommendation.get('children')   
        
        return render_template('compare.html', aqi=quality, category=categ, dominant=dominant, effects=effects, children=children,
                                            my_aqi=my_quality, my_category=my_categ, my_dominant=my_dominant, my_effects=my_effects, my_children=my_children)
    else:
        return render_template('map.html')


if __name__ == '__main__': 
    compare.run() 