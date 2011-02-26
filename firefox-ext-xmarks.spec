Summary: Xmarks Bookmark Synchronizer extension for firefox
Name: firefox-ext-xmarks
Version: 3.9.5
Release: %mkrel 1
License: GPLv2+
Group: Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/2410
Buildarch: noarch
Source: http://releases.mozilla.org/pub/mozilla.org/addons/2410/xmarks_sync-%{version}-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_epoch}:%{firefox_version}
Obsoletes: mozilla-firefox-ext-foxmarks < %{version}-%{release}
Provides: mozilla-firefox-ext-foxmarks = %{version}-%{release}
Obsoletes: firefox-ext-foxmarks < %{version}-%{release}
Provides: firefox-ext-foxmarks = %{version}-%{release}
Obsoletes: firefox-ext-xmarks < %{version}-%{release}
BuildRequires: firefox-devel

%description
If you use Firefox on more than one computer, you'll want Xmarks. Install
Xmarks on each computer, and it will work silently in the background to keep
your bookmarks synchronized. You can also log in to my.xmarks.com to manage
your bookmarks from any computer.

A simple wizard guides you through the startup process. After that, just forget
about it. It's simple and solid.

Xmarks was formerly known as Foxmarks.

%prep
%setup -q -c -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}
