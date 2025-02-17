FROM centos:7

ARG RELEASE="master"
ENV RELEASE=${RELEASE}
ARG REPOSITORY="https://github.com/ICS-MU/pam_oauth2_device"
ENV REPOSITORY=${REPOSITORY}

RUN yum install -y centos-release-scl scl-utils --nogpgcheck
RUN yum update -y
RUN yum install -y devtoolset-7-gcc* --nogpgcheck

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
 && if [ "${RELEASE}" = "master" ] ; then \
      export SOURCE=${REPOSITORY}/archive/refs/heads/${RELEASE}.tar.gz; \
    else \
      export SOURCE=${REPOSITORY}/archive/v${RELEASE}.tar.gz; \
    fi \
 && curl -L -O $SOURCE; echo "Used: $SOURCE"; 


COPY --chown=builder:builder pamoauth2device.spec .

RUN scl enable devtoolset-7 -- rpmbuild -ba --define "version ${RELEASE}" --define "repository ${REPOSITORY}" pamoauth2device.spec
