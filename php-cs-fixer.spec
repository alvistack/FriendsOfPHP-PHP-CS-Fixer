%global debug_package %{nil}

%global __strip /bin/true

%global __brp_mangle_shebangs /bin/true

Name: php-cs-fixer
Epoch: 100
Version: 3.8.0
Release: 1%{?dist}
BuildArch: noarch
Summary: PHP Coding Standards Fixer
License: MIT
URL: https://github.com/FriendsOfPHP/PHP-CS-Fixer/tags
Source0: %{name}_%{version}.orig.tar.gz
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
install -Dpm755 -t %{buildroot}%{_bindir} usr/bin/php-cs-fixer

%check

%files
%license LICENSE
%{_bindir}/*

%changelog
