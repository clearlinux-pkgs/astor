#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astor
Version  : 0.8.1
Release  : 37
URL      : https://files.pythonhosted.org/packages/5a/21/75b771132fee241dfe601d39ade629548a9626d1d39f333fde31bc46febe/astor-0.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/21/75b771132fee241dfe601d39ade629548a9626d1d39f333fde31bc46febe/astor-0.8.1.tar.gz
Summary  : Read/rewrite/write Python ASTs
Group    : Development/Tools
License  : BSD-3-Clause
Requires: astor-license = %{version}-%{release}
Requires: astor-python = %{version}-%{release}
Requires: astor-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
astor -- AST observe/rewrite
        =============================

%package license
Summary: license components for the astor package.
Group: Default

%description license
license components for the astor package.


%package python
Summary: python components for the astor package.
Group: Default
Requires: astor-python3 = %{version}-%{release}

%description python
python components for the astor package.


%package python3
Summary: python3 components for the astor package.
Group: Default
Requires: python3-core
Provides: pypi(astor)

%description python3
python3 components for the astor package.


%prep
%setup -q -n astor-0.8.1
cd %{_builddir}/astor-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603387359
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/astor
cp %{_builddir}/astor-0.8.1/LICENSE %{buildroot}/usr/share/package-licenses/astor/1664a4cbae596c411a3f8a61f3c1e73058afb323
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/astor/1664a4cbae596c411a3f8a61f3c1e73058afb323

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
