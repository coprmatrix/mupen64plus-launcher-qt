%define _name   mupen64plus-launcher-qt

Name:           %{_name}
Version:        1.17
Release:        0
Summary:        A customizable launcher for Mupen64Plus
Group:          Applications/Emulators
License:        BSD
URL:            https://github.com/dh4/mupen64plus-qt
Source0:        %{url}/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  qt6-qtbase-devel
BuildRequires:  quazip-qt6-devel
BuildRequires:  SDL2-devel
BuildRequires:  patchelf
BuildRequires:  sed

%description
Mupen64Plus-Qt is a customizable launcher for the mupen64plus-ui-console
frontend. It was adapted from CEN64-Qt to work with Mupen64Plus.

See the README at https://www.github.com/dh4/mupen64plus-qt for a detailed
description of its features and usage.

%global debug_package %{nil}

%prep
%autosetup -n %{_name}-%{version}

%build
cmake CMakeLists.txt
make %{?_smp_mflags}

%install
install -Dm755 "mupen64plus-qt"                     "%{buildroot}%{_bindir}/%{_name}"
patchelf --remove-rpath                             "%{buildroot}%{_bindir}/%{_name}"
install -Dm644 "resources/mupen64plus-qt.desktop"   "%{buildroot}%{_datadir}/applications/%{_name}.desktop"
sed -i 's~mupen64plus-qt~%{_name}~g;'               "%{buildroot}%{_datadir}/applications/%{_name}.desktop"
install -Dm644 "resources/images/mupen64plus.png"   "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{_name}.png"
install -Dm644 "resources/mupen64plus-qt.6"         "%{buildroot}%{_mandir}/man6/%{_name}.6"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{_name}.png
%{_mandir}/man6/%{_name}.6*

