Summary:	Ruby open3 with exit reporting
Summary(pl.UTF-8):   open3 w Rubym z raportowaniem wyjścia
Name:		ruby-open4
Version:	0.1.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://www.codeforpeople.com/lib/ruby/open4/open4-%{version}.tgz
# Source0-md5:	aab7035d09a19af38a7468d7f1cb93c9
URL:		http://www.codeforpeople.com/lib/ruby/open4/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby open3 with exit reporting.

%description -l pl.UTF-8
open3 w Rubym z raportowaniem wyjścia.

%prep
%setup -q -n open4-%{version}
cp %{_datadir}/setup.rb .

%build
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
