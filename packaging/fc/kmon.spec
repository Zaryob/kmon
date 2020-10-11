Name:		kmon
Version:	0.8
Release:	1
Summary:	Ken's MONitor

Vendor:		Kenneth Salerno
Group:		System Administration Tools
License:	GNU GPL
#URL:		
Source0:	kmon-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
This is a simple VM and I/O monitor that takes vmstat output and pairs it with
the top CPU consumers displaying some useful stats for each PID.
The purpose of this script is performance monitoring and troubleshooting
bottlenecks all in one screen.

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/local/bin/kmon
%doc /usr/local/share/man/man8/kmon.8


%changelog
* Tue Mar 16 2010 kens - 0.8-1
- Added feature to automatically detect rows and columns of console window to
  make output consistent for users
- Added the display of the light weight process count per PID (num of threads)
- Added resident physical RAM stats in MB

* Thu Mar 4 2010 kens - 0.7-1
- Added splash screen with version info during startup
- Moved vmstat output to the bottom of the screen because wrapping sometimes
  made the ps table appear to jump up and down
- Standardized the ps table header across all platforms to keep the look
  consistent across all Operating Systems (and helped with column spacing)
- Converted procps vmstat (Linux) block values to MB for column spacing reasons

* Sun Feb 28 2010 kens - 0.6-1
- I gave up trying to catch only PIDs in the Uninterruptible and Runnable
  states because they most often change states much too quickly and go right
  back to Sleeping...

* Tue Feb 23 2010 kens - 0.5-1
- fixed display issue on OpenBSD
- optimized case statement and updated man page and README file
- fixed AM/am regex from uptime output

* Mon Feb 22 2010 kens - 0.4-1
- improved output formatting and added Memory information for each process

* Mon Feb 22 2010 kens - 0.3-2
- manual page edit

* Mon Feb 22 2010 kens - 0.3-1
- I now display the pdflush and kswap processes.  I also rearranged the logo

* Sat Feb 21 2010 kens - 0.2-1
- initial
