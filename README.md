This web application allows users to check the current weather for any city by entering the city name in a search box.
Upon submitting the form, it fetches weather data from OpenWeather API, displaying the temperature and weather description. 
If the city is invalid or an error occurs, it provides an error message. It's a simple, user-friendly interface for accessing weather information.

dont forget to change directory to your api folder

1 install FastAPI and Uvicorn and dependencies for html templates and fetch openweather api using terminal
"pip install fastapi uvicorn"
"pip install fastapi uvicorn jinja2 requests"

2 ready the project structure

3 run uvicorn main:app --reload or python -m uvicorn main:app

4 open http://127.0.0.1:8000

push the API to the GitHub
(you must first install git)

go to cmd or terminal and write

1.
echo "# prac" >> README.md
git init
git add README.md

git add .

2.
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Jordibot-art/prac.git
git push -u origin main


to pull(members only not owner of the GitHub rep)

1. Fork it and copy https and go to the terminal

copy only exist on GitHub so we pull it to become our local
2. git clone (https), and then change directory into the project eg 

cd Test-Repo

3. git checkout -b new_branch

4. code index.html

5. git add .

6. git commit -m "Update Print Statement"

7. git status

8. git push origin new_branch

10. go to pull request tab
then new pull request next
merge branch in the right





