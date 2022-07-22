%global debug_package %{nil}

Name: php-cs-fixer
Epoch: 100
Version: 3.9.5
Release: 1%{?dist}
BuildArch: noarch
Summary: PHP Coding Standards Fixer
License: MIT
URL: https://github.com/FriendsOfPHP/PHP-CS-Fixer/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
Requires: php-cli >= 7.4

%description
The PHP Coding Standards Fixer (PHP CS Fixer) tool fixes your code to
follow standards; whether you want to follow PHP coding standards as
defined in the PSR-1, PSR-2, etc., or other community driven ones like
the Symfony one. You can also define your (team's) style through
configuration.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -d %{buildroot}%{_datadir}/php/vendor
cp -rfT vendor %{buildroot}%{_datadir}/php/vendor
pushd %{buildroot}%{_bindir} && \
    ln -fs %{_datadir}/php/vendor/php-cs-fixer/php-cs-fixer php-cs-fixer && \
    popd
chmod a+x %{buildroot}%{_datadir}/php/vendor/php-cs-fixer/php-cs-fixer
fdupes -qnrps %{buildroot}%{_datadir}/php/vendor

%check

%files
%license LICENSE
%dir %{_datadir}/php
%dir %{_datadir}/php/vendor
%{_bindir}/*
%{_datadir}/php/vendor/*

%changelog
