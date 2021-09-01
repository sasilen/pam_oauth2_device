# pam_oauth2_device version
%define _version %{rel}
%define _repository %{repository}
%define _source %{location}
%define _lib /lib64
%{!?_version: %define _version master}
%{!?_repository: %define _repository https://github.com/ICS-MU/pam_oauth2_device}

%if "%{_version}" == "master"
%{!?_location: %define _location %{_repository}/archive/refs/heads/%{_version}.tar.gz}
%else
%{!?_location: %define _location %{_repository}/archive/v%{_version}.tar.gz}
%endif


Name:    pamoauth2device
Version: %{_version}
Release: 1%{?dist}
Summary: PAM module for OAuth 2.0 Device flow
License: Apache-2.0
URL:     https://github.com/ICS-MU/pam_oauth2_device
Source0: %{_location}
#Source0: https://github.com/jsurkont/pam_oauth2_device/archive/refs/tags/v0.1.1.tar.gz


# List of build-time dependencies:
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libcurl-devel
BuildRequires: openldap-devel
BuildRequires: pam-devel


# List of runtime dependencies:
Requires: curl
Requires: openldap-clients


%description
PAM module that allows authentication against external OpenID Connect
identity provider using OAuth 2.0 Device Flow.

%global debug_package %{nil}

%prep
%setup -q -n pam_oauth2_device-%{_version}


%build
make


%install
mkdir -p ${RPM_BUILD_ROOT}%{_lib}/security
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/pam_oauth2_device
install pam_oauth2_device.so ${RPM_BUILD_ROOT}%{_lib}/security
cp config_template.json ${RPM_BUILD_ROOT}%{_sysconfdir}/pam_oauth2_device/config.json


%check
# no test.


%files
%doc LICENSE README.md
%{_lib}/security/pam_oauth2_device.so
%{_sysconfdir}/pam_oauth2_device/config.json


%changelog
* Thu Aug 26 2021 Sami Silén <sami.silen@csc.fi> - 0.1.2-1
- Changed sources to point current master repository

* Thu Nov 21 2019 Jaroslaw Surkont <jaroslaw.surkont@unibas.ch> - 0.1.1-1
- Add username_attribute to config (#7)
- Add client authentication to device endpoint (#6)

* Fri Aug 09 2019 Jaroslaw Surkont <jaroslaw.surkont@unibas.ch> - 0.1.0-1
- first build for pamoauth2device.
