Summary:	A graphical FTP client for KDE
Summary(pl):	Graficzny klient FTP dla KDE
Name:		kftpgrabber
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://kftpgrabber.sf.net/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	549d4575fc0240c3ef9f249a7587d902
URL:		http://kftpgrabber.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl
KFTPGrabber jest graficznym klientem FTP dla KDE. Wyposa¿ony jest w
mi³y dla oka GUI, obs³uguje szyfrowane po³±czenia (SSL i SFTP),
przesy³anie site-to-site (FXP) oraz posiada zak³adki.

%prep
%setup -q

%build
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
%{_libdir}/kde3/*.la
%{_datadir}/apps/%{name}
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/*.desktop
%{_includedir}/kftpgrabber/*.h
