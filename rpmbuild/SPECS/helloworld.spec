%define _topdir /Users/chenliwei/RubymineProjects/helloworld/rpmbuild
%define _tmppath /Users/chenliwei/RubymineProjects/helloworld/rpmbuild/tmp
%define name helloworld
%define version 1.1
%define release static
%define arch amd64

Name: %{name}
Version: %{version}
Release: %{release}
Summary: helloworld
Group: Applications
License: GPLv3+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-%{arch}
Source0: %{name}-%{version}-%{release}-%{arch}.tar.gz

%description
THIS IS JUST supposed to show hello world.

%prep
%setup

%build

%install
%make_install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -d %{buildroot}%{_bindir}
ln -s ../bin/helloworld %{buildroot}%{_bindir}


%files
%{_bindir}/*

%clean
rm -rf %{buildroot}