Summary:	RAW-image converter written in GTK+
Name:		rawstudio
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
# Source0-md5:	09844b550fbfd35f02623a549d5b4c33
Patch0:		%{name}-DESTDIR.patch
URL:		http://rawstudio.org/
BuildRequires:	lcms-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rawstudio is an open source raw-image converter written in GTK+.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	distdir=$RPM_BUILD_ROOT/%{_datadir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
