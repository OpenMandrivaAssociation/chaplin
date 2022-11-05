Summary:	A dvd chapter tool
Name:		chaplin
Version:	1.10
Release:	11
License:	GPL
Group:		Video
Url:		http://www.lallafa.de/bp/chaplin.html
Source0:	https://www.lallafa.de/bp/files/%{name}-%{version}.tgz
Patch0:		chaplin-1.10-include.patch
Patch1:		chaplin-1.10-Makefile.patch
#Patch0:		http://archive.ubuntu.com/ubuntu/pool/multiverse/c/chaplin/chaplin_1.10-0.0.diff.gz
#Patch0:		http://archive.ubuntu.com/ubuntu/pool/multiverse/c/chaplin/chaplin_1.10-0.2ubuntu6.diff.gz
BuildRequires:	pkgconfig(dvdread)

%description
The tool parses a DVD disc or image and extracts 
the exact duration for each chapter of a given title.

%files
%{_bindir}/chaplin
%{_bindir}/chaplin-genmenu

#--------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}

# remove binary
rm -f %{name}

%build
%before_configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install chaplin $RPM_BUILD_ROOT/%{_bindir}
install chaplin-genmenu $RPM_BUILD_ROOT/%{_bindir}

