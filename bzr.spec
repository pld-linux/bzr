Summary:	Bazaar - a distributed revision control system
Summary(pl.UTF-8):	Bazaar - rozproszony system kontroli wersji
Name:		bzr
Version:	2.6.0
Release:	2
License:	GPL v2+
Group:		Development/Version Control
# https://launchpad.net/bzr/2.6/2.6.0/+download/bzr-2.6.0.tar.gz
Source0:	http://launchpad.net/bzr/2.6/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	28c86653d0df10d202c6b842deb0ea35
Patch0:		locale-path.patch
Patch1:		ca-certificates.patch
URL:		http://bazaar.canonical.com/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	zlib-devel
Requires:	python
Requires:	python-cElementTree
# pdb module required by bzr
Requires:	python-devel-tools
Requires:	python-paramiko
Requires:	python-pycurl
Obsoletes:	bazaar
Conflicts:	qbzr < 0.22
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

%package -n bash-completion-%{name}
Summary:	bash-completion for bzr
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-%{name}
This package provides bash-completion for bzr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# move out of contrib, as we package contrib as doc
mv contrib/bash/bzr bash_completion.sh

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--install-data %{_datadir} \
	--root=$RPM_BUILD_ROOT

%py_postclean

# bash-completion
install -d $RPM_BUILD_ROOT/etc/bash_completion.d
install -p bash_completion.sh $RPM_BUILD_ROOT/etc/bash_completion.d/%{name}

# Use independently packaged python-elementtree instead
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/util/elementtree

# don't package tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/bash_completion/tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/launchpad/test_*.py*
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/netrc_credential_store/tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/news_merge/tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/tests
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/util/tests

# sco locale is not supported by glibc
rm -rf $RPM_BUILD_ROOT%{_localedir}/sco

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*.txt NEWS README TODO contrib
%attr(755,root,root) %{_bindir}/bzr
%{_mandir}/man1/bzr.1*
%dir %{py_sitedir}/bzrlib
%{py_sitedir}/bzrlib/*.py[co]
%attr(755,root,root) %{py_sitedir}/bzrlib/_*.so
%{py_sitedir}/bzrlib/bundle
%{py_sitedir}/bzrlib/branchfmt
%{py_sitedir}/bzrlib/doc
%{py_sitedir}/bzrlib/doc_generate
%{py_sitedir}/bzrlib/export
%{py_sitedir}/bzrlib/filters
%{py_sitedir}/bzrlib/help_topics
%{py_sitedir}/bzrlib/plugins
%{py_sitedir}/bzrlib/repofmt
%{py_sitedir}/bzrlib/smart
%{py_sitedir}/bzrlib/store
%{py_sitedir}/bzrlib/transport
%{py_sitedir}/bzrlib/ui
%{py_sitedir}/bzrlib/util
%{py_sitedir}/bzrlib/version_info_formats
%{py_sitedir}/*.egg-info

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
/etc/bash_completion.d/%{name}
