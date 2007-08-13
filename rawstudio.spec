Summary:	RAW-image converter written using GTK+
Summary(pl.UTF-8):	Konwerter obrazów RAW napisany z użyciem GTK+
Name:		rawstudio
Version:	0.5.1
%define	_svnrev		1352
%define	_snapday	20070813
%define	_rel		1
Release:	1.%{_svnrev}.%{_snapday}.%{_rel}
License:	GPL v2+
Group:		X11/Applications/Graphics
# Original source:
#Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
# SVN snapshot:
Source0:	http://rawstudio.org/files/daily/%{name}-%{_snapday}-%{_svnrev}.tar.bz2
# Source0-md5:	6e0d630f90311397ada70b502716580c
Patch0:		%{name}-pl_desktop.patch
Patch1:		%{name}-no_gettext_h.patch
URL:		http://rawstudio.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libxml2-devel >= 2.4
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rawstudio is an open source raw-image converter written using GTK+ library.

%description -l pl.UTF-8
Rawstudio to mający otwarte źródła konwerter obrazów RAW napisany z użyciem
biblioteki GTK+.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}/*.png
