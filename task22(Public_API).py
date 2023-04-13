# 1.What is meant by stateless nature in RestAPI?
# Stateless: REST APIs are stateless, meaning that 
# calls can be made independently of one another, 
# and each call contains all of the data necessary 
# to complete itself successfully.

# 2. 403, 503, 301 Status Codes?
# 403: status code indicates that the server understands the request but refuses to authorize it.
# 503: The HTTP 503 Service Unavailable server error response code indicates that the server is 
# temporarily not ready to handle the request.
# 301: ndicates that the resource requested has been permanently moved to the URL given by the Location header. 
# And all the future requests should use the new URL.

# 3.USE public API and use all http methods on it.

# 1st we use GET Method.
import requests
import json
var1_url = "https://dog.ceo/api/breeds/image/random"
response=requests.get(var1_url)
print (response.json())

# 2nd we use POST Method.
var_url = "https://dog.ceo/api/breeds/image/random"
data = {"Breed":"German" ,"Age":"7 months" , "color" :"brown"}
print(type(data))
response=requests.post(var_url,json=data)
print(response)
print (response.json())

# 3rd we use PUT Method (for Update the data)
data = {"age": "9 months","color" :"white"}
response = requests.put(var_url , json = data)
print(type(var_url))
print(response)
print(response.json())

# 4th we use PATCH Method
breed = {"Breed" :"pug"}
response = requests.patch(var_url , json = data)
print(type(var_url))
print(response)
print(response.json())

# 5th we use DELETE Method
response = requests.delete(var_url)
print(response)
print(response.json())