Summary:	FTP client for KDE
Name:		kftpgrabber
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://kftpgrabber.sourceforge.net/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	80d0f75a5b62ea05297bad67d859815b
URL:		http://kftpgrabber.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRequires:	howl-devel
BuildRequires:	qsa-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTP client for KDE.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_desktopdir} \
	Iconsdir=%{_pixmapsdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/%{name}
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*/*/*.png
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/*.desktop
