# Flask Tutorial in Visual Studio Code

Neste repo foi criado um app usando flask com hello world no / e rota para /hello/\<name> que retorna o nome passado como parametro.

[Tutorial Flask do VSCode](<https://code.visualstudio.com/docs/python/tutorial-flask>)

[Source Readme](.\tutorial-flask.md)

## Rodar o app local

1. Defina variável local: `$env:FLASK_APP ="hello_app.webapp"`
1. Rodar flask: `flask run`

## Rodar em container

1. Build the Image: `docker build . -t vscode101:latest`
2. Run the container: `docker run --name webapp --detach --publish 5000:5000  vscode101:latest`