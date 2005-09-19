%bcond_with	tests
Summary:	Bazaar-NG is a changeset oriented revision control system
Name:		bzr
Version:	0.0.7
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://www.bazaar-ng.org/pkg/%{name}-%{version}.tar.gz
# Source0-md5:	e4d95bd7f6cdd9eb5bd1a62ec2a45db2
URL:		http://bazaar.canonical.com/Bzr
Requires:	diffutils
Requires:	patch
Requires:	tar
%pyrequires_eq  python
BuildRequires:	python
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
