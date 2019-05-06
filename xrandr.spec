#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1BEF3D8401A68861 (aplattner@nvidia.com)
#
Name     : xrandr
Version  : 1.5.0
Release  : 7
URL      : http://xorg.freedesktop.org/releases/individual/app/xrandr-1.5.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/app/xrandr-1.5.0.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/app/xrandr-1.5.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : HPND
Requires: xrandr-bin = %{version}-%{release}
Requires: xrandr-license = %{version}-%{release}
Requires: xrandr-man = %{version}-%{release}
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xrender)

%description
xrandr - primitive command line interface to X11 Resize, Rotate, and Reflect
(RandR) extension

%package bin
Summary: bin components for the xrandr package.
Group: Binaries
Requires: xrandr-license = %{version}-%{release}

%description bin
bin components for the xrandr package.


%package license
Summary: license components for the xrandr package.
Group: Default

%description license
license components for the xrandr package.


%package man
Summary: man components for the xrandr package.
Group: Default

%description man
man components for the xrandr package.


%prep
%setup -q -n xrandr-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557106651
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557106651
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xrandr
cp COPYING %{buildroot}/usr/share/package-licenses/xrandr/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xkeystone
/usr/bin/xrandr

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xrandr/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xrandr.1
