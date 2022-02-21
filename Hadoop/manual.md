Минимальные технические требования:
- RAM: > 2 Gb;
- CPUs: > 1 2.1MHz;
- Разрядность - 64-bit version.
- Свободного дисковое пространство > 15 Gb.
Программные требования:
- Docker-compose (2 and later);
- Docker;

!!! ALL COMMANDS must be executed from context where docker-compose files are situated !!!


## To build images locally and start, run theese commands

```
docker-compose -f docker-compose_build.yaml && docker-compose -f docker-compose_build.yaml up -d
```

### to stop them

```
docker-compose -f docker-compose_build.yaml down
```

## To download images and start containers, run this command

```
docker-compose up -d
```

### to stop them

```
docker-compose down
```

## to see containers

run \<docker ps\>  and u will see containers "hadoop-headnode", "hadoop-worker"

## how do volumes work ?
Docker volumes was used and to see them run \<docker volume ls\>, u will se 

```
DRIVER    VOLUME NAME
local     hadoop_headnode_data_mount1
local     hadoop_headnode_data_mount2
local     hadoop_worker_data_mount1
local     hadoop_worker_data_mount2
```
u can also took at network due to executing \<docker network ls\>

```
NETWORK ID     NAME                DRIVER    SCOPE
190aa59d54e6   bridge              bridge    local
f122a8ad9c3b   hadoop_hadoop-net   bridge    local
d35e4214a15f   host                host      local
9ec3a298772d   none                null      local
```

## Here is one env - "$HEADNODE_HOST", which must be set in both containers and should be equel headnode service name.

## to see wed-pages open http://localhost:9870/  and  http://localhost:1000/ in Browser
