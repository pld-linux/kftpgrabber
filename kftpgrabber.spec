Summary:	A graphical FTP client for KDE
Summary(pl.UTF-8):	Graficzny klient FTP dla KDE
Name:		kftpgrabber
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.kftp.org/uploads/files/%{name}-%{version}.tar.bz2
# Source0-md5:	dbbbca5cd4303db886a2d8dac39dd98c
Patch0:         kde-ac260-lt.patch
URL:		http://www.kftp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-filesystem-devel
BuildRequires:	boost-regex-devel
BuildRequires:	howl-devel
BuildRequires:	kdelibs-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	qsa-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KFTPGrabber is a graphical FTP client for KDE. It provides a nice GUI
for all file transfer operations, it supports encrypted connections
(both SSL and SFTP), site-to-site (FXP) transfers and complete bookmark
system.

%description -l pl.UTF-8
KFTPGrabber jest graficznym klientem FTP dla KDE. Wyposażony jest w
miły dla oka GUI, obsługuje szyfrowane połączenia (SSL i SFTP),
przesyłanie site-to-site (FXP) oraz posiada zakładki.

%prep
%setup -q 
%patch0 -p1

%build
%{__aclocal} -I admin
%{__autoconf}
%configure \
	--with-extra-includes=%{_includedir}/qsa \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__sed} -i 's,^Categories.*,Categories=Qt;KDE;Network;FileTransfer;,' kftpgrabber/src/kftpgrabber.desktop

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_desktopdir} \
	Iconsdir=%{_pixmapsdir} \
	kde_htmldir=%{_kdedocdir}

# One header file, unnesesary in package.
rm $RPM_BUILD_ROOT%{_includedir}/kftpgrabber/*.h

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/%{name}
%{_datadir}/config.kcfg/*.kcfg
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/*.desktop
