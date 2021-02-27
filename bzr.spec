# TODO: python3 when supported upstream (currently it uses cobjects, whith don't exist in python 3.2+)

Summary:	Bazaar - a distributed revision control system
Summary(pl.UTF-8):	Bazaar - rozproszony system kontroli wersji
Name:		bzr
Version:	2.7.0
Release:	1
License:	GPL v2+
Group:		Development/Version Control
#Source0Download: https://launchpad.net/bzr/+download
Source0:	https://launchpad.net/bzr/2.7/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	8e5020502efd54f5925a14a456b88b89
Patch0:		locale-path.patch
Patch1:		ca-certificates.patch
URL:		http://bazaar.canonical.com/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	zlib-devel
Requires:	python >= 1:2.6
Requires:	python-bzr = %{version}-%{release}
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

%package -n python-bzr
Summary:	Bazaar library for Python 2
Summary(pl.UTF-8):	Biblioteka Bazaar dla Pythona 2
Group:		Libraries/Python
# pdb module required by bzr
Requires:	python-devel-tools >= 1:2.6
Requires:	python-paramiko
Requires:	python-pycurl

%description -n python-bzr
Bazaar is a friendly distributed version control system.

This package contains Python 2 library.

%description -n python-bzr -l pl.UTF-8
Bazaar to przyjazny, rozproszony system kontroli wersji.

Ten pakiet zawiera bibliotekę Pythona 2.

%package -n bash-completion-%{name}
Summary:	bash-completion for bzr
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion
BuildArch:	noarch

%description -n bash-completion-%{name}
This package provides bash-completion for bzr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# move out of contrib, as we package contrib as doc
%{__mv} contrib/bash/bzr bash_completion.sh

%build
%py_build

%if 0
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if 0
%py3_install \
	--install-data %{_datadir}
%endif

%py_install \
	--install-data %{_datadir}

%py_postclean

# bash-completion
install -d $RPM_BUILD_ROOT/etc/bash_completion.d
install -p bash_completion.sh $RPM_BUILD_ROOT/etc/bash_completion.d/%{name}

# don't package tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/bash_completion/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/launchpad/test_*.py*
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/netrc_credential_store/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/plugins/news_merge/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/util/tests

%if 0
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/bzrlib/plugins/bash_completion/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/bzrlib/plugins/launchpad/test_*.py*
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/bzrlib/plugins/netrc_credential_store/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/bzrlib/plugins/news_merge/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/bzrlib/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/bzrlib/util/tests
%endif

# sco locale is not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sco

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*.txt NEWS README TODO contrib
%attr(755,root,root) %{_bindir}/bzr
%{_mandir}/man1/bzr.1*

%files -n python-bzr
%defattr(644,root,root,755)
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
%{py_sitedir}/bzr-%{version}-py*.egg-info

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
/etc/bash_completion.d/%{name}
