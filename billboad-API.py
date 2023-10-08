
import streamlit as st
import requests

url = "https://billboard-api2.p.rapidapi.com/hot-100"

querystring = {"date":"2019-05-11","range":"1-10"}

headers = {
	"X-RapidAPI-Key": "c5ba79aa11mshdfde9f60a584633p1a7415jsn49495e531674",
	"X-RapidAPI-Host": "billboard-api2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())