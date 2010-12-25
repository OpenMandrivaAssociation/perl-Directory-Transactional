%define upstream_name    Directory-Transactional
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Traverse files in L<Directory::Transactional>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Directory/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(Data::Stream::Bulk)
BuildRequires: perl(Data::GUID)
BuildRequires: perl(Directory::Scratch)
BuildRequires: perl(File::NFSLock)
BuildRequires: perl(File::Path)
BuildRequires: perl(Hash::Util::FieldHash::Compat)
BuildRequires: perl(List::Util)
BuildRequires: perl(Moose)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Scope::Guard)
BuildRequires: perl(Set::Object)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::TempDir)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides lock based transactions over a set of files with full
supported for nested transactions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


