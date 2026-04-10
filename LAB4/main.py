from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()
@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}

@app.get("/greet")
def greet(name:str="Student"):
    return {"greeting": f"Hello, {name}!"}
#html
@app.get("/html", response_class=HTMLResponse)
def html_page():
    return """
    <html>
     <head>
       <title>Simple Page</title>
     </head>
     <body>
       <h1 style="color:purple;"> Hello from FastAPI!</h1>
       <p> This is a simple HTML page. </p>
       <a href="https://www.instagram.com/">Link to Instagram</a>
     </body>
    </html>
    """
movies=[
    {"title":"The Notebook","year":2004},
    {"title":"Interstellar","year":2014},
    {"title":"The Dark Knight","year":2008}
]

@app.get("/movies")
def get_movies():
    return {"movies": movies}

@app.get("/movies/filter")
def filter_movies(year:int=2004):
    filtered=[m for m in movies if m["year"]>=year]
    return {"filtered_movies": filtered}