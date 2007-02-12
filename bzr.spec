Summary:	Bazaar-NG - a changeset oriented revision control system
Summary(pl.UTF-8):   Bazaar-NG - system kontroli wersji zorientowany na zestawy zmian
Name:		bzr
Version:	0.14
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://bazaar-vcs.org/releases/src/%{name}-%{version}.tar.gz
# Source0-md5:	281c777f377cc149b6ba60c720f70033
Patch0:		%{name}-FHS.patch
URL:		http://bazaar-vcs.org/
BuildRequires:	python >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
Requires:	python-Crypto
Requires:	python-cElementTree
Requires:	python-pycurl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bazaar-NG (aka bzr, later to be named Bazaar 2) is a community project
led by canonical to develop a free software distributed revision
control system that is powerful, friendly, scalable and easy to use. A
revision control system is a tool that developers and system
administrators use to keep track of the changes to files over time.
Additionally, a revision control system such as Bazaar-NG eases the
burdens of working together in teams.

Bazaar-NG is a changeset oriented revision control system. Changeset
oriented revision control systems collect the logically related
changes to individual files together into one cohesive group which
typically represent a bug fix or a new feature. These changesets are
easily transferred from one branch to another with simple to use
commands like "bzr pull" and "bzr branch".

Bazaar-NG is also a distributed revision control system. A distributed
revision control such as Bazaar-NG not only allows a project to have
multiple branches, but users to have multiple private branches as
well. Bazaar-NG makes it easy for users to make a branch that is based
off of another branch, make changes and then later merge the branches
back together. Importantly, the general public can make a new branch
based upon an authoritive branch of a project, fix one or more things
and then offer the branch back to the upstream for merging. Bazaar-NG
also supports the sharing of branches between developers.

%description -l pl.UTF-8
Bazaar-NG (znany też jako bzr, później ma być nazwany Bazaar 2) to
publiczny projekt mający na celu stworzenie wolnodostępnego
rozproszonego systemu kontroli wersji będącego potężnym, przyjaznym,
skalowalnym i łatwym w użyciu. System kontroli wersji to narzędzie
używane przez programistów i administratorów systemów do śledzenia
zmian dokonywanych w plikach w ciągu czasu. Ponadto system kontroli
wersji taki jak Bazaar-NG zmniejsza trudności wspólnej pracy w
zespołach.

Bazaar-NG to system zorientowany na zestawy zmian. Takie systemy
zbierają logicznie powiązane zmiany w poszczególnych plikach w jedną
zwartą grupę zwykle reprezentującą poprawkę błędu lub nową właściwość.
Te zestawy zmian są łatwo przesyłane z jednej gałęzi do innej poprzez
proste w użyciu polecenia takie jak "bzr pull" i "bzr branch".

Bazaar-NG jest także rozproszonym systemem kontroli wersji.
Rozproszony system taki jak Bazaar-NG nie tylko umożliwia istnienie w
projekcie wielu gałęzi, ale także pozwala użytkownikom na posiadanie
prywatnych gałęzi. Bazaar-NG czyni łatwym dla użytkownika stworzenie
gałęzi opartej na innej gałęzi, dokonanie zmian i późniejsze
połączenie tych gałęzi. Co ważniejsze, każdy może stworzyć nową gałąź
w oparciu o dowolną gałąź projektu, poprawić jedną lub więcej rzeczy i
zaoferować swoją gałąź do włączenia z powrotem do głównego projektu.
Bazaar-NG obsługuje także współdzielenie gałęzi między programistami.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt HACKING NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/bzr.1*
%{py_sitescriptdir}/bzrlib
