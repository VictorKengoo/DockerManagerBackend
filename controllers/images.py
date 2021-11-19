import docker
from starlette.responses import JSONResponse
from config import settings
import docker

DOCKER_CLIENT = docker.DockerClient(base_url="http://{}:{}".format(settings.DOCKER_HOST_IP, settings.DOCKER_HOST_PORT))


def getById(req):
    imageId = req.path_params['image_id']
    output = []

    try:
        image = DOCKER_CLIENT.images.get(imageId)
    except Exception as e :
        print("Error getting image {0} ".format(e))
        return JSONResponse(output, status_code=200)


    name, tag = image.attrs["RepoTags"][0].split(":")
    output.append(
        {
            "ShortId": image.short_id.split(":")[1],
            "Tag": tag,
            "Name": name,
            "CreatedAt": image.attrs["Created"].split(".")[0]
        }
    )    
    return JSONResponse(output, status_code=200)

def getAll(req):
    images = None
    output = []

    try:
        images = DOCKER_CLIENT.images.list()
    except Exception as e :
        print("Error listing all images {0} ".format(e))
        return JSONResponse(output, status_code=200)

    print("Images: {0}".format(images))
    for image in images:
        try:
            name, tag = image.attrs["RepoTags"][0].split(":")
            output.append(
                {
                    "ShortId": image.short_id.split(":")[1],
                    "Tag": tag,
                    "Name": name,
                    "CreatedAt": image.attrs["Created"].split(".")[0]
                }
            )
        except :
            print("Error reading image {0}".format(image))
        
    
    return JSONResponse(output, status_code=200)

async def pull(req):
    image = None
    output = []

    try:
        inputData = await req.json()        
    except:
        print("Body is null")
        return JSONResponse(output, status_code=200)
    
    try:
        tag = inputData["tag"] if 'tag' in inputData else 'latest'
        image = DOCKER_CLIENT.images.pull(inputData["name"], tag=tag)
    except Exception as e:
        print("Error pulling image {0} . Exception: {1}".format(inputData["name"], e))
        return JSONResponse({"Error": "Error not known: {0}".format(e.args[0].response.content)}, status_code=500)   
    
    if image != None:
        name, tag = image.attrs["RepoTags"][0].split(":")
        output.append(
            {
                "ShortId": image.short_id.split(":")[1],
                "Tag": tag,
                "Name": name,
                "CreatedAt": image.attrs["Created"].split(".")[0]
            }
        )

    return JSONResponse(output, status_code=200)

def deleteById(req):
    imageId = req.path_params['image_id']
    try:
        DOCKER_CLIENT.images.remove(imageId)
    except Exception as e :
        print("Error deleting image {0} . Exception: {1}".format(imageId, e))
        if "No such image:" in str(e.args[0].response.content):
            return JSONResponse({"Error":"No such images as {0}".format(imageId)}, status_code=404)  
        else:
            return JSONResponse({"Error": "Error not known: {0}".format(e.args[0].response.content)}, status_code=500)          
    
    return JSONResponse(status_code=204)

def deleteAll(req):
    images = DOCKER_CLIENT.images.list()
    output = []
    for image in images:
        name_tag = image.attrs["RepoTags"][0]
        print("Deleting image: {0}".format(name_tag))
        DOCKER_CLIENT.images.remove(image.short_id.split(":")[1])
        output.append(name_tag)

    return JSONResponse({"Deleted":output}, status_code=200)
        