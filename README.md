# containers

To build a container:
```
docker build -t <container_tag> <what to build>
docker build -t ferriolcalvet/bgreference .
```

To test that it works:
```
docker run <container_tag> <command>
docker run ferriolcalvet/bgreference ls /bgdatacache/datasets/genomereference
```

To push it to Docker Hub:
```
docker push <container_tag>
docker push ferriolcalvet/bgreference
```


To pull it in the form of singularity image:
```
singularity pull --name <container_image_name> <link_to_container>
singularity pull --name docker.io-ferriolcalvet-bgreference.img docker://docker.io/ferriolcalvet/bgreference
```


