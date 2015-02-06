%define name chaplin
%define version 1.10 
%define release 10

Summary: A dvd chapter tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: http://archive.ubuntu.com/ubuntu/pool/multiverse/c/chaplin/chaplin_1.10-0.0.diff.gz
Patch1: chaplin-1.10-include.patch.bz2
License: GPL
Group: Video 
Url: http://www.lallafa.de/bp/chaplin.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libdvdread-devel

%description
The tool parses a DVD disc or image and extracts 
the exact duration for each chapter of a given title.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install chaplin $RPM_BUILD_ROOT/%{_bindir}
install chaplin-genmenu $RPM_BUILD_ROOT/%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/chaplin
%{_bindir}/chaplin-genmenu


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10-9mdv2011.0
+ Revision: 616995
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.10-8mdv2010.0
+ Revision: 424799
- rebuild

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 1.10-7mdv2009.0
+ Revision: 278240
- rebuild for new libdvdread

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.10-6mdv2009.0
+ Revision: 240519
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 07 2007 Erwan Velu <erwan@mandriva.org> 1.10-4mdv2008.0
+ Revision: 81708
- Rebuild
- Import chaplin



* Thu Jun 22 2006 Erwan Velu <erwan@seanodes.com> 1.10-3
- Rebuild

* Mon Mar 20 2006 Erwan Velu <erwan@seanodes.com> 1.10-2mdk
- mkrel
- Using debian patch
- Fixing includes

* Fri Feb  4 2005 Erwan Velu <erwan@seanodes.com> 1.10-1mdk
- First MDK release 
