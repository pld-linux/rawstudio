Summary:	RAW-image converter written in GTK+
Summary(pl):	Konwerter obraz�w RAW napisany w GTK+
Name:		rawstudio
Version:	0.4.1
%define	_snap	svn953
Release:	1.%{_snap}.1
License:	GPL v2+
Group:		X11/Applications/Graphics
#Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
Source0:	http://www.blues.gda.pl/SOURCES/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	b6826f3cb792ca222dfab3bbb2117609
Patch0:		%{name}-DESTDIR.patch
URL:		http://rawstudio.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libxml2-devel >= 2.4
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rawstudio is an open source raw-image converter written in GTK+.

%description -l pl
Rawstudio to maj�cy otwarte �r�d�a konwerter obraz�w RAW napisany w
GTK+.

%prep
%setup -q
#%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png