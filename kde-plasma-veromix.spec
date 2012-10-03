Name:           kde-plasma-veromix
Version:        0.18.3
Release:        1%{?dist}
Summary:        A mixer for the Pulseaudio sound server

License:        GPLv3+
URL:            http://code.google.com/p/veromix-plasmoid/
Source0:        http://veromix-plasmoid.googlecode.com/files/veromix_%{version}.orig.tar.gz

BuildRequires:  kde-filesystem
BuildRequires:  kde-workspace-devel
BuildRequires:  qt4-devel
BuildRequires:  plasma-scriptengine-python
BuildRequires:  pyxdg
BuildRequires:  dbus-python
BuildRequires:  pulseaudio
BuildRequires:  kdesdk-scripts
BuildRequires:  ladspa-swh-plugins
BuildRequires:  gettext


%description
KDE (Plasma) applet for a mixer for the Pulseaudio sound server.

%prep
%setup -q -n veromix


%build
make %{?_smp_mflags}


%install
make install-plasmoid DESTDIR=$RPM_BUILD_ROOT
%find_lang veromix

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :

%files -f veromix.lang
%doc Changelog COPYING
%{_datadir}/dbus-1/services/org.veromix.pulseaudio.*.service
%{_datadir}/icons/veromix.png
%{_kde4_datadir}/kde4/apps/plasma/plasmoids/veromix-plasmoid
%{_kde4_datadir}/kde4/services/plasma-widget-veromix.desktop
%{_datadir}/veromix


%changelog
* Wed Oct 03 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.18.3-1.R
- Initial release
