# Packaging pam_oauth2_device

## Building a deb package

(Tested on Ubuntu 18.04)

1. Update package metadata in the `debian` directory. Specifically, update the
   `changelog` file. Update pam_oauth2_device version in `deb/build.sh` and
   `deb/Dockerfile`.
2. Follow the commands in `deb/build.sh` script to build the package.
   Alternatively, build the package in a docker container `deb/build.sh`
   (signing is currently not supported).

```bash
docker build -t pamoauth2device-deb-build .
docker run --rm -v ${PWD}:/data pamoauth2device-deb-build bash -c 'cp *.deb /data'
```
