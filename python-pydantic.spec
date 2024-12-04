# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pydantic
Epoch: 100
Version: 2.10.3
Release: 1%{?dist}
BuildArch: noarch
Summary: Data validation using Python type hinting
License: MIT
URL: https://github.com/pydantic/pydantic/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Data validation and settings management using python type hinting.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pydantic
Summary: Data validation using Python type hinting
Requires: python3
Requires: python3-annotated-types >= 0.6.0
Requires: python3-pydantic-core >= 2.27.1
Requires: python3-typing-extensions >= 4.12.2
Provides: python3-pydantic = %{epoch}:%{version}-%{release}
Provides: python3dist(pydantic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pydantic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pydantic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pydantic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pydantic) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pydantic
Data validation and settings management using python type hinting.

%files -n python%{python3_version_nodots}-pydantic
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pydantic
Summary: Data validation using Python type hinting
Requires: python3
Requires: python3-annotated-types >= 0.6.0
Requires: python3-pydantic-core >= 2.27.1
Requires: python3-typing-extensions >= 4.12.2
Provides: python3-pydantic = %{epoch}:%{version}-%{release}
Provides: python3dist(pydantic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pydantic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pydantic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pydantic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pydantic) = %{epoch}:%{version}-%{release}

%description -n python3-pydantic
Data validation and settings management using python type hinting.

%files -n python3-pydantic
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
