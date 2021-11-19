from starlette.routing import Route
from controllers import containers, images

api_routes = [
    Route('/images', images.getAll, name="getAll", methods=["GET"]),
    Route('/images/{image_id:str}', images.getById, name="getById", methods=["GET"]),
    Route('/images/{image_id:str}', images.deleteById, name="deleteById", methods=["DELETE"]),
    Route('/images', images.deleteAll, name="deleteAll", methods=["DELETE"]),    
    Route('/images', images.pull, name="pull", methods=["POST"]),    

    Route('/containers', containers.getAll, name="getAll", methods=["GET"]),
    Route('/containers/{container_id:str}', containers.getById, name="getById", methods=["GET"]),
    Route('/containers/{container_id:str}', containers.deleteById, name="deleteById", methods=["DELETE"]),
    Route('/containers', containers.deleteAll, name="deleteAll", methods=["DELETE"]),    
    Route('/containers', containers.run, name="run", methods=["POST"]),
]