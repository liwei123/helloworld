Summary:            A program that shows helloworld
Name:               helloworld
Version:            2.1.5
Release:            21%{?dist}
License:            GPLv2+
Source:             %{name}-%{version}.tar.gz
Group:              Development/Debuggers
URL:                https://limitless-savannah-32560.herokuapp.com

%description
THIS IS JUST supposed to show hello world.

%prep
%autosetup -n %{name}

%build
%configure
make %{?_smp_mflags}

%install
%make_install

install -m 755 -d %{buildroot}/%{_sbindir}
ln -s ../bin/eject %{buildroot}/%{_sbindir}

%find_lang %{name}

%files -f %{name}.lang
%doc README TODO COPYING ChangeLog
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*

%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
