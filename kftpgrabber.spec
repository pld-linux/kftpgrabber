Summary:	A graphical FTP client for KDE
Summary(pl):	Graficzny klient FTP dla KDE
Name:		kftpgrabber
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://kftpgrabber.sf.net/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	80d0f75a5b62ea05297bad67d859815b
URL:		http://kftpgrabber.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	howl-devel
BuildRequires:	kdelibs-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	qsa-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KFTPGrabber is a graphical FTP client for KDE. It provides a nice GUI
for all file transfer operations, it supports encrypted connections
(both SSL and SFTP), site-to-site (FXP) transfers and complete bookmark
system.

%description -l pl
KFTPGrabber jest graficznym klientem FTP dla KDE. Wyposa�ony jest w
mi�y dla oka GUI, wspiera szyfrowane po��czenia (SSL i SFTP),
site-to-site (FXP) oraz posiada zak�adki.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/%{name}
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*/*/*.png
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/*.desktop
