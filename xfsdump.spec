Summary: Administrative utilities for the XFS filesystem
Name: xfsdump
Version: 3.0.4
Release: 2%{?dist}
# Licensing based on generic "GNU GENERAL PUBLIC LICENSE"
# in source, with no mention of version.
License: GPL+
Group: System Environment/Base
URL: http://oss.sgi.com/projects/xfs/
Source0: ftp://oss.sgi.com/projects/xfs/cmd_tars/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libtool, gettext, gawk
BuildRequires: xfsprogs-devel, libuuid-devel, libattr-devel ncurses-devel
Requires: xfsprogs >= 2.6.30, attr >= 2.0.0

ExclusiveArch: x86_64

%description
The xfsdump package contains xfsdump, xfsrestore and a number of
other utilities for administering XFS filesystems.

xfsdump examines files in a filesystem, determines which need to be
backed up, and copies those files to a specified disk, tape or other
storage medium.	 It uses XFS-specific directives for optimizing the
dump of an XFS filesystem, and also knows how to backup XFS extended
attributes.  Backups created with xfsdump are "endian safe" and can
thus be transfered between Linux machines of different architectures
and also between IRIX machines.

xfsrestore performs the inverse function of xfsdump; it can restore a
full backup of a filesystem.  Subsequent incremental backups can then
be layered on top of the full backup.  Single files and directory
subtrees may be restored from full or partial backups.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DIST_ROOT=$RPM_BUILD_ROOT install
# remove non-versioned docs location
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/xfsdump/

(cd $RPM_BUILD_ROOT/%{_sbindir}; rm xfsdump xfsrestore)
(cd $RPM_BUILD_ROOT/%{_sbindir}; ln -s ../../sbin/xfsdump .)
(cd $RPM_BUILD_ROOT/%{_sbindir}; ln -s ../../sbin/xfsrestore .)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README doc/COPYING doc/CHANGES doc/README.xfsdump doc/xfsdump_ts.txt
%{_mandir}/man8/*
%{_sbindir}/*
/sbin/*

%changelog
* Mon Apr 19 2010 Eric Sandeen <sandeen@redhat.com> 3.0.4-2
- Restrict build to x86_64 for RHEL6 (#576259)

* Wed Jan 13 2010 Eric Sandeen <sandeen@redhat.com> 3.0.4-1
- New upstream release

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.0.1-3.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-2
- Fix up build-requires after e2fsprogs splitup

* Tue May 05 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-1
- New upstream release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Eric Sandeen <sandeen@redhat.com> 3.0.0-1
- New upstream release

* Wed Nov 12 2008 Eric Sandeen <sandeen@redhat.com> 2.2.48-2
- Enable parallel builds

* Sun Feb 10 2008 Eric Sandeen <sandeen@redhat.com> - 2.2.48-1
- Update to xfsdump version 2.2.48
- First build with gcc-4.3

* Mon Sep 10 2007 Eric Sandeen <sandeen@redhat.com> - 2.2.46-1
- Update to xfsdump version 2.2.46
- Dropped O_CREAT patch, now upstream

* Fri Aug 24 2007 Eric Sandeen <sandeen@redhat.com> - 2.2.45-3
- Update license tag
- Fix up O_CREAT opens with no mode
- Add gawk to buildrequires

* Tue Jun 19 2007 Eric Sandeen <sandeen@redhat.com> - 2.2.45-2
- Remove readline-devel & libtermcap-devel BuildRequires

* Thu May 31 2007 Eric Sandeen <sandeen@redhat.com> - 2.2.45-1
- Update to xfsdump 2.2.45

* Wed Aug 31 2006 Russell Cattelan <cattelan@thebarn.com> - 2.2.42-2
- Remove Distribution: tag

* Wed Aug 23 2006 Russell Cattelan <cattelan@thebarn.com> - 2.2.42-1
- update to version 2.2.42 

* Tue Aug 22 2006 Russell Cattelan <cattelan@thebarn.com> - 2.2.38-3
- Fix the /usr/sbin sym links to relative links
- Add the Distribution tag
- Add ncurses-devel to buildrequires

* Tue Aug 16 2006 Russell Cattelan <cattelan@thebarn.com> - 2.2.38-2
- install removes the makefile installed version of the docs
	package the docs based in the version specfic directory
 
* Wed Aug  9 2006 Russell Cattelan <cattelan@thebarn.com> - 2.2.38-1
- Add xfsdump to Fedorda
