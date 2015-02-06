%define tarbname XQilla

%define enable_debug 1
%{?_enable_debug: %{expand: %%global enable_debug 1}}

Name: xqilla
Version: 2.3.0
Release: 2
Epoch: 1
Group: System/Libraries
Summary: XQilla is an XQuery and XPath 2 library
URL: http://xqilla.sourceforge.net/HomePage
License:  Apache License v2
Source0: http://downloads.sourceforge.net/project/xqilla/xqilla/%{version}/%{tarbname}-%{version}.tar.gz
BuildRequires: xerces-c-devel >= 2.8.0
BuildRequires: libicu-devel 

%description
XQilla is an XQuery and XPath 2 library.

%files
%defattr(0755,root,root)
%{_bindir}/*

#------------------------------------------------------------------------

%define libxqilla %mklibname xqilla 4
%define libxqilla_devel %mklibname xqilla -d

%package -n %{libxqilla}
Summary: XQilla is an XQuery and XPath 2 library
Group: System/Libraries

%description  -n %{libxqilla}
XQilla is an XQuery and XPath 2 library.

%files -n  %{libxqilla}
%defattr(0755,root,root)
%{_libdir}/libxqilla.so.*

#------------------------------------------------------------------------

%package -n %{libxqilla_devel}
Summary: Xqilla devel library
Group: Development/Databases
Provides: libxqilla-devel = %epoch:%version
Provides: xqilla-devel = %epoch:%version
Requires: %libxqilla = %epoch:%version-%release

%description  -n %{libxqilla_devel}
Xqilla devel library

%files -n  %{libxqilla_devel}
%defattr(0755,root,root)
%{_libdir}/libxqilla.so
%{_includedir}/xqilla
%{_includedir}/xqc.h

%prep
%setup -q -n %tarbname-%version

%build
autoreconf -fi
CPPFLAGS="-DPIC -fPIC" 
export CPPFLAGS

%configure \
	--with-xerces=%_prefix \
%if %{enable_debug}
	--enable-debug \
%endif
	--disable-static

%make

%install
make DESTDIR=%buildroot install
