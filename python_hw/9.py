import docker
import termcolor
from docker.errors import APIError

client = docker.from_env()

def get_stopped_containers():
    print ("\033[31mThere are some stopped containers\n")
    for container in client.containers.list(all=True, filters={"status":["exited","exited","paused","restarting"]}):
       string = container.name + '---' + container.short_id + '---' + container.status
       string = string.replace('-', termcolor.colored('-', 'red'))
       print (f'{string}\n')
    print ('===' * 20)


def get_all_containers():
    for container in client.containers.list(all=True):
       string = container.name + '---' + container.short_id + '---' + container.status
       string = string.replace('-', termcolor.colored('-', 'green'))
       print (f'{string}')
    print ('===' * 20)

def get_all_images():
    for image in client.images.list():
        string = f' {image.tag}, \n' + '---' *2  +image.short_id
        string = string.replace('-', termcolor.colored('-', 'green'))
        print (f'{string}\n')
    print ('===' * 20)

def main():
    get_stopped_containers()
    get_all_containers()
    get_all_images()
    
docker_client = docker.APIClient(base_url='unix://var/run/docker.sock')
def get_containers(filter=None):
    """return a list of all container, or return a list that matches the filter"""
    for container in docker_client.containers(all=True):
        container_info = docker_client.inspect_container(container['Id'])
        print (container_info)
        if filter is None or filter in container_info['Name']:
            yield container
print ([c.get('Id') for c in get_containers()])
        

if __name__ == '__main__':
    	 main()  
