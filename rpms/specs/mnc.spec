%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}
# Upstream using Github, Github provides a mechanism to create 
# tarballs on demand, either from a specific commit revision, 
# or from a specific tag. If the upstream does not create tarballs 
# for releases, you can use this mechanism to produce them. 
# If the upstream does create tarballs you should use them as 
# tarballs provide an easier trail for people auditing the packages. 
%global commit 8e5ba111fbafc42da55e13b491f1b25f0413d396
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mnc
Version:        1.12
Release:        1%{?dist}
Summary:        Multicast NetCat

Group:          System Environment/Shells
License:        BSD
URL:            http://en.japannext.co.jp
Source0:        https://github.com/rascyber/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

# BuildRequires:  
# Requires:  
# BuildArch: noarch
# Requires: redhat-release >= %{version}
# ExclusiveArch: %{ix86} x86_64 
BuildRoot: %{_tmppath}/%{name}-buildroot-%(%{__id_u} -n)     
 
%description
Mnc is a simple, one-direction-at-a-time, "netcat"-like application using
multicast. The aim is to provide a tool for easy debugging and testing when
setting up a multicast network or host. MNC supports IPv4 and IPv6
any-source-multicast and single-source-multicast.
 
%prep
%setup -qn %{name}-%{commit}
 
%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/share/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/local/bin

install -c -m 0755 -d $RPM_BUILD_ROOT/usr/local/share/man/man1
install -c -m 0644 doc/mnc.1 $RPM_BUILD_ROOT/usr/local/share/man/man1/
install -c -m 0755 -d $RPM_BUILD_ROOT/usr/local/bin
install -c -s -m 0755  mnc $RPM_BUILD_ROOT/usr/local/bin
 
%clean
rm -rf $RPM_BUILD_ROOT
 
%post
echo " "
echo "install of mnc complete!"

%find_lang %{name} --with-man 
%files
%defattr(-,root,root,-)
%doc README
%doc LICENCE

/usr/local/bin/mnc
/usr/local/share/man/man1/mnc.1

%changelog
* Fri Aug 29 2014 Sternly K Simon <sternly@mobicyberdev.com> - 1.12-1
- Initial RPM package.