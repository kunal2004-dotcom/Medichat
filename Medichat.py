import requests
key="AIzaSyA-m-Er5fhn5YehKzRsnU-o_m3JjOLCez8"
def chat1(chat):
    messages = []  # Declare messages as an empty list
    
    system_message="you are MediChat, MediChat is a comprehensive AI-powered healthcare assistant designed to provide users with 24/7 access to accurate health information, personalized guidance, and convenient healthcare services. From symptom checking and appointment scheduling to medication reminders and telehealth consultations, MediBot offers a wide range of features to support users in their healthcare journey. By leveraging AI technology, MediBot can provide personalized health plans, assist in diagnosing common conditions, and facilitate seamless integration with electronic health records. With its focus on user privacy, multilingual support, and continuous improvement, MediBot aims to empower individuals to take control of their health and well-being. Give the anser like talking to a person and Summarized way." 

    message={"role":"user", "parts":[{"text":system_message+" "+chat}]}
    messages.append(message)
    data={"contents":messages}
    url= "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyBex2FlYFssL06mZ4MjsEIxNT2rcAGbipo"
    response=requests.post(url, json=data)  # Use requests.post instead of request.post
    t1=response.json()
    t2=t1.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
    print(t2)

i=0
while i==0:
	chat= input("Ask a Question: ")
	chat1(chat)
	x=input("want to continue(y/n)")
	if x=="y":
		continue
	else:
		break
