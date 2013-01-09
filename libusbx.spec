%define api 1.0
%define major 0
%define libname %mklibname usbx %api %major
%define devellibname %mklibname -d usbx %api
%define devellibnamest %mklibname -d -s usbx %api

Summary:        Library for accessing USB devices
Name:           libusbx
Version:        1.0.14
Release:        2
Source0:        http://downloads.sourceforge.net/libusbx/libusbx-%{version}.tar.bz2
License:        LGPLv2+
Group:          System/Libraries
URL:            http://sourceforge.net/apps/mediawiki/libusbx/
BuildRequires:  doxygen
Provides:       libusbx1 = %{version}-%{release}
Provides:       libusbx = %{version}-%{release}
Provides:       libusb1 = %{version}-%{release}
Obsoletes:      libusb1 <= 1.0.9

%description
This package provides a way for applications to access USB devices.

Libusbx is a fork of the original libusb, which is a fully API and ABI
compatible drop in for the libusb-1.0.9 release. The libusbx fork was
started by most of the libusb-1.0 developers, after the original libusb
project did not produce a new release for over 18 months.

Note that this library is not compatible with the original libusb-0.1 series,
if you need libusb-0.1 compatibility install the libusb package.

%package -n %libname
Summary: Libusbx is a fork of the original libusb
Group:  System/Libraries

%description -n %libname
Libusbx is a fork of the original libusb, which is a fully API and ABI
compatible drop in for the libusb-1.0.9 release. The libusbx fork was
started by most of the libusb-1.0 developers, after the original libusb
project did not produce a new release for over 18 months.


%package -n     %devellibname
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}-devel-doc = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Provides:       libusbx1-devel = %{version}-%{release}
Provides:       libusb1-devel = %{version}-%{release}
Provides:       libusbx-devel = %{version}-%{release}
Provides:       usbx-devel = %{version}-%{release}
Provides:       usb1-devel = %{version}-%{release}
Provides:       usb1.0-devel = %{version}-%{release}
Obsoletes:      libusb1-devel <= 1.0.9

%description -n	%devellibname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


#static package
%package -n     %devellibnamest
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}-devel-doc = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Requires:       %{devellibname} = %{version}-%{release}
Provides:       libusbx1-static-devel = %{version}-%{release}
Provides:       libusb1-static-devel = %{version}-%{release}
Provides:       libusbx-static-devel = %{version}-%{release}
Provides:       usbx-devel-static = %{version}-%{release}
Provides:       usb1-static-devel = %{version}-%{release}
Provides:       usb1.0-static-devel = %{version}-%{release}
Obsoletes:      libusb1-static-devel <= 1.0.9

%description -n	%devellibnamest
The %{name}-static-devel package contains libraries and header files for
developing applications that use %{name}.


%package	devel-doc
Summary:        Development files for %{name}
Group:          Development/C
Provides:       libusb1-devel-doc = %{version}-%{release}
Obsoletes:      libusb1-devel-doc <= 1.0.9
BuildArch:      noarch

%description	devel-doc
This package contains API documentation for %{name}.


%prep
%setup -q
for i in examples/*.c; do
    iconv -f ISO-8859-1 -t UTF-8 -o $i.new $i
    touch -r $i $i.new
    mv $i.new $i
done


%build
libtoolize --force
autoheader
autoconf
autoreconf -fiv
%configure --enable-examples-build
%make
pushd doc
make docs
popd


%install
%makeinstall_std
rm %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc AUTHORS COPYING README NEWS
%{_libdir}/*.so.%{major}*

%files -n %{devellibnamest}
%{_libdir}/libusb-1.0.a

%files -n %{devellibname}
%{_includedir}/libusb-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libusb-1.0.pc

%files devel-doc
%doc doc/html examples/*.c
