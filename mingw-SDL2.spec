%{?mingw_package_header}

Name:           mingw-SDL2
Version:        2.0.3
Release:        8%{?dist}
Summary:        MinGW Windows port of SDL2 cross-platform multimedia library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.libsdl.org/
Source0:        http://www.libsdl.org/release/SDL2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  dos2unix

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc

# Not required at the moment, but SDL does contain plenty of C++ code,
# I just haven't worked out how to enable it.
#BuildRequires:  mingw32-gcc-c++

%ifarch %{ix86}
BuildRequires: nasm
%endif

# Don't try to re-implement D3D11 pieces which are already part of mingw-w64
Patch0:        SDL2-prevent-duplicate-d3d11-declarations.patch

# Workaround a gcc compatibility issue
Patch1:        SDL2-fix-gcc-compatibility.patch


%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.


# Win32
%package -n mingw32-SDL2
Summary:        MinGW Windows port of SDL cross-platform multimedia library

%description -n mingw32-SDL2
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win32 (static)
%package -n mingw32-SDL2-static
Summary:        MinGW Windows port of SDL cross-platform multimedia library
Requires:       mingw32-SDL2 = %{version}-%{release}

%description -n mingw32-SDL2-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64
%package -n mingw64-SDL2
Summary:        MinGW Windows port of SDL cross-platform multimedia library

%description -n mingw64-SDL2
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64 (static)
%package -n mingw64-SDL2-static
Summary:        MinGW Windows port of SDL cross-platform multimedia library
Requires:       mingw64-SDL2 = %{version}-%{release}

%description -n mingw64-SDL2-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.


%?mingw_debug_package


%prep
%setup -q -n SDL2-%{version}
%patch0 -p0 -b .d3d11
%patch1 -p0 -b .gcc
dos2unix COPYING.txt README.txt


%build
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# Remove test library.
rm $RPM_BUILD_ROOT%{mingw32_libdir}/libSDL2_test.a
rm $RPM_BUILD_ROOT%{mingw64_libdir}/libSDL2_test.a

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-SDL2
%doc README.txt COPYING.txt
%{mingw32_bindir}/SDL2.dll
%{mingw32_bindir}/sdl2-config
%{mingw32_libdir}/libSDL2.dll.a
%{mingw32_libdir}/libSDL2main.a
%{mingw32_libdir}/pkgconfig/sdl2.pc
%{mingw32_datadir}/aclocal/sdl2.m4
%{mingw32_includedir}/SDL2

# Win32 (static)
%files -n mingw32-SDL2-static
%{mingw32_libdir}/libSDL2.a

# Win64
%files -n mingw64-SDL2
%doc README.txt COPYING.txt
%{mingw64_bindir}/SDL2.dll
%{mingw64_bindir}/sdl2-config
%{mingw64_libdir}/libSDL2.dll.a
%{mingw64_libdir}/libSDL2main.a
%{mingw64_libdir}/pkgconfig/sdl2.pc
%{mingw64_datadir}/aclocal/sdl2.m4
%{mingw64_includedir}/SDL2

# Win64 (static)
%files -n mingw64-SDL2-static
%{mingw64_libdir}/libSDL2.a


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Anonymous Maarten <anonymous.maarten@gmail.com> - 2.0.3-7
- Added static package.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.3-5
- Don't try to re-implement D3D11 pieces which are already part of mingw-w64
- Workaround a gcc compatibility issue

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.3-3
- Fix rpmlint warnings

* Tue May 13 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.3-2
- Removed redundant BuildRequires

* Mon May 12 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.3-1
- Initial rpm
