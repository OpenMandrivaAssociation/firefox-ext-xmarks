%define ff_epoch 0
%define ff_ver 3.0.8

%define _mozillapath %{_libdir}/firefox-%{ff_ver}
%define _mozillaextpath %{_mozillapath}/extensions

Summary: Foxmarks Bookmark Synchronizer extension for firefox
Name: firefox-ext-foxmarks
Version: 2.7.2
Release: %mkrel 2
License: GPLv2+
Group: Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/2410
Source: http://releases.mozilla.org/pub/mozilla.org/addons/2410/foxmarks_bookmark_synchronizer-%{version}-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: mozilla-firefox = %{ff_epoch}:%{ff_ver}
Obsoletes: mozilla-firefox-ext-foxmarks < %{version}-%{release}
Provides: mozilla-firefox-ext-foxmarks = %{version}-%{release}

%description
If you use Firefox on more than one computer, you'll want Foxmarks. Install
Foxmarks on each computer, and it will work silently in the background to keep
your bookmarks synchronized. You can also log in to my.foxmarks.com to manage
your bookmarks from any computer.

A simple wizard guides you through the startup process. After that, just forget
about it. It's simple and solid.

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %_mozillapath
%{_mozillaextpath}
