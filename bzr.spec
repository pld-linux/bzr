Summary:	Bazaar - a distributed revision control system
Summary(pl.UTF-8):	Bazaar - rozproszony system kontroli wersji
Name:		bzr
Version:	2.2.1
Release:	2
License:	GPL v2
Group:		Development/Version Control
Source0:	http://launchpad.net/bzr/2.2/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	8a6abd8f888fb3e0845e2044d41a24bc
# from https://bugs.launchpad.net/bzr/+bug/612096
Patch0:		py27.patch
URL:		http://bazaar.canonical.com/
BuildRequires:	python >= 1:2.4
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	zlib-devel
%pyrequires_eq  python
Requires:	python-cElementTree
# pdb module required by bzr
Requires:	python-devel-tools
Requires:	python-paramiko
Requires:	python-pycurl
Obsoletes:	bazaar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bazaar (aka bzr) is a community project led by Canonical Limited to
develop a free software distributed revision control system that is
powerful, friendly, scalable and easy to use. Although Bazaar is a
distributed version control system it can also be used in a
centralized manner using lock step development and checkouts. Features
include:
- file and directory renames
- merging file renames
- versioning symbolic links
- knit merges instead of three-way merges
- gpg revision signing
- build-in high-speed web interface
- tags
- easy to learn normal file-system commands
- extensive Unicode support

Additional features like: cherry picking, other DVCS support, GUI and
many more are accessible from 3rd-party-tools and plugins.

%description -l pl.UTF-8
Bazaar (znany też jako bzr) to publiczny projekt mający na celu
stworzenie wolnodostępnego rozproszonego systemu kontroli wersji
będącego potężnym, przyjaznym, skalowalnym i łatwym w użyciu. Pomimo,
że Bazaar jest zaprojektowany do pracy w rozproszonym środowisku, może
być również używany w scentralizowanym modelu. Do głównych możliwości
należą:
- obsługa zmian nazw dla katalogów i plików
- scalanie pomiędzy plikami ze zmienioną nazwą
- obsługa dowiązań symbolicznych
- zaawansowane zespalanie zamiast tradycyjnego trójdrożnego
- podpisywanie rewizji przez gpg
- wbudowany wysokowydajny interfejs sieciowy
- tagi
- łatwy w użyciu interfejs linii poleceń
- szeroka obsługa Unikodu

Dodatkowe możliwości takie jak: cherry picking, obsługa innych
systemów kontroli wersji, GUI są dostępne poprzez dodatkowe pakiety
rozszerzeń.

%prep
%setup -q
%patch0 -p0

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--install-data %{_datadir} \
	--root=$RPM_BUILD_ROOT

%py_postclean

# don't package tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/bash_completion/tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/launchpad/test_*.py*
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/netrc_credential_store/tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/news_merge/tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/util/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt NEWS README TODO
%attr(755,root,root) %{_bindir}/bzr
%{_mandir}/man1/bzr.1*
%{py_sitedir}/bzrlib
%if "%{py_ver}" > "2.4"
%{py_sitedir}/*.egg-info
%endif
