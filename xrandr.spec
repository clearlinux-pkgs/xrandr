#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xrandr
Version  : 1.5.0
Release  : 6
URL      : http://xorg.freedesktop.org/releases/individual/app/xrandr-1.5.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/app/xrandr-1.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : HPND
Requires: xrandr-bin
Requires: xrandr-doc
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xrandr)

%description
xrandr - primitive command line interface to X11 Resize, Rotate, and Reflect
(RandR) extension

%package bin
Summary: bin components for the xrandr package.
Group: Binaries

%description bin
bin components for the xrandr package.


%package doc
Summary: doc components for the xrandr package.
Group: Documentation

%description doc
doc components for the xrandr package.


%prep
cd ..
%setup -q -n xrandr-1.5.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xkeystone
/usr/bin/xrandr

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
