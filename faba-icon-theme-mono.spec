%global commit 2006c52
%global snapshot .git20160927.%{commit}

Name:           faba-icon-theme-mono
Version:        4.3
Release:        1%{snapshot}%{?dist}
Summary:        Faba Icon Theme (Monochrome)

License:        LGPL-3.0+ or CC-BY-SA-3.0
URL:            http://www.snwh.org/moka

# git clone https://github.com/snwh/faba-mono-icons
# cd faba-mono-icons
# git archive --prefix=faba-icon-theme-mono-%{version}/ master | bzip2 >../faba-icon-theme-mono-%{version}.tar.bz
Source0:        faba-icon-theme-mono-4.3.tar.bz2

BuildArch:      noarch
BuildRequires:  automake
BuildRequires:  icon-naming-utils
BuildRequires:  gtk2
Requires:       hicolor-icon-theme
Requires:       faba-icon-theme
Requires:       moka-icon-theme
Requires:       gnome-icon-theme

%description
The monochromatic panel icon sets for Faba.


%prep
%setup -q
find -L . -type l -print -delete
./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%doc AUTHORS README.md
%license COPYING LICENSE
%{_datadir}/icons/Faba-Mono
%ghost %{_datadir}/icons/Faba-Mono/icon-theme.cache
%{_datadir}/icons/Faba-Mono-Dark
%ghost %{_datadir}/icons/Faba-Mono-Dark/icon-theme.cache


%post
touch --no-create %{_datadir}/icons/Faba-Mono &>/dev/null || :
touch --no-create %{_datadir}/icons/Faba-Mono-Dark &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/Faba-Mono &>/dev/null
    touch --no-create %{_datadir}/icons/Faba-Mono-Dark &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/Faba-Mono &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/Faba-Mono-Dark &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/Faba-Mono &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/Faba-Mono-Dark &>/dev/null || :


%changelog
* Tue Sep 27 2016 Jajauma's Packages <jajauma@yandex.ru> - 4.3-1.git20160927.2006c52
- Public release
