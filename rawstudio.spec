Summary:	RAW-image converter written using GTK+
Summary(pl.UTF-8):	Konwerter obrazów RAW napisany z użyciem GTK+
Name:		rawstudio
Version:	0.6
%define	_svnrev		1486
%define	_snapday	20071029
%define	_rel		0.1
Release:	1.%{_svnrev}.%{_snapday}.%{_rel}
#Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
# Original source:
#Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
# SVN snapshot:
Source0:	http://rawstudio.org/files/daily/%{name}-%{_snapday}-%{_svnrev}.tar.bz2
# Source0-md5:	159c9dad900f2d3ac8f9c741bb15a2b4
Patch0:		%{name}-pl_desktop.patch
Patch1:		%{name}-rev1487-demosaic.patch
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
cd src
%patch1 -p0

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
