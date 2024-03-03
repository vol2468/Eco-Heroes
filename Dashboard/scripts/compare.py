from flask import Flask, render_template, request
import requests
import json

compare = Flask(__name__) 
@compare.route('/') 

def compare(): #(latitude, longitude)
    if request.method == 'POST':
        currlatitude=0 #database
        currlongitude=0 #database
        mapdata=request.form
        latitude=34
        longitude=float(mapdata.get('long'))
        url = 'https://airquality.googleapis.com/v1/currentConditions:lookup'
        KEY = 'AIzaSyB9dQ6T8KIegYRV4j8FSlPdVGKc9EuhY68'
        header = {"X-goog-api-key": KEY, "Content-Type": "application/json"}
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
            "languageCode": "en"
        }
        response = requests.post(url, json=data, headers=header)
        api_response = response.json()
        index=api_response.get('indexes')
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
    

        # json_data = json.dumps(api_response, indent=2)
        
        return render_template('compare.html', index=index, First=indexFirst, aqi=quality, 
                               category=categ, dominant=dominant, pollutant=pollutant, effects=effects, children=children, latitude=latitude)

if __name__ == '__main__': 
    compare.run() 