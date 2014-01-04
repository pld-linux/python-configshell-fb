#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define module	configshell
Summary:	A Python library for building configuration shells
Name:		python-configshell-fb
Version:	1.1.fb10
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://codeload.github.com/agrover/configshell-fb/tar.gz/v%{version}
# Source0-md5:	72e152e33785bd975cc3848653d1f0bd
URL:		https://github.com/agrover/configshell-fb
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
# remove BR: python-devel for 'noarch' packages.
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
Requires:	python-modules
Requires:	python-pyparsing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
configshell-fb is a Python library that provides a framework for
building simple but nice CLI-based applications.

%package -n python3-configshell-fb
Summary:	A Python library for building configuration shells
Group:		Libraries/Python
Requires:	python3-pyparsing

%description -n python3-configshell-fb
configshell-fb is a Python library that provides a framework for
building simple but nice CLI-based applications.

%prep
%setup -q -n configshell-fb-%{version}

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
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
%endif
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/myshell

%if %{with python3}
%files -n python3-configshell-fb
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/configshell_fb-*-py*.egg-info
%endif
%dir %{_examplesdir}/python3-configshell-fb-%{version}
%attr(755,root,root) %{_examplesdir}/python3-configshell-fb-%{version}/myshell