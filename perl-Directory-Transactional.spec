%define upstream_name    Directory-Transactional
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Traverse files in L<Directory::Transactional>
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Directory/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Data::Stream::Bulk)
BuildRequires:	perl(Data::GUID)
BuildRequires:	perl(Directory::Scratch)
BuildRequires:	perl(File::NFSLock)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(Hash::Util::FieldHash::Compat)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Set::Object)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::TempDir)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This module provides lock based transactions over a set of files with full
supported for nested transactions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 654313
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 624813
- import perl-Directory-Transactional

