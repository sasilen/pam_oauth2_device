FROM centos:8

#ARG RELEASE="0.1.1"
ARG RELEASE="master"
ENV RELEASE=${RELEASE}
#ENV REPOSITORY="https://github.com/ICS-MU/pam_oauth2_device"
ENV REPOSITORY="https://github.com/jsurkont/pam_oauth2_device"

# RUN echo ${REPOSITORY}

#RUN dnf group install "Development Tools" -y

RUN yum install -y \
    gcc \
    gcc-c++ \
    libcurl-devel \
    make \
    openldap-devel \
    pam-devel \
    rpm-build \
 && yum clean all

RUN groupadd builder \
 && useradd --create-home --gid builder builder

USER builder

WORKDIR /home/builder

RUN mkdir -p rpmbuild/SOURCES \
 && cd rpmbuild/SOURCES \
 && if [ "${RELEASE}" = "master" ]; then \
      export SOURCE=${REPOSITORY}/archive/refs/heads/${RELEASE}.tar.gz; \
    else \
      export SOURCE=${REPOSITORY}/archive/v${RELEASE}.tar.gz; \
    fi \
 && curl -L -O $SOURCE; echo $SOURCE; 


COPY --chown=builder:builder pamoauth2device.spec .

RUN rpmbuild -ba --define "version ${RELEASE}" --define "repository ${REPOSITORY}" pamoauth2device.spec
