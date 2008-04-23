Summary:	RAW-image converter written using GTK+
Summary(pl.UTF-8):	Konwerter obrazów RAW napisany z użyciem GTK+
Name:		rawstudio
Version:	1.0
# Keep it for future snapshots because releases are not-so-frequent:
%define	_svnrev		1624
%define	_snapday	20080130
%define	_rel		3
#Release:	1.%{_svnrev}.%{_snapday}.%{_rel}
Release:	%{_rel}
License:	GPL v2+
Group:		X11/Applications/Graphics
# SVN snapshot:
#Source0:	http://rawstudio.org/files/daily/%{name}-%{_snapday}-%{_svnrev}.tar.bz2
# Original source:
Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
# Source0-md5:	26ddd38ccb5d74f7c7c6759dae13b7ad
Patch0:		%{name}-cz_locale.patch
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
Rawstudio is an open source raw-image converter written using GTK+
library.

%description -l pl.UTF-8
Rawstudio to mający otwarte źródła konwerter obrazów RAW napisany z
użyciem biblioteki GTK+.

%prep
%setup -q
%patch0 -p1

cd po
mv cz.po cs.po
mv cz.gmo cs.gmo

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.png
%{_iconsdir}/%{name}.png
%{_datadir}/%{name}
