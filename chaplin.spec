%define name chaplin
%define version 1.10 
%define release %mkrel 3

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
