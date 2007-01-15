Summary:	RAW-image converter written in GTK+
Summary(pl):	Konwerter obrazów RAW napisany w GTK+
Name:		rawstudio
Version:	0.4.1
%define	_svnrev		1055
%define	_snapday	20070116
Release:	1.%{_svnrev}.%{_snapday}.0.1
License:	GPL v2+
Group:		X11/Applications/Graphics
# Original source:
#Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
# SVN snapshot:
#Source0:	http://www.blues.gda.pl/SOURCES/%{name}-%{version}-svn%{_svnrev}.tar.bz2
Source0:	http://rawstudio.org/files/daily/%{name}-%{_snapday}-%{_svnrev}.tar.bz2
# Source0-md5:	ef59999054b3e1547d4eb3f8f4bd8518
Patch0:		%{name}-DESTDIR.patch
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
Rawstudio is an open source raw-image converter written in GTK+.

%description -l pl
Rawstudio to maj±cy otwarte ¼ród³a konwerter obrazów RAW napisany w
GTK+.

%prep
%setup -q -n %{name}

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
%{_pixmapsdir}/%{name}.png
