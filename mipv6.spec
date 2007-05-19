Summary:	MIPL Mobile IPv6
Name:		mipv6
Version:	2.0.2
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.mobile-ipv6.org/software/download/%{name}-%{version}.tar.gz
# Source0-md5:	2cf58dca0ab3c38223e25dbecba8ed37
URL:		http://www.mobile-ipv6.org/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIPL Mobile IPv6 for Linux is an implementation of the Mobility
Support in IP version 6 (RFC 3775).

%prep
%setup -q

%build
%configure \
	--enable-vt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS INSTALL* NEWS README* THANKS
