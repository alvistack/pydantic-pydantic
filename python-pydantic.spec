%global debug_package %{nil}

Name: python-pydantic
Epoch: 100
Version: 1.10.0
Release: 1%{?dist}
Summary: Data validation using Python type hinting
License: MIT
URL: https://github.com/pydantic/pydantic/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
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
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pydantic
Summary: Data validation using Python type hinting
Requires: python3
Requires: python3-typing-extensions >= 4.1.0
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
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pydantic
Summary: Data validation using Python type hinting
Requires: python3
Requires: python3-typing-extensions >= 4.1.0
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
%{python3_sitearch}/*
%endif

%changelog
