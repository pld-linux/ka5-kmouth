%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kmouth
Summary:	kmouth
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	738edce3a241ced07467389b31dc3cf2
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Speech-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcompletion-devel >= 5.46.0
BuildRequires:	kf5-kconfig-devel >= 5.46.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.46.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.46.0
BuildRequires:	kf5-kcrash-devel >= 5.46.0
BuildRequires:	kf5-kdoctools-devel >= 5.46.0
BuildRequires:	kf5-ki18n-devel >= 5.46.0
BuildRequires:	kf5-kio-devel >= 5.46.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.46.0
BuildRequires:	kf5-kxmlgui-devel >= 5.46.0
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

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-qm

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
