Summary:	GStreamer streaming media editor and GUI tools
Name:		gst-editor
Version:	0.5.0
Release:	1
License:	LGPL
Group:		Applications/Multimedia
Source0:	http://dl.sf.net/gstreamer/%{name}-%{version}.tar.gz
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	gstreamer-devel >= 0.6.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	scrollkeeper
Requires:	libxml2 >= 2.0.0
Requires:	libgnomeui >= 2.0.0
Requires:	gstreamer >= 0.6.0
Requires:	libglade2 >= 2.0.0
Requires:	scrollkeeper >= 0.3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains gst-editor and a few graphical tools. gst-editor
is a development tool for graphically creating applications based on
GStreamer. gst-launch-gui is an extension of gst-launch allowing you
to dynamically turn on logging domains. gst-inspect-gui is a graphical
element browser.

%package devel
Summary:	Development headers for the Editor
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package provides the necessary development libraries and include
files to allow you to embed the editor in other applications or call
upon its functionality.

%package static
Summary:	Static files for the Editor
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static files for gst-editor.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

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
%doc AUTHORS COPYING NEWS README ChangeLog INSTALL COPYING
%attr(755,root,root) %{_bindir}/gst-editor
%attr(755,root,root) %{_bindir}/gst-launch-gui
%attr(755,root,root) %{_bindir}/gst-inspect-gui
%{_libdir}/*.so.*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-%{version}
%{_libdir}/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
