Name:       xcp-efivar-utils
Version:    1.0.0
Release:    2~xeu.2%{?dist}
Summary:    XCP-ng UEFI variable utility library
License:    BSD-2-Clause AND GPL-2.0-only
URL:        https://github.com/xcp-ng/xcp-efivar-utils

# https://github.com/xcp-ng/xcp-efivar-utils/releases/tag/v1.0.0
Source0:    xcp_efivar_utils-1.0.0-py3-none-any.whl

BuildRequires:  python3-devel python3-pip
BuildArch:      noarch

Requires:       openssl

%description
This library contains an assortment of useful Python functions for manipulating
UEFI variables on XCP-ng pools and VMs.

%install
python3 -m pip install "%{SOURCE0}" --root %{buildroot}

%files
/usr/bin/*
%{python3_sitelib}/xcp_efivar_utils*

%changelog
* Wed Jul 29 2026 Tu Dinh <ngoc-tu.dinh@vates.tech> - 1.0.0-2
- Rebuild for XCP-ng 9

* Fri Jul 10 2026 Tu Dinh <ngoc-tu.dinh@vates.tech> - 1.0.0-1
- Initial version
