%define api	1.0
%define major	0
%define libname	%mklibname usb %{api} %{major}
%define devname	%mklibname -d usb %{api}

Summary:	Library for accessing USB devices
Name:		libusb
Version:	1.0.22
Release:	3
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libusb.info
Source0:	https://github.com/libusb/libusb/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	pkgconfig(udev)

%description
This package provides a way for applications to access USB devices.

Note that this library is not compatible with the original libusb-0.1 series,
if you need libusb-0.1 compatibility install the libusb-compat package.

%package -n	%{libname}
Summary:	Library for accessing USB devices
Group:		System/Libraries

%description -n	%{libname}
libusb is a C library that provides generic access to USB devices. It is
intended to be used by developers to facilitate the production of
applications that communicate with USB hardware.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel-doc < 1.0.15-2

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -q
for i in examples/*.c; do
    iconv -f ISO-8859-1 -t UTF-8 -o $i.new $i
    touch -r $i $i.new
    mv $i.new $i
done
autoreconf -fiv

%build
%configure \
	--disable-static \
	--enable-examples-build

%make
cd doc
make docs
cd -


%install
%makeinstall_std

mkdir %{buildroot}/%{_lib}
mv %{buildroot}%{_libdir}/libusb-%{api}.so.%{major}* %{buildroot}/%{_lib}
ln -srf %{buildroot}/%{_lib}/libusb-%{api}.so.%{major}.*.* %{buildroot}%{_libdir}/libusb-%{api}.so

%files -n %{libname}
/%{_lib}/libusb-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS README NEWS
%{_includedir}/libusb-1.0
%{_libdir}/libusb-%{api}.so
%{_libdir}/pkgconfig/libusb-1.0.pc
%doc doc/html examples/*.c
