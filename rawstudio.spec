Summary:	RAW-image converter written in GTK+
Summary(pl.UTF-8):	Konwerter obrazów RAW napisany w GTK+
Name:		rawstudio
Version:	0.5.1
%define	_svnrev		1183
%define	_snapday	20070312
Release:	1.%{_svnrev}.%{_snapday}.1
#Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
# Original source:
#Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
# SVN snapshot:
Source0:	http://rawstudio.org/files/daily/%{name}-%{_snapday}-%{_svnrev}.tar.bz2
# Source0-md5:	2f0bfa06115628297f4d478fd0f1a270
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

%description -l pl.UTF-8
Rawstudio to mający otwarte źródła konwerter obrazów RAW napisany w
GTK+.

%prep
%setup -q -n %{name}
#setup -q

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
