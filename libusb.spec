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
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		https://libusb.info
Source0:	https://github.com/libusb/libusb/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	doxygen
BuildRequires:	locales-extra-charsets
BuildRequires:	pkgconfig(udev)
%if %{with compat32}
BuildRequires:	devel(libudev)
%endif

%patchlist
# Modifications from upstream, needed to pull in support for
# SuperSpeedPlus devices, already used by android-tools
https://github.com/libusb/libusb/commit/5c64e52554daa0a7d297154cbc07fee039f8727f.patch
https://github.com/libusb/libusb/commit/6cf58bac95ff62cd3453cba2c898993b40e1da66.patch
https://github.com/libusb/libusb/commit/51d2c0ffce90916a4950904e12ea091288e8fca5.patch
https://github.com/libusb/libusb/commit/6c0ae1ab456da49e7805115e77ce0428ace4ea41.patch
https://github.com/libusb/libusb/commit/233a8de6f9bfb47d767f9d3272532abfce71d05f.patch
https://github.com/libusb/libusb/commit/288d82f15e18dd89893b8db0839a7503361f0643.patch
https://github.com/libusb/libusb/commit/a07ecfe02aeea6861bbefebd9ab064eae7e15b51.patch
https://github.com/libusb/libusb/commit/d81e80aa5a45c6d24eb1b2556e089c2f21194581.patch
https://github.com/libusb/libusb/commit/4e246a73eea05bcd1e1e8d1d8d2a7d6b3fcff773.patch
https://github.com/libusb/libusb/commit/1c1bad9d128052fa82ba2c648875276f0189c3a2.patch
https://github.com/libusb/libusb/commit/43107c84e4a5f6b15c296eff8cc3578100f35dce.patch
https://github.com/libusb/libusb/commit/2f2e072ce5079c434e348b2a66fcf4669fca3848.patch
https://github.com/libusb/libusb/commit/a99a2581026d9a62409f5314c8c9c553c10cc432.patch
https://github.com/libusb/libusb/commit/f8a6c412f51c974d8c70fd100e28b3b69b9d3318.patch
https://github.com/libusb/libusb/commit/f00f06e9ebfcb5673c636e75d1f3d06375eccf03.patch
https://github.com/libusb/libusb/commit/5b17c383f8dd27e6938ffcc125c2a839db72c1ff.patch
https://github.com/libusb/libusb/commit/fef78a96e37936f16c10c43c9a220683f7c2ff74.patch
https://github.com/libusb/libusb/commit/b00332d34eaf54a9a77ec309e5d1782c10e34038.patch
https://github.com/libusb/libusb/commit/8b507434facfd4e4e9c31e99b6a698176a54d970.patch
https://github.com/libusb/libusb/commit/42e8a9ff2c7bcef600cfd48dcc5d2ad167a9737d.patch
https://github.com/libusb/libusb/commit/34d2ca5c636de25932059d3d48126390cae1e374.patch
https://github.com/libusb/libusb/commit/48c6bdea805d5eacc284910242e146b06b178b8d.patch
https://github.com/libusb/libusb/commit/de1398db35890408b2f465bc135c04b816ef2f19.patch
https://github.com/libusb/libusb/commit/2a138c6f12988c42eaa9dd663581faa700c44abe.patch
https://github.com/libusb/libusb/commit/2c32efa20e30c1fc93a37b5c7cf1858ce7fa0fb8.patch
https://github.com/libusb/libusb/commit/d795c0b821899e8611e3694ac72c36a843bef310.patch
https://github.com/libusb/libusb/commit/5144b1c7b3518863905137af04e75392e9670bb8.patch
https://github.com/libusb/libusb/commit/016a0de33ac94b19c7772d6c20fbea7fec23bf68.patch
https://github.com/libusb/libusb/commit/678c81271b266b955211791e70fe5f16feacb0e0.patch
https://github.com/libusb/libusb/commit/916c740076d960f2b759e264a0fb456643182590.patch
https://github.com/libusb/libusb/commit/e678b3fad58a508cbd0a6e6dc777fb48346f948b.patch
https://github.com/libusb/libusb/commit/00454ab087774a62b314805b51215bba81a99aa8.patch
https://github.com/libusb/libusb/commit/9ffdb7fe6ed8f1f303e851a1088fc05a3bae713d.patch
https://github.com/libusb/libusb/commit/85055a412b9e0f76c762f01400c046b4318db9a8.patch
https://github.com/libusb/libusb/commit/a7e471dd485bff853ca984c2f32d9b508fe913b6.patch
https://github.com/libusb/libusb/commit/3616e751b108945b9a8622cfe6fc8049c18a1ae8.patch
https://github.com/libusb/libusb/commit/418aadc0f9017b7a1bc237f72ffcf684da167567.patch
https://github.com/libusb/libusb/commit/6883f84f931b3c8e975a9b7877680df8406495c5.patch
https://github.com/libusb/libusb/commit/a18a964abaea2cd569c5c18f21b31126237f8a46.patch
https://github.com/libusb/libusb/commit/9cf84577cea84b313c202a3740c3220f31e0b6b8.patch
https://github.com/libusb/libusb/commit/e3ccc46b6eced61e29464b6751e9ac07fd63a329.patch
https://github.com/libusb/libusb/commit/55f8c95551890089db2560eae33efbf7d1b6ae42.patch
https://github.com/libusb/libusb/commit/197e3052cdd3f875820d0b2436c98a22ff070f0d.patch
https://github.com/libusb/libusb/commit/e8d76b1a129ca61315c6ef0f71f5c0f363db70b8.patch
https://github.com/libusb/libusb/commit/c3873d5c2ce95ca4b6259e4be8b07daaa68ad768.patch
https://github.com/libusb/libusb/commit/bd0fcdb4c2d2e75f684392502cc103402179817d.patch
https://github.com/libusb/libusb/commit/9d595d4e4ae41cdcb890d58531f522f7cdbae155.patch
https://github.com/libusb/libusb/commit/bc12cda784beb8c0ca72a68d1306309745213501.patch
https://github.com/libusb/libusb/commit/d04fc0e60bbca237876ab80530b6e5bae9b73ebd.patch
https://github.com/libusb/libusb/commit/4528752cbecd0ff84c5df2e17453060d8971b3b2.patch
https://github.com/libusb/libusb/commit/30ec25f738e6f4fab2e0781f452ab6144fa3b15f.patch
https://github.com/libusb/libusb/commit/a3199696e2abe3ff5054db4a341d2081a2b664e8.patch
https://github.com/libusb/libusb/commit/8776b8021aeafe9ba9db3b899a8a801867c1c9af.patch
https://github.com/libusb/libusb/commit/467b6a8896daea3d104958bf0887312c5d14d150.patch
https://github.com/libusb/libusb/commit/28a6afb6905bc2c6895b53b0e81a89671cd6f517.patch
https://github.com/libusb/libusb/commit/0b4eda697f0bd9b817a7c29b4f7fd9513e69c606.patch
https://github.com/libusb/libusb/commit/7adb2913cebe8f5cba84f68f817a75d3034e9d17.patch
https://github.com/libusb/libusb/commit/7bc88c0f084f3814d8887bb8dd5ea095be176983.patch
https://github.com/libusb/libusb/commit/de38189e8014fa393f4d8c1d9d3fdf5e2a95899d.patch

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
