#FROM opensuse/leap:15.0
FROM suse/sle15:latest

ARG RELEASE="master"
ENV RELEASE=${RELEASE}
ARG REPOSITORY="https://github.com/ICS-MU/pam_oauth2_device"
ENV REPOSITORY=${REPOSITORY}

RUN zypper install -y \
    gcc \
    gcc-c++ \
    libcurl-devel \
    curl \
    make \
    openldap2-devel \
    pam-devel \
    rpm-build \
 && zypper clean -a

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
 && curl -L -O $SOURCE; echo "Used: $SOURCE"; 


COPY --chown=builder:builder pamoauth2device.spec .

RUN rpmbuild -ba --define "version ${RELEASE}" --define "repository ${REPOSITORY}" pamoauth2device.spec
