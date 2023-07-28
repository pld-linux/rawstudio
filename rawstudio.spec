Summary:	RAW-image converter written using GTK+
Summary(pl.UTF-8):	Konwerter obrazów RAW napisany z użyciem GTK+
Name:		rawstudio
Version:	2.0
Release:	16
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	https://rawstudio.org/files/release/%{name}-%{version}.tar.gz
# Source0-md5:	b2f86b8ca6b83ad954e3104c4cb89e9b
Patch0:		%{name}-libpng15.patch
Patch1:		am.patch
Patch2:		lensfun.patch
Patch3:		exiv2-version.patch
Patch4:		%{name}-exiv2.patch
Patch5:		%{name}-extern-c.patch
Patch6:		%{name}-link.patch
URL:		https://rawstudio.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	exiv2-devel
BuildRequires:	fftw3-single-devel >= 3
BuildRequires:	flickcurl-devel
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	lcms-devel
BuildRequires:	lensfun-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 2.4
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	xorg-lib-libX11-devel
Requires:	gtk+2 >= 2:2.8.0
Requires:	libxml2 >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rawstudio is an open source raw-image converter written using GTK+
library.

%description -l pl.UTF-8
Rawstudio to mający otwarte źródła konwerter obrazów RAW napisany z
użyciem biblioteki GTK+.

%package devel
Summary:	Header files for rawstudio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki rawstudio
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for rawstudio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki rawstudio.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export CXXFLAGS="%{rpmcxxflags} -Wno-narrowing"
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/librawstudio-%{version}.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/rawstudio
%attr(755,root,root) %{_libdir}/librawstudio-%{version}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librawstudio-%{version}.so.0
%{_datadir}/rawspeed
%{_datadir}/rawstudio
%{_desktopdir}/rawstudio.desktop
%{_iconsdir}/rawstudio.png
%{_pixmapsdir}/rawstudio

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librawstudio-%{version}.so
%{_includedir}/%{name}-%{version}
%{_pkgconfigdir}/%{name}-%{version}.pc
