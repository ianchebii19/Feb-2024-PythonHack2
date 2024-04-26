import requests
from django.shortcuts import render

def home(request):
  # USING APIS => Example 1
  response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random?language=en')
  res1 = response.json()
  result = res1["text"]

  response2 = requests.get('https://www.boredapi.com/api/activity')
  data2 = response2.json()
  result2 = data2["activity"]
  response3 = requests.get('https://dog.ceo/api/breeds/image/random')
  data3 = response3.json()
  result3 = data3["message"]
  if request.method == 'POST':
    photo=request.POST['photo']
  else:
    photo=None



  return render(request, 'templates/index.html', {'result': result,'photo':photo, 'result2': result2, 'result3': result3, })