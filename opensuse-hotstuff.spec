#
# spec file for package opensuse-hotstuff
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           opensuse-hotstuff
Version:        1.0
Release:        0
Summary:        Mirror configuration files for opensuse-hotstuff
License:        GPL-3.0-only
URL:            https://github.com/openSUSE/opensuse-hotstuff
Source0:        opensuse-hotstuff-%{version}.tar.xz
BuildArch:      noarch
Requires:       rsync

%description
Mirror configuration files for opensuse-hotstuff

%prep
%setup 

%build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/rsyncd.d
for conff in etc/rsyncd.d/*; do
 install -m 644 ${conff} %{buildroot}/%{_sysconfdir}/rsyncd.d/
done

%files
%dir %{_sysconfdir}/rsyncd.d
%{_sysconfdir}/rsyncd.d/conference
%{_sysconfdir}/rsyncd.d/rsync.busy_banner
%{_sysconfdir}/rsyncd.d/rsyncd-opensuse-hotstuff-160gb
%{_sysconfdir}/rsyncd.d/rsyncd-opensuse-hotstuff-160gb-devel
%{_sysconfdir}/rsyncd.d/rsyncd-opensuse-hotstuff-30gb
%{_sysconfdir}/rsyncd.d/rsyncd-opensuse-hotstuff-30gb-devel
%{_sysconfdir}/rsyncd.d/rsyncd-opensuse-hotstuff-80gb
%{_sysconfdir}/rsyncd.d/rsyncd-opensuse-hotstuff-80gb-devel
%{_sysconfdir}/rsyncd.d/rsyncd-opensuse-hotstuff-full
%{_sysconfdir}/rsyncd.d/rsyncd-opensuse-hotstuff-full-devel
%{_sysconfdir}/rsyncd.d/rsyncd-opensuse-ports
%{_sysconfdir}/rsyncd.d/rsyncd-public.motd
%{_sysconfdir}/rsyncd.d/rsyncd-stage.motd

%license LICENSE
%doc README.md

%changelog
