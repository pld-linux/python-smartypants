#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python fork of SmartyPants
Summary(pl.UTF-8):	Pythonowa wersja SmartyPants
Name:		python-smartypants
Version:	2.0.1
Release:	6
License:	BSD
Group:		Libraries/Python
##Source0Download: https://pypi.org/simple/smartypants/
#Source0:	https://files.pythonhosted.org/packages/source/s/smartypants/smartypants-%{version}.tar.gz
# 2.0.1 missing on pypi, so...
#Source0Download: https://github.com/leohemsted/smartypants.py/releases
Source0:	https://github.com/leohemsted/smartypants.py/archive/v%{version}/smartypants.py-%{version}.tar.gz
# Source0-md5:	27957540f4718e892039b2ed208c78f3
URL:		https://pypi.org/project/smartypants/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
smartypants is a Python fork of SmartyPants. It can turn:
- straight or backticks quotes into HTML quote entities
- dashes into en- and em-dash entities
- three consecutive dots into an ellipsis entity

%description -l pl.UTF-8
smartypants to pythonowa wersja SmartyPants. Potrafi zamieniać:
- proste lub odwrotne cudzysłowy na encje cudzysłowów HTML
- kreski na encje pauzy i półpauzy
- trzy kropki na encję wielokropka

%package -n python3-smartypants
Summary:	Python fork of SmartyPants
Summary(pl.UTF-8):	Pythonowa wersja SmartyPants
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-smartypants
smartypants is a Python fork of SmartyPants. It can turn:
- straight or backticks quotes into HTML quote entities
- dashes into en- and em-dash entities
- three consecutive dots into an ellipsis entity

%description -n python3-smartypants -l pl.UTF-8
smartypants to pythonowa wersja SmartyPants. Potrafi zamieniać:
- proste lub odwrotne cudzysłowy na encje cudzysłowów HTML
- kreski na encje pauzy i półpauzy
- trzy kropki na encję wielokropka

%package apidocs
Summary:	API documentation for Python smartypants module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona smartypants
Group:		Documentation

%description apidocs
API documentation for Python smartypants module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona smartypants.

%prep
%setup -q -n smartypants.py-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/smartypants{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/smartypants{,-3}
ln -sf smartypants-3 $RPM_BUILD_ROOT%{_bindir}/smartypants
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYING README.rst
%attr(755,root,root) %{_bindir}/smartypants-2
%{py_sitescriptdir}/smartypants.py[co]
%{py_sitescriptdir}/smartypants-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-smartypants
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/smartypants
%attr(755,root,root) %{_bindir}/smartypants-3
%{py3_sitescriptdir}/smartypants.py
%{py3_sitescriptdir}/__pycache__/smartypants.cpython-*.py[co]
%{py3_sitescriptdir}/smartypants-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
