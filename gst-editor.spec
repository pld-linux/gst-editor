Summary:	GStreamer streaming media editor and GUI tools
Summary(pl):	GStreamer - edytor strumieni medialnych i narzędzia GUI
Name:		gst-editor
Version:	0.5.0
Release:	2
License:	LGPL
Group:		Applications/Multimedia
Source0:	http://dl.sf.net/gstreamer/%{name}-%{version}.tar.gz
# Source0-md5:	53bc099fd0cdc2007cd61f6145ab03e1
Patch0:		%{name}-desktop.patch
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	gstreamer-devel >= 0.6.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	scrollkeeper
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires:	gstreamer >= 0.6.0
Requires:	libglade2 >= 2.0.0
Requires:	libgnomeui >= 2.3.3.1-2
Requires:	libxml2 >= 2.0.0
Requires:	scrollkeeper >= 0.3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains gst-editor and a few graphical tools. gst-editor
is a development tool for graphically creating applications based on
GStreamer. gst-launch-gui is an extension of gst-launch allowing you
to dynamically turn on logging domains. gst-inspect-gui is a graphical
element browser.

%description -l pl
Ten pakiet zawiera gst-editor oraz kilka narzędzi graficznych.
gst-editor to narzędzie programistyczne do graficznego tworzenia
aplikacji opartych na GStreamerze. gst-launch-gui to rozszerzenie
gst-launch pozwalające dynamicznie włączać domeny logowania.
gst-inspect-gui to graficzna przeglądarka elementów.

%package devel
Summary:	Development headers for the Editor
Summary(pl):	Pliki nagłówkowe edytora
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package provides the necessary development include files to allow
you to embed the editor in other applications or call upon its
functionality.

%description devel -l pl
Ten pakiet dostarcza plików nagłówkowych pozwalających na osadzanie
edytora w innych aplikacjach lub wywoływania jego funkcjonalności.

%package static
Summary:	Static files for the Editor
Summary(pl):	Statyczne biblioteki edytora
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static files for gst-editor.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki gst-editora.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
scrollkeeper-update -q

%postun
/sbin/ldconfig
scrollkeeper-update -q

%files
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
