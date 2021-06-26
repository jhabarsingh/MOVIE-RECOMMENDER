 **Backend EC2 Instance has been terminated so api's won't work**

**NOTES**
* [Video Link](https://youtu.be/elyK9-kDG7g)
* [Recommender API](https://github.com/jhabarsingh/MOVIE-RECOMMENDER#how-to-use-the-django-recommendation-api)

*To use the Recommender API that I have created in this project Click on this [Link](https://github.com/jhabarsingh/MOVIE-RECOMMENDER#how-to-use-the-django-recommendation-api)*

# [MOVIE-RECOMMENDER](http://movie-recommender-jhabar.000webhostapp.com/)  ⚡️ [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/jhabarsingh/MOVIE-RECOMMENDER/blob/main/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/jhabarsingh/MOVIE-RECOMMENDER)](https://github.com/jhabarsingh/MOVIE-RECOMMENDER/stargazers)  [![GitHub contributors](https://img.shields.io/github/contributors/jhabarsingh/MOVIE-RECOMMENDER.svg)](https://github.com/jhabarsingh/MOVIE-RECOMMENDER/graphs/contributors)  [![GitHub issues](https://img.shields.io/github/issues/jhabarsingh/MOVIE-RECOMMENDER.svg)](https://github.com/jhabarsingh/MOVIE-RECOMMENDER/issues) [![GitHub forks](https://img.shields.io/github/forks/jhabarsingh/MOVIE-RECOMMENDER.svg?style=social&label=Fork)](https://GitHub.com/jhabarsingh/MOVIE-RECOMMENDER/network/)


<br />

<p align="center">
  <img src="https://github.com/jhabarsingh/MOVIE-RECOMMENDER/blob/main/docs/poster.png?raw=true" />
</p>
<details>
  <summary>:zap: TECH STACK</summary>
  <br/>
  <div style="display:flex;justify-content:space-around">
  <img  title="Django" src="https://icon-library.com/images/django-icon/django-icon-0.jpg" width="50px" height="50px" style="margin-right:5px;" />
  <img titlt="Vuejs"   src="https://vuejs.org/images/logo.png" width="50px" height="50px"  style="margin-right:5px;"/>
  <img  title="Vuex" src="https://s3.amazonaws.com/coursetro/posts/144-full.png"  height="50px" style="margin-right:5px;"     />
  <img  title="Vuetify" src="https://cdn.worldvectorlogo.com/logos/vuetify.svg" height="50px"  style="margin-right:5px;"/>
    <img  title="Sk-learn" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" height="50px" style="margin-right:5px;" />
  
  <img  title="Docker" src="https://pbs.twimg.com/profile_images/1273307847103635465/lfVWBmiW_400x400.png" height="50px" style="margin-right:5px;" />

</div>
</details>

<details>
  <summary>:zap: AWS SERVICES</summary>
  <br/>
  <div style="display:flex;justify-content:space-around">
    <img  title="AWS EC2" src="https://i0.wp.com/www.sndkcorp.com/wp-content/uploads/2019/09/amazon-ec2.png?fit=360%2C230&ssl=1" height="70px" style="margin-right:5px;" />
</details>

<br />

## Apis Used To Fetch Movie Details

<img  title="TMDB" src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg" height="50px" style="margin-right:5px;" />
  
<br />

# About
  [MOVIE-RECOMMENDER](http://movie-recommender-jhabar.000webhostapp.com/) is a Web app built using **Django** and **Vuejs**. The **Machine Learning Algorithm** used to implement recommender system is **Cosine similarity**. To fetch the movie and it's cast detail **TMDB** Apis is used.

<br />

# How To Use The Django Recommendation Api?

![Django Apis](https://github.com/jhabarsingh/MOVIE-RECOMMENDER/blob/main/docs/api.png?raw=true)

### Javascript
  
```js
  let movieName = "Avatar"; // Name of movie
  let URL = "http://ec2-3-142-140-94.us-east-2.compute.amazonaws.com:8000/recommender/";
  let options = {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "text": movieName
      })
  }
  
  fetch(URL, options)
  .then(res => res.json())
  .then(movies => console.log(movies)) // Array of all recommender Movies
  .catch(err => console.log(err.response))
  


```

  
### Python
```python

import requests
import json
movieName = "Avatar"
URL = "http://ec2-3-142-140-94.us-east-2.compute.amazonaws.com:8000/recommender/"


headers = {
	'Content-Type': 'application/json'
}
data = json.dumps({
	'text': movieName
})
response = requests.post(URL, data=data, headers=headers)
data = json.loads(response.text)
print(data)



```

<br />
	
# [Cosine Similarity](https://www.geeksforgeeks.org/cosine-similarity/)
> The recommender system calculates the cosine similarity beween the different movies and lesser the angle ‘θ’ greated is the similarity.
	
<p align="center">
	<img src="https://github.com/jhabarsingh/MOVIE-RECOMMENDER/blob/main/docs/cosine_similarity.png?raw=true" />
</p>
	
*To know more about the **Cosine Similarity** Read this [Blog](https://www.geeksforgeeks.org/cosine-similarity/)*
	
<br />
	
# [Django Backend Setup](http://ec2-3-142-140-94.us-east-2.compute.amazonaws.com:8000/recommender/)

### Using venv
```bash
git clone https://github.com/jhabarsingh/MOVIE-RECOMMENDER.git 
cd MOVIE-RECOMMENDER
python3 -m venv env # Python 3.6.9 or 3.7.0 version 
source env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver
```

### Using conda
```bash
git clone https://github.com/jhabarsingh/MOVIE-RECOMMENDER.git 
cd MOVIE-RECOMMENDER
conda create -n hatespeech python==3.7 
conda activate hatespeech
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver
```

### Using Docker

```bash
sudo apt-get install docker docker-compose # Install docker, docker-compose on linux
git clone https://github.com/jhabarsingh/MOVIE-RECOMMENDER.git
cd MOVIE-RECOMMENDER
sudo docker-compose up
```

## Vuejs Setup

[Install node](https://nodejs.org/en/download/) |
[Install vue/cli](https://cli.vuejs.org/)
```bash
 git clone https://github.com/jhabarsingh/MOVIE-RECOMMENDER.git
 cd MOVIE-RECOMMENDER
 npm install   # Nodejs should be installed
 npm run start # Vuejs should be installed
 ```

<br />
	
# [Want To Contribute](https://medium.com/mindsdb/contributing-to-an-open-source-project-how-to-get-started-6ba812301738)
### You can contribute to this project in many ways
 1. You can create an issue if you find any bug.
 2. You can work on an existing issue and Send PR.
 3. You can make changes in the design if it is needed.
 4. Even if you find any grammatical or spelling mistakes then also you can create an issue.

> *I would be glad to see a notification saying `User {xyz} created a Pull Request`.
I promise to review it.*
