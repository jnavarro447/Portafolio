import docker
import time
import requests

#
# Los diferentes estados que puede tener un contenedor:
# Created -> Cuando recien se crea un contenedor, se asigna este estado. No usa CPU o memoria.
# Running -> El proceso esta corriendo en entorno aislado dentro del contenedor.
# Restarting -> Estan reiniciando los procesos.
# Exited -> Cuando los procesos dentro del contenedor terminan. No se usa CPU ni memoria.
# Paused -> Procesos estan suspendidos por tiempo indefinido. Consume la misma memoria que corriendo, en CPU se libera.
# Dead -> Contenedor no es funcional. Cuando eliminamos contenedor y algunos recursos estan en uso por proceso externo.
#

# Variables globales
client = docker.from_env()
container_id = "a98a1351fda8"
container = None


def create_container():
    container_obj = client.containers.run("internship-api-project",
                                          detach=True,
                                          name="fastAPIProject",
                                          ports={'8000/tcp': ('0.0.0.0', 8000)},
                                          )
    global container_id
    container_id = container_obj.id


def run_container(container):
    container.start()


def unpause_container(container):
    container.unpause()


def main():
    while True:
        global container

        try:
            container = client.containers.get(container_id)
        except requests.exceptions.HTTPError:
            print("No se encontro contenedor, creando un nuevo contenedor...")
            create_container()
        except docker.errors.NotFound:
            print("ID no identificado, creando nuevo contenedor")
            create_container()
        except docker.errors.APIError:
            print("ID no identificado, creando nuevo contenedor pin")
            create_container()

        container_status = container.status
        print(container_status)

        if container_status != "running":
            if container_status == "paused":
                print("Contenedor en paused")
                unpause_container(container)
            elif container_status == "created" or container_status == "exited":
                print("Contenedor just to run")
                run_container(container)
            elif container_status == "restarting":
                print("Procesos en contenedor reiniciando")
                # time.sleep(2.0)
            elif container_status == "dead":
                print("Contenedor ha sido eliminado. \nCreando nuevo contenedor...")
                container = None
                create_container()
        time.sleep(3)


main()
