%define api	0.2
%define major	1
%define libname	%mklibname %{name} %{api} %{major}
%define libgrlnet	%mklibname grlnet %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define girgrlnet %mklibname grlnet-gir %{api}
%define develname	%mklibname -d %{name}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Content discovery framework
Name:		grilo
Version:	0.2.3
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

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{girgrlnet}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libgrlnet} = %{version}-%{release}

%description -n %{girgrlnet}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Libraries/include files for Grilo framework
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgrlnet} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.

This package contains the core library and elements, as well as
general and API documentation.

%prep
%setup -q
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--enable-vala \
	--enable-gtk-doc \
	--enable-introspection \
	--enable-grl-net \
	--disable-tests

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_libdir}/grilo-%{api} %{buildroot}%{_datadir}/grilo-%{api}/plugins

# Remove files that will not be packaged
rm -f %{buildroot}%{_bindir}/grilo-simple-playlist

%files
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/grl-inspect*
%{_bindir}/grilo-test-ui*
%{_libdir}/grilo-%{api}
%{_datadir}/grilo-%{api}/plugins
%{_mandir}/man1/grl-inspect.1.*

%files -n %{libname}
%{_libdir}/libgrilo-%{api}.so.%{major}*

%files -n %{libgrlnet}
%{_libdir}/libgrlnet-%{api}.so.*

%files -n %{girname}
%{_libdir}/girepository-1.0/Grl-%{api}.typelib

%files -n %{girgrlnet}
%{_libdir}/girepository-1.0/GrlNet-%{api}.typelib

%files -n %{develname}
%doc AUTHORS COPYING NEWS README TODO
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}-%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*



%changelog
* Tue Nov 13 2012 Arkady L. Shane <ashejn@rosalab.ru> 0.2.3-1
- update to 0.2.3

* Thu Oct  3 2012 Arkady L. Shane <ashejn@rosalab.ru> 0.2.0-1
- update to 0.2.0

* Mon Mar 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.1.18-1
+ Revision: 784298
- imported package grilo

