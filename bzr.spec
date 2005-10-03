Summary:	Bazaar-NG - a changeset oriented revision control system
Summary(pl):	Bazaar-NG - system kontroli wersji zorientowany na zestawy zmian
Name:		bzr
Version:	0.0.9
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://www.bazaar-ng.org/pkg/%{name}-%{version}.tar.gz
# Source0-md5:	e6b1e5e561556f29ac00ce00433c9077
URL:		http://www.bazaar-ng.org/
BuildRequires:	python
%pyrequires_eq  python
Requires:	diffutils
Requires:	patch
Requires:	tar
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

%description -l pl
Bazaar-NG (znany te¿ jako bzr, pó¼niej ma byæ nazwany Bazaar 2) to
publiczny projekt maj±cy na celu stworzenie wolnodostêpnego
rozproszonego systemu kontroli wersji bêd±cego potê¿nym, przyjaznym,
skalowalnym i ³atwym w u¿yciu. System kontroli wersji to narzêdzie
u¿ywane przez programistów i administratorów systemów do ¶ledzenia
zmian dokonywanych w plikach w ci±gu czasu. Ponadto system kontroli
wersji taki jak Bazaar-NG zmniejsza trudno¶ci wspólnej pracy w
zespo³ach.

Bazaar-NG to system zorientowany na zestawy zmian. Takie systemy
zbieraj± logicznie powi±zane zmiany w poszczególnych plikach w jedn±
zwart± grupê zwykle reprezentuj±c± poprawkê b³êdu lub now± w³a¶ciwo¶æ.
Te zestawy zmian s± ³atwo przesy³ane z jednej ga³êzi do innej poprzez
proste w u¿yciu polecenia takie jak "bzr pull" i "bzr branch".

Bazaar-NG jest tak¿e rozproszonym systemem kontroli wersji.
Rozproszony system taki jak Bazaar-NG nie tylko umo¿liwia istnienie w
projekcie wielu ga³êzi, ale tak¿e pozwala u¿ytkownikom na posiadanie
prywatnych ga³êzi. Bazaar-NG czyni ³atwym dla u¿ytkownika stworzenie
ga³êzi opartej na innej ga³êzi, dokonanie zmian i pó¼niejsze
po³±czenie tych ga³êzi. Co wa¿niejsze, ka¿dy mo¿e stworzyæ now± ga³±¼
w oparciu o dowoln± ga³±¼ projektu, poprawiæ jedn± lub wiêcej rzeczy i
zaoferowaæ swoj± ga³±¼ do w³±czenia z powrotem do g³ównego projektu.
Bazaar-NG obs³uguje tak¿e wspó³dzielenie ga³êzi miêdzy programistami.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt HACKING NEWS README TODO tutorial.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/bzrlib
