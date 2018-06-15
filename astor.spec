#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astor
Version  : 0.6.2
Release  : 9
URL      : https://pypi.python.org/packages/d8/be/c4276b3199ec3feee2a88bc64810fbea8f26d961e0a4cd9c68387a9f35de/astor-0.6.2.tar.gz
Source0  : https://pypi.python.org/packages/d8/be/c4276b3199ec3feee2a88bc64810fbea8f26d961e0a4cd9c68387a9f35de/astor-0.6.2.tar.gz
Summary  : Read/rewrite/write Python ASTs
Group    : Development/Tools
License  : BSD-3-Clause
Requires: astor-python3
Requires: astor-license
Requires: astor-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

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
Requires: astor-python3

%description python
python components for the astor package.


%package python3
Summary: python3 components for the astor package.
Group: Default
Requires: python3-core

%description python3
python3 components for the astor package.


%prep
%setup -q -n astor-0.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529090943
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/astor
cp LICENSE %{buildroot}/usr/share/doc/astor/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/astor/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
