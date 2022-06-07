# {cookiecutter.project_name} API

endpoints are in `doc/openapi.json`

## DEV

1. `source .alias`
2. If change in requirements; rebuild docker : `build_{cookiecutter.project_name}_api_dev`
3. Run docker : `run_{cookiecutter.project_name}_api_dev`
4. Accessible from http://0.0.0.0:10002

OR

1. If change in requirements; rebuild docker : `docker build -t {cookiecutter.project_name}_api -f Dockerfile.dev .`
2. Run docker : `docker run -it --rm --name bioinstory_api -p 10002:80 -v `pwd`/backend:/code/backend {cookiecutter.project_name}_api`
3. Accessible from http://0.0.0.0:10002

## Unitesting

`run_{cookiecutter.project_name}_api_dev pytest`
