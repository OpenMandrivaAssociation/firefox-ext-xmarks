Summary: Xmarks Bookmark Synchronizer extension for firefox
Name: firefox-ext-xmarks
Version: 4.1.0
Release: 1
License: GPLv2+
Group: Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/2410
Buildarch: noarch
Source: http://releases.mozilla.org/pub/mozilla.org/addons/2410/xmarks_sync-%{version}-fx+sm.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_version}
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


%changelog
* Tue Jun 21 2011 Funda Wang <fwang@mandriva.org> 3.9.10-1mdv2011.0
+ Revision: 686494
- update to new version 3.9.10

* Thu Apr 14 2011 Juan Luis Baptiste <juancho@mandriva.org> 3.9.9-1
+ Revision: 652887
- Updated to 3.9.9

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 3.9.5-1
+ Revision: 640060
- New version 3.9.5

* Tue Jan 18 2011 Funda Wang <fwang@mandriva.org> 3.9.2-3
+ Revision: 631478
- build for new ff ext dir

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 3.9.2-2mdv2011.0
+ Revision: 628878
- rebuild for new firefox

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 3.9.2-1mdv2011.0
+ Revision: 598558
- update to new version 3.9.2

* Thu Sep 02 2010 Funda Wang <fwang@mandriva.org> 3.8.6-1mdv2011.0
+ Revision: 575507
- update to new version 3.8.6

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 3.6.14-3mdv2011.0
+ Revision: 561171
- rebuild for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 3.6.14-2mdv2010.1
+ Revision: 549354
- rebuild with FF 3.6.6

  + Funda Wang <fwang@mandriva.org>
    - New version 3.6.14

* Wed Apr 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.5.10-3mdv2010.1
+ Revision: 532638
- don't provide empty debug package

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 3.5.10-2mdv2010.1
+ Revision: 531080
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 3.5.10-1mdv2010.1
+ Revision: 526988
- update to new version 3.5.10

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 3.4.6-2mdv2010.1
+ Revision: 494802
- rebuild

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 3.4.6-1mdv2010.1
+ Revision: 480372
- new version 3.4.6 (ff 3.6b5)

* Wed Dec 16 2009 Funda Wang <fwang@mandriva.org> 3.3.3-3mdv2010.1
+ Revision: 479193
- rebuild for new ff

* Sun Nov 08 2009 Funda Wang <fwang@mandriva.org> 3.3.3-2mdv2010.1
+ Revision: 462800
- rebuild for new ff

* Thu Sep 24 2009 Juan Luis Baptiste <juancho@mandriva.org> 3.3.3-1mdv2010.0
+ Revision: 448487
- Updated to 3.3.3.

* Wed Sep 16 2009 Funda Wang <fwang@mandriva.org> 3.3.2-1mdv2010.0
+ Revision: 443380
- new version 3.3.2

* Tue Aug 18 2009 Gustavo De Nardin <gustavodn@mandriva.com> 3.1.0-5mdv2010.0
+ Revision: 417675
- buildrequire firefox-devel, which provides the new macros for building extensions
- make use of the firefox package macros
- rebuild for firefox 3.5.2

* Tue Aug 04 2009 Eugeni Dodonov <eugeni@mandriva.com> 3.1.0-4mdv2010.0
+ Revision: 408638
- rebuild for firefox 3.0.13

* Fri Jul 31 2009 Funda Wang <fwang@mandriva.org> 3.1.0-3mdv2010.0
+ Revision: 405035
- rebuild for new ff

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 3.1.0-2mdv2010.0
+ Revision: 385771
- rebuild for new ff

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 3.1.0-1mdv2010.0
+ Revision: 381246
- new version 3.1.0

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 3.0.2-1mdv2010.0
+ Revision: 369574
- Xmarks 3.0.2
- rename to xmarks

* Sat Mar 28 2009 Gustavo De Nardin <gustavodn@mandriva.com> 2.7.2-2mdv2009.1
+ Revision: 361851
- rebuild for firefox 3.0.8

* Thu Mar 12 2009 Funda Wang <fwang@mandriva.org> 2.7.2-1mdv2009.1
+ Revision: 354081
- New version 2.7.2

* Wed Feb 04 2009 Funda Wang <fwang@mandriva.org> 2.6.0-1mdv2009.1
+ Revision: 337292
- rename to firefox
- rename to firefox
- New version 2.6.0

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 2.5.3-2mdv2009.1
+ Revision: 318922
- rebuild for new ff

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 2.5.3-1mdv2009.1
+ Revision: 303706
- new version 2.5.3

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 2.1.0.12-2mdv2009.0
+ Revision: 289184
- rebuild for new FF

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 2.1.0.12-1mdv2009.0
+ Revision: 258205
- New version 2.1.0.12

* Wed Jul 30 2008 Tiago Salem <salem@mandriva.com.br> 2.0.47.4-4mdv2009.0
+ Revision: 256467
- add conditional to ff3

* Wed Jul 16 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.47.4-3mdv2009.0
+ Revision: 236322
- rebuilt for mozilla-firefox-2.0.0.16

* Thu Jul 03 2008 Tiago Salem <salem@mandriva.com.br> 2.0.47.4-2mdv2009.0
+ Revision: 231260
- Rebuild for firefox 2.0.0.15

* Sun Jun 29 2008 Funda Wang <fwang@mandriva.org> 2.0.47.4-1mdv2009.0
+ Revision: 229994
- New version 2.0.47.4

* Sat Jun 07 2008 Funda Wang <fwang@mandriva.org> 2.0.46.9-1mdv2009.0
+ Revision: 216576
- New version 2.0.46.9

* Fri Apr 18 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.45-2mdv2009.0
+ Revision: 195590
- rebuild for mozilla-firefox-2.0.0.14

* Mon Apr 14 2008 Tiago Salem <salem@mandriva.com.br> 2.0.45-1mdv2009.0
+ Revision: 192816
- upgrade to 2.0.45. 2.0.43 does not work anymore.

* Wed Mar 26 2008 Tiago Salem <salem@mandriva.com.br> 2.0.43-3mdv2008.1
+ Revision: 190330
- bump ff_ver and release

* Fri Mar 07 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.43-2mdv2008.1
+ Revision: 181496
- Rebuilt against FF 2.0.0.12

* Fri Feb 01 2008 Funda Wang <fwang@mandriva.org> 2.0.43-1mdv2008.1
+ Revision: 161201
- New version 2.0.43

* Wed Jan 23 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.41-1mdv2008.1
+ Revision: 157231
- new upstream: 2.0.41. Closes: #37047

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2008.1
+ Revision: 117795
- own firefox directories so that they're not left behind on uninstall

* Tue Dec 11 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.0.1-3mdv2008.1
+ Revision: 117475
- Rebuilt for FF 2.0.0.11

* Mon Nov 05 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.0.1-2mdv2008.1
+ Revision: 106113
- New firefox: 2.0.0.9

* Fri Oct 19 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.0.1-1mdv2008.1
+ Revision: 100392
- Rebuilt against FF 2.0.0.8.

* Wed Aug 01 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.0.1-1mdv2008.0
+ Revision: 57664
- Building for FF 2.0.0.6
- Import mozilla-firefox-ext-foxmarks

