# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: php-cs-fixer
Epoch: 100
Version: 3.58.0
Release: 1%{?dist}
BuildArch: noarch
Summary: PHP Coding Standards Fixer
License: MIT
URL: https://github.com/FriendsOfPHP/PHP-CS-Fixer/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes

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
