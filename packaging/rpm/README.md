# Packaging pam_oauth2_device

## Building a rpm package

By default docker builds RPM from the 'https://github.com/ICS-MU/pam_oauth2_device' master branch. This behaviour can be overwritten by docker build-args, this is not yet needed by ICS-MU repository because the lack of releases.

1. Build up RPM (select version and repository if needed)
2. In the `rpm` directory, build the container and extract the rpm file.


```bash
# ICS-MU master
docker build -t pamoauth2device-rpm-build .

# Other Repo and other tag
docker build -t pamoauth2device-rpm-build --build-arg REPOSITORY="https://github.com/jsurkont/pam_oauth2_device" --build-arg RELEASE="0.1.1" .

# Optain RPMs from the package
docker run --rm -v ${PWD}:/data pamoauth2device-rpm-build cp -r 'rpmbuild/RPMS /data'
```
