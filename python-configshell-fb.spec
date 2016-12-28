#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define module	configshell
Summary:	ConfigShell - Python 2 library for building configuration shells
Summary(pl.UTF-8):	ConfigShell - biblioteka Pythona 2 do tworzenia powłok konfiguracyjnych
Name:		python-configshell-fb
Version:	1.1.fb15
Release:	4
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://codeload.github.com/agrover/configshell-fb/tar.gz/v%{version}
# Source0-md5:	1b4c0ba08e45aa44b7bb8796229d4330
URL:		https://github.com/agrover/configshell-fb
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
Requires:	python-pyparsing
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
%endif
%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-configshell-fb-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-configshell-fb-%{version}
sed -i '1s|^#!.*python\b|#!%{__python3}|' $RPM_BUILD_ROOT%{_examplesdir}/python3-configshell-fb-%{version}/*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/configshell_fb-*.egg-info
%endif
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/myshell
%endif

%if %{with python3}
%files -n python3-configshell-fb
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/configshell_fb-*-py*.egg-info
%dir %{_examplesdir}/python3-configshell-fb-%{version}
%attr(755,root,root) %{_examplesdir}/python3-configshell-fb-%{version}/myshell
%endif
