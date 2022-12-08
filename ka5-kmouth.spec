#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kmouth
Summary:	kmouth
Name:		ka5-%{kaname}
Version:	22.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	8fa9415e88cbe5c3ca5c8cb5c266b2b9
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Speech-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMouth is a program which enables persons that cannot speak to let
their computer speak, e.g. mutal people or people who have lost their
voice. It has a text input field and speaks the sentences that you
enter. It also has support for user defined phrasebooks.

%description -l pl.UTF-8
KMouth jest programem, który pozwala osobom, które nie mogą
mówić, by komputer mówił za nich, np, niemowom, lub osobom, które
straciły głos. Program ma pole tekstowe i wymawia zdania wprowadzane
z klawiatury. Wspiera też listę wyrażeń definiowanych przez
użytkownika.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kmouthrc
%attr(755,root,root) %{_bindir}/kmouth
%{_desktopdir}/org.kde.kmouth.desktop
%{_iconsdir}/hicolor/16x16/actions/phrase.png
%{_iconsdir}/hicolor/16x16/actions/phrasebook.png
%{_iconsdir}/hicolor/16x16/apps/kmouth.png
%{_iconsdir}/hicolor/22x22/actions/phrase.png
%{_iconsdir}/hicolor/22x22/actions/phrasebook.png
%{_iconsdir}/hicolor/22x22/apps/kmouth.png
%{_iconsdir}/hicolor/32x32/actions/phrase.png
%{_iconsdir}/hicolor/32x32/actions/phrasebook.png
%{_iconsdir}/hicolor/32x32/apps/kmouth.png
%{_iconsdir}/hicolor/48x48/apps/kmouth.png
%{_datadir}/kmouth
%dir %{_datadir}/kxmlgui5/kmouth
%{_datadir}/kxmlgui5/kmouth/kmouthui.rc
%{_datadir}/kxmlgui5/kmouth/phrasebookdialogui.rc
%{_datadir}/metainfo/org.kde.kmouth.appdata.xml
%lang(ca) %{_mandir}/ca/man1/kmouth.1*
%lang(da) %{_mandir}/da/man1/kmouth.1*
%lang(de) %{_mandir}/de/man1/kmouth.1*
%lang(es) %{_mandir}/es/man1/kmouth.1*
%lang(et) %{_mandir}/et/man1/kmouth.1*
%lang(fr) %{_mandir}/fr/man1/kmouth.1*
%lang(it) %{_mandir}/it/man1/kmouth.1*
%lang(C) %{_mandir}/man1/kmouth.1*
%lang(nl) %{_mandir}/nl/man1/kmouth.1*
%lang(pt) %{_mandir}/pt/man1/kmouth.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kmouth.1*
%lang(ru) %{_mandir}/ru/man1/kmouth.1.*
%lang(sv) %{_mandir}/sv/man1/kmouth.1*
%lang(uk) %{_mandir}/uk/man1/kmouth.1*
