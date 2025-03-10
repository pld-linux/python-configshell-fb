#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define module	configshell
Summary:	ConfigShell - Python 2 library for building configuration shells
Summary(pl.UTF-8):	ConfigShell - biblioteka Pythona 2 do tworzenia powłok konfiguracyjnych
Name:		python-configshell-fb
Version:	1.1.fb25
Release:	8
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://github.com/open-iscsi/configshell-fb/releases
Source0:	https://github.com/open-iscsi/configshell-fb/archive/v%{version}/configshell-fb-%{version}.tar.gz
# Source0-md5:	e4d5394815712f661c04917a429f3e06
URL:		https://github.com/open-iscsi/configshell-fb
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with python2}
BuildRequires:	python-modules >= 1:2.4
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.4
Requires:	python-pyparsing
Requires:	python-urwid
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
configshell-fb is a Python library that provides a framework for
building simple but nice CLI-based applications.

%description -l pl.UTF-8
configshell-fb to biblioteka Pythona udostępniająca szkielet do
tworzenia prostych, ale ładnych aplikacji opartych na linii poleceń.

%package -n python3-configshell-fb
Summary:	ConfigShell - Python 3 library for building configuration shells
Summary(pl.UTF-8):	ConfigShell - biblioteka Pythona 3 do tworzenia powłok konfiguracyjnych
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-pyparsing
Requires:	python3-urwid

%description -n python3-configshell-fb
configshell-fb is a Python library that provides a framework for
building simple but nice CLI-based applications.

%description -n python3-configshell-fb -l pl.UTF-8
configshell-fb to biblioteka Pythona udostępniająca szkielet do
tworzenia prostych, ale ładnych aplikacji opartych na linii poleceń.

%prep
%setup -q -n configshell-fb-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/myshell
%endif
%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-configshell-fb-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-configshell-fb-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python3},' $RPM_BUILD_ROOT%{_examplesdir}/python3-configshell-fb-%{version}/myshell
sed -i '1s|^#!.*python\b|#!%{__python3}|' $RPM_BUILD_ROOT%{_examplesdir}/python3-configshell-fb-%{version}/*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/configshell
%{py_sitescriptdir}/configshell_fb
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/configshell_fb-*-py*.egg-info
%endif
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/myshell
%endif

%if %{with python3}
%files -n python3-configshell-fb
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/configshell
%{py3_sitescriptdir}/configshell_fb
%{py3_sitescriptdir}/configshell_fb-*-py*.egg-info
%dir %{_examplesdir}/python3-configshell-fb-%{version}
%attr(755,root,root) %{_examplesdir}/python3-configshell-fb-%{version}/myshell
%endif
