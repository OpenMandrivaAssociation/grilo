%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

%define api	0.3
%define major	1
%define major_grlnet	0
%define major_grlpls	0
%define libname	%mklibname %{name} %{api} %{major}
%define libgrlnet	%mklibname grlnet %{api} %{major_grlnet}
%define libgrlpls	%mklibname grlpls %{api} %{major_grlpls}
%define girname %mklibname %{name}-gir %{api}
%define girgrlnet %mklibname grlnet-gir %{api}
%define girgrlpls %mklibname grlpls-gir %{api}
%define devname	%mklibname -d %{name}


Summary:	Content discovery framework
Name:		grilo
Version:	0.3.6
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://live.gnome.org/Grilo
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	vala-tools
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(totem-plparser)

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library and elements.

%package -n %{libname}
Summary:	Libraries files for Grilo framework
Group:		System/Libraries

%description -n %{libname}
This package contains the core library for %{name}.

%package -n %{libgrlnet}
Summary:	Libraries files for Grilo framework
Group:		System/Libraries

%description -n %{libgrlnet}
This package contains the grlnet library for %{name}.

%package -n %{libgrlpls}
Summary:        Libraries files for Grilo framework
Group:          System/Libraries

%description -n %{libgrlpls}
This package contains the grlnet library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{girgrlnet}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girgrlnet}
GObject Introspection interface description for %{name}.

%package -n %{girgrlpls}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries

%description -n %{girgrlpls}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Libraries/include files for Grilo framework
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgrlnet} = %{version}-%{release}
Requires:       %{libgrlpls} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Requires:	%{girgrlnet} = %{version}-%{release}
Requires:       %{girgrlpls} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.

This package contains the core library and elements, as well as
general and API documentation.

%prep
%setup -q
%apply_patches

%build
%configure \
	--enable-vala \
	--enable-gtk-doc \
	--enable-introspection \
	--enable-grl-net \
	--disable-tests \
	--enable-compile-warnings=no

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_libdir}/grilo-%{api} %{buildroot}%{_datadir}/grilo-%{api}/plugins

# Remove files that will not be packaged
rm -f %{buildroot}%{_bindir}/grilo-simple-playlist

%find_lang %{name} || touch %{name}.lang

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/grl-inspect-%{api}
%{_bindir}/grl-launch-%{api}
%{_bindir}/grilo-test-ui-%{api}
%{_libdir}/grilo-%{api}
%{_datadir}/grilo-%{api}/plugins
%{_mandir}/man1/grl-inspect-%{api}.1.*
%{_mandir}/man1/grl-launch-%{api}.1.*
%{_mandir}/man1/grilo-test-ui-%{api}.1.*

%files -n %{libname}
%{_libdir}/libgrilo-%{api}*

%files -n %{libgrlnet}
%{_libdir}/libgrlnet-%{api}.so.%{major_grlnet}*

%files -n %{libgrlpls}
%{_libdir}/libgrlpls-%{api}.so.%{major_grlnet}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Grl-%{api}.typelib

%files -n %{girgrlnet}
%{_libdir}/girepository-1.0/GrlNet-%{api}.typelib

%files -n %{girgrlpls}
%{_libdir}/girepository-1.0/GrlPls-%{api}.typelib

%files -n %{devname}
%doc AUTHORS COPYING NEWS README TODO
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}-%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*

