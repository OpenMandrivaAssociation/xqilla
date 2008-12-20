%define tarbname XQilla

%define enable_debug 1
%{?_enable_debug: %{expand: %%global enable_debug 1}}

Name: xqilla
Version: 2.1.1
Release: %mkrel 4
Epoch: 1
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary: XQilla is an XQuery and XPath 2 library
URL: http://xqilla.sourceforge.net/HomePage
License:  Apache License v2
Source0: %tarbname-%version.tar.gz
Patch0: XQilla-2.1.1-lib64.patch
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
%{_libdir}/libxqilla.la
%{_includedir}/xqilla

%prep
%setup -q -n %tarbname-%version
%if "%_lib" != "lib"
%patch0 -p1
%endif

%build
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
rm -rf %buildroot
make DESTDIR=%buildroot install

%clean
rm -rf $RPM_BUILD_ROOT

