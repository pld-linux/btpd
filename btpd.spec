Summary:	Bittorent client
Name:		btpd
Version:	0.13
Release:	0.1
License:	BSD-like
Group:		Applications
Source0:	http://www.murmeldjur.se/btpd/%{name}-%{version}.tar.gz
# Source0-md5:	0d9c4a672eea6f298fa6e44d94da1657
URL:		http://www.murmeldjur.se/btpd/
Patch0:		%{name}-asneeded.patch
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
btpd is a bittorrent client consisting of a daemon and client commands,
which can be used to read and/or manipulate the daemon state. The daemon
is capable of running several torrents simultaneously and only uses one
tcp port. It's fairly low on resource usage and should be perfect for
file distribution sites. Efficient downloads and ease of use makes this
client a good choice for the casual user as well.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
