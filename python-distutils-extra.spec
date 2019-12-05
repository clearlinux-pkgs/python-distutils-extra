#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD14EF15DAFE11347 (martin@piware.de)
#
Name     : python-distutils-extra
Version  : 2.39
Release  : 6
URL      : https://launchpad.net/python-distutils-extra/trunk/2.39/+download/python-distutils-extra-2.39.tar.gz
Source0  : https://launchpad.net/python-distutils-extra/trunk/2.39/+download/python-distutils-extra-2.39.tar.gz
Source99 : https://launchpad.net/python-distutils-extra/trunk/2.39/+download/python-distutils-extra-2.39.tar.gz.asc
Summary  : Enhancements to the Python build system
Group    : Development/Tools
License  : GPL-2.0
Requires: python-distutils-extra-license = %{version}-%{release}
Requires: python-distutils-extra-python = %{version}-%{release}
Requires: python-distutils-extra-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
python-distutils-extra can be used with python's distutils or the enhanced
setuptools.

%package license
Summary: license components for the python-distutils-extra package.
Group: Default

%description license
license components for the python-distutils-extra package.


%package python
Summary: python components for the python-distutils-extra package.
Group: Default
Requires: python-distutils-extra-python3 = %{version}-%{release}

%description python
python components for the python-distutils-extra package.


%package python3
Summary: python3 components for the python-distutils-extra package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-distutils-extra package.


%prep
%setup -q -n python-distutils-extra-2.39

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560911114
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-distutils-extra
cp LICENSE %{buildroot}/usr/share/package-licenses/python-distutils-extra/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-distutils-extra/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
