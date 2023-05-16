# Todo List App With Flask

Learn Flask for Python - Full Tutorial from freecodecamp.org


[Video Tutorial](<https://www.youtube.com/watch?v=Z1RJmh_OqeA>)

[Source Code](<https://github.com/jakerieger/FlaskIntroduction>)

## Rodar o app local

1. Defina variável local: `$env:FLASK_APP ="todoapp.app"`
1. Rodar flask: `flask run`

## Rodar em container

1. Build the Image: `docker build . -t todoapp:latest`
2. Run the container: `docker run --name webapp --detach --publish 5000:5000  todoapp:latest`