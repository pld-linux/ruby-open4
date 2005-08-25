%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
Summary:	Ruby open3 with exit reporting
Name:		ruby-open4
Version:	0.1.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.codeforpeople.com/lib/ruby/open4/open4-%{version}.tgz
# Source0-md5:	aab7035d09a19af38a7468d7f1cb93c9
URL:		http://www.codeforpeople.com/lib/ruby/open4/
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	setup.rb
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby open3 with exit reporting.

%prep
%setup -q  -n open4-%{version}

%build
cp /usr/share/setup.rb .
ruby setup.rb config \
  --rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

rdoc --ri -o ri
rdoc -o rdoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}
install -d $RPM_BUILD_ROOT%{ruby_ridir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_ridir}/*
%{ruby_rubylibdir}/open4*
