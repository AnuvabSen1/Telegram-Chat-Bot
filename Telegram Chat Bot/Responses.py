from datetime import datetime
def sample_responses(input_text):
 user_message= str(input_text).lower()
 if user_message in ("hello" , "hi" , "sup"):
  return "Hey! how is it going?"
 if user_message in ("who are you" , "who are you?" , "who are you?!"):
  return "I am Amrita Kesh, I am from Durgapur,India "
 if user_message in ("time" , "time?" , "date", "date?"):

  now= datetime.now()
  date_time=now.strftime("%d/%m/%y, %H:%M:%S")
  return str(date_time)

 return "I dont understand you boy"
