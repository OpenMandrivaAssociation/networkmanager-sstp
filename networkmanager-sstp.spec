%define	url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_ld_no_undefined 1
%define	oname	sstp-client

%define major	0
%define libname %mklibname %{oname} %{major}
%define devname %mklibname %{oname} -d


Summary:	NetworkManager integration for sstp
Name:		networkmanager-sstp
Version:	1.0.9
Release:	1
License:	GPLv2+
Group:		System/Base
Url:		http://sourceforge.net/projects/%{oname}/
Source0:	http://downloads.sourceforge.net/project/%{oname}/%{oname}/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	ppp-devel
Requires:	gtk+3
Requires:	dbus
Requires:	NetworkManager
Requires:	shared-mime-info
Requires:	GConf2
Requires:	gnome-keyring
Requires:	%{libname} = %{EVRD}
Requires(post,postun): desktop-file-utils

%description
This package contains software for integrating the sstp software
with NetworkManager and the GNOME desktop

%package -n %{libname}
Summary:    Main library for %{name}
Group:      System/Libraries

%description -n %{libname}
This package contains software for integrating the sstp software
with NetworkManager and the GNOME desktop

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{name} = %{EVRD}

%description -n	%{devname}
This package contains the development files for %{name}.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-more-warnings=yes \
	--with-gtkver=3 \
	--with-tests=yes

%make

%install
%makeinstall_std

%files
%{_sbindir}/sstpc
%{_libdir}/pppd/2.4.5/sstp-pppd-plugin.so
%{_docdir}/%{oname}/*.example
%{_mandir}/man8/sstpc*

%files -n %{libname}
%{_libdir}/libsstp_api*.so

%files -n %{devname}
%{_libdir}/pkgconfig/%{oname}-1.0.pc
%{_includedir}/%{oname}/sstp-api.h
