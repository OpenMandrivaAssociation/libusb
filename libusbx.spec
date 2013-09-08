%define api	1.0
%define major	0
%define libname	%mklibname usb %{api} %{major}
%define devname	%mklibname -d usb %{api}

Summary:	Library for accessing USB devices
Name:		libusbx
Version:	1.0.17
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://sourceforge.net/apps/mediawiki/libusbx/
Source0:	http://downloads.sourceforge.net/libusbx/libusbx-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	udev-devel

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

%description -n	%{libname}
Libusbx is a fork of the original libusb, which is a fully API and ABI
compatible drop in for the libusb-1.0.9 release. The libusbx fork was
started by most of the libusb-1.0 developers, after the original libusb
project did not produce a new release for over 18 months.

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

%build
%configure2_5x \
	--disable-static \
	--enable-examples-build

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
/%{_lib}/libusb-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS README NEWS
%{_includedir}/libusb-1.0
%{_libdir}/libusb-%{api}.so
%{_libdir}/pkgconfig/libusb-1.0.pc
%doc doc/html examples/*.c

