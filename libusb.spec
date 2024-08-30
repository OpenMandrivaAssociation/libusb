%global optflags %{optflags} -Wno-error=maybe-uninitialized

# libusb is used by wine and sdl2 (which is used by many games)
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define api 1.0
%define major 0
%define libname %mklibname usb %{api} %{major}
%define devname %mklibname -d usb %{api}
%define lib32name %mklib32name usb %{api} %{major}
%define dev32name %mklib32name -d usb %{api}

Summary:	Library for accessing USB devices
Name:		libusb
Version:	1.0.27
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libusb.info
Source0:	https://github.com/libusb/libusb/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	doxygen
BuildRequires:	locales-extra-charsets
BuildRequires:	pkgconfig(udev)
%if %{with compat32}
BuildRequires:	devel(libudev)
%endif

%description
This package provides a way for applications to access USB devices.

Note that this library is not compatible with the original libusb-0.1 series,
if you need libusb-0.1 compatibility install the libusb-compat package.

%package -n %{libname}
Summary:	Library for accessing USB devices
Group:		System/Libraries

%description -n %{libname}
libusb is a C library that provides generic access to USB devices. It is
intended to be used by developers to facilitate the production of
applications that communicate with USB hardware.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel-doc < 1.0.15-2

%description -n %{devname}
This package includes the development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	Library for accessing USB devices (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
libusb is a C library that provides generic access to USB devices. It is
intended to be used by developers to facilitate the production of
applications that communicate with USB hardware.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package includes the development files for %{name}.
%endif

%prep
%autosetup -p1

for i in examples/*.c; do
    iconv -f ISO-8859-1 -t UTF-8 -o $i.new $i
    touch -r $i $i.new
    mv $i.new $i
done
autoreconf -fiv

export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32 \
	--disable-examples-build
cd ..
%endif
mkdir build
cd build
%configure \
	--enable-examples-build

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

cd build/doc
make docs
cd -

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libusb-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS README NEWS
%{_includedir}/libusb-1.0
%{_libdir}/libusb-%{api}.so
%{_libdir}/pkgconfig/libusb-1.0.pc
%doc examples/*.c

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libusb-%{api}.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libusb-%{api}.so
%{_prefix}/lib/pkgconfig/libusb-1.0.pc
%endif
