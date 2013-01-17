%define	api	1.0
%define	major	0
%define	libname	%mklibname usb %{api} %{major}
%define	devname	%mklibname -d usb %{api}
%define	static	%mklibname -d -s usb %{api}

Summary:        Library for accessing USB devices
Name:           libusbx
Version:        1.0.14
Release:        3
Source0:        http://downloads.sourceforge.net/libusbx/libusbx-%{version}.tar.bz2
License:        LGPLv2+
Group:          System/Libraries
URL:            http://sourceforge.net/apps/mediawiki/libusbx/
BuildRequires:  doxygen

%description
This package provides a way for applications to access USB devices.

Libusbx is a fork of the original libusb, which is a fully API and ABI
compatible drop in for the libusb-1.0.9 release. The libusbx fork was
started by most of the libusb-1.0 developers, after the original libusb
project did not produce a new release for over 18 months.

Note that this library is not compatible with the original libusb-0.1 series,
if you need libusb-0.1 compatibility install the libusb package.

%package -n	%{libname}
Summary:	Libusbx is a fork of the original libusb
Group:		System/Libraries
%define oldlib	%{mklibname usbx %{api} %{major}}
%rename		%{oldlib}

%description -n	%{libname}
Libusbx is a fork of the original libusb, which is a fully API and ABI
compatible drop in for the libusb-1.0.9 release. The libusbx fork was
started by most of the libusb-1.0 developers, after the original libusb
project did not produce a new release for over 18 months.


%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name}-devel-doc = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
%define	olddev	%{mklibname -d usbx %{api}}
%rename		%{olddev}

%description -n	%{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     %{static}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}-devel-doc = %{version}-%{release}
Requires:       %{devname} = %{version}-%{release}
%define	oldstat	%{mklibname -d -s usbx %{api}}
%rename		%{oldstat}
Obsoletes:      libusb1-static-devel <= 1.0.9

%description -n	%{static}
The %{name}-static-devel package contains libraries and header files for
developing applications that use %{name}.


%package	devel-doc
Summary:        Development files for %{name}
Group:          Development/C
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
libtoolize --force
autoheader
autoconf
autoreconf -fiv

%build
%configure --enable-examples-build
%make
pushd doc
make docs
popd


%install
%makeinstall_std

mkdir %{buildroot}/%{_lib}
mv %{buildroot}%{_libdir}/libusb-%{api}.so.%{major}* %{buildroot}/%{_lib}
ln -srf %{buildroot}/%{_lib}/libusb-%{api}.so.%{major}.*.* %{buildroot}%{_libdir}/libusb-%{api}.so

%files -n %{libname}
%doc AUTHORS README NEWS
/%{_lib}/libusb-%{api}.so.%{major}*

%files -n %{static}
%{_libdir}/libusb-1.0.a

%files -n %{devname}
%{_includedir}/libusb-1.0
%{_libdir}/libusb-%{api}.so
%{_libdir}/pkgconfig/libusb-1.0.pc

%files devel-doc
%doc doc/html examples/*.c
