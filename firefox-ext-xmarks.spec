Summary:	Xmarks Bookmark Synchronizer extension for firefox
Name:		firefox-ext-xmarks
Version:	4.1.0
Release:	2
License:	GPLv2+
Group:		Networking/WWW
Url:		https://addons.mozilla.org/en-US/firefox/addon/2410
Source0:	http://releases.mozilla.org/pub/mozilla.org/addons/2410/xmarks_sync-%{version}-fx+sm.xpi
Buildarch:	noarch

BuildRequires:	firefox-devel
Requires:	firefox >= %{firefox_version}
Provides:	firefox-ext-foxmarks = %{version}-%{release}

%description
If you use Firefox on more than one computer, you'll want Xmarks. Install
Xmarks on each computer, and it will work silently in the background to keep
your bookmarks synchronized. You can also log in to my.xmarks.com to manage
your bookmarks from any computer.

A simple wizard guides you through the startup process. After that, just forget
about it. It's simple and solid.

Xmarks was formerly known as Foxmarks.

%prep
%setup -qc

%install
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

%files
%{firefox_extdir}

