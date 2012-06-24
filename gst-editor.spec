Summary:	GStreamer streaming media editor and GUI tools
Summary(pl):	GStreamer - edytor strumieni medialnych i narz�dzia GUI
Name:		gst-editor
Version:	0.8.0
Release:	2
License:	LGPL
Group:		Applications/Multimedia
Source0:	http://gstreamer.freedesktop.org/src/gst-editor/%{name}-%{version}.tar.gz
# Source0-md5:	00e004ad68f9b90138b87ec729cb1607
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale-names.patch
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	gstreamer-devel >= 0.8.9
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires:	gstreamer >= 0.8.9
Requires:	libglade2 >= 1:2.5.1
Requires:	libgnomeui >= 2.10.0-2
Requires:	libxml2 >= 1:2.6.19
Requires:	scrollkeeper >= 0.3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains gst-editor and a few graphical tools. gst-editor
is a development tool for graphically creating applications based on
GStreamer. gst-launch-gui is an extension of gst-launch allowing you
to dynamically turn on logging domains. gst-inspect-gui is a graphical
element browser.

%description -l pl
Ten pakiet zawiera gst-editor oraz kilka narz�dzi graficznych.
gst-editor to narz�dzie programistyczne do graficznego tworzenia
aplikacji opartych na GStreamerze. gst-launch-gui to rozszerzenie
gst-launch pozwalaj�ce dynamicznie w��cza� domeny logowania.
gst-inspect-gui to graficzna przegl�darka element�w.

%package devel
Summary:	Development headers for the Editor
Summary(pl):	Pliki nag��wkowe edytora
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package provides the necessary development include files to allow
you to embed the editor in other applications or call upon its
functionality.

%description devel -l pl
Ten pakiet dostarcza plik�w nag��wkowych pozwalaj�cych na osadzanie
edytora w innych aplikacjach lub wywo�ywania jego funkcjonalno�ci.

%package static
Summary:	Static files for the Editor
Summary(pl):	Statyczne biblioteki edytora
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static files for gst-editor.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki gst-editora.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po

# AS_VERSION
head -n 79 aclocal.m4 > acinclude.m4
# AS_LIBTOOL
tail -n +1045 aclocal.m4 | head -n 61 >> acinclude.m4
# AS_AUTOTOOLS_ALTERNATE, GST_DEBUGINFO, AS_COMPILER_FLAG
tail -n +7184 aclocal.m4 | head -n 130 >> acinclude.m4
# AS_AC_EXPAND
tail -n +7374 aclocal.m4 | head -n 43 >> acinclude.m4

%build
%{__libtoolize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%scrollkeeper_update_post

%postun
/sbin/ldconfig
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gst-editor
%attr(755,root,root) %{_bindir}/gst-launch-gui
%attr(755,root,root) %{_bindir}/gst-inspect-gui
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
